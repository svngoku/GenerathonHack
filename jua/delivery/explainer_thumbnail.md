# Explainer video + thumbnail (frameworks adapted from higgsfield-ai/skills, MIT)

## Explainer: FACE CAM, ≤ 60s, 8 required items (official deck)
**Format:** Marty's face on camera for the whole minute. Real process footage can appear as picture-in-picture or quick cutaways: the Arcads pipeline shown as a node graph (references → restoration stages → shots → music), rejected takes, `log.md`. **No avatar, no generated presenter.**

**Script rules:** about 150 words total, one block of about 18 words (≈ 7s) per item, numbers spelled out, never say "in this video", every fact from the logs. Don't invent any struggle.

| # | Required item | Cutaway | Script block (≈ 7s — fill the [brackets] from real experience) |
|---|---|---|---|
| 1 | Inspiration | worn original | "Old family photos keep faces but lose names. I wanted a film about the one thing AI can't restore." |
| 2 | What it is | original → restored split | "Jua — More Than a Photograph: AI restores a woman's face; only a living voice can give back her name." |
| 3 | How I built it | node graph of the pipeline | "Locked references, a restoration in stages, one frozen-face motion shot, hands and sound, then a score that resolves on the name." |
| 4 | Tools used | model names on screen | "All in Arcads: GPT Image and Nano Banana to restore, Veo and Seedance for motion, ElevenLabs and Suno for music." |
| 5 | Challenges | rejected takes side by side | "[Real, e.g. video models kept making her blink — I rejected N takes; finding a true testimony.]" |
| 6 | Proud of | the silence beat | "[Real, e.g. the moment the music stops and a real voice says her name.]" |
| 7 | What I learned | restoration log | "[Real, e.g. limbic narration is restraint — breath, touch and silence move people more than any effect.]" |
| 8 | What's next | Jua UI | "Bring this into Jua: restore archives with families, and let communities write the names back themselves." |

Cutaway B-roll prompts (only if you need generated inserts), one locked STYLE line pasted into every block:
```
STYLE REFERENCE: match the attached frame exactly — warm late daylight, wooden table, paper grain, honey #D9A35F / paper #F4EAD5 palette.
SCENE: {one action for this beat}. MOTION: {one camera move}.
AUDIO: ambient room sound only — no voice, no music.
NEGATIVE: lip-sync, captions, on-screen text, logos, watermark, colour drift.
```

## Thumbnail (1280×720)
**Rules:** brainstorm at least 5 concepts, combine at most 2 frameworks, it must read in under 1 second at about 120px wide, and it must be **truthful** to the film.

| Concept | Framework | Idea |
|---|---|---|
| **A (recommended)** | Before / After | the damaged original (left) and the restored print (right) on the table; a hand holds a pen over the blank sleeve between them |
| B | Posed portrait | the restored face fills 50% of the frame with a torn edge visible; the name slot on the sleeve is empty |
| C | Information gap | the original print with "WHO WAS SHE?" in a baked overlay |
| D | Before / After + gap | A, plus a small baked "?" where the name goes |
| E | Hands | top-down: a young hand and an old hand both touching the print |

**Prompt order** (nano-banana-2, refs: `original.png`, `restored.png`, `hands_sheet.png`):
Frame (16:9 thumbnail) → Scene → Text policy (**image fully text-free**) → Subject at 40–60% of the frame, face sharp, with the IDENTITY LOCK → Key element (pen, blank sleeve) → Composition (one hero on a power third) → Background (wooden table, soft) → Lighting (warm key + soft fill + gentle rim on the print edge) → Grade (restrained, warm; this film is calm).

**Text:** optional, and baked afterwards (HTML render → canvas → PNG, fonts loaded first), max 3 words.

**QA:** face matches the restored print · no stray text or watermark · baked text correct letter for letter · readable at 120px · promises nothing the film doesn't show.
