# Prompts — Jua (all run in Arcads; context in `00_brief/jua_context.md`, models in `model_map.md`)

## Prompt rules (adapted from higgsfield-ai/skills, MIT)
1. **Edits describe the change, never the input.** The model already has the photo; re-describing it invites re-creation.
2. **Image-to-video describes motion only.** The start frame already defines the scene.
3. **Phrase bans positively** where possible ("pixel-faithful where undamaged" instead of "don't change the face"), and add a NEGATIVE line for video.
4. **Declare the references first:** begin every multi-image prompt with `IMAGE REFERENCES: image 1 = …; image 2 = …`, always in the same order.
5. **Under ~200 tokens.** Long prompts make models drift.
6. **One change per pass.** State what changes, then freeze everything else.

## Identity lock (paste into every image/video prompt that shows her)
```
IDENTITY LOCK: the woman in image 1 — reproduce this exact person with a photographic identity match: same bone structure, eye shape, nose, lips, jawline, skin tone, hairline and hair texture. Do not beautify, average, age, or restyle the face. Expression unchanged, exactly as in the source.
```

## Shot 02 — staged restoration (gpt-image-2-5-sunburst, A/B nano-banana-2)
Each stage takes the **previous approved stage** as input. Log each one in `03_restore/log.md`: `stage | step | model | prompt | file | verdict`.

Stage template:
```
IMAGE REFERENCES: image 1 = [previous stage]; image 2 = original scan (identity reference only).
[IDENTITY LOCK]
Change ONLY: [STAGE CHANGE]. Keep pose, clothing, background, framing, crop, grain and tone exactly unchanged, pixel-faithful where undamaged.
```
| Stage | File | `[STAGE CHANGE]` |
|---|---|---|
| 1 | `stage_1_dust.png` | remove dust, specks and small spots |
| 2 | `stage_2_cracks.png` | repair the cracks, crease and torn edge by continuing the surrounding texture |
| 3 | `stage_3_clarity.png` → `locked/restored.png` | recover sharpness and contrast so the face reads clearly, as a well-preserved print of the same negative; black-and-white, natural grain, natural skin texture |
| 4 (optional, disclosed) | `stage_4_color.png` | colorize conservatively with muted, period-plausible tones |

Reject a stage if the face drifts: compare eyes, nose, mouth, jaw and hairline against the previous stage.

## Shot 03 — restrained motion (veo31, startFrame = `locked/restored.png`)
```
MOTION: slow, steady camera push-in toward the face; a soft band of warm window light drifts left to right across the print. The photograph is a still object on a wooden table — the image inside it is completely frozen.
AUDIO: quiet room tone only — no voice, no music.
NEGATIVE: face movement, blinking, mouth movement, lip-sync, expression change, head turn, paper warping, added text, lettering, logos, watermark, colour change.
```
6s, 16:9, 1080p. Roll 2; reject any take where the face changes.

## Shot 04 — hands with the voice (seedance-2.5, reference mode)
```
IMAGE REFERENCES: image 1 = hands_sheet; image 2 = locked/restored.png (the print); image 3 = room_plate. AUDIO REFERENCE: the testimony recording (timing only).
SCENE: top-down, warm late daylight; the hands from image 1 hold the print from image 2 still on the table from image 3.
MOTION: almost none — a thumb moves slightly along the print's edge during pauses in the voice; static camera.
AUDIO: natural room sound only — no music, no generated voice.
NEGATIVE: extra fingers, the photo changing, added text, lettering, camera movement.
```

## Shot 05 — the handoff (seedance-2.5, start/end frame mode)
Start = blank sleeve on the table, pen beside it. End = the same sleeve with the name area still **blank**; the name is added in the edit.
```
MOTION: a young hand picks up the pen and writes one short word on the sleeve, unhurried; static top-down camera.
AUDIO: pen scratch on paper, room tone — no music, no voice.
NEGATIVE: legible generated letters, extra fingers, camera movement.
```
**The name itself is never generated.** Either (a) film a real hand writing it on real paper, or (b) bake it as an overlay: render the name in a handwriting web font in HTML, wait for `document.fonts.load()` before drawing, export to PNG through a canvas, and animate a left-to-right reveal mask synced to the pen. Script fonts get little or no stroke. Check the PNG is flattened pixels, not a live overlay.

## Fictional mode only — generated portrait (seedream_5_pro A/B nano-banana-2) → `locked/original.png`
```
Black-and-white studio portrait photograph, [FICTIONAL PLACE], [YEAR]. A woman in her thirties, seated, three-quarter view, calm direct gaze, [DRESS FROM 02_source/research.md]. Plain painted studio backdrop. Authentic print wear: faded contrast, fine scratches, a crease across one corner, a slightly torn edge. Silver-gelatin grain, uninhabited background, untouched by any modern element. An original fictional person, not a real individual.
```
Then run the staged restoration on it exactly as you would on a real photo.

## Fictional mode only — lock set (nano-banana-2)
```
IMAGE REFERENCES: image 1 = palette swatch.
SCENE: top-down, 16:9, warm late daylight on a worn wooden table; a young person's hands, [SKIN TONE, RING, SLEEVE], shown in three panels: resting flat, holding a small print, holding a pen. Natural anatomy, five fingers each. Plain, text-free.
```

## Captions
Source: the shot 04 testimony audio. Output: burned-in EN subtitles plus an FR version. Check every name and place by ear with the witness; never trust auto-transcription of names.

## Critic pass → see AGENT_PROMPTS.md phase 8 (pass / partial / fail rubric)
