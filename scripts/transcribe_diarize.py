"""Transcribe audio with word-level timestamps and speaker labels via WhisperX.

Usage:
    python scripts/transcribe_diarize.py raw/<slug>.mp4

Requires processed/<slug>/audio.wav (run extract_audio.py first) and an HF_TOKEN
env var with the pyannote/speaker-diarization model license accepted at
huggingface.co (one-time manual step).

Writes processed/<slug>/transcript.json and processed/<slug>/subtitles.srt
"""

import json
import os
import sys
from datetime import timedelta
from pathlib import Path

import whisperx

ROOT = Path(__file__).resolve().parent.parent


def to_srt_timestamp(seconds: float) -> str:
    td = timedelta(seconds=max(0.0, seconds))
    total_ms = int(td.total_seconds() * 1000)
    hh, rem = divmod(total_ms, 3_600_000)
    mm, rem = divmod(rem, 60_000)
    ss, ms = divmod(rem, 1000)
    return f"{hh:02d}:{mm:02d}:{ss:02d},{ms:03d}"


def write_srt(segments: list[dict], path: Path) -> None:
    lines = []
    for i, seg in enumerate(segments, start=1):
        speaker = f"[{seg.get('speaker', 'SPEAKER')}] " if seg.get("speaker") else ""
        lines.append(str(i))
        lines.append(f"{to_srt_timestamp(seg['start'])} --> {to_srt_timestamp(seg['end'])}")
        lines.append(f"{speaker}{seg['text'].strip()}")
        lines.append("")
    path.write_text("\n".join(lines))


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

    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        sys.exit("HF_TOKEN env var not set — required for speaker diarization.")

    device = "cpu"
    model = whisperx.load_model("small", device, compute_type="int8")
    audio = whisperx.load_audio(str(audio_path))
    result = model.transcribe(audio, batch_size=8)

    align_model, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], align_model, metadata, audio, device)

    diarize_model = whisperx.diarize.DiarizationPipeline(token=hf_token, device=device)
    diarize_segments = diarize_model(audio)
    result = whisperx.assign_word_speakers(diarize_segments, result)

    segments = [
        {
            "start": seg["start"],
            "end": seg["end"],
            "speaker": seg.get("speaker", "UNKNOWN"),
            "text": seg["text"].strip(),
            "word_count": len(seg["text"].split()),
        }
        for seg in result["segments"]
    ]

    transcript = {"slug": slug, "language": result.get("language"), "segments": segments}
    (out_dir / "transcript.json").write_text(json.dumps(transcript, indent=2))
    write_srt(segments, out_dir / "subtitles.srt")
    print(f"processed/{slug}/transcript.json ({len(segments)} segments)")


if __name__ == "__main__":
    main()
