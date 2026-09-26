# Prompts — Jua (all run in Arcads; context in `00_brief/jua_context.md`)

## Shot 02 — staged restoration (gpt-image-2-5-sunburst, A/B nano-banana-2 — see model_map.md)
Always feed the **previous stage** as input, never regenerate from text. After each stage, append a line to `03_restore/log.md`: `stage | step | model | prompt | file`.

Shared lock (prepend to every stage):
```
RESTORATION, NOT RE-CREATION. Keep the exact same person, face shape, features, expression, pose, clothing, background, framing and crop. Do not beautify, slim, smooth skin, change age, or add/remove anything. Output the same photograph, only repaired.
```
- **Stage 1 — dust & specks** → `stage_1_dust.png`
  `Remove dust, specks and small spots only. Keep film grain, tone and all damage larger than a speck.`
- **Stage 2 — cracks & tears** → `stage_2_cracks.png`
  `Repair the cracks, crease and torn edge by continuing the surrounding texture. Do not repaint areas that are undamaged.`
- **Stage 3 — clarity** → `stage_3_clarity.png` → copy to `locked/restored.png`
  `Recover sharpness and contrast so the face is clearly readable, as if from a well-preserved print of the same negative. Keep black-and-white, keep natural grain, no plastic skin.`
- **Stage 4 — colour (optional, disclose it)** → `stage_4_color.png`
  `Colorize conservatively with muted, period-plausible tones.` → end card must say "Colour is an AI interpretation."

Reject a stage if the face identity drifts. Compare side by side with the previous stage.

## Shot 03 — restrained motion (veo31 startFrame, alt kling-3.0 / seedance-2.5)
Input: `locked/restored.png` (real photos: only with the owner's permission to upload to Arcads).
```
CONSTRAINTS: Render ONLY what is described. The person in the photograph does NOT move: no blinking, no smiling, no lip or head movement, no change in expression or identity. No added text, props, color, or background changes.
Duration 6s, 16:9. The photograph lies on a wooden table. Slow, steady camera push-in toward the face. A soft band of warm window light moves slowly from left to right across the print. Paper grain and edges stay stable. One continuous shot, no cuts.
```
Roll 2 variants; reject any take where the face changes.

## Fictional mode only — generated portrait (seedream_5_pro A/B nano-banana-2) → `locked/original.png`
```
Black-and-white studio portrait photograph, [FICTIONAL PLACE], [YEAR]. A woman in her thirties, seated, three-quarter view, calm direct gaze, [HEADWRAP / CLOTHING TYPICAL OF THAT PLACE AND DECADE — research, don't guess]. Plain painted studio backdrop. Authentic print wear: faded contrast, fine scratches, a crease across one corner, slightly torn edge. Silver-gelatin grain. No text, no watermark, no modern elements. An original fictional person, not a real individual.
```
Then run the staged restoration above on it exactly as you would a real photo.

## Fictional mode only — hands on table B-roll (seedance-2.5, refs: hands_sheet + table_close)
```
CONSTRAINTS: Live motion video. Render ONLY what is described. No text, logos, or extra objects.
Top-down, 16:9, warm late daylight on a worn wooden table. A young person's hands slide an old black-and-white portrait print out of a paper sleeve and lay it flat. Natural hand anatomy, five fingers each. Static camera. 5s.
```

## Captions (Arcads captions/translate)
Source: witness audio from shot 04. Output: burned-in EN subtitles + FR version. Check every word of the name and place by ear with the witness — never trust auto-transcription of names.

## Critic pass (kit prompt H, extended)
```
Review this cut against the brief. Score 0–5: emotional readability muted, honesty (original visible, no invented facts, face unaltered in motion), first 3 seconds, testimony clarity. List blocking issues + the smallest fix.
```
