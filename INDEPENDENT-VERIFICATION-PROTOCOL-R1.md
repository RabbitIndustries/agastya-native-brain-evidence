# Agastya Native Brain Independent Verification Protocol R1

Purpose: allow an independent evaluator to determine whether the supplied Agastya checkpoint satisfies the published from-scratch native-lineage claims without requiring public release of proprietary weights or corpus.

## Inputs to evaluator

1. Frozen step-0 checkpoint or controlled hash-verification access.
2. ANTR2-R1 tokenizer artifact.
3. Frozen architecture source/configuration.
4. Initialization source and provenance manifest.
5. Clean-P0 training/acceptance manifests.
6. Selected corpus-manifest hashes and training-token accounting evidence.
7. Frozen post-training checkpoint selected for benchmark evaluation.

## Verification gates

### V1 — Artifact identity
- Recompute SHA-256 of tokenizer, architecture source, step-0 checkpoint and supplied manifests.
- Match against Public Evidence R1.

### V2 — Random initialization
- Inspect step-0 checkpoint and initialization source.
- Verify deterministic seed derivation.
- Confirm optimizer state is absent at step 0.
- Confirm production training is false at step 0.

### V3 — Weight ancestry
- Verify provenance declaration: third_party_weight_ancestry=false.
- Verify teacher_weight_ancestry=ZERO.
- Inspect state initialization path for absence of third-party checkpoint loading before step 0.

### V4 — Tokenizer ancestry
- Verify tokenizer SHA-256 and tokenizer structure.
- Review tokenizer creation records sufficient to determine whether vocabulary/merges were trained as an Agastya artifact rather than imported from another model.
- Record any unresolved provenance gaps explicitly.

### V5 — Parameter count and architecture
- Independently count unique model parameters.
- Verify architecture configuration and tied-weight treatment.
- Compare against published 1,264,715,776 unique parameters.

### V6 — Training lineage continuity
- Verify checkpoint chain from step 0 to selected trained checkpoint using immutable hashes/manifests.
- Verify no unapproved external weight insertion occurs in the chain.

### V7 — Benchmark replay
- Freeze model version, tokenizer, prompts, scoring, tool permissions and environment.
- Run agreed public suites.
- Publish exact harness/version and confidence/variance where applicable.

## Required evaluator output

A signed report containing:
- evaluator identity/organization
- date
- artifact hashes
- PASS/FAIL/INCONCLUSIVE for V1–V7
- methods
- deviations
- conflicts or unresolved questions
- benchmark results, if executed
- signed report hash

## Public status rules

- Do not use “independently verified” until V1–V6 are PASS.
- Do not publish an external performance rank until V7 uses directly comparable frozen suites.
