---
name: build-style-bible
description: Runs pattern discovery and style synthesis across every reel already processed by /analyze-reel, producing the reusable Style Bible. Usage: /build-style-bible
---

You are acting as the Lead/Orchestrator. Run this only after every reference reel has been
through `/analyze-reel` — check first with Glob for `analysis/*/merged.json` and tell the user
how many reels are covered before proceeding (if it's a small fraction of the full set, confirm
with the user whether they want to proceed now or wait until more are analyzed).

## Step 1 — Pattern discovery

Dispatch the `pattern-discovery-agent` (single Agent call — this step is inherently
cross-video, not parallelizable per video). It reads all `analysis/*/merged.json` and writes
`pattern-discovery.json` at the repo root.

## Step 2 — Style synthesis

Once `pattern-discovery.json` exists, dispatch the `style-synthesizer-agent`. It reads
`pattern-discovery.json` and writes `style-bible.json` and `style-bible.md` at the repo root.

## Step 3 — Report

Read `style-bible.md` yourself and give the user a short summary (3-5 bullets) of the strongest
invariant patterns found, so they can sanity-check it against the reels they actually watched
before relying on it for script/prompt generation.
