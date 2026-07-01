"""Pull one keyframe per detected scene, plus periodic samples, for visual analysis.

Usage:
    python scripts/extract_keyframes.py raw/<slug>.mp4

Requires processed/<slug>/scene_boundaries.json (run detect_scenes.py first).
Writes processed/<slug>/keyframes/scene-<i>.jpg and periodic-<n>.jpg
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PERIODIC_INTERVAL_SEC = 1.0


def extract_frame(video_path: Path, timestamp: float, out_path: Path) -> None:
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-ss", f"{timestamp:.3f}",
            "-i", str(video_path),
            "-frames:v", "1",
            "-q:v", "2",
            str(out_path),
        ],
        check=True,
        capture_output=True,
    )


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    video_path = Path(sys.argv[1])
    slug = video_path.stem
    out_dir = ROOT / "processed" / slug
    scenes_path = out_dir / "scene_boundaries.json"
    if not scenes_path.exists():
        sys.exit(f"Missing {scenes_path} — run detect_scenes.py first.")

    keyframes_dir = out_dir / "keyframes"
    keyframes_dir.mkdir(parents=True, exist_ok=True)

    scenes = json.loads(scenes_path.read_text())["scenes"]
    for scene in scenes:
        mid = (scene["start"] + scene["end"]) / 2
        extract_frame(video_path, mid, keyframes_dir / f"scene-{scene['index']}.jpg")

    duration = scenes[-1]["end"] if scenes else 0.0
    n = 0
    t = 0.0
    while t < duration:
        extract_frame(video_path, t, keyframes_dir / f"periodic-{n}.jpg")
        t += PERIODIC_INTERVAL_SEC
        n += 1

    print(f"processed/{slug}/keyframes/ ({len(scenes)} scene frames, {n} periodic frames)")


if __name__ == "__main__":
    main()
