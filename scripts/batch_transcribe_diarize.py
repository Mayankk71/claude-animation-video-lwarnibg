"""Transcribe+diarize every video in raw/ that doesn't have a transcript yet.

Usage:
    python scripts/batch_transcribe_diarize.py

Loads the whisper/align/diarization models once and reuses them across every
video (unlike calling transcribe_diarize.py once per video), which matters
once you're processing dozens of reels instead of one. Requires HF_TOKEN and
processed/<slug>/audio.wav for each video (run extract_audio.py first).
"""

import os
import sys
from pathlib import Path

import whisperx

from transcribe_diarize import transcribe_one

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        sys.exit("HF_TOKEN env var not set — required for speaker diarization.")

    device = "cpu"
    print("Loading whisper model...")
    asr_model = whisperx.load_model("small", device, compute_type="int8")
    print("Loading diarization model...")
    diarize_model = whisperx.diarize.DiarizationPipeline(token=hf_token, device=device)
    align_cache: dict = {}

    videos = sorted((ROOT / "raw").glob("*.mp4"))
    done, skipped, failed = 0, 0, []
    for video_path in videos:
        slug = video_path.stem
        transcript_path = ROOT / "processed" / slug / "transcript.json"
        if transcript_path.exists():
            skipped += 1
            continue
        try:
            transcribe_one(video_path, asr_model, align_cache, diarize_model, device)
            done += 1
            print(f"[{done + skipped}/{len(videos)}] transcribed {slug}")
        except Exception as e:
            failed.append((slug, str(e)))
            print(f"FAILED {slug}: {e}")

    print(f"\nDone: {done} transcribed, {skipped} already had transcripts, {len(failed)} failed.")
    if failed:
        for slug, err in failed:
            print(f"  - {slug}: {err}")


if __name__ == "__main__":
    main()
