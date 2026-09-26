# Restoration log — every result explains itself

Mode: **FICTIONAL proof of concept** — Brazzaville, 1890. No real person is depicted.
Source: `02_source/portrait_variant_A.png` (picked by director) → `locked/original.png`, untouched.
Model for every stage: Arcads `nano-banana-2` (Nano Banana Edit), 16:9, input = previous stage only.
Shared lock prepended to every stage prompt (see `01_bible/prompts.md`).

Honesty notes:
- Clothing and backdrop were chosen by the model, not researched. Nothing in the image is period fact.
- The prompt specifies silver-gelatin grain; an 1890 Brazzaville print would more likely be albumen (brown-toned). Kept as written.

| stage | step | model | prompt | file | input | Arcads asset | face check vs previous |
|---|---|---|---|---|---|---|---|
| 0 | fictional portrait (generated) | nano-banana-2 | prompts.md "Fictional mode only — generated portrait", place/year = Brazzaville, 1890; clothing = "simple everyday clothing of that place and period" (not researched) | `locked/original.png` | text only | 06a652cb-c5e8-40d3-9760-d245a256dcfc | — |
| 1 | dust & specks | nano-banana-2 | lock + "Remove dust, specks and small spots only. Keep film grain, tone and all damage larger than a speck." | `03_restore/stage_1_dust.png` | stage 0 | 7bb0b581-fe05-4e8b-a737-05752ed12883 | PASS — same eyes, nose, lips, hairline, expression; specks removed; crack, crease, torn corner kept; slightly softer tone |
| 2 | cracks & tears | nano-banana-2 | lock + "Repair the cracks, crease and torn edge by continuing the surrounding texture. Do not repaint areas that are undamaged." | `03_restore/stage_2_cracks.png` | stage 1 | c746fb5d-da22-4a40-8b5a-225617d7550a | PASS — face, pose, clothing, backdrop unchanged; crack, crease, torn corner rebuilt (print corners now intact). Watch: fine halftone-like dot texture on skin slightly stronger |
| 3 | clarity | nano-banana-2 | lock + "Recover sharpness and contrast so the face is clearly readable, as if from a well-preserved print of the same negative. Keep black-and-white, keep natural grain, no plastic skin." | `03_restore/stage_3_clarity.png` → `locked/restored.png` | stage 2 | 45bf1744-e17a-4caf-b3e9-368f8d16856d | PASS — eyes, nose, mouth, ears, hairline match stage 2 and the original; sharper, more contrast; slightly cooler/darker overall. Fine dot texture on skin is inherited from the generated original, not new drift |
| 4 | colour | — | skipped (not requested) | — | — | — | — |

## A/B per model_map.md §1 (added after main gained model_map.md)
| stage | step | model | prompt | file | input | Arcads asset | face check |
|---|---|---|---|---|---|---|---|
| 1 | dust & specks | gpt-image-2-5-sunburst | same lock + stage 1 prompt | `03_restore/ab_sunburst/stage_1_dust.png` (1920x1072) | stage 0 | 91deb785-463f-4f34-9689-6beda87518dc | REJECT — more drift than nano-banana-2: face longer and darker, brow/hairline changed, partly removed the crack it was told to keep, lower resolution |

Decision: nano-banana-2 chain kept (less face drift). Sunburst chain stopped at stage 1. On-screen caption for shot 02 therefore reads `· Nano Banana 2`, not `· GPT Image 2.5` as jua_context.md suggests.
`locked/restored.png` = stage 3 above — **pending Marty's approval** (CLAUDE.md: promote to locked/ only after approval).
