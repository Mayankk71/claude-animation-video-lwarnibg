"""Detect shot/scene boundaries via PySceneDetect's content-aware detector.

Usage:
    python scripts/detect_scenes.py raw/<slug>.mp4

Writes processed/<slug>/scene_boundaries.json
"""

import json
import sys
from pathlib import Path

from scenedetect import ContentDetector, SceneManager, open_video

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    video_path = Path(sys.argv[1])
    slug = video_path.stem
    out_dir = ROOT / "processed" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    video = open_video(str(video_path))
    scene_manager = SceneManager()
    # Reels are short and fast-cut; a lower threshold catches subtle cuts a
    # feature-film default would miss.
    scene_manager.add_detector(ContentDetector(threshold=24.0, min_scene_len=3))
    scene_manager.detect_scenes(video=video)
    scene_list = scene_manager.get_scene_list()

    scenes = [
        {
            "index": i,
            "start": start.get_seconds(),
            "end": end.get_seconds(),
        }
        for i, (start, end) in enumerate(scene_list)
    ]

    if not scenes:
        duration = video.duration.get_seconds() if video.duration else 0.0
        scenes = [{"index": 0, "start": 0.0, "end": duration}]

    (out_dir / "scene_boundaries.json").write_text(json.dumps({"slug": slug, "scenes": scenes}, indent=2))
    print(f"processed/{slug}/scene_boundaries.json ({len(scenes)} scenes)")


if __name__ == "__main__":
    main()
