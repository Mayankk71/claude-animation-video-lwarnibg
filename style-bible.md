# Style Bible

**Source:** synthesized from `pattern-discovery.json`, which cross-referenced specialist analysis of all **46** reference reels ("Low Battery People").
**Purpose:** a durable, reusable reference for `/generate-script` and Veo3 prompt construction for the sales-objection-skit niche. This document should not need to be regenerated unless new reference reels are analyzed.

## How to read the classifications

Every rule below is tagged with a classification and an evidence count, both traced directly to `pattern-discovery.json`. Nothing here is a new claim invented for this document.

| Tag | Meaning | Rough prevalence | How to treat it |
|---|---|---|---|
| **invariant** | Holds across nearly the whole set | typically 40+/46 | Hard rule — break only with strong justification |
| **frequent** | Clear majority, not universal | roughly 24-39/46 | Default choice; deviate only when the scenario calls for it |
| **optional** | Recurs but isn't the majority | roughly 7-24/46 | Legitimate, never required; use when it fits |
| **one_off** | Only 1-3 of 46 reels | 1-3/46 | Not house style — reference only |

### The three format outliers — do not use as templates

Three reels break from the dominant format hard enough that the user flagged them explicitly. **Do not treat any of these as the house style, and do not let `/generate-script` default toward them:**

1. **"Then vs Now" montage** (`lowbattterypeople-1780817666...`) — a multi-location relationship montage spanning 6+ distinct settings with almost no dialogue, resolving on a deadpan domestic punchline instead of the usual single static two-shot. Also one of the sources of the rapid fast-cut editing outlier below.
2. **"Paul" monologue with live-action B-roll** (`lowbattterypeople-1781353439...`) — a direct-to-camera mock-motivational parody intercut with live-action product B-roll (watch, coffee, pen), punctured by a submissive reveal from an unseen off-screen character. Also drives the fast-cut editing outlier.
3. **Fast-cut restaurant piece** (`lowbattterypeople-1780666530...`) — rapid-fire fast-cut editing (10-18+ cuts, sub-1-second average shot length) for mock-commercial pacing, versus the dominant slow, low-cut, two-shot format.

Everything else in this document describes the other 43-45 reels, which converge tightly on a single reusable formula.

---

## 1. Structure (Story / Screenplay)

### Runtime and format
The reference reels are dramatically shorter than the ~20-25s the pipeline docs originally assumed: **runtime clusters at roughly 9.5-17.5 seconds** (invariant, 45/46), staged as a **single-scene micro-sketch** — one location, one continuous beat of action, no scene breaks. When adapting to sales-objection skits, target this same compressed runtime rather than padding toward 20-25s; the format's comedic engine (see Comedy, below) depends on brevity and a tight, held silence, not on a longer build.

### Cold open (invariant, 43/46)
Every reel begins **already in progress**. There is no establishing shot, no scene-setting narration, no "Meet Dave, he's about to..." setup. The camera simply cuts in mid-conversation or mid-argument. For the sales-objection adaptation: open the clip with the rep and prospect already mid-call — the objection surfaces within the first line or two, not built up to.

### Hook and setup are fused, not staged (frequent, 36/46)
Unlike a classical hook → setup → escalation structure, the reference reels compress the hook and setup into **one continuous exchange**. The premise and the first comedic beat land almost simultaneously rather than in separate escalating scenes. Concretely: don't write a "here's our situation" line followed by a separate "and here's the twist forming" line — collapse them into 1-2 lines that do both jobs at once.

### No external conflict (frequent, 34/46)
There is essentially never a physical obstacle or an escalating argument. The entire "conflict" of the scene is either:
- a **held silence**, or
- **one** skeptical follow-up question.

That's it — no raised voices, no back-and-forth arguing, no third beat of escalation. For sales-objection skits, this means: after the objection is stated, the rep gets at most one clarifying/pushback line before the scene resolves. Do not write a multi-round negotiation.

### Ending: hard cut to a branded outro card (invariant, 46/46)
Every single reel — no exceptions — ends on a **hard cut to a static black outro card**. There is no narrative resolution, no reply to the punchline, no character "button" moment after the joke. The card itself frequently carries two additional elements:
- A **yellow ticket/ribbon graphic** reading "NEW EPISODE DAILY" as an implicit come-back-tomorrow CTA (frequent, 39/46).
- An **"Episode NN"** number, often with an episode-specific title (e.g., "THAT LOOK", "MARRIAGE TRANSLATION"), burned into the corner of the *opening* hook shot, not the outro card itself (frequent, 30/46).

For the sales-objection niche, this translates to: end on a hard cut to a static branded card immediately after the punchline's silence — no "and then the call continues," no visible resolution of the objection.

### Beat-by-beat timing map

| Beat | Timing | Evidence |
|---|---|---|
| Cold open | 0:00, no establishing shot | invariant, 43/46 |
| Hook + setup (fused) | ~first 30-45% of runtime | frequent, 36/46 |
| Minimal conflict | mid-clip; silence or one follow-up question | frequent, 34/46 |
| Build-up pause | 0.6-3.3s, longest silence in the clip, right before/after punchline | invariant, 43/46 |
| Punchline | short capitulation line or one unbroken escalating sentence | frequent 27/46 (short line) / optional 18/46 (unbroken sentence) |
| Post-punchline hold | 1-3s trailing silence | frequent, 30/46 |
| Outro card | hard cut, static, branded, no resolution | invariant, 46/46 |

---

## 2. Dialogue

### Volume and line length (invariant, 46/46)
Dialogue volume is very low: **1-8 short transcribed lines per video**, averaging roughly **3-12 words per line**. This is not a stripped-down summary of a longer script — the format is built around saying almost nothing. When writing sales-objection scripts, resist the instinct to over-explain the objection or the rebuttal; the whole scene should read as legible from a handful of clipped lines.

### Vocal similarity between speakers (frequent, 34/46)
An interesting artifact surfaced in the source analysis: automated speaker diarization frequently collapsed a clearly two-person exchange into a single `SPEAKER_00` tag. That's a transcription quirk, but it's a useful signal about the *performance* — the two voices read as tonally similar, flat, and non-overlapping enough that a diarization model struggled to tell them apart. Write both characters' lines in a similarly flat register rather than giving one character a sharply different vocal "color."

A genuine, cleanly diarized two-speaker back-and-forth also occurs and is a perfectly good option (optional, 10/46) — clean alternation is not wrong, it's simply not the majority pattern.

### Silence placement (invariant, 43/46)
The **single longest silence in the entire clip** always sits immediately adjacent to the punchline — either as a build-up beat right before it, or as a hold right after it. This is the load-bearing structural rule of the whole format: the pause is doing comedic work that the dialogue itself doesn't need to do.

### The punchline itself
Two patterns recur for how the punchline line is constructed:
1. **Ultra-short capitulation/button line** (frequent, 27/46): 1-3 words — literal examples logged include "No.", "Good.", "Yeah.", "Acid reflex." The punchline is often barely a sentence.
2. **One unbroken escalating sentence** (optional, 18/46): delivered with **no internal pause**, arriving immediately after the clip's biggest build-up pause, using a front-loaded escalating clause structure (the sentence builds toward its own twist without a breath in the middle).

Either pattern is valid; pick based on whether the objection/reveal reads better as a blunt one-word capitulation or as a single dry, run-on reveal.

### Voice notes (how to *write* lines in this style)
Dialogue here is written to be *said*, not *read*: short, clipped, declarative sentences with low pitch variation and no expressive vocal escalation, even when the content is emotionally loaded. Write lines as if the character has already emotionally checked out of the stakes of the conversation — flat statements, flat questions, never raised-voice arguing, never trailing ellipses or interruptions. Avoid exclamation points in script text; avoid stage directions implying vocal intensity ("shouts," "exclaims"). The punchline especially should be writable as a plain, complete sentence or a bare 1-3 word reply — it doesn't need a vocal flourish to land, because the surrounding pause (see above) is carrying the comedic weight.

---

## 3. Comedy Mechanics

### Deadpan is the engine (invariant, 44/46)
This is the single most load-bearing comedic principle in the entire set, explicitly named as the driving mechanism in almost every source write-up: **every line is read flat and matter-of-fact, no matter how emotionally loaded the content is.** Jokes are never "sold" with a performed reaction. When writing and prompting, never ask for an animated, surprised, or heightened delivery on the punchline — flat delivery *is* the joke.

### The silence is a beat, not a gap (frequent, 38/46)
"Awkward silence" is explicitly logged as its own comedic mechanism in the source analysis, distinct from ordinary pacing pauses. The held pause itself performs part of the joke — the discomfort of the silence is doing work, not just separating two lines. Script it as an explicit beat (a pause marker with intent), not as incidental breathing room.

### Irony / misdirection (frequent, 33/46)
The dominant joke *shape*: open with a sincere- or serious-sounding claim or question, then undercut it with a **mundane, petty, or absurd** reveal. The comedic distance is between the register of the setup (serious) and the smallness of the payoff (mundane) — not between a setup and an outlandish, over-the-top payoff.

### Recognition humor via hyper-specific detail (frequent, 29/46)
Rather than broad exaggeration, the joke is often anchored on **one exact, quantified detail** — a specific number, day, or price. Recognition of that precise, oddly specific detail (not a vague generalization) is what triggers the laugh. For sales-objection scripts, this suggests anchoring jokes on a very specific number/detail (an exact dollar figure, an exact number of days "thinking about it," etc.) rather than a generic exaggeration.

### No slapstick (frequent, 36/46)
No physical sight gag or slapstick carries the joke in the large majority of reels. Comedy is dialogue- and micro-expression-driven **within an otherwise completely static frame** — bodies don't move to make the joke land; faces and words do.

### Withholding the reaction (optional, 17/46)
In a substantial minority of reels, the scene withholds any reaction shot or reply after the punchline entirely — it cuts straight from the joke line to the branded outro card with no capper shot. This is a legitimate, punchy option, not a requirement.

### Rare exception: physical sight gag as payoff (one_off, 2/46)
In two reels, the payoff is a physical sight gag rather than a spoken line (a soccer-celebration-style collapse; a single animated tear). This is a genuine outlier relative to the "no slapstick" rule above and should be treated as a rare, occasionally-available option — not a technique to reach for by default, and definitely not to be layered onto every script.

---

## 4. Character Design and Performance

### Cast size and relationship (invariant, 41/46)
Exactly **two on-screen principal characters** carry the entire scene. In the source reels this is a heterosexual long-term couple (husband/wife) — an established, familiar-with-each-other dynamic is the point, not the specific genders. For the sales-objection adaptation, preserve the two-hander structure and the sense of an ongoing, familiar relationship between the two roles (sales rep and prospect), even though they are professional counterparts rather than a married couple.

### The "low battery" face (invariant, 43/46)
Both characters share a signature resting facial design: **permanently heavy-lidded/half-closed eyes** and a **flat, slightly downturned mouth** as the default expression — held **regardless of what's being said**. This is the visual analog of the deadpan-delivery comedy rule above: the face never "performs" the emotional content of the line.

### Nose and glasses (invariant, 42/46)
An **elongated, exaggerated wedge/conical nose** (especially pronounced on the male character), frequently paired with **small round glasses**. This is a core piece of the recognizable character silhouette and should be treated as close to non-negotiable for character-design prompts.

### Device fixation as staged disengagement (frequent, 22/46)
One partner — usually the male character — holds or fixates on a phone/device while the other speaks, visually enacting distraction or disengagement rather than active listening. This is a cheap, reliable visual shorthand worth reusing directly in the sales-objection context (e.g., the prospect glancing at their phone or a second monitor while the rep talks).

### Avoiding eye contact (frequent, 27/46)
The two characters rarely make direct eye contact with each other — both tend to face forward toward the camera or a shared focal point (a TV, in the source reels) rather than turning toward one another, even mid-argument. For a Google Meet framing, this maps naturally onto both participants looking at their own screen/camera rather than at each other (which, notably, is also how real video calls actually look).

### Adaptation note: deadpan/static is not the same as lifeless
This is a deliberate small **adaptation choice for Veo3 prompting, not a reel-evidence classification** — flagging it separately so it isn't confused with the invariant/frequent/optional tags above. A real test generation rendered the non-speaking character as fully inert while their partner talked, and it read as lifeless/uncanny on screen even though "no reaction, no eye contact" is the evidence-backed style. When prompting a silently-listening character (not a character deliberately withholding a reaction to a punchline — that specific choice should stay fully inert, see the "withholding the reaction" rule under Comedy), it's fine to describe a small amount of quiet, settled attentiveness rather than literal total motionlessness, as long as it stops well short of an actual reaction, an eyebrow move, a blink, or eye contact with the other character.

### Who delivers the punchline (optional, 24/46)
In a substantial share of reels, the **female character** delivers the final punchline or verdict line. This is a real pattern but not a majority behavior — treat it as a legitimate default lean (e.g., leaning toward giving the "reactive"/decision-holding role the last word) rather than a rule.

### Rare exception: unseen off-screen character (one_off, 2/46)
In two reels, an off-screen character (spoken about or heard, never shown) delivers the twist purely through the on-screen character's reaction to them. This is a usable but rare technique — appropriate if a scenario specifically benefits from implying a third party (e.g., a prospect's unseen boss/spouse) without ever showing them.

---

## 5. Camera and Cinematography

### Static, locked-off camera (invariant, 44/46)
The camera **never pans or tilts** anywhere in the reference set. Every shot change is achieved through a **hard cut between fully static, locked-off setups** — the frame itself never moves except via the one narrow exception below. This is a hard constraint for Veo3 prompting: camera motion instructions should default to "static" for every shot unless the push-in (below) is specifically called for.

### The one permitted camera move: straight push-in (optional, 14/46)
Where camera movement does occur, it is a **slow, continuous, straight-line push-in (zoom in)** toward a character's face — never a pan, tilt, orbit, dolly-around, or handheld move. It's typically timed to **land tight right on the punchline**, mechanically reinforcing the pause/punchline structure described above.

### Single unbroken shot (optional, 16/46)
A meaningful minority of reels play the entire joke — every line of dialogue — in **one unbroken static shot with zero internal cuts**. This is a clean, simple option, especially for shorter or two-line scripts.

### Shot/reverse-shot (frequent, 26/46)
The more common pattern: open on a **wide static two-shot** establishing both characters and the setting, then cut to **isolated close-ups on each speaker's face** for their individual lines. This hard cut — not a camera zoom — is the mechanism that shifts visual attention to whichever character is currently speaking; a zoom-out/zoom-back-in choreography following the conversation appears in only 1 of 46 reels, and that video's own analysis flags it as the sole exception to the static-camera rule, not a pattern to build on.

### Isolating the punchline (frequent, 30/46)
Regardless of which shot pattern is used elsewhere, the punchline itself is very often delivered in a **tight close-up on one character's face alone**, with the partner cropped out of frame or softly blurred. This isolates the deadpan delivery from any competing visual information at the exact moment the joke lands.

### Optional composition: Wes-Anderson symmetry (optional, 7/46)
For public/social settings specifically (restaurant, diner), a **symmetrical, centered, Wes-Anderson-style framing** appears, typically with a **shallow-depth-of-field, softly blurred crowd of extras** behind the two leads. Reserve this composition for scenes that are explicitly set in a public/social location; it's not part of the default domestic-interior look.

---

## 6. Animation and Motion Technique

This is the category most directly load-bearing for Veo3 prompt fidelity — read closely.

### Material: stop-motion-*styled* CG, not real stop-motion (invariant, 44/46)
The reels are rendered as **3D CGI using a felted-wool/clay-look shader** that is deliberately designed to *evoke* stop-motion — but the source analysis is explicit that this is **not genuine frame-by-frame stop-motion**. Concretely, there is:
- no set jitter,
- no visible fingerprints or tool marks in the material,
- perfectly consistent lighting across frames,
- perfectly consistent, smooth camera moves (no stepped/staccam judder).

This distinction matters enormously for Veo3 prompting: ask for the *material look* of stop-motion (matte, fibrous, clay/felt surface, non-reflective) combined with *fully smooth CG motion* — do NOT ask for "stop-motion animation" as a motion technique, which would introduce jitter/judder/frame-holding that the reference set explicitly does not have.

### No blinking (invariant, 40/46)
No blink is captured in any sampled keyframe across either character in the large majority of reels. Eyes stay open in the heavy-lidded default pose for the **entire clip**. Prompt for "no blinking" explicitly if the generation model defaults to adding natural blinks.

### Animation budget is almost entirely facial (invariant, 41/46)
The animation effort is concentrated almost entirely on the **face** — mouth, eyebrows, eyelids. Torso, arms, and legs stay **locked and static** with no idle secondary motion: no breathing sway, no cloth simulation, no hair simulation, for the majority of the shot. This is a strong, specific, and highly Veo3-prompt-actionable rule: explicitly instruct "body stays completely still, no idle movement, only face animates."

### Mouth shapes: discrete visemes, not fluid lip-sync (frequent, 30/46)
Mouth shapes read as a **small library of discrete held/swapped viseme poses** synced to caption words — not continuous, phoneme-level fluid lip-sync. The mouth appears to snap or hold between a limited set of distinct shapes rather than smoothly morphing through every phoneme. This is part of what gives the format its "puppet" quality and should be requested explicitly if possible ("mouth shapes swap between a small number of held poses on each word" rather than "realistic lip-sync").

### Static background/props (frequent, 33/46)
Background and set props — furniture, dishes, window light, wall decor — are **pixel-static across every sampled frame** with zero ambient motion: no drifting dust, no flickering light, no swaying curtains. Prompt for a completely inert, non-animated environment.

### One looping gesture per character (optional, 15/46)
A meaningful minority of reels give each character exactly **one recurring physical gesture** — a glasses-fidget, a phone-scroll, a knitting motion — that is held or looped for most of the shot rather than continuously re-animated with new business. This is a good, cheap way to add a touch of life to an otherwise static body without breaking the "locked body" rule above.

---

## 7. Editing and Pacing

### Low cut count (invariant, 42/46)
Overall cut count is low: **0-6 hard cuts** for the entire piece, consistent with the dominant single-scene, largely static-camera format. This is not a fast-cut style.

### Hard cuts as the default transition (frequent, 36/46)
Transitions are almost exclusively **hard cuts**; dissolves/wipes are rare and, when they do appear, are reserved specifically for the transition into the outro card — never used mid-scene between dialogue shots.

### Silent hold before the outro (frequent, 32/46)
A **silent reaction/hold beat** follows the punchline before the cut to the outro card in a clear majority of reels, rather than cutting away from the joke the instant the line ends. (Note this pattern coexists with the "withhold the reaction shot entirely" comedy option above — the hold beat and a visible reaction shot are not the same thing; the hold can simply be more silence on the same shot.)

### Average shot length (frequent, 35/46)
Average shot length across the piece clusters at roughly **2-7 seconds**.

### Not the house style: rapid-fire fast cuts (one_off, 3/46)
Rapid-fire fast-cut editing — **10-18+ cuts, sub-1-second average shot length** — appears in three reels, used for montage or mock-commercial pacing. This is a deliberate, occasional stylistic departure in the source set, not the format's identity. See the format-outliers section above; do not build fast-cut pacing into the default script/prompt pipeline.

---

## 8. Audio

### No music (invariant, 46/46)
**Zero background music** is present in any of the 46 reels — confirmed absent across every video's audio analysis, with no exceptions. This is a hard rule: do not add a score or ambient music bed to generated content in this style.

### No sound effects (invariant, 46/46)
**Zero sound effects or foley** are present or logged in any reel — no whooshes, no impacts, no ambient room sound cues, nothing beyond the dialogue itself. Treat generated audio as dialogue-plus-silence only.

### Pause placement around the punchline (invariant, 43/46)
As established above (structure/dialogue), the single longest silence in the clip — **roughly 0.6-3.3 seconds** — always sits immediately adjacent to the punchline, either as a build-up beat before it or a trailing hold after it. This is the format's core comedic-timing mechanism and shows up consistently across nearly the entire set.

### Flat vocal performance (frequent, 34/46)
Dialogue reads as **short, clipped, low-pitch-variation declarative sentences** rather than expressive or escalating vocal performance — reinforcing the deadpan comedy principle at the audio-delivery level, not just the writing level.

### Trailing silence before the outro card (frequent, 30/46)
A trailing silence of roughly **1-3 seconds** follows the very last line of dialogue before the hard cut to the outro card.

---

## 9. Environment and Art Direction

### One location, no scene changes (invariant, 42/46)
A **single unchanging set/location** carries the entire episode — there is never a location or scene change. All visual variety within a piece comes purely from reframing (wide two-shot vs. tight close-up) of the *same* background, never from cutting to a different place.

### Lighting: warm, soft, single-source, shallow DOF (frequent, 33/46)
The dominant lighting setup is **warm, soft, naturalistic light from a single practical, motivated source** visible or implied in the frame — a table lamp, a window, a candle — combined with a **shallow depth of field** that softly blurs the background. This is one of the most directly portable rules to the sales-objection niche: a laptop/monitor glow or a desk lamp reads as an equally valid "single practical motivated source" for a home-office Google Meet setting.

### Domestic interior as default location (frequent, 27/46)
The default location type is a **domestic interior** — kitchen, bedroom, or living-room couch. This should be the default assumption for generated scenes unless the scenario specifically calls for something else.

### Public/social settings as an alternative (optional, 16/46)
A meaningful minority of reels are set in a **public/social location** instead — restaurant, park, sidewalk, parking garage, car, salon. This is a legitimate alternative when a scenario benefits from it (and it's also where the optional Wes-Anderson symmetrical-crowd composition tends to appear, see Camera above).

### Devices as plot-relevant props (frequent, 24/46)
A **smartphone or laptop** is visible on screen and is tied directly to the scene's plot or joke in roughly half the reels — not just incidental set dressing. This maps very directly onto the sales-objection niche, where a laptop showing the Google Meet call *is* the plot-relevant device.

### Rings as relationship signaling (optional, 11/46)
A visible **wedding/engagement ring** on at least one character is used in a meaningful minority of reels as a small, legible prop that signals the married-couple relationship. The general technique — a small, legible prop that signals the characters' established role relative to each other — is portable even where the specific prop (a ring) isn't; for the sales-objection niche this role could be filled by something like a visible company badge/branding, a CRM tool open on screen, etc., though note this specific substitution is an *adaptation suggestion*, not a traced finding.

---

## 10. Prompt and Script Generation Guidelines

### Veo3 style keyword bank

Use these phrases directly when constructing Veo3 generation prompts. They are written to be concrete and prompt-usable, not generic mood adjectives, and each one traces back to a rule above.

**Material / shader**
- "felted-wool / soft clay stop-motion-look shader on all characters and props — matte, fibrous, non-reflective surface, no glossy CG highlights"
- "CG-clean stop-motion pastiche — perfectly smooth motion, NO set jitter, NO visible fingerprints or tool marks, NO frame strobing; a stylized stop-motion LOOK rendered with fully consistent CG smoothness, not genuine frame-by-frame stop-motion"
- "muted, warm, desaturated color palette consistent with a felt/clay material — avoid glossy or highly saturated CG rendering"

**Character design**
- "heavy-lidded, half-closed 'low battery' eyes as the default resting expression, no blinking during the shot"
- "flat, slightly downturned mouth at rest, held even through emotionally loaded lines — deadpan face sculpt, not an expressive/animated face rig"
- "elongated wedge/conical nose; small round glasses on at least one character"
- "(prompt-craft note, not a visual trait — supersedes any earlier, softer version of this rule) when reference images are attached, do not describe character appearance in the prompt text AT ALL, not even briefly by name/role, and state the 'reference images are attached' instruction only ONCE per prompt set, never repeated inside every individual shot. Real test generations kept drifting from the reference images through two earlier, progressively-trimmed attempts at this rule; repeating any instructional language about the images inside every shot's generation text is itself the kind of clutter that competes with image conditioning"
- "(prompt-craft note, not a visual trait) never restate a static composition/layout that's already shown in an attached reference image — this includes the Google Meet split-screen framing itself. Don't write 'two video tiles side by side, labeled X and Y' or 'left tile: SALES REP, right tile: PROSPECT' if a reference image already shows that exact framing; say only that the scene matches the attached reference image, then describe what a still image can't show — motion and dialogue. If a shot's framing doesn't match any single reference image (e.g. a cropped close-up), describe only the cut/reframe itself, not the whole composition"

**Rig / animation**
- "animate only the mouth, eyebrows, and eyelids; keep torso, arms, and legs completely locked and static — no idle breathing sway, no cloth simulation, no hair simulation"
- "mouth reads as a small set of discrete held viseme poses swapped on each spoken word, not continuous fluid phoneme-level lip-sync"
- "at most one small looping gesture per character (e.g., tapping a keyboard, adjusting glasses, scrolling a phone) held for most of the shot"
- "(niche creative adaptation, not reel-sourced — supersedes the 'settled attentiveness' note below and see the Niche Creative Adaptations section) characters actively, visibly react to each other's lines — human-scale, restrained expression, not exaggerated/anime — including a brief reactive glance toward one's own screen or the other participant's tile. This deliberately overrides the source reels' 'no reaction, no eye contact' default for this niche only"

**Camera**
- "locked-off, static camera for every shot — no pans, no tilts, no handheld shake"
- "the only allowed camera movement is a slow, continuous, straight-line push-in toward a character's face, timed to land tight exactly on the punchline"
- "shot/reverse-shot pattern — open on a wide static two-shot, cut to isolated tight close-ups per speaker, partner cropped out of frame or softly blurred during the other's line"
- "(retired — do not prompt this, see note below) an earlier version of this bank asked for a dynamic active-speaker highlight ring on the Google Meet tile; real test generations rendered it on the wrong tile, on both tiles at once in mismatched colors, or lingering after the speaker stopped. Leave Meet-tile chrome static in the generation prompt and add any highlight ring by hand in post-production instead"

**Lighting / set**
- "warm, soft, naturalistic key light motivated by a single practical in-frame source (desk lamp, window, laptop/monitor glow); shallow depth of field with a softly blurred background"
- "completely static background — furniture, screens, props, and decor do not move, drift, flicker, or animate at all between frames"
- "single unchanging location for the whole scene; visual variety comes only from reframing between the wide two-shot and tight close-ups, never a location change"
- "(optional, public settings only) symmetrical, centered Wes-Anderson-style framing with a shallow-DOF, softly blurred crowd of background extras"

**Editing / audio / performance**
- "0-6 hard cuts total, no dissolves or wipes except optionally into the closing card; average shot length 2-7 seconds"
- "no score, no sound design, no foley, no ambient room noise of any kind — complete silence except the spoken dialogue itself; do not add any environmental or 'authenticity' audio"
- "every line, including the punchline, delivered in a flat, low-pitch-variation, deadpan monotone regardless of emotional stakes" (this describes the source reels; see the niche-adaptation override just below for how this niche's vocal delivery should actually be prompted)
- "(niche creative adaptation, not reel-sourced) vocal delivery for this niche is naturalistic and restrained-awkward rather than strict flat monotone — a reluctant line should sound genuinely reluctant (soft, hesitant), not robotic; keep it low-key and human, never escalated or exaggerated"
- "hold a long silence (0.6-3.3s) directly before or after the punchline; no filler movement or sound during the hold"
- "(prompt-craft note) a scripted interruption needs explicit 'voices overlap' language, not just 'cuts her off' — say the interrupting line starts while the first character's voice is still audible on their last word, and that the first line stops abruptly, unfinished. A real test generation with fairly strong cut-off language still rendered the interruption as a clean back-to-back handoff (about a 0.06s gap, no real overlap) — push harder in the text, though Veo3 may still tend to serialize dialogue regardless"
- "(optional) burned-in episode/scenario label in the corner of the opening shot; static branded end-card with hard cut, no narrative resolution shown after it"

### Retired: Google Meet active-speaker highlight (do not prompt this)

An earlier version of this document asked every Veo3 shot to describe a dynamic highlight ring
appearing on whichever character's tile was currently speaking — a Google-Meet-realism addition,
not traced to the reference reels. A real test generation showed this doesn't work: the highlight
appeared on the wrong tile while the other character was actually speaking, both tiles lit up
simultaneously in two different colors, and a highlight lingered on a tile after that character had
stopped talking. It's a timed, conditional visual effect tied precisely to audio content, and the
model isn't reliably tracking it — asking for it just adds confusion. **Leave Meet-tile chrome
static in every generation prompt; add any active-speaker highlight by hand in post-production
instead, synced exactly to the real dialogue timing.**

### Niche Creative Adaptations (Sales-Objection Skits)

Everything else in this document is a record of what the 46 source reels actually do. This section is different on purpose: it's a set of **deliberate creative choices for the sales-objection niche, made on the user's explicit direction, that knowingly override specific reel-derived tendencies** rather than extend them. Do not confuse these with the invariant/frequent/optional evidence tags used elsewhere — they carry no evidence count because they aren't reel findings. The reasoning: the source reels and this niche aren't in the same situation (an in-person couple vs. two people on a Google Meet call), so faithfully reproducing every reel tendency stops being the goal once it works against what the sales-objection content actually needs, which is legible, relatable awkwardness rather than a faithful replica of "Low Battery People."

- **Expressive, human-scale reactions are encouraged, not suppressed.** The reel-derived "avoid eye contact" and "stay inert while listening" defaults are deliberately overridden for this niche. Characters should visibly, believably react to what the other person just said — including a brief reactive glance toward their own screen or the other participant's tile (not literal eye contact through the call, which wouldn't make sense for a video call anyway, but a legible "I see what you just did" beat). Keep it restrained and human-scale — explicitly **not anime-exaggerated** — a small, real reaction, not a big cartoon one.
- **Every dialogue beat needs an explicit action/expression line for both characters, not just whoever is speaking.** A prompt that only describes the speaker and leaves the listener unstated is a prompt where the model is free to leave that character looking dead in-frame — this is exactly what produced the flat, inert quality in earlier test generations. Even a simple "her expression holds steady, no reaction yet" for the listener is enough; the point is never leaving a character's face/eyes undescribed for a whole beat just because they aren't the one talking.
- **The comedic core for this niche is awkwardness — pacing and expression — not a punchline mechanism.** The source reels' "hyper-specific undercut line" punchline shape isn't a requirement here; held silences and readable discomfort do more of the work than a clever final line does. Scripts don't need to force a one-liner "reveal" structure.
- **Vocal delivery is naturalistic and restrained-awkward, not strict deadpan monotone.** A reluctant, stalling line should sound genuinely reluctant — soft, hesitant, a little deflated — rather than flat and robotic. Still low-key and controlled, never escalated or shouty.
- **An opening silent "settling in" business beat is standard before dialogue starts.** Not reel-evidence (nothing like this appears in the 46 source reels) — added for two practical/creative reasons: (1) it gives editing room to composite a blurred topic-card graphic over the opening seconds afterward, the same way the outro card is built in a video editor rather than generated with Veo3; (2) it's a small, natural character beat (e.g. the Sales Rep writing something in a notebook while the call connects). Keep this beat itself low-key and silent — no dialogue, no exaggerated business — it's a pacing device, not a joke.

### Script structure template

Use this beat-by-beat skeleton as the scaffold for every generated script. Timings are approximate and should scale to the total-runtime target.

```
TOTAL RUNTIME TARGET: 9.5-17.5s, single unbroken scene.
CAST: sales rep + prospect on a Google Meet call — two-person, established/
      professionally-familiar dynamic, in place of the reference reels'
      married couple.

[0:00] COLD OPEN
  Cut in already mid-conversation. No establishing shot, no narration.
  Static locked-off wide two-shot (e.g. split-screen / Meet-tile framing)
  showing both participants already engaged.

[~0:00-0:05] HOOK + SETUP (fused into one exchange)
  1-3 short declarative lines (~3-12 words each), deadpan delivery, low
  pitch variation. The objection ("it's too expensive", "I'll think about
  it") surfaces here, stated plainly rather than argued.
  Optional: one participant fixates on a phone / second screen rather than
  making direct eye contact with the camera / other tile.

[~0:05-0:08] MINIMAL CONFLICT BEAT
  No escalating argument. Either a held silence, or exactly one skeptical
  follow-up / pushback line.

[~0:08-0:10] BUILD-UP PAUSE
  The single longest silence in the script: 0.6-3.3s, placed immediately
  before the punchline. Optional: the sole camera push-in (slow,
  straight-line, toward one character's face) lands here.

[~0:10-0:12] PUNCHLINE
  Either a 1-3 word capitulation/verdict line, or one unbroken escalating
  sentence with no internal pause. Structure as irony/misdirection (a
  sincere-sounding claim undercut by a mundane/petty/absurd reveal) or as
  recognition humor anchored on one hyper-specific quantified detail (an
  exact price, day, or number). Cut to a tight close-up on the speaker's
  face alone, deadpan, partner cropped/blurred out.

[~0:12-0:14] POST-PUNCHLINE HOLD
  1-3s of trailing silence. No reaction shot or reply required; camera
  holds static.

[~0:14] HARD CUT TO OUTRO CARD
  Static black branded end card (brand name + credit line). Optional:
  "new content daily"-style CTA graphic and an episode/scenario label.
  No narrative resolution shown.
```

### Hard "do not" list for generated scripts and prompts

These follow directly from the invariant/near-invariant rules above and from the three flagged format outliers:

- Do not pad runtime toward 20-25s or write multiple scenes/locations.
- Do not add an establishing shot, narration, or scene-setting text at the open.
- Do not write an escalating argument or more than one pushback beat.
- Do not add music or sound effects of any kind.
- Do not use camera pans, tilts, orbits, or handheld movement — static or a single straight push-in only.
- Do not default to fast-cut montage editing (that's a 3/46 outlier, not the house style).
- Do not animate blinking, idle body sway, cloth, or hair.
- Do not resolve the objection or show a visible reply/reaction after the punchline's hold beat.
- Do not intercut live-action footage or switch to direct-to-camera monologue address (that's the "Paul" outlier, 1/46).
