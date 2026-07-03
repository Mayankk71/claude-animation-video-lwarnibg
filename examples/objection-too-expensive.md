# Script — Prospect says "it's too expensive"

**Runtime:** ~13s across 6 shots
**Characters:**
- **Sales Rep** — woman, dark hair in a neat high bun (no loose strands crossing the face), gold hoop earrings, cream chunky cable-knit turtleneck sweater, heavy-lidded droopy resting eyes, closed neutral flat mouth at rest.
- **Prospect** — man, bald with a ring of dark curly hair, thick dark eyebrows, heavy-lidded droopy eyes, small round black wire glasses, a pronounced elongated conical nose, black suit jacket over a white shirt and black tie, faint closed-mouth smile line at rest.

**Canonical reference images (generated directly from the Style Bible's invariant character rules — use these, not any earlier version):**
- `references/characters/sales-rep-v2.png`
- `references/characters/prospect-v2.png`

**Setting:** Google Meet call, both on video. Prospect: wood desk, softly blurred bookshelf + framed art + warm table lamp behind him. Sales Rep: wood desk, softly blurred abstract art print + bookshelf + potted plant + warm table lamp behind her.

## Beat map

| Beat | Time | What happens |
|---|---|---|
| Cold open + Hook/Setup (fused) | 0:00–0:04 | Already mid-call. Sales Rep asks for a decision; Prospect states the objection flatly, immediately — no build-up. |
| Minimal conflict | 0:04–0:06 | Sales Rep asks exactly one flat follow-up question. No pushback, no value pitch, no argument. |
| Build-up pause | 0:06–0:08 | The script's longest silence. Camera pushes slowly in on Prospect's static face. |
| Punchline | 0:08–0:11 | Prospect delivers one unbroken sentence — a hyper-specific, mundane detail that undercuts his own objection. |
| Post-punchline hold / CTA | 0:11–0:13 | Cut to Sales Rep's tile, flat, no reply. Hard cut to outro card. |

## Dialogue

**[0:00] Sales Rep:** "So — any thoughts on the proposal?"
**[0:01] Prospect:** "Yeah. It's too expensive."
**[0:04] Sales Rep:** "Too expensive compared to what?"
**[0:06] *(silence — 2s, longest pause in the script)***
**[0:08] Prospect:** "The eleven-dollar oat milk latte I bought waiting for this call to start."
**[0:11] *(silence — 2s trailing hold, no reply from Sales Rep)***

## On-screen text / CTA

Hard cut to static black card: **"LOW BATTERY PITCHES"** / small credit line / yellow ribbon graphic: **"NEW OBJECTION DAILY"**. No resolution shown — the call does not visibly continue. Make this card directly in your video editor (Veo3 can't reliably render clean text) — see `templates/veo3-prompt-template.md`'s Generation practicalities.

## Why this follows the Style Bible

Fuses hook+setup into one exchange (invariant, 36/46), uses exactly one flat follow-up as the only "conflict" with zero escalation (frequent, 34/46), places the single longest pause immediately before the punchline (invariant, 43/46), and lands the punchline as one unbroken, hyper-specific-detail sentence rather than a vague exaggeration (optional pattern, 18/46 + 29/46) — irony/misdirection mechanism: a sincere-sounding budget objection undercut by a petty, specific personal expense. No reaction shot after the punchline (optional, 17/46), ends on a hard cut to a branded card with zero narrative resolution (invariant, 46/46). The punchline is given to the Prospect, matching the "decision-holding/reactive role gets the last word" optional pattern (24/46).

---

# Veo3 Prompt Set — Prospect says "it's too expensive"

**⚠ Generate each shot below as its own separate Veo3 clip. Do not paste multiple shots into one
generation call.** Testing this against a real generation confirmed that combining shots into
one prompt causes the model to compress everything into a single continuous take, which silently
drops the held-silence pause, flattens the punchline into naturalistic (not deadpan) delivery,
and inserts an unprompted reaction shot. See `templates/veo3-prompt-template.md`'s "Generation
practicalities" section for the full explanation — every instruction below is written to counter
that specific failure mode.

**Style keywords (from the Style Bible):** felted-wool/clay stop-motion-*look* CG shader (not real stop-motion — no jitter, no fingerprints, fully smooth motion); heavy-lidded "low battery" eyes on both characters, no blinking; flat downturned mouth held through emotionally loaded lines; elongated nose + small round glasses on the Prospect; animation concentrated on mouth/eyebrows/eyelids only, body completely locked/static; discrete held viseme mouth poses, not fluid lip-sync; locked-off static camera except one permitted slow straight push-in landing on the punchline; warm soft single-source practical light (table lamp) with shallow DOF; fully static background; muted desaturated color palette; no music, no SFX; deadpan low-pitch-variation delivery throughout.

**Attach `references/characters/sales-rep-v2.png` and `references/characters/prospect-v2.png` as image-conditioning input to every single shot generation**, in addition to the text description, for character consistency.

## Shot 1 — Cold open / Hook+Setup (0:00–0:04)

```
Stop-motion-look 3D CG animation, felted-wool clay-texture shader on two
puppet-style characters, matte and fibrous skin with visible fiber
texture, no glossy CG highlights, no set jitter, no visible fingerprints
— fully smooth CG motion underneath a handmade-look material. Static
locked-off wide shot framed as a Google Meet split screen: two video
tiles side by side, labeled "Sales Rep" and "Prospect" in the
lower-left corner of each tile.

Left tile: SALES REP, a woman with dark hair pulled back neatly into a
high bun with no loose strands crossing her face, thick dark eyebrows,
heavy-lidded droopy half-closed eyes, gold hoop earrings, wearing a
cream chunky cable-knit turtleneck sweater, hands clasped calmly on a
wood desk. Behind her, softly blurred: an abstract art print, a
bookshelf, a potted plant, and a warm lit table lamp.

Right tile: PROSPECT, a bald man with a ring of dark curly hair, thick
dark eyebrows, heavy-lidded droopy eyes, small round black wire
glasses, a pronounced elongated conical nose, a faint closed-mouth
smile line at rest, wearing a black suit jacket, white shirt, and black
tie, hands clasped on a wood desk. Behind him, softly blurred: a
bookshelf, framed art, and a warm lit table lamp.

Movement, beat by beat: at the start of the shot, the Sales Rep's mouth
opens and closes through 2-3 discrete held viseme shapes as she speaks
her line; her eyebrows lift very slightly (a few millimeters) on the
word "thoughts" and settle back immediately after. Her eyes do not
change from their heavy-lidded resting openness at any point — no
widening, no extra blink. Her hands, torso, and the Prospect's entire
body remain completely motionless and silent while she speaks. As soon
as she finishes, the Prospect's mouth opens through 1-2 held viseme
shapes for his short reply; his eyebrows and eyes do not move at all
during his line. Neither character blinks anywhere in this shot.

Dialogue: Sales Rep says, flat and matter-of-fact, "So — any thoughts
on the proposal?" Immediately after, with no gap, Prospect replies,
same flat register: "Yeah. It's too expensive." No music, no sound
effects, dialogue only. Camera does not move at any point in this shot.
```
Notes: Establishing two-shot per the shot/reverse-shot default. Both characters deliver flat, low-pitch dialogue with no vocal escalation.

## Shot 2 — Minimal conflict (0:04–0:06)

```
Same static two-tile Meet framing as Shot 1, same felted-wool CG-clean
shader, camera completely motionless throughout.

Movement, beat by beat: the Sales Rep's mouth opens through 2 discrete
held viseme shapes as she asks her line; her eyebrows do not raise, her
eyes do not widen — no argumentative or escalating physical cue of any
kind. The instant she finishes speaking, her mouth returns to its
closed neutral resting shape and does not move again for the rest of
this shot. The Prospect's entire body — face, eyes, mouth, hands — stays
completely motionless and silent for the full duration of this shot; he
does not react to her question in any way.

Dialogue: Sales Rep asks, flat and matter-of-fact, no rising energy:
"Too expensive compared to what?" No music, no SFX.
```
Notes: This is the script's only "conflict" beat — one flat follow-up question, no pushback, no value-defense speech, no physical reaction from either character.

## Shot 3 — Build-up pause (0:06–0:08)

```
Hard cut to an isolated tight close-up on the Prospect alone — the
Sales Rep's tile is fully cropped out of frame. Same felted-wool
clay-look CG shader, matte and fibrous, heavy-lidded unblinking eyes
behind small round glasses, elongated nose, faint closed-mouth smile
line. Slow, continuous, straight-line push-in toward his face — the
only camera movement in the entire piece — beginning at the start of
this shot and continuing smoothly through to the end.

This entire clip shows the character in complete silence and stillness:
no dialogue, no lip movement, no eyebrow movement, no blinking, no
change in expression of any kind, for the full 2-second duration. His
hands remain exactly as clasped as in the previous shot, completely
unmoving. Background (bookshelf, framed art, warm lamp) stays
completely static behind him, softly blurred by shallow depth of field.
No music, no sound effects, no filler movement of any kind — this is a
held silence, the longest pause in the piece, and nothing in the frame
should move except the slow camera push-in itself.
```
Notes: This silence must read as measurably longer and more inert than any other moment in the piece — it is the load-bearing comedic-timing beat per the Style Bible. Generate this as its own dedicated clip; do not let it bleed into the talking shots on either side of it.

## Shot 4 — Punchline (0:08–0:11)

```
Continuous framing with Shot 3's tight close-up on the Prospect (push-in
now settled tight on his face), same static clay/felt shader, no
blinking, faint closed-mouth resting expression before he begins to
speak.

Movement, beat by beat: his mouth opens through a small sequence of
discrete held viseme shapes as he delivers the full line in one
continuous breath with no internal pause between words or clauses. His
eyebrows and eyes do not move at all during delivery — no emphasis
raise, no widening on the reveal. As the line ends, his mouth returns
immediately to its closed neutral resting shape; the rest of his face
does not change.

Dialogue, delivered as one unbroken sentence, completely deadpan, flat
and low-pitch throughout, with the pitch staying level or dropping
slightly at the end — explicitly NOT rising into a question, no
questioning inflection anywhere in the line: "The eleven-dollar oat
milk latte I bought waiting for this call to start." Only his mouth
moves through the held viseme poses; his eyebrows, eyes, hands, and the
rest of his body remain completely locked and static. No music, no
sound effects.
```
Notes: Punchline isolates the Prospect in tight close-up per the invariant punchline-framing rule; delivered as one unbroken escalating-detail sentence anchored on a hyper-specific quantified detail ($11, oat milk latte). The explicit "not a question / no rising inflection" instruction directly addresses the upward inflection that showed up in the first real test generation.

## Shot 5 — Post-punchline hold (0:11–0:13)

```
Hard cut to an isolated static close-up on the Sales Rep alone, the
Prospect's tile fully cropped out. Same felted-wool CG shader,
heavy-lidded droopy eyes unblinking, closed neutral mouth held
completely still. Camera fully locked, no movement of any kind.

For the entire 2-second duration of this shot, her expression does not
change from how it appeared at the end of Shot 2: no surprise, no
eyebrows raising, no eyes widening, no mouth movement, no head tilt, no
new expression forming at any point. She does not reply and does not
react to the line she just heard — this shot is a flat, unreactive
hold, not a reaction shot. Warm table-lamp lighting unchanged. No
music, no sound effects.
```
Notes: The first real test generation inserted an unprompted surprised reaction here (raised eyebrows, widened eyes) — this shot's language exists specifically to prevent that. No reaction or reply is shown; per the Style Bible this is a legitimate, common choice, not a gap to fill.

## Shot 6 — Outro card

**Do not generate this with Veo3.** Make it directly in your video editor (e.g. CapCut): a static black card, centered white/gold serif text reading "LOW BATTERY PITCHES," a small credit line beneath it, and a yellow ribbon-style graphic reading "NEW OBJECTION DAILY" in the lower third. No characters, no motion, no camera movement, no music, no sound effects. Text-rendering in video generation models is unreliable — this is faster and cleaner built as a title slide in editing.

## Continuity notes

Keep both characters' models exactly as shown in `references/characters/sales-rep-v2.png` and `references/characters/prospect-v2.png` across every shot: the Prospect's bald head, ring of dark hair, round black glasses, elongated conical nose, black suit/tie, and heavy-lidded eyes; the Sales Rep's neat high bun, gold hoop earrings, cream cable-knit sweater, and — now corrected to match the Style Bible's invariant rule — heavy-lidded droopy eyes matching the Prospect's degree of heaviness, not wide or alert. Keep each character's own set dressing (Prospect: bookshelf + framed art + lamp; Sales Rep: abstract art print + bookshelf + plant + lamp) and the warm/muted desaturated color grade identical across all shots — the only visual variation across the whole piece should come from reframing (wide two-shot → isolated close-ups), never a location or character-design change, and never a camera movement beyond the single push-in in Shots 3–4. Attach both reference images to every shot's generation call, not just once.
