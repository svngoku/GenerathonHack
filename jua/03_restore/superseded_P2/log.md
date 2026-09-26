# Restoration log — every result explains itself (phase 3, redo on P2)

Mode: FICTIONAL proof of concept — Brazzaville, 1890. No real person is depicted.
Input: `locked/original.png` = P2 (seedream_5_pro, asset 80ab873f-4198-4edc-8add-208b9af110a4), untouched.
Template: prompts.md stage template — `IMAGE REFERENCES: image 1 = previous stage; image 2 = original (identity only)` + IDENTITY LOCK + `Change ONLY: [stage]… pixel-faithful where undamaged.`
Each stage: gpt-image-2-5-sunburst AND nano-banana-2 from the same previous stage; keep the one with less face drift (eyes, nose, mouth, jaw, hairline). Candidates in `03_restore/ab/`.
Earlier variant-A run: `superseded_variantA/log.md`.

Format: `stage | step | model | prompt | file | verdict`

| stage | step | model | prompt | file | verdict |
|---|---|---|---|---|---|
| 1 | dust & specks | gpt-image-2-5-sunburst | template, change = "remove dust, specks and small spots" | `ab/stage_1_sunburst.png` (42a437c1-f922-468e-be9d-64cafecdf479, 1920x1072) | REJECT — face reframed/enlarged, brow harder, deeper shadows |
| 1 | dust & specks | nano-banana-2 | same | `ab/stage_1_nano.png` → `stage_1_dust.png` (41b51f86-d124-42a9-a9c3-a437c06c9bf4, 2752x1536) | KEEP — eyes, nose, lips, jaw, hairline match original; torn corner kept; slightly cooler |
| 2 | cracks & tears | gpt-image-2-5-sunburst | template, change = "repair the cracks, crease and torn edge by continuing the surrounding texture" | `ab/stage_2_sunburst.png` (458dedb5-7a73-4270-99dd-837cc7827090, 1920x1072) | REJECT — face rounder and darker, heavier shadows |
| 2 | cracks & tears | nano-banana-2 | same | `ab/stage_2_nano.png` → `stage_2_cracks.png` (44cb3395-7a98-46c6-9338-320aa1ff67e5) | KEEP — face matches stage 1; torn corner and edge repaired; faint pink cast on backdrop |
| 3 | clarity | gpt-image-2-5-sunburst | template, change = "recover sharpness and contrast so the face reads clearly, as a well-preserved print of the same negative; monochrome warm albumen tone, natural grain, natural skin texture" ("black-and-white" → "monochrome warm albumen tone" per research fact 5) | `ab/stage_3_sunburst.png` (3534ca12-642f-4cab-9891-18c79c93260f, 1920x1072) | REJECT — heavier brow, rounder face, stronger shadows |
| 3 | clarity | nano-banana-2 | same | `ab/stage_3_nano.png` → `stage_3_clarity.png` (829ed8d7-53ca-4280-b27c-e866723fb804) | KEEP — eyes, nose, mouth, jaw, hairline match stage 2 and original; sharper; fine dot-screen texture on skin at full size; skin slightly darker from contrast |
| 4 | colour | — | skipped (not requested) | — | — |

Result: nano-banana-2 won every stage (sunburst drifted each time). Shot 02 captions: `stage N · step · Nano Banana 2`. `stage_3_clarity.png` → `locked/restored.png` **on Marty's approval**. Credits for phase 3: 0 (daily image limit).
