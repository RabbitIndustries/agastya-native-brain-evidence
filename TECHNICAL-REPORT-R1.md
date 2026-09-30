# Agastya AGI v01 — Native Brain Technical Evidence Report R1

## Abstract

Rabbit Industries Pvt Ltd publishes this R1 evidence report to make the Agastya AGI v01 from-scratch native-model lineage externally citable. The release exposes cryptographic artifact identifiers and validation/acceptance records while retaining proprietary raw weights, corpus and source code.

## Core claim under test

Agastya's canonical Native Brain lineage is defined as:

Agastya corpus -> Agastya tokenizer -> Agastya architecture -> RANDOM INITIALIZATION -> Agastya pretraining -> Agastya post-training -> Agastya Native Brain

The R1 evidence manifests record a fresh step-0 checkpoint, zero teacher-weight ancestry, false third-party weight ancestry, false third-party tokenizer artifact import, and a PASS checkpoint validation.

## Architecture and scale

- Unique parameters: 1,264,715,776
- Dense architecture
- Canonical context: 4,096 tokens
- Tokenizer vocabulary: 98,320
- Tokenizer model: BPE
- Normalization: NFC
- Pre-tokenization: ByteLevel

## Step-0 provenance

The published weight-lineage manifest exposes:
- architecture source hash
- architecture hash
- tokenizer hash
- deterministic random seed
- seed-derivation hash
- record-selection hash
- token-cache hash
- step-0 checkpoint hash and byte length

The public package does not redistribute the raw 2.53 GB checkpoint.

## Validation

The checkpoint-validation manifest records PASS for random initialization, zero teacher ancestry, false third-party weight ancestry, tokenizer identity and exact unique parameter count.

The Clean-P0 R2 final acceptance manifest records PASS and completed_zero_third_party=true.

## Evidence scope

This R1 report is company-generated evidence. It is externally citable because the package is publicly accessible with stable URLs, checksums, machine-readable manifests and citation metadata.

Independent external verification remains pending and must be completed before describing Agastya as independently verified.

## Benchmark scope

Comparable frontier benchmark scores are not asserted until an identical frozen evaluation harness is run and independently replayed. Internal diagnostics are not substituted for public same-suite results.

## Next publication gates

1. Independent evaluator replay.
2. Signed verification report.
3. DOI-backed archival deposit.
4. Public model card mirror.
5. Research preprint.
6. Same-suite benchmark submission / external leaderboard evaluation where applicable.

## Persistent identifier

Published Zenodo DOI: [10.5281/zenodo.23054425](https://doi.org/10.5281/zenodo.23054425)

This DOI identifies the published Zenodo R1 evidence record.

Zenodo record: https://zenodo.org/records/23054425
