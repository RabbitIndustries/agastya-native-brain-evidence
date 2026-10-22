#!/usr/bin/env python3
"""Idempotent publisher for the Agastya F3 8B source-token candidate Zenodo version.

Requires an authorized owner Zenodo access token in ZENODO_ACCESS_TOKEN.
Never prints the token, never edits the already-published September R1 record,
and does not create a separate unrelated DOI family.
"""
import hashlib
import json
import os
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = "https://zenodo.org"
PARENT_ID = "23054425"
ORIGINAL_DOI = "10.5281/zenodo.23054425"
CONCEPT_DOI = "10.5281/zenodo.23054424"
NEW_VERSION = "R2-F3-8B-SOURCE-TOKEN-CANDIDATE"
ARCHIVE_NAME = "Agastya-F3-8B-Source-Token-Candidate-Evidence-R1-Zenodo.zip"
ARCHIVE_SHA256 = "2017f00f03c3d6af356db064e4e3f16e399d30bd4625335a9bfc0939927f3cd3"
ARCHIVE_URL = (
    "https://github.com/RabbitIndustries/agastya-native-brain-evidence/releases/"
    "download/v1.1.0-f3-8b-token-evidence-r1/" + ARCHIVE_NAME
)

TOKEN = os.getenv("ZENODO_ACCESS_TOKEN", "").strip()


def query(method, url, data=None, content_type=None, authenticated=False):
    if not url.startswith(ROOT + "/api/"):
        raise RuntimeError("Refused unexpected API destination")
    headers = {"User-Agent": "RabbitIndustries-F3-8B-Evidence-Publisher/1.0"}
    if authenticated:
        if not TOKEN:
            raise RuntimeError("Zenodo authorized depositor credential is missing")
        headers["Authorization"] = "Bearer " + TOKEN
    if content_type:
        headers["Content-Type"] = content_type
    if isinstance(data, (dict, list)):
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = Request(url, data=data, method=method, headers=headers)
    try:
        with urlopen(request, timeout=65) as response:
            body = response.read()
    except HTTPError as exc:
        raise RuntimeError(
            f"Zenodo {method} request rejected (HTTP {exc.code}); "
            "check record ownership, API scopes, or Zenodo API availability"
        ) from None
    except URLError as exc:
        raise RuntimeError(f"Zenodo {method} request unavailable: {type(exc.reason).__name__}") from None
    if not body:
        return {}
    return json.loads(body.decode("utf-8"))


def versions():
    obj = query("GET", ROOT + f"/api/records/{PARENT_ID}/versions")
    return (obj.get("hits") or {}).get("hits", [])


def existing_8b_record():
    for rec in versions():
        metadata = rec.get("metadata") or {}
        version = metadata.get("version") or ""
        title = metadata.get("title") or ""
        if version == NEW_VERSION or ("F3" in title and "8B" in title and "Source-Token" in title):
            doi = rec.get("doi") or (metadata.get("doi") if isinstance(metadata.get("doi"), str) else None)
            print("ZENODO_8B_VERSION_ALREADY_PUBLISHED", "id", rec.get("id"), "doi", doi)
            return True
    return False


def download_checked_archive():
    req = Request(ARCHIVE_URL, headers={"User-Agent": "AgastyaF3Publication/1.0"})
    try:
        with urlopen(req, timeout=60) as stream:
            blob = stream.read(1000001)
    except Exception as exc:
        raise RuntimeError(f"Unable to retrieve verified GitHub archive: {type(exc).__name__}") from None
    if len(blob) > 1000000:
        raise RuntimeError("Refused unexpected archive size")
    if hashlib.sha256(blob).hexdigest() != ARCHIVE_SHA256:
        raise RuntimeError("Archive SHA256 mismatch; no Zenodo version created")
    print("ARCHIVE_INTEGRITY_PASS", len(blob))
    return blob


def fresh_or_reusable_draft():
    url = ROOT + f"/api/records/{PARENT_ID}/draft"
    try:
        draft = query("GET", url, authenticated=True)
    except RuntimeError as exc:
        if "HTTP 404" not in str(exc):
            raise
        draft = None
    if draft:
        version = (draft.get("metadata") or {}).get("version")
        if version != NEW_VERSION:
            raise RuntimeError("An unrelated draft exists for the original Zenodo record; refusing to overwrite")
        print("REUSING_EXISTING_8B_DRAFT", draft.get("id"))
        return draft

    pub = query("GET", ROOT + f"/api/records/{PARENT_ID}", authenticated=True)
    if pub.get("doi") != ORIGINAL_DOI:
        raise RuntimeError("Original DOI does not match the authorized record")
    print("ORIGINAL_ZENODO_DOI_VERIFIED", ORIGINAL_DOI)
    created = query("POST", ROOT + f"/api/records/{PARENT_ID}/versions", data={}, authenticated=True)
    if not created.get("id"):
        raise RuntimeError("New-version draft creation returned no ID")
    print("NEW_ZENODO_VERSION_DRAFT_CREATED", created.get("id"))
    return created


def save_metadata(draft):
    metadata = dict(draft.get("metadata") or {})
    if not metadata:
        raise RuntimeError("New version has no inherited metadata; refusing unsafe creation")
    metadata["title"] = "Agastya AGI v01 Native Brain Evidence R2 - F3 8B Source-Token Candidate"
    metadata["version"] = NEW_VERSION
    metadata["publication_date"] = datetime.now(timezone.utc).date().isoformat()
    metadata["description"] = (
        "<p>Rabbit Industries Pvt Ltd. The Agastya F3 R2 candidate training record documents "
        "<strong>8,000,000,000 source training tokens</strong> completed on 19 October 2026 "
        "(final optimizer step 7,639, exact raw ledger counter reconciled).</p>"
        "<p>8B denotes <strong>training source tokens, not model parameters</strong>. "
        "This is a candidate-training evidence milestone. Production promotion is not authorized; "
        "independent verification and external benchmark acceptance are pending. "
        "The separate 1B base-repair canary is rejected/held.</p>"
        "<p>This is a versioned supplement to original R1 DOI "
        "<a href='https://doi.org/10.5281/zenodo.23054425'>10.5281/zenodo.23054425</a>. "
        "Original records and proprietary model weights, corpus and tokenizer are unchanged.</p>"
        "<p>GitHub release: "
        "<a href='https://github.com/RabbitIndustries/agastya-native-brain-evidence/releases/"
        "tag/v1.1.0-f3-8b-token-evidence-r1'>F3 8B evidence prerelease</a>.</p>"
    )
    metadata.pop("doi", None)
    access = draft.get("access") or {"record": "public", "files": "public"}
    files = draft.get("files") or {"enabled": True}
    links = draft.get("links") or {}
    url = links.get("self") or ROOT + "/api/records/" + str(draft["id"]) + "/draft"
    if not url.endswith("/draft"):
        url = ROOT + "/api/records/" + str(draft["id"]) + "/draft"
    payload = {"metadata": metadata, "access": access, "files": files}
    obj = query("PUT", url, data=payload, authenticated=True)
    if (obj.get("metadata") or {}).get("version") != NEW_VERSION:
        raise RuntimeError("Zenodo did not confirm R2 metadata")
    print("ZENODO_METADATA_SAVED", obj.get("id"))
    return obj


def upload_archive(draft, content):
    id_ = str(draft["id"])
    files_url = ROOT + "/api/records/" + id_ + "/draft/files"
    existing = query("GET", files_url, authenticated=True)
    entries = existing.get("entries") or {}
    if ARCHIVE_NAME in entries:
        detail = entries[ARCHIVE_NAME]
        if detail.get("status") == "completed":
            print("ZENODO_ARCHIVE_ALREADY_COMMITTED")
            return
        raise RuntimeError("Incomplete archive entry exists in Zenodo draft; manual reconciliation needed")
    initiated = query("POST", files_url, data=[{"key": ARCHIVE_NAME}], authenticated=True)
    parts = initiated.get("entries") or []
    part = next((x for x in parts if x.get("key") == ARCHIVE_NAME), None)
    if not part:
        raise RuntimeError("Zenodo did not initialize the archive entry")
    links = part.get("links") or {}
    content_url = links.get("content") or files_url + "/" + quote(ARCHIVE_NAME) + "/content"
    commit_url = links.get("commit") or files_url + "/" + quote(ARCHIVE_NAME) + "/commit"
    query("PUT", content_url, data=content, content_type="application/octet-stream", authenticated=True)
    query("POST", commit_url, authenticated=True)
    print("ZENODO_ARCHIVE_UPLOADED_AND_COMMITTED", ARCHIVE_NAME)


def publish(draft):
    links = draft.get("links") or {}
    url = links.get("publish") or ROOT + "/api/records/" + str(draft["id"]) + "/draft/actions/publish"
    obj = query("POST", url, authenticated=True)
    id_ = obj.get("id") or draft["id"]
    verified = query("GET", ROOT + "/api/records/" + str(id_))
    doi = verified.get("doi")
    if verified.get("status") != "published" or not doi or doi == ORIGINAL_DOI:
        raise RuntimeError("Zenodo publication did not verify as a separate DOI")
    if verified.get("conceptdoi") != CONCEPT_DOI:
        raise RuntimeError("Zenodo DOI-family mismatch; do not claim an R1 version")
    print("ZENODO_8B_VERSION_PUBLISHED", "https://doi.org/" + doi)


def main():
    if existing_8b_record():
        return
    if not TOKEN:
        raise RuntimeError(
            "ZENODO_AUTH_MISSING: configure a deposit-authorized Zenodo token in "
            "the GitHub Actions repository secret ZENODO_ACCESS_TOKEN; never paste it into chat"
        )
    blob = download_checked_archive()
    draft = fresh_or_reusable_draft()
    draft = save_metadata(draft)
    upload_archive(draft, blob)
    publish(draft)


if __name__ == "__main__":
    main()
