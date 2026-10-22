# Zenodo R2 Publication — F3 8B Source-Token Candidate

**Checked:** 22 October 2026  
**Present public Zenodo version:** R1, DOI [10.5281/zenodo.23054425](https://doi.org/10.5281/zenodo.23054425)  
**Version family:** [10.5281/zenodo.23054424](https://doi.org/10.5281/zenodo.23054424)  
**8B new-version DOI:** **NOT ISSUED — DEPOSITOR AUTHORIZATION REQUIRED**

The original R1 record remains unchanged. This new publication must be made through **New version**, not as an overwrite or an unrelated DOI family.

## Completed publication work

1. The 8B source-token evidence note and JSON are available on GitHub and Hugging Face.
2. The SHA-256-checked evidence ZIP is attached to [GitHub prerelease v1.1.0-f3-8b-token-evidence-r1](https://github.com/RabbitIndustries/agastya-native-brain-evidence/releases/tag/v1.1.0-f3-8b-token-evidence-r1).
3. Archive SHA-256: `2017f00f03c3d6af356db064e4e3f16e399d30bd4625335a9bfc0939927f3cd3`.
4. The GitHub [Zenodo new-version publisher](https://github.com/RabbitIndustries/agastya-native-brain-evidence/actions/workflows/publish-agastya-f3-8b-zenodo-version.yml) is configured to require an account-owned secret `ZENODO_ACCESS_TOKEN`, then verify the archive, create a draft within the original record's version family, upload the ZIP and publish/verify a **new** DOI. Its no-credential protection was exercised successfully; **the live authenticated deposit has not been tested or performed**.

## Account-owner action (do not share tokens in chat)

1. Sign into the Zenodo account that owns [the original R1 record](https://zenodo.org/records/23054425).
2. From [Zenodo Applications](https://zenodo.org/account/settings/applications/), create an access token with only the deposit permissions required for new-version publication (Zenodo's API documents `deposit:write` and `deposit:actions`).
3. Store it only in the private GitHub Actions repository secret [ZENODO_ACCESS_TOKEN](https://github.com/RabbitIndustries/agastya-native-brain-evidence/settings/secrets/actions/new) — never commit it or paste it into messages.
4. Open [the publisher workflow](https://github.com/RabbitIndustries/agastya-native-brain-evidence/actions/workflows/publish-agastya-f3-8b-zenodo-version.yml) and select **Run workflow**, then verify the new DOI in the [Zenodo version list](https://zenodo.org/records/23054425/versions).
5. If Zenodo rejects the API new-version action, use **New version** in the original record's authenticated web UI, upload [the checksum-verified ZIP](https://github.com/RabbitIndustries/agastya-native-brain-evidence/releases/download/v1.1.0-f3-8b-token-evidence-r1/Agastya-F3-8B-Source-Token-Candidate-Evidence-R1-Zenodo.zip), publish, and verify the resulting new DOI. Do not claim issuance until verified.

**Evidence boundary:** 8B means eight billion training **source tokens**, not eight billion model parameters. Production promotion remains unauthorized. The archive contains no proprietary weights, complete tokenizer, private training data or credentials.
