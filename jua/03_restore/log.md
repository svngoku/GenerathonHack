# Restoration log — every result explains itself (phase 3 on K1, Kinshasa 1972)

Mode: FICTIONAL proof of concept. Input: `locked/original.png` = K1 (seedream_5_pro, asset 3334cbcf-0ed1-4598-825a-b40642aa02d1).
Template: prompts.md stage template (IMAGE REFERENCES + IDENTITY LOCK + "Change ONLY … pixel-faithful where undamaged"). Each stage A/B: gpt-image-2-5-sunburst vs nano-banana-2 from the same previous stage. Earlier runs: `superseded_P2/`, `superseded_variantA/`.

| stage | step | model | prompt | file | verdict |
|---|---|---|---|---|---|
| 1 | dust & specks | gpt-image-2-5-sunburst | template, change = "remove dust, specks and small spots" | `ab/stage_1_sunburst.png` (a5692979-7737-4298-9649-b01182583f89) | REJECT — face softer and rounder |
| 1 | dust & specks | nano-banana-2 | same | `stage_1_dust.png` (7bfc1e3a-8751-4526-af2d-d70c0d12daf6) | KEEP — eyes, nose, mouth, jaw, headwrap match K1 |
| 2 | cracks & tears | gpt-image-2-5-sunburst | "repair the cracks, crease and torn edge…" | `ab/stage_2_sunburst.png` (4797d6c7-adc1-4674-ae8b-1a8309a4d004) | REJECT — face shape shifts |
| 2 | cracks & tears | nano-banana-2 | same | `stage_2_cracks.png` (83106d13-77ab-40b4-9413-dc84f2d3fe91) | KEEP — face unchanged vs stage 1; torn edge repaired |
| 3 | clarity | gpt-image-2-5-sunburst | "recover sharpness and contrast … black-and-white, natural grain, natural skin texture" | `ab/stage_3_sunburst.png` (384db841-5dc3-41d5-8635-741fc4cbf044) | REJECT — face rounder, heavier |
| 3 | clarity | nano-banana-2 | same | `stage_3_clarity.png` (78a7a614-4869-4980-a6ad-312caa742910) | KEEP — sharper, identity matches K1; fine texture on skin at full size |
| 4 | colour | — | skipped | — | — |

Nano Banana 2 won all three stages. Shot captions: `stage N · step · Nano Banana 2`. stage 3 → `locked/restored.png` on Marty's approval. Credits: 0.
