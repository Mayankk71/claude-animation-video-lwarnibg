---
name: generate-script
description: Generates a new script and Veo3 prompt set for a given sales-objection scenario, using the Style Bible. Usage: /generate-script "prospect says the price is too high"
---

Input: `$ARGUMENTS` is a short description of the objection/scenario (e.g. "prospect says the
price is too high", "prospect says I'll think about it").

Require `style-bible.json` and `style-bible.md` to exist at the repo root — if they don't, stop
and tell the user to run `/build-style-bible` first; do not improvise a style from scratch.

## Step 1 — Read the source of truth

Read `style-bible.json` (for the structured rules and `prompt_generation_guidelines`) and
`templates/script-template.md` and `templates/veo3-prompt-template.md`.

## Step 2 — Write the script

Fill in `templates/script-template.md` for a two-character scene: a sales rep and a prospect on
a video call, hitting the objection in `$ARGUMENTS`, following the Style Bible's structural
rules (beat timing, dialogue voice/rhythm rules, comedic mechanism) as closely as the scenario
allows. Keep total runtime within the Style Bible's typical duration range (should be ~20-25s
per the source reels).

## Step 3 — Write the Veo3 prompt

Fill in `templates/veo3-prompt-template.md`, one prompt block per beat/shot, using
`prompt_generation_guidelines.veo3_style_keywords` from the Style Bible so the visual/animation
style matches what was actually found across the 47 reels — not a generic stop-motion
description.

## Step 4 — Save and report

Save the combined result to `examples/<scenario-slug>.md` (slugify `$ARGUMENTS`). Report a short
summary to the user with the punchline and the total runtime, and note this file is what they
should read — no JSON to open.
