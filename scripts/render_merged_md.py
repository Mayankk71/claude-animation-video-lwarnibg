"""Render a human-readable merged.md from an already-written merged.json.

Usage:
    python scripts/render_merged_md.py <slug>
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def line(label: str, value) -> str:
    if value in (None, "", [], {}):
        return ""
    return f"**{label}:** {value}\n\n"


def render(m: dict) -> str:
    out = [f"# Reel breakdown — {m['video_slug']}\n\n**Duration:** {m['duration_sec']:.1f}s\n\n"]

    story = m["story"]
    out.append("## Story & structure\n\n")
    for beat in ("hook", "setup", "conflict", "punchline", "ending"):
        b = story.get(beat)
        if not b:
            continue
        out.append(f"- **{beat.capitalize()}** ({b.get('start')}s–{b.get('end')}s): {b.get('description', '')}")
        if b.get("why_it_works"):
            out.append(f" — *{b['why_it_works']}*")
        if b.get("cta_or_text_overlay"):
            out.append(f" — overlay: {b['cta_or_text_overlay']}")
        out.append("\n")
    if story.get("narrative_notes"):
        out.append(f"\n{story['narrative_notes']}\n")

    dialogue = m["dialogue"]
    out.append("\n## Dialogue\n\n")
    for l in dialogue.get("lines", []):
        flag = " *(interruption)*" if l.get("interruption") else ""
        out.append(f"- **[{l['speaker']}]** ({l['start']}s–{l['end']}s, {l['word_count']}w, "
                    f"pause before {l['pause_before_sec']}s){flag}: \"{l['text']}\"\n")
    if dialogue.get("speech_rhythm_notes"):
        out.append(f"\n{dialogue['speech_rhythm_notes']}\n")
    if dialogue.get("conversational_flow_notes"):
        out.append(f"\n{dialogue['conversational_flow_notes']}\n")

    comedy = m["comedy"]
    out.append("\n## Why it lands (comedy)\n\n")
    for b in comedy.get("comedic_beats", []):
        out.append(f"- **{b['mechanism']}** ({b['start']}s–{b['end']}s): {b['description']} — {b['why_it_lands']}\n")
    if comedy.get("overall_comedic_style_notes"):
        out.append(f"\n{comedy['overall_comedic_style_notes']}\n")

    character = m["character"]
    out.append("\n## Characters\n\n")
    for c in character.get("characters", []):
        out.append(f"**{c['name_or_role']}**\n")
        for field in ("personality_traits", "emotional_range", "expressions", "gestures"):
            for item in c.get(field, []):
                out.append(f"- {item}\n")
        if c.get("interactions_notes"):
            out.append(f"\n{c['interactions_notes']}\n")
        out.append("\n")

    camera = m["camera"]
    out.append("## Camera\n\n")
    for s in camera.get("shots", []):
        out.append(f"- {s['start']}s–{s['end']}s: **{s['shot_type']}**, {s['camera_movement']} — {s['composition_notes']}\n")
    if camera.get("framing_patterns_notes"):
        out.append(f"\n{camera['framing_patterns_notes']}\n")

    animation = m["animation"]
    out.append("\n## Animation & visual technique\n\n")
    for field in ("technique", "facial_animation_notes", "eye_and_blink_notes", "head_movement_notes",
                  "gesture_notes", "idle_motion_notes", "frame_rate_feel", "overall_animation_style_notes"):
        val = animation.get(field)
        if val:
            out.append(f"- {val}\n")

    editing = m["editing"]
    out.append(f"\n## Editing\n\n{editing.get('cut_count', 0)} cuts, "
               f"avg shot length {editing.get('avg_shot_length_sec', 0)}s.\n\n")
    for c in editing.get("cuts", []):
        out.append(f"- {c['timestamp']}s: {c['transition_type']} — {c['reason']}\n")
    for r in editing.get("reaction_shots", []):
        out.append(f"- Reaction shot {r['start']}s–{r['end']}s: {r['description']}\n")
    if editing.get("pacing_notes"):
        out.append(f"\n{editing['pacing_notes']}\n")

    audio = m["audio"]
    out.append("\n## Audio (inferred)\n\n")
    for field in ("voice_delivery_notes", "pitch_energy_notes", "silence_usage_notes"):
        val = audio.get(field)
        if val:
            out.append(f"- {val}\n")
    music = audio.get("music", {})
    if music.get("present"):
        out.append(f"- Music: {music.get('style', '')} — {music.get('notes', '')}\n")

    environment = m["environment"]
    out.append("\n## Environment\n\n")
    if environment.get("backgrounds"):
        out.append(f"{environment['backgrounds']}\n\n")
    if environment.get("props"):
        out.append(f"**Props:** {', '.join(environment['props'])}\n\n")
    if environment.get("lighting_notes"):
        out.append(f"**Lighting:** {environment['lighting_notes']}\n\n")
    if environment.get("color_palette"):
        out.append(f"**Color palette:** {', '.join(environment['color_palette'])}\n\n")
    if environment.get("visual_complexity_notes"):
        out.append(f"{environment['visual_complexity_notes']}\n")

    return "".join(out)


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    slug = sys.argv[1]
    analysis_dir = ROOT / "analysis" / slug
    merged = json.loads((analysis_dir / "merged.json").read_text())
    (analysis_dir / "merged.md").write_text(render(merged))
    print(f"wrote {analysis_dir / 'merged.md'}")


if __name__ == "__main__":
    main()
