from __future__ import annotations

import argparse
from pathlib import Path

from common import resolve_items


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Run DiariZen and save RTTM outputs only.")
    ap.add_argument("--input-dir", help="Folder containing audio files.")
    ap.add_argument("--manifest", help="JSONL manifest with audio_filepath and optional session_name.")
    ap.add_argument("--output-dir", required=True, help="Output directory for RTTM files.")
    ap.add_argument(
        "--model-name",
        default="BUT-FIT/diarizen-wavlm-large-s80-md-v2",
        help="DiariZen model name or local path.",
    )
    return ap.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    items = resolve_items(args.input_dir, args.manifest)

    try:
        from diarizen.pipelines.inference import DiariZenPipeline
    except Exception as exc:
        raise SystemExit(
            "Could not import DiariZenPipeline. Please install DiariZen first. "
            f"Original error: {exc}"
        )

    pipeline = DiariZenPipeline.from_pretrained(args.model_name, rttm_out_dir=str(output_dir))

    for item in items:
        audio_path = Path(item["audio_path"])
        session_name = item["session_name"]
        pipeline(str(audio_path), sess_name=session_name)
        print(f"saved {session_name}.rttm")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
