from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict


AUDIO_EXTS = {".wav", ".flac", ".mp3", ".m4a"}


def discover_audio(input_dir: Path) -> List[Path]:
    files = [p for p in input_dir.rglob("*") if p.is_file() and p.suffix.lower() in AUDIO_EXTS]
    return sorted(files)


def load_manifest(manifest_path: Path) -> List[Dict]:
    rows = []
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def resolve_items(input_dir: str | None, manifest_path: str | None) -> List[Dict]:
    if not input_dir and not manifest_path:
        raise ValueError("Provide either --input-dir or --manifest.")
    if input_dir and manifest_path:
        raise ValueError("Use only one of --input-dir or --manifest.")

    if manifest_path:
        rows = load_manifest(Path(manifest_path))
        items = []
        for row in rows:
            audio = Path(row["audio_filepath"]).expanduser()
            session = row.get("session_name") or audio.stem
            items.append({"audio_path": audio, "session_name": session})
        return items

    audio_files = discover_audio(Path(input_dir).expanduser())
    return [{"audio_path": p, "session_name": p.stem} for p in audio_files]


def write_jsonl(rows: List[Dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")
