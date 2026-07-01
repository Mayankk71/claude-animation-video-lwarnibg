"""Extract duration, fps, and resolution for a video via ffprobe.

Usage:
    python scripts/extract_metadata.py raw/<slug>.mp4

Writes processed/<slug>/metadata.json
"""

import json
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

    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            str(video_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    probe = json.loads(result.stdout)

    video_stream = next(s for s in probe["streams"] if s["codec_type"] == "video")
    audio_streams = [s for s in probe["streams"] if s["codec_type"] == "audio"]

    num, den = video_stream.get("r_frame_rate", "0/1").split("/")
    fps = float(num) / float(den) if float(den) else 0.0

    metadata = {
        "slug": slug,
        "duration_sec": float(probe["format"].get("duration", 0.0)),
        "fps": round(fps, 3),
        "width": video_stream.get("width"),
        "height": video_stream.get("height"),
        "has_audio": bool(audio_streams),
        "codec": video_stream.get("codec_name"),
    }

    (out_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
