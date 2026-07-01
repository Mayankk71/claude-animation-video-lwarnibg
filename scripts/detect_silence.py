"""Detect pause/silence windows in the audio track via ffmpeg's silencedetect filter.

Usage:
    python scripts/detect_silence.py raw/<slug>.mp4

Requires processed/<slug>/audio.wav (run extract_audio.py first).
Writes processed/<slug>/silence_pauses.json
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

START_RE = re.compile(r"silence_start:\s*(-?[\d.]+)")
END_RE = re.compile(r"silence_end:\s*(-?[\d.]+)\s*\|\s*silence_duration:\s*([\d.]+)")


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    video_path = Path(sys.argv[1])
    slug = video_path.stem
    out_dir = ROOT / "processed" / slug
    audio_path = out_dir / "audio.wav"
    if not audio_path.exists():
        sys.exit(f"Missing {audio_path} — run extract_audio.py first.")

    result = subprocess.run(
        [
            "ffmpeg",
            "-i", str(audio_path),
            "-af", "silencedetect=noise=-30dB:d=0.15",
            "-f", "null", "-",
        ],
        capture_output=True,
        text=True,
    )

    pauses = []
    pending_start = None
    for line in result.stderr.splitlines():
        start_match = START_RE.search(line)
        if start_match:
            pending_start = float(start_match.group(1))
            continue
        end_match = END_RE.search(line)
        if end_match and pending_start is not None:
            pauses.append(
                {
                    "start": pending_start,
                    "end": float(end_match.group(1)),
                    "duration": float(end_match.group(2)),
                }
            )
            pending_start = None

    (out_dir / "silence_pauses.json").write_text(json.dumps({"slug": slug, "pauses": pauses}, indent=2))
    print(f"processed/{slug}/silence_pauses.json ({len(pauses)} pauses)")


if __name__ == "__main__":
    main()
