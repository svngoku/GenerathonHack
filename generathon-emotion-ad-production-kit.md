# Generathon #2 — Emotion-first production kit

Ready-to-fill resource template for September 26–27, 2026. Event: [Generathon #2](https://luma.com/ywjzbr8t?tk=JJPMJQ). Reference workflow: [Higgsfield commercial prompt breakdown](https://higgsfield.ai/blog/ai-commercial-youtube-guide). The event offers short film (maximum 3 minutes), animation with a marked visual-atmosphere shift (maximum 2 minutes), and a physical-product ad; teams of 1–3 submit by Sunday 14:00. The emotion is described as “chosen” by the event, so do not lock a final emotion until the kickoff briefing. [web:1][web:2]

## 0. One-page brief — fill at kickoff

- Track: [Sell the Feeling / Animate the Shift / Two Minutes to Move]
- Assigned/chosen emotion: [EMOTION]; starting emotion: [BEFORE]; ending emotion: [AFTER]
- Audience: [WHO]; physical product, if ad: [PRODUCT]; product truth: [WHAT IT REALLY DOES]
- One-line concept: “When [PERSON] encounters [PRODUCT / EVENT], [SENSORY TRIGGER] turns [BEFORE] into [AFTER].”
- Proof shot: [THE ONE VISIBLE ACTION THAT MAKES THE CHANGE BELIEVABLE]
- End frame / line: [PACKSHOT + 3–6 WORD TAGLINE]; language: [FR/EN]; duration: [TARGET]
- Aspect ratio: [16:9 / 9:16]; export specification: [CHECK BRIEF]; submission URL: [CHECK DISCORD/ORGANIZER]
- Deliverable owner: [NAME]; final export owner: [NAME]; fallback stills owner: [NAME]
- Emotion test: A viewer can identify [AFTER] with sound muted and no explanatory text: [YES/NO].

## 1. The reusable resource manifest

Create one shared folder. Only promote approved assets to `locked/`.

```text
project/
  00_brief/brief.md, rules.md, references.md
  01_bible/visual_bible.md, emotion_arc.md, shotlist.csv
  02_refs/character/, product/, locations/, palette/
  03_stills/shot_01_start.png, shot_01_end.png, ...
  04_video/shot_01_v01.mp4, ...
  05_audio/music/, sfx/, voice/, licenses.md
  06_edit/timeline/, graphics/, exports/
  locked/character.png, product.png, location.png, hero_frame.png
  delivery/final.mp4, thumbnail.png, pitch.md
```

`references.md`: URL | creator | purpose | usage rights | local filename. `licenses.md`: asset | source | permitted use | proof/link. Avoid unlicensed music, trademarks, and unauthorized likenesses.

## 2. Extracted Higgsfield method

The article's transferable method is to create character sheets, location plates and a product reference first; compose keyframes using those references; animate a single clear action with controlled camera instructions; use separate start/end frames for transformations; preserve product geometry and frame composition in revisions; finish atmosphere in the edit. Its spy/perfume storyline is an example, not a template to copy. The article also uses a separate CCTV look in DaVinci rather than asking generation to solve everything. [web:2]

| Asset | Lock before animating | Acceptance check |
|---|---|---|
| Character | Face, outfit, silhouette, expression range | Same person across three test angles |
| Product | Shape, color, label, scale, orientation | Same physical object in hero and action shots |
| Location | Geometry, light direction, color palette | Background continuity across wide and close views |
| Emotion arc | Body language, lighting, sound transition | Shift is visible without the pitch |
| Camera | Framing, lens feel, motion | One principal movement per shot |

## 3. Paste-ready prompt library

Replace bracketed tokens and attach the indicated references. Use model-specific `@asset` handles only if your tool supports them.

### A. Concept generator

```text
Act as creative director for a 24-hour generative-video challenge. Track: [TRACK]. Required emotion: [EMOTION]. Physical product if relevant: [PRODUCT]. Audience: [AUDIENCE]. Generate 5 original concepts achievable with 4–6 shots, 1–2 characters, 1 location, and a single clear emotional turn. For each give: one-sentence hook, before→after emotion, visual proof, product role, sound cue, feasibility risk, and end frame. Avoid dialogue-dependent reveals. Rank by emotional clarity and production feasibility; choose one.
```

### B. Visual bible

```text
Create a compact visual bible for: [CONCEPT]. Emotion progression: [BEFORE] → [AFTER]. Fixed elements: protagonist [DESCRIPTION], product [EXACT PHYSICAL FEATURES], location [GEOMETRY], wardrobe [DETAILS]. Start palette [COLORS/LIGHT]; end palette [COLORS/LIGHT]. Visual motif [MOTIF]. Camera grammar [STATIC/HANDHELD/SLOW PUSH]. Preserve natural texture, believable anatomy, coherent shadows, and the same product silhouette. Output a continuity checklist and 5 shot descriptions, not images.
```

### C. Character sheet / product master / empty room

```text
CHARACTER REFERENCE SHEET: One consistent original character: [DESCRIPTION]. Neutral plain background. Three panels: waist-up front, full-body front, full-body back. Same face, hairstyle, proportions and outfit in every panel. Even soft light, natural skin texture. No labels or extra people.
```

```text
PRODUCT MASTER: One physical [PRODUCT], exact geometry [SHAPE], material [MATERIAL], signature detail [DETAIL], color [COLOR]. Isolated three-quarter view on a neutral backdrop; clean product photography. Keep proportions mechanically plausible. No invented text, extra parts, or duplicate product. Reserve typography for post-production.
```

```text
LOCATION PLATE: Empty [LOCATION], [SPATIAL GEOMETRY], [KEY OBJECT], [LIGHT DIRECTION], starting palette [PALETTE]. Frame [WIDE/ANGLE]. No people, no product, no text. Natural materials, stable architecture, room for foreground subject. Generate a second matching angle with the same layout.
```

### D. Still/keyframe composite

```text
Use reference 1 ONLY for character identity; reference 2 ONLY for product design; reference 3 ONLY for environment and lighting. Compose shot [NUMBER]: [FRAMING] of [SUBJECT] at [POSITION], [PRODUCT] at [POSITION]. Action frozen at [EXACT MOMENT]. Expression: [OBSERVABLE FACIAL/BODY CUES]. Foreground [DETAIL]; background [DETAIL]. Palette [COLORS], light [DIRECTION], depth of field [SETTING]. Preserve the references' identities and geometry; no extra fingers, duplicated objects, text, or unrequested props.
```

### E. Motion with start/end frames

```text
START FRAME: [FILE]. END FRAME: [FILE]. Duration: [DURATION]. One continuous shot, [STATIC CAMERA / SLOW PUSH]. Subject performs ONE action: [ACTION]. In the first half [VISIBLE BEFORE STATE]; at [TRIGGER] [PHYSICAL CHANGE]; by the last frame [VISIBLE AFTER STATE]. Keep character face, product silhouette, background layout, hand count and camera perspective stable. No cuts, new objects, morphing, text, or arbitrary camera movement.
```

### F. Surgical correction

```text
Edit ONLY [REGION/PROPERTY] in the supplied frame. Change [CURRENT] to [TARGET]. Lock camera angle, crop, lens perspective, character identity, product shape/size/position, lighting direction, background geometry and every other element. Do not add objects. Return one revised frame.
```

### G. Hero end frame

```text
Product [PRODUCT] in sharp focus at [POSITION], matching the product master exactly. The emotional consequence [HUMAN ACTION/EXPRESSION] is visible softly out of focus behind it. Lighting progresses to [AFTER PALETTE]. Leave clean negative space at [AREA] for tagline added in edit. No generated lettering or extra logos.
```

### H. Critic / selection pass

```text
Review this storyboard and generated shots against the brief. Score each 0–5 for emotional readability, product clarity, continuity, temporal coherence, and first-three-second hook. List only blocking issues and the smallest possible fix. Flag any claim, music, likeness, logo or asset with unclear rights. Identify which shot can be replaced by a still plus edit if generation fails.
```

## 4. Shot plan — adaptable 30–45 second ad

| Shot | Time | Function | Generate | Emotion evidence |
|---|---:|---|---|---|
| 01 | 0–4s | Hook: visual contradiction or striking gesture | Strong still → short motion | Initial state immediately legible |
| 02 | 4–10s | Establish person and unmet need | Character + room keyframe | Body language, not exposition |
| 03 | 10–17s | Reveal product as meaningful object | Product master + close-up | Product recognizable |
| 04 | 17–26s | Physical interaction triggers shift | Start/end keyframes | Clearly visible cause → effect |
| 05 | 26–35s | Human reaction + atmosphere shift | Expression + changed light | Assigned emotion unmistakable |
| 06 | 35–42s | Hero packshot + tagline | Locked product frame | Product and feeling remembered |

For animation or film, keep the same asset and continuity method but replace the packshot with a narrative resolution; honor the relevant track duration and animation-atmosphere requirement. [web:1]

## 5. Event execution and fallback

- Before arrival: log into generation/editing tools; test one still and one video; confirm storage, export, reference-upload workflow and credit balance. Bring charger/headphones and a locally accessible copy of this kit.
- Saturday 10:00 kickoff: confirm the emotion, official constraints, scoring, submission format and credits. The event lists an Arcads AI workshop at 11:00. [web:1]
- First 90 minutes after brief: select concept, lock emotion beat and product; generate visual bible, character/product/location masters and one hero still.
- Next block: produce the key emotional-change shot before peripheral scenes; only then fill missing shots. Review rough cut early with a person who has not heard the concept.
- Sunday morning: lock picture, sound, typography and export. Aim for an internal cutoff ahead of the listed Sunday 14:00 hard submission deadline. [web:1]
- If motion breaks: use approved stills with deliberate crop/pan, cuts, sound design and color shift; never sacrifice the visible emotional turn for extra effects.

## 6. Pitch / final QA

Pitch: “We chose [EMOTION]. Our protagonist begins [BEFORE]. When [TRIGGER], the image and sound shift to [AFTER]. [PRODUCT / STORY ELEMENT] is not just shown; it causes the feeling. Watch for [VISIBLE PROOF] in shot [N].”

Final check: emotion legible muted; physical product visible if ad; no continuity drift; no unexplained duplicate characters or props; no fake product claims; legible title/end card; audio peaks checked; playback tested outside editor; file opens; submission link and time verified.
