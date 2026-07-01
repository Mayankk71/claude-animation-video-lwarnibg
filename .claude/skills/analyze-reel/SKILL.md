---
name: analyze-reel
description: Runs the full single-video pipeline (preprocess, 9 parallel specialist agents, merge) for one reference reel. Usage: /analyze-reel raw/<slug>.mp4
---

You are acting as the Lead/Orchestrator for this pipeline. Per the project spec, you orchestrate
and merge — you do not perform the specialist analysis yourself; that's the 9 subagents' job.

Input: `$ARGUMENTS` is the path to a video, e.g. `raw/objection-price.mp4`. Derive `<slug>` from
the filename stem.

## Step 1 — Preprocess (shared data, computed once)

Run these in order via Bash, stopping on any failure rather than continuing with partial data:

```
python scripts/extract_metadata.py <video_path>
python scripts/extract_audio.py <video_path>
python scripts/transcribe_diarize.py <video_path>
python scripts/detect_scenes.py <video_path>
python scripts/extract_keyframes.py <video_path>
python scripts/detect_silence.py <video_path>
```

Confirm `processed/<slug>/` now contains: `metadata.json`, `audio.wav`, `transcript.json`,
`subtitles.srt`, `scene_boundaries.json`, `silence_pauses.json`, `keyframes/`.

## Step 2 — Parallel specialist analysis

Dispatch all 9 specialist subagents **in a single message with 9 parallel Agent tool calls**
(story-agent, dialogue-agent, comedy-agent, character-agent, camera-agent, animation-agent,
editing-agent, audio-agent, environment-agent), each told the video slug and instructed to read
only `processed/<slug>/` and write `analysis/<slug>/<their-name>.json`. Do not run them
sequentially — the whole point of a shared preprocessing stage is that they can all work off it
at once with no dependency on each other.

Wait for all 9 to complete and confirm each wrote its file before moving on.

## Step 3 — Merge (you do this yourself, not a subagent)

Read all 9 `analysis/<slug>/*.json` files yourself. Write `analysis/<slug>/merged.json`
combining them under top-level keys matching each agent's name (`story`, `dialogue`, `comedy`,
`character`, `camera`, `animation`, `editing`, `audio`, `environment`), plus a `video_slug` and
`duration_sec` field pulled from `processed/<slug>/metadata.json`.

Then write `analysis/<slug>/merged.md` — a single readable page a human can skim in under a
minute: hook and overall structure, key dialogue lines with timing, why the comedic/relatable
beat works, animation/visual style in plain language, and editing rhythm. This is the file the
user will actually read; the JSON is only for the later pattern-discovery and synthesis stages.

Report back: the slug processed, and a one-line summary of the story hook found, so the user can
sanity-check without opening any files.
