# AppTek + Suqrat DiariZen / Sortformer Run

This package is for **inference only**.

Please run the two diarization models below and return the **hypothesis RTTM outputs only**.

## Models

- `BUT-FIT/diarizen-wavlm-large-s80-md-v2`
- `nvidia/diar_streaming_sortformer_4spk-v2.1`

## Input manifests

- `manifests/apptek_available_now.jsonl`
- `manifests/suqrat_full_1_2_3.jsonl`

## Audio path placeholders

The manifests use placeholders because the audio will be on the station.

Please replace:

- `<APPTEK_AUDIO_ROOT>`
- `<SUQRAT_AUDIO_ROOT>`

with the actual audio locations on the station before running.

## Required outputs

Please return only the generated **RTTM hypothesis outputs** under:

- `outputs/diarizen/`
- `outputs/sortformer_v2/`

Suggested structure:

- `outputs/diarizen/apptek/`
- `outputs/diarizen/suqrat_1_2_3/`
- `outputs/sortformer_v2/apptek/`
- `outputs/sortformer_v2/suqrat_1_2_3/`

## Run commands

Enter the package directory first:

```bash
cd apptek-suqrat-diarizen-sortformer-run
```

Create the output folders first:

```bash
mkdir -p outputs/diarizen/apptek outputs/diarizen/suqrat_1_2_3
mkdir -p outputs/sortformer_v2/apptek outputs/sortformer_v2/suqrat_1_2_3
```

### DiariZen

AppTek:

```bash
zsh scripts/run_diarizen.sh manifests/apptek_available_now.jsonl outputs/diarizen/apptek python manifest
```

Suqrat_1 + Suqrat_2 + Suqrat_3:

```bash
zsh scripts/run_diarizen.sh manifests/suqrat_full_1_2_3.jsonl outputs/diarizen/suqrat_1_2_3 python manifest
```

### Sortformer v2

Before running Sortformer, set:

```bash
export NEMO_ROOT=<NEMO_ROOT>
```

AppTek:

```bash
zsh scripts/run_sortformer.sh manifests/apptek_available_now.jsonl outputs/sortformer_v2/apptek "$NEMO_ROOT" streaming python manifest
```

Suqrat_1 + Suqrat_2 + Suqrat_3:

```bash
zsh scripts/run_sortformer.sh manifests/suqrat_full_1_2_3.jsonl outputs/sortformer_v2/suqrat_1_2_3 "$NEMO_ROOT" streaming python manifest
```

## What to return

Please return only the generated **RTTM hypothesis outputs** from:

- `outputs/diarizen/`
- `outputs/sortformer_v2/`
