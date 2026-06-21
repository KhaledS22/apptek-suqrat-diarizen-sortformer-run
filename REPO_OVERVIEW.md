# Repo Overview

## What this repo does

This repo runs DiariZen and Sortformer v2 on AppTek and Suqrat manifests and produces RTTM outputs.

## When to use it

Use this repo when the team wants a clean handoff package for GPU or station inference.

## Most important files

- `manifests/apptek_available_now.jsonl`
- `manifests/suqrat_full_1_2_3.jsonl`
- `scripts/run_diarizen.sh`
- `scripts/run_diarizen.py`
- `scripts/run_sortformer.sh`
- `scripts/run_sortformer.py`

## How to run it

1. Replace audio-root placeholders in the manifests.
2. Create the output folders.
3. Run the selected model using the local shell script.
4. Return RTTM outputs only.

## Expected output

- RTTM hypothesis files for AppTek
- RTTM hypothesis files for Suqrat
