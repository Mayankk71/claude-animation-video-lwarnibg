"""Download all reference reels from a shared Google Drive folder into raw/.

Usage:
    python scripts/fetch_from_drive.py <drive-folder-url>

The folder must be shared as "Anyone with the link - Viewer". Downloaded files are
renamed to url-safe slugs (lowercase, spaces/punctuation -> hyphens) so every other
script can address a video as raw/<slug>.mp4.
"""

import re
import sys
from pathlib import Path

import gdown

RAW_DIR = Path(__file__).resolve().parent.parent / "raw"


def slugify(name: str) -> str:
    stem = Path(name).stem
    slug = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    return slug or "reel"


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    folder_url = sys.argv[1]
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    downloaded = gdown.download_folder(url=folder_url, output=str(RAW_DIR), quiet=False, use_cookies=False)
    if not downloaded:
        print("No files downloaded — check that the folder is shared as 'Anyone with the link'.")
        sys.exit(1)

    used_slugs: set[str] = set()
    for path_str in downloaded:
        path = Path(path_str)
        if path.suffix.lower() not in {".mp4", ".mov", ".m4v", ".webm"}:
            continue
        slug = slugify(path.name)
        candidate, n = slug, 2
        while candidate in used_slugs:
            candidate, n = f"{slug}-{n}", n + 1
        used_slugs.add(candidate)
        target = RAW_DIR / f"{candidate}{path.suffix.lower()}"
        if path != target:
            path.rename(target)
        print(f"raw/{target.name}")

    print(f"\n{len(used_slugs)} video(s) ready in raw/")


if __name__ == "__main__":
    main()
