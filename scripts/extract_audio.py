"""Isolate the audio track of a video as a 16kHz mono WAV (whisper-ready).

Usage:
    python scripts/extract_audio.py raw/<slug>.mp4

Writes processed/<slug>/audio.wav
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    video_path = Path(sys.argv[1])
    slug = video_path.stem
    out_dir = ROOT / "processed" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "audio.wav"

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", str(video_path),
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            str(out_path),
        ],
        check=True,
        capture_output=True,
    )
    print(f"processed/{slug}/audio.wav")


if __name__ == "__main__":
    main()
