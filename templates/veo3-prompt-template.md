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
- **Every dialogue beat needs an explicit action/expression line for BOTH characters, not just the
  one who's talking.** Don't write "she says X, he reacts" and leave it there — describe what the
  speaking character's face and mouth are doing as they deliver the line, AND separately describe
  what the listening character's face/eyes are doing at that same moment, even if the answer is
  "stays steady, no reaction yet." If a two-character shot has two lines back to back, give this
  same speaker/listener pair of action lines for each line — never let a character go a whole beat
  with no stated expression just because they aren't the one speaking right then. This is what
  actually produces the reactive, alive quality this niche is going for (see the Style Bible's
  "Niche Creative Adaptations" section) — a line of dialogue with no listener reaction described is
  a line where the model is free to leave that character looking dead in-frame.
- **Held-silence beats need their own dedicated shot**, prompted as e.g. "this entire clip shows
  the character in complete silence and stillness — no dialogue, no lip movement, no change in
  expression — for the full duration," not as a pause folded into a longer talking shot.
- **Punchline delivery needs explicit flatness language** — e.g. "delivered as a flat, complete
  declarative statement, not a question, no rising inflection at the end" — directly in the shot
  prompt, since generation models default toward naturalistic vocal escalation unless told
  otherwise.
- **Platform watermarks are unavoidable** (e.g. a small Gemini sparkle icon in-frame) — this is
  not a prompt problem and doesn't need addressing; crop it out in post if it matters.
- **Do not try to prompt a dynamic active-speaker tile highlight at all — leave Meet-tile chrome
  static and add any highlight ring in post-production instead.** An earlier version of this rule
  asked for a highlight ring to appear/disappear on whichever tile is currently speaking. A real
  test generation showed this doesn't work: the highlight appeared on the wrong tile while the
  other character was actually speaking, both tiles lit up at once in two different colors, and a
  highlight lingered on a tile well after that character had stopped talking. This is a timed,
  conditional visual effect tied precisely to audio content, and the model isn't reliably tracking
  it — asking for it just adds confusion without a payoff. If you want the active-speaker highlight
  look, composite it by hand afterward in a video editor, synced exactly to the real dialogue
  timing, rather than prompting for it.
- **When reference images are attached, do not describe character appearance in the shot prompt
  text at all, and state the "reference images are attached" instruction only ONCE per prompt set —
  never repeat it inside every individual shot.** Real test generations kept drifting from the
  attached character images through two earlier, progressively-trimmed attempts at this rule (first
  a full appearance description, then a shortened "must match the reference image" note repeated in
  every shot) — repeating any instructional language about the images inside each shot's actual
  generation text is itself the kind of prompt clutter that competes with image conditioning. State
  once, near the top of the whole prompt set (outside any shot's code block), that reference images
  are attached and must be used as-is; inside each shot's generation text, don't name characters by
  tile position either (see the next bullet) — just point at "the attached reference image" for
  who/what/where, and describe only what the image can't show.
- **Never restate a static composition/layout that's already shown in an attached reference image
  — including the Google Meet split-screen framing itself.** This generalizes the appearance-text
  rule above: it's not just hair/nose/glasses that competes with image conditioning, any redundant
  description of what a reference image already depicts can too, including framing/positioning
  language like "two video tiles side by side, labeled X and Y" or "left tile: SALES REP, right
  tile: PROSPECT" — the layout reference image (`references/layout/gmeet-normal.png`) already shows
  that exact framing, so restating it in text is both redundant and risks the model reconciling two
  slightly different descriptions of the same thing instead of just using the image. The fix: when a
  shot's framing matches an attached reference image, say only something like "the scene and both
  characters are exactly as shown in the attached reference image — animate it," then move straight
  into what the image *can't* convey: motion and dialogue. When a shot's framing doesn't exactly
  match any single reference image (e.g. a cropped close-up), describe only the *change* — the
  cut/reframe itself — not the full composition.
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
- **Characters should actively, visibly react to each other — this supersedes the earlier "subtle
  settled attentiveness" guidance, which still read as lifeless/uncanny in real test generations.**
  This is a deliberate creative choice for the sales-objection niche (not something the source
  reels do — they mostly show zero reaction and avoid eye contact) made because the point of this
  niche's content is legible awkwardness, not a faithful replica of the reference reels' deadpan
  formula. Write real, human-scale reactions: a brief reactive glance toward one's own screen or
  the other participant's tile, a small readable shift in expression — restrained and natural, not
  anime-exaggerated. See the Style Bible's "Niche Creative Adaptations" section for the full
  rationale and for related overrides (naturalistic vocal delivery instead of strict deadpan
  monotone, and an opening silent business beat before dialogue starts).
- **Open on a few seconds of silent business before any dialogue starts**, e.g. a character
  writing something in a notebook while the call connects — not found in the source reels, but
  useful for two reasons: it gives you room to composite a blurred topic-card graphic over the
  opening footage afterward (build it in your video editor, the same way the outro card is built,
  not generated with Veo3), and it's a small natural character beat. Keep this beat itself quiet
  and low-key, no dialogue.
- **The comedic core for this niche is awkwardness — pacing and expression — not a forced
  punchline.** Don't feel obligated to reproduce the source reels' "hyper-specific undercut line"
  shape; held silences and readable discomfort are doing more of the work here than a clever final
  line.
