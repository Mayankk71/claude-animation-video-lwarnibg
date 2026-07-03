<!--
Fill-in-the-blank Veo3 prompt template consumed by /generate-script.
Style keywords must come from style-bible.json's prompt_generation_guidelines.veo3_style_keywords
— do not invent a visual style not backed by the Style Bible.
-->

# Veo3 Prompt Set — {{SCENARIO}}

**Generate each shot below as its own separate Veo3 clip. Do not combine multiple shots into
one generation call** — see "Generation practicalities" at the bottom of this file for why.

**Style keywords (from the Style Bible):** {{VEO3_STYLE_KEYWORDS}}

**Reference images:** {{REFERENCE_IMAGE_PATHS}} <!-- attach as image-conditioning input to every
shot generation if the tool supports it, in addition to the text description -->

## Shot 1 — {{BEAT_NAME}} ({{T_START}}–{{T_END}})

```
{{PROMPT_TEXT}}
```
Notes: {{SHOT_NOTES}} <!-- camera, animation technique, lighting/color callouts specific to this shot -->

## Shot 2 — {{BEAT_NAME}} ({{T_START}}–{{T_END}})

```
{{PROMPT_TEXT}}
```
Notes: {{SHOT_NOTES}}

<!-- repeat one block per shot in the beat map; keep shot count/pacing consistent with the
     Style Bible's editing rules (cut frequency, avg shot length) -->

## Continuity notes

{{CONTINUITY_NOTES}} <!-- character appearance, set, and color palette to keep consistent across all shots -->

## Generation practicalities

Lessons learned from actually testing this pipeline against a real Veo3/Gemini generation —
apply these to every prompt this template produces, not just as a one-off fix:

- **One shot = one generation.** Veo3/Gemini caps a single generation at roughly 8-10 seconds.
  Pasting multiple beats into one combined prompt causes the model to compress everything into
  one continuous take — this is what silently eats held-silence pauses, flattens the punchline
  delivery, and drops the outro card. Always generate each `## Shot N` block as its own separate
  clip, then assemble them in a video editor afterward.
- **Spell out every movement and reaction literally, not just in mood language.** Don't write
  "she looks surprised" or "he reacts flatly" and assume the model infers the right degree.
  Write the actual physical beat: which feature moves, how far, in what order, and what stays
  completely still. E.g. instead of "deadpan reaction," write "his mouth stays in its resting
  closed-line position, eyebrows do not move, eyes stay at their existing heavy-lidded openness
  — no new expression forms at any point in this shot." This applies to every shot, not only the
  ones that are explicitly about stillness or a reaction — vague direction is exactly what let
  an unprompted surprised reaction slip into a real test generation.
- **Held-silence beats need their own dedicated shot**, prompted as e.g. "this entire clip shows
  the character in complete silence and stillness — no dialogue, no lip movement, no change in
  expression — for the full duration," not as a pause folded into a longer talking shot.
- **Punchline delivery needs explicit flatness language** — e.g. "delivered as a flat, complete
  declarative statement, not a question, no rising inflection at the end" — directly in the shot
  prompt, since generation models default toward naturalistic vocal escalation unless told
  otherwise.
- **Platform watermarks are unavoidable** (e.g. a small Gemini sparkle icon in-frame) — this is
  not a prompt problem and doesn't need addressing; crop it out in post if it matters.
- **State the active-speaker tile highlight explicitly in every shot that shows Meet-tile chrome.**
  Real Google Meet puts a colored highlight ring around whichever participant's tile is currently
  producing audio. Every shot prompt must say, in plain terms, whose tile is highlighted right now
  and why: highlight the currently-speaking character's tile border for exactly the span they're
  talking (matching `references/layout/gmeet-active-speaker.png`), keep the other character's tile
  in its plain unhighlighted state (matching `references/layout/gmeet-normal.png`), and show
  **neither** tile highlighted during a shared silence/pause beat. If a shot's framing crops down
  to a single character's tile, still state explicitly whether that tile's border (if visible in
  frame) is highlighted or plain for that beat — don't leave it implicit. This is a sales-objection-
  niche UI-realism addition, not a trait found in the source reels (see the Style Bible's Prompt
  and Script Generation Guidelines section for how it's flagged there).
- **When reference images are attached, don't re-describe appearance at length in the text
  prompt — a real test generation drifted away from the attached character images, and the
  likely cause is a long freeform appearance description in the text competing with the image
  conditioning.** Identify each character briefly by name/role only (e.g. "SALES REP" / "PROSPECT")
  and state once, plainly, that their appearance must match the attached reference image exactly
  with no deviation — do not restate hair, nose, glasses, clothing, etc. in prose in every shot.
  Save the full appearance description for the human-readable character section at the top of the
  script file (for your own reference), not for the generation prompt text itself.
- **State explicitly that there is no ambient or background audio of any kind.** A real test
  generation added its own room tone / ambient noise unprompted, apparently to make the scene
  read as more "authentic." Don't just say "no music, no SFX" — say it as a hard negative in every
  shot: "complete silence except the spoken dialogue itself — no ambient room tone, no rustling,
  no incidental environmental sound, nothing added for realism."
- **A static camera and hard cuts are the real mechanism for shifting focus between speakers —
  not a zoom.** It's tempting to ask for a push-in/pull-back/push-in choreography to visually
  follow the conversation, but the source reels essentially never do this (a zoom-out camera move
  appears in only 1 of 46 reference reels, flagged in its own analysis as the sole exception). What
  actually shifts attention between speakers in the other 45 is a **hard cut** to the other
  character's static shot — keep using shot/reverse-shot cuts for this, not continuous camera
  movement, and reserve the one permitted push-in exclusively for landing on the punchline.
- **"Deadpan and static" is not the same as "checked out" — a fully inert listening character can
  read as lifeless/uncanny in a real generation even though it's technically correct.** It's a
  legitimate adaptation choice (not something found in the source reels, which mostly show zero
  reaction) to give the listening character a small amount of quiet, attentive stillness — e.g.
  eyes remain steady and settled rather than described as "completely motionless" — as long as it
  stops well short of a visible reaction, an eyebrow move, a blink, or eye contact with the other
  character. Keep this subtle and only apply it to shots where a character is silently listening,
  never to a shot that is deliberately staging "no reaction" to a punchline (that withheld-reaction
  choice is real, evidence-backed style and should stay fully inert).
