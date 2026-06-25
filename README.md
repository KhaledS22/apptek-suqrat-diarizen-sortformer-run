# AppTek and Suqrat DiariZen / Sortformer Run

## What this repo does

This repo is an inference-only run package for generating hypothesis RTTM outputs on AppTek and Suqrat using DiariZen and Sortformer v2.

## Why it was created

This repo was created so the team can run heavy diarization inference on a station or GPU environment without needing the full evaluation workspace. It keeps the run package small, clear, and easy to hand off.

## Main workflow

1. Prepare the station paths for the audio roots.
2. Use the provided manifests.
3. Run DiariZen or Sortformer v2 with the local scripts.
4. Return the RTTM hypothesis outputs only.

## Input

- AppTek audio files
- Suqrat audio files
- JSONL manifests
- NeMo root for Sortformer

## Output

- RTTM hypothesis files under `outputs/diarizen/`
- RTTM hypothesis files under `outputs/sortformer_v2/`

## Important scripts

| Script | Purpose |
| ------ | ------- |
| `manifests/apptek_available_now.jsonl` | Manifest for the AppTek matched set. |
| `manifests/suqrat_full_1_2_3.jsonl` | Manifest for the three full Suqrat files. |
| `scripts/run_diarizen.sh` | Shell entry point for DiariZen runs. |
| `scripts/run_diarizen.py` | Python runner for DiariZen on manifest or folder input. |
| `scripts/run_sortformer.sh` | Shell entry point for Sortformer runs. |
| `scripts/run_sortformer.py` | Python runner for Sortformer on manifest or folder input. |
| `scripts/common.py` | Shared helper logic used by both runners. |

## How to run

Enter the repo:

```bash
cd <repo-folder>
```

Create output folders:

```bash
mkdir -p outputs/diarizen/apptek outputs/diarizen/suqrat_1_2_3
mkdir -p outputs/sortformer_v2/apptek outputs/sortformer_v2/suqrat_1_2_3
```

Replace the manifest placeholders with station audio roots:

- `<APPTEK_AUDIO_ROOT>`
- `<SUQRAT_AUDIO_ROOT>`

Run DiariZen on AppTek:

```bash
zsh scripts/run_diarizen.sh manifests/apptek_available_now.jsonl outputs/diarizen/apptek python manifest
```

Run DiariZen on Suqrat:

```bash
zsh scripts/run_diarizen.sh manifests/suqrat_full_1_2_3.jsonl outputs/diarizen/suqrat_1_2_3 python manifest
```

Run Sortformer on AppTek:

```bash
zsh scripts/run_sortformer.sh manifests/apptek_available_now.jsonl outputs/sortformer_v2/apptek <NEMO_ROOT> streaming python manifest
```

Run Sortformer on Suqrat:

```bash
zsh scripts/run_sortformer.sh manifests/suqrat_full_1_2_3.jsonl outputs/sortformer_v2/suqrat_1_2_3 <NEMO_ROOT> streaming python manifest
```

## What is NOT included

This repo does not include:

- raw audio
- dataset dumps
- reference RTTM
- metrics
- logs
- tokens
- credentials
- large outputs

## Notes for the team

- This repo is intentionally small and handoff-friendly.
- It is for inference only, not evaluation.
- The only expected return from the run is RTTM hypothesis output.
- `outputs/*/.gitkeep` files are only placeholders to preserve empty output folders in Git; they are not real model outputs.
