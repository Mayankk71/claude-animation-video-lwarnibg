# Reel-to-Prompt Style Analysis System

This repo reverse-engineers the creative formula behind a set of reference short-form
animation reels (stop-motion, ~20-25s each) so that formula can be reused to write new
scripts and generate Veo3 prompts for an unrelated niche (sales-objection skits).

It does **not** copy any reference video's content — it extracts the recurring *structural,
comedic, visual, and editing patterns* across the whole set, separates true signature from
one-off choices, and turns that into a reusable "Style Bible."

## Pipeline at a glance

1. `python scripts/fetch_from_drive.py <drive-folder-url>` — downloads all reference videos
   from a shared Google Drive folder into `raw/<slug>.mp4`.
2. `/analyze-reel raw/<slug>.mp4` — preprocesses one video (transcript, subtitles, scene
   boundaries, keyframes, silence timing, metadata — written once to `processed/<slug>/`),
   then fans out 9 specialist agents in parallel to analyze it, then merges their output into
   `analysis/<slug>/merged.json` + `merged.md`. Repeat for every reel (pilot on 2-3 first).
3. `/build-style-bible` — once all reels are analyzed, finds patterns across all of them
   (invariant / frequent / optional / one-off) and synthesizes `style-bible.json` +
   `style-bible.md`, the reusable knowledge base.
4. `/generate-script "<objection or scenario>"` — uses the Style Bible + `templates/` to
   produce a new script and a Veo3-ready generation prompt under `examples/`.

Reference videos only need to be (re-)analyzed when new examples are added — step 4 reuses
the Style Bible indefinitely.

## What to read vs. what to ignore

- **Read**: any `.md` file — `analysis/<slug>/merged.md`, `style-bible.md`, `examples/*.md`.
  These are plain-English and are the actual deliverables.
- **Ignore**: the paired `.json` files. They exist only so agents can hand data to each other
  reliably (9 specialists → merge → pattern discovery → synthesis).

## Directory roles

- `raw/` — source videos (gitignored, not committed: size + third-party content).
- `processed/` — shared preprocessing output per video (gitignored, regenerable from `raw/`).
- `analysis/` — per-video specialist findings + merged breakdown (committed).
- `style-bible.{json,md}` — the master synthesized formula (committed).
- `templates/` — fill-in-the-blank script and Veo3 prompt templates.
- `examples/` — generated scripts/prompts for specific objection scenarios (committed).
- `.claude/agents/` — the 11 specialist/orchestration subagents.
- `.claude/skills/` — the 3 slash commands (`analyze-reel`, `build-style-bible`, `generate-script`).

## Setup

```
apt-get install -y ffmpeg
pip install -r scripts/requirements.txt
```

`transcribe_diarize.py` needs a Hugging Face token with the `pyannote/speaker-diarization`
model license accepted (one-time, manual, at huggingface.co — can't be automated on your
behalf). Export it as `HF_TOKEN` before running that script.
