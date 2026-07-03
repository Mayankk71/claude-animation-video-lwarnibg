# Script — Prospect says "it's too expensive" → "I need to think about it"

**Runtime:** ~12s across 5 generated shots + outro card
**Characters:**
- **Sales Rep** — woman, dark hair in a neat high bun (no loose strands crossing the face), gold hoop earrings, cream chunky cable-knit turtleneck sweater, heavy-lidded droopy resting eyes, closed neutral flat mouth at rest. (Human-reference only — see "no appearance text in shot prompts" below.)
- **Prospect** — man, bald with a ring of dark curly hair, thick dark eyebrows, heavy-lidded droopy eyes, small round black wire glasses, a pronounced elongated conical nose, black suit jacket over a white shirt and black tie, faint closed-mouth smile line at rest. (Human-reference only.)

**Canonical reference images:**
- `references/characters/sales-rep-v2.png`
- `references/characters/prospect-v2.png`
- `references/layout/gmeet-active-speaker.png` — reference for the highlighted/glowing tile border shown around whichever character is currently speaking
- `references/layout/gmeet-normal.png` — reference for the plain, unhighlighted tile border shown when a character is not speaking

**No appearance text in shot prompts.** The character bullets above are for your own reference only. Every Veo3 shot prompt below states only that reference images are attached and must be animated exactly as shown — it does not re-describe hair, nose, glasses, or clothing in prose anywhere. A real test generation kept drifting from the attached reference images until this appearance text was removed entirely, even after an earlier attempt only trimmed it down rather than cutting it completely.

**Setting:** Google Meet call, both on video. Prospect: wood desk, softly blurred bookshelf + framed art + warm table lamp behind him. Sales Rep: wood desk, softly blurred abstract art print + bookshelf + potted plant + warm table lamp behind her.

## Beat map

| Beat | Time | What happens |
|---|---|---|
| Silent open (niche adaptation) | 0:00–0:02 | No dialogue. Sales Rep writes something in a notebook; Prospect sits settled. Canvas for a blurred topic-card overlay added in post. |
| Opening exchange | 0:02–0:05 | Sales Rep names the price; Prospect visibly reacts, then objects. |
| Reactive pause (niche adaptation) | 0:05–0:07 | Sales Rep has a small, legible reaction beat — a glance to the side — before her rebuttal. |
| Interrupted rebuttal (niche adaptation) | 0:07–0:10 | Sales Rep starts her comeback; Prospect audibly talks over her with a stalling line. |
| Closing hold | 0:10–0:12 | Sales Rep settles into a flat, resigned stillness. Hard cut to outro card. |

## Dialogue

**[0:02] Sales Rep:** "So it's only $30 a month."
**[0:03] Prospect:** "That's too expensive."
**[0:05–0:07] *(pause — Sales Rep's reactive beat)***
**[0:07] Sales Rep:** "It's cheaper than your—" *(cut off)*
**[0:08] Prospect (talking over her):** "Noo... I need to think about it."

## On-screen text / CTA

Hard cut to static black card: **"LOW BATTERY PITCHES"** / small credit line / yellow ribbon graphic: **"NEW OBJECTION DAILY"**. No resolution shown — the call does not visibly continue. Make this card, and the blurred topic-card overlay for Shot 1, directly in your video editor (Veo3 can't reliably render clean text) — see `templates/veo3-prompt-template.md`'s Generation practicalities.

## Why this follows the Style Bible — and where it deliberately doesn't

**Still reel-evidence-grounded:** the felted-wool CG material and character design, the fully static locked-off camera with hard cuts (never a zoom), the single unchanging location, the warm single-source lighting and muted palette, complete silence except spoken dialogue, and the fused cold-open (invariant, 43/46 — the objection surfaces within the first line or two once dialogue starts).

**Deliberately overridden for this niche, per explicit creative direction** (see the Style Bible's "Niche Creative Adaptations" section): both characters now visibly react to each other (a reactive glance, a flicker of discomfort) instead of staying inert and avoiding eye contact, which is what the source reels actually do; vocal delivery is naturalistic/restrained-awkward rather than strict deadpan monotone; the opening silent business beat and the mid-script interruption aren't reel-sourced at all. The reasoning: the source reels' formula was built for a same-room couple, not a Google Meet call, and the actual goal for this niche is legible awkwardness — the pauses and the expressions — rather than a faithful reproduction of the reels' punchline mechanism.

---

# Veo3 Prompt Set — Prospect says "it's too expensive" → "I need to think about it"

**⚠ Generate each shot below as its own separate Veo3 clip. Do not paste multiple shots into one
generation call.** Combining shots into one prompt causes the model to compress everything into a
single continuous take, eating pauses and flattening delivery. See `templates/veo3-prompt-template.md`'s
"Generation practicalities" section for the full explanation.

**Style keywords (from the Style Bible):** felted-wool/clay stop-motion-*look* CG shader (not real stop-motion — no jitter, no fingerprints, fully smooth motion); heavy-lidded "low battery" eyes, no blinking; elongated nose + small round glasses on the Prospect; animation concentrated on mouth/eyebrows/eyelids, body otherwise still; discrete held viseme mouth poses; locked-off static camera, hard cuts between speakers (never a zoom), one permitted slow push-in reserved for a key beat; warm soft single-source practical light with shallow DOF; fully static background; muted desaturated palette; complete silence except spoken dialogue, nothing added for "realism"; the currently-speaking character's Meet tile shows a highlighted glowing border while the other stays plain (niche UI addition). **Niche creative adaptations layered on top (not reel-sourced):** characters visibly, restrainedly react to each other — a reactive glance, a flicker of discomfort — rather than staying inert; vocal delivery is naturalistic/restrained-awkward, not strict deadpan monotone; an opening silent business beat before dialogue starts.

**Reference images are attached for each character and for both Meet-tile highlight states — animate the characters exactly as shown in `references/characters/sales-rep-v2.png` and `references/characters/prospect-v2.png`. Do not describe their appearance in any shot prompt text below.**

## Shot 1 — Silent open / niche pacing beat (0:00–0:02)

```
Stop-motion-look 3D CG animation, felted-wool clay-texture shader,
matte and fibrous skin with visible fiber texture, no glossy CG
highlights, no set jitter, no visible fingerprints — fully smooth CG
motion underneath a handmade-look material. The scene and both
characters are exactly as shown in the attached reference image —
animate it.

Neither video tile has a highlighted border right now — both stay in
their plain, quiet resting state for the entire shot, since neither
person is speaking.

Movement, beat by beat: the Sales Rep looks down, quietly writing
something on a notepad on her desk, her pen moving in small, natural,
repeated strokes — this is the only movement she makes. The Prospect
sits still and settled, looking toward his own screen, doing nothing
else. No dialogue from either character. Keep all motion low-key and
unhurried, not exaggerated.

Complete silence — no dialogue, no music, no sound effects, no ambient
room tone, nothing added for "realism." Camera does not move at any
point in this shot.
```
Notes: This shot is the canvas for a blurred topic-card graphic (e.g. "OBJECTION: IT'S TOO EXPENSIVE") composited over the footage afterward in your video editor — do not add text or blur in the Veo3 generation itself. Niche creative addition, not reel-sourced: buys pacing room before dialogue starts and doubles as a small character beat.

## Shot 2 — Opening exchange (0:02–0:05)

```
Same framing as Shot 1, exactly as shown in the attached reference
image, same felted-wool CG-clean shader, camera completely motionless
throughout.

The instant the Sales Rep begins speaking, a soft glowing colored ring
appears around the border of her video tile, showing she's the one
talking, while the Prospect's tile stays plain. The instant she
finishes, that glow disappears from her tile and immediately appears
around the Prospect's tile instead for the duration of his reply, then
disappears again the instant he finishes.

Movement, beat by beat: the Sales Rep delivers her line in a light,
casual, matter-of-fact tone, mouth moving through natural viseme
shapes. As she finishes, the Prospect visibly reacts before he speaks —
a brief, readable flicker of discomfort: his eyebrows draw in slightly
and his mouth tightens for a beat. Keep this small, human, and
restrained — not exaggerated or cartoonish. He then replies, flat but
genuine, not robotic-deadpan.

Dialogue: Sales Rep, warm and casual: "So it's only $30 a month." After
a brief natural beat, Prospect, a little flat and resigned: "That's too
expensive." Complete silence otherwise — no ambient room tone, no
music, no sound effects, nothing added for "realism."
```
Notes: The objection lands almost immediately once dialogue starts, per the reel-evidence fused hook+setup pattern. The Prospect's visible discomfort here is a niche creative adaptation — restrained, human-scale reaction, overriding the source reels' inert-listening default.

## Shot 3 — Reactive pause (0:05–0:07)

```
Hard cut to an isolated close-up on the Sales Rep alone, exactly as
shown in her attached reference image, the Prospect out of frame. Same
felted-wool CG shader.

If her tile's border is visible within this close-up, it stays plain
and unhighlighted for the entire shot — she isn't speaking.

Movement, beat by beat: no dialogue. She takes a short, visible beat
processing what he just said: her eyes flick briefly to the side, as
if glancing toward her own screen or his tile — a small, legible
reaction — then settle back forward. This is one small movement, held
briefly, then over; restrained, not an exaggerated expression. No other
part of her face or body moves.

Complete silence — no dialogue, no music, no sound effects, no ambient
room tone, nothing added for "realism."
```
Notes: This is a niche creative adaptation, not reel-sourced (the source reels avoid this kind of legible reaction) — see the Style Bible's Niche Creative Adaptations section. This beat is where the script's awkwardness actually lives, not in a punchline.

## Shot 4 — Interrupted rebuttal (0:07–0:10)

```
Hard cut back to the same framing as Shot 2, exactly as shown in the
attached reference image, same felted-wool CG-clean shader, camera
completely motionless throughout.

The instant the Sales Rep begins speaking, a glowing colored ring
appears around her tile's border while his stays plain. Partway
through her line, the instant the Prospect starts talking over her,
that same glow appears around his tile too — for a brief moment both
tiles glow at once, since both people are talking simultaneously, the
way a real video call shows it. As her line is cut off, the glow
disappears from her tile; his tile keeps glowing for the rest of his
line, then the glow disappears the instant he finishes.

Movement, beat by beat: the Sales Rep begins her rebuttal with the same
light, confident delivery as Shot 2. Before she can finish, the
Prospect visibly cuts in: his mouth starts moving partway through her
sentence — an audible interruption, not a clean turn-taking exchange.
His own expression shows mild discomfort/reluctance as he does it,
eyebrows slightly drawn, a stalling quality to his delivery. The Sales
Rep's mouth stops moving abruptly as she's cut off; a brief, readable
flicker of surprise/mild frustration crosses her face — small and
restrained, not exaggerated — as she registers being interrupted, then
she holds still for the remainder of the shot.

Dialogue: Sales Rep, warm and confident, begins: "It's cheaper than
your—" and is audibly cut off mid-sentence. Talking over her, Prospect,
soft, hesitant, a little whiny and reluctant — genuinely stalling, not
flat deadpan: "Noo... I need to think about it." Complete silence
otherwise — no ambient room tone, no music, no sound effects, nothing
added for "realism."
```
Notes: The interruption and both characters' visible reactions to it are the centerpiece niche creative adaptation in this script — deliberately more expressive than the source reels' inert-listening default (see the Style Bible's Niche Creative Adaptations section). Keep the overlap brief and legible, not chaotic.

## Shot 5 — Closing hold (0:10–0:12)

```
Hard cut to an isolated close-up on the Sales Rep alone, exactly as
shown in her attached reference image, the Prospect out of frame. Same
felted-wool CG shader.

If her tile's border is visible within this crop, it stays plain and
unhighlighted for the entire shot — she isn't speaking and doesn't
reply.

Movement, beat by beat: no dialogue. Her expression settles into a
small, restrained, resigned stillness — the mild frustration from Shot
4 fades into a flat, quiet "well, that's that" beat. One small, subtle
settle of her shoulders, nothing more. Hold essentially still for the
remainder of the shot.

Complete silence — no music, no sound effects, no ambient room tone,
nothing added for "realism."
```
Notes: A restrained, human closing beat — awkward stillness rather than a punchline reaction, matching the niche's actual comedic core (pacing and expression, not a forced final line).

## Shot 6 — Outro card

**Do not generate this with Veo3.** Make it directly in your video editor (e.g. CapCut): a static black card, centered white/gold serif text reading "LOW BATTERY PITCHES," a small credit line beneath it, and a yellow ribbon-style graphic reading "NEW OBJECTION DAILY" in the lower third. No characters, no motion, no camera movement, no music, no sound effects. Text-rendering in video generation models is unreliable — this is faster and cleaner built as a title slide in editing.

## Continuity notes

Keep both characters' models exactly as shown in `references/characters/sales-rep-v2.png` and `references/characters/prospect-v2.png` across every shot — attach both images (plus the two Meet-layout images for the two-tile shots) to every single generation call and rely on them entirely for appearance and composition. **None of the shot prompts above describe hair, nose, glasses, clothing, or the Google Meet split-screen layout in prose** — through several rounds of trimming, first appearance text and then the tile-position/layout description ("two tiles side by side," "left tile / right tile") both turned out to be redundant with what the attached reference images already show, and re-stating either one in text risked confusing the model rather than helping it. Every shot now just points at "the attached reference image" for scene, character, and framing, and only describes what a still image can't show: motion, dialogue, and timed transitions like the active-speaker highlight. Keep each character's own set dressing (Prospect: bookshelf + framed art + lamp; Sales Rep: abstract art print + bookshelf + plant + lamp) and the warm/muted desaturated color grade identical across all shots — the only visual variation across the whole piece should come from reframing (wide two-shot → isolated close-ups), never a location or character-design change, and never a camera movement beyond the source reels' static-camera-plus-hard-cuts default (no zooms).

Also keep the active-speaker tile highlight behavior consistent across every shot, per `references/layout/gmeet-active-speaker.png` (highlighted border reference) and `references/layout/gmeet-normal.png` (plain border reference), including the brief dual-highlight moment during Shot 4's interruption. This is a niche-specific UI-realism addition, not a trait sourced from the reference reels.

**On the reactivity adjustment (all shots except the outro):** this script deliberately overrides the source reels' "avoid eye contact, stay inert while listening" default. Both characters now visibly, restrainedly react to each other — a reactive glance, a flicker of discomfort, a visible interruption — because the actual goal for this niche is legible, relatable awkwardness rather than a faithful reproduction of the reels' deadpan formula, which was built for a same-room couple, not a Google Meet call. Keep every reaction human-scale and restrained — explicitly not anime-exaggerated — a small real reaction, not a big cartoon one. See the Style Bible's "Niche Creative Adaptations" section for the full rationale and for the related opening-silent-beat and naturalistic-vocal-delivery overrides.
