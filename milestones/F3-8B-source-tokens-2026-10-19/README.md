# Agastya AGI F3 — 8 Billion Source-Token Candidate Milestone

**Publisher:** Rabbit Industries Pvt Ltd  
**Milestone date:** 19 October 2026 (UTC)  
**Evidence package:** F3-8B-SOURCE-TOKENS-CANDIDATE-R1  
**Status:** Training milestone complete; candidate only; production promotion not authorized.

## Precisely scoped claim

The Agastya F3 R2 candidate training record reports exactly **8,000,000,000 source tokens** consumed against an 8,000,000,000-token target (100.0%), after terminal ledger reconciliation and a final checkpoint. **8B means training source tokens, not 8 billion model parameters.** This is not proof of independent evaluation, benchmark supremacy, model release approval, or production suitability.

## Auditable source record (internal artifact identifiers)

- Training status file: `/workspace/agastya-f3-runtime-r2/F3-TRAINING-STATUS-R2.json`
- Training status SHA-256: `c5c00ae774eccd17c39bd4da601c5ab0605af699bd2970b6cf3f3eb06987bbc3`
- Final checkpoint metadata: `/workspace-global/agastya/training/f3-r2/checkpoints/F3-CANDIDATE-R2-8000000000.json`
- Checkpoint metadata SHA-256: `5cd15798046e52c889e26843676b7a178da84b9adecce039fed98ec508ed3880`
- Final proprietary checkpoint SHA-256 **recorded in metadata** (not independently re-hashed for this publication): `3e0ec187db627012e9e5eba9f73285b76f2185562b7c83841bc54e496e6325af`
- Final checkpoint size on the training system: 21,442,876,013 bytes; optimizer step 7,639.
- Exposure-ledger manifest: `/workspace/agastya-f3-production-cache-r2/F3-EXPOSURE-LEDGER-MANIFEST-R2.json`
- Exposure-ledger manifest SHA-256: `c12b4cbb49d2f5d1a7b549760e010c4abb434af09889a599d77370adad935966`
- Source tokens: 8,000,000,000; exposure records: 10,368,986; terminal ledger counter reconciled: true.
- Training completion record timestamp: 2026-10-19T14:40:36.126712+00:00.

## Release boundaries and validation

- Candidate training completion: **RECORDED COMPLETE**.
- Final model acceptance: **NOT CLAIMED**.
- Production promotion: **NOT AUTHORIZED** (`promotion_authorized=false`).
- Independent third-party verification and same-suite external benchmarks: **PENDING**.
- Subsequent 1B base-repair canary gate: **REJECTED / HOLD**, per 21 October gate record. This does not revoke the historical raw 8B training completion.
- F3.2 continuation is separate and must not be disturbed by evidence publication.
- Evidence file hashes above were calculated by read-only inspection on the connected Agni V2 system. The full 21.4-GB checkpoint was not freshly re-hashed; the listed checkpoint digest is from its recorded metadata.

## Provenance / continuity

This supplementary milestone package is **not** a replacement for the earlier R1 evidence release or its DOI. Original evidence: [GitHub R1](https://github.com/RabbitIndustries/agastya-native-brain-evidence/releases/tag/v1.0.0-evidence-r1), [Zenodo R1](https://doi.org/10.5281/zenodo.23054425), and [canonical site](https://zippri.com/agastya-native-brain-evidence/).

## Disclosure scope

This public package contains only selected numerical training status and cryptographic identifiers. Proprietary model weights, dataset records, tokenizer files, trainer source, private infrastructure configuration, credentials, and private checkpoint binaries are not distributed. This does not change any deployment, training, promotion, or freeze policy.

## Final publication — Zenodo R2 DOI issued

**Official R2 DOI:** [10.5281/zenodo.23557660](https://doi.org/10.5281/zenodo.23557660)  
**Zenodo public record:** https://zenodo.org/records/23557660  
**R2 version:** `R2-F3-8B-SOURCE-TOKEN-CANDIDATE`  
**Published:** 22 October 2026  
**Concept DOI (all versions):** https://doi.org/10.5281/zenodo.23054424  
**Historical R1 DOI (preserved):** https://doi.org/10.5281/zenodo.23054425

The public record was checked with Zenodo's API as `published`. Its 4,603-byte ZIP has the MD5 checksum `3493ddfc97b01bb9c94cf38050a26287`, matching the prepared archive. See [R2 Zenodo publication status](ZENODO-PUBLISHING-STATUS.md) and [machine-readable publication manifest](ZENODO-R2-PUBLICATION.json).

As elsewhere in this report, the 8B milestone means **training source tokens**, not 8B model parameters. Production promotion remains unauthorized.
