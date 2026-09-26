# Explainer video + thumbnail (frameworks adapted from higgsfield-ai/skills, MIT)

## Explainer (≤ 90s, target 85s)
**Format:** Marty on camera or voice-over, cut with real process footage: Arcads screens, the `log.md` files, restoration stages, rejected takes. Rejected takes are the most honest proof of the struggle.

**Script rules:** blocks of 20–24 words (≈ 8–9s each). No timecodes or stage directions, numbers spelled out, never say "in this video". Every fact comes from the logs; don't invent any.

| # | Beat (form field) | Visual | Script block (fill from real experience) |
|---|---|---|---|
| 1 | Hook | worn original → restored, split | "AI can bring back a face from a damaged photograph. It cannot bring back her name. That gap is what this film is about." |
| 2 | About | shot 04 still + waveform | "Jua is my workspace to make, restore, and keep African heritage images together. Here, a real voice gives back what restoration can't." |
| 3 | Tools & why | Arcads screen, model names | "I ran Jua's pipeline in Arcads: [models] for a staged restoration, [veo] for one frozen-face shot, [seedance] for hands and sound." |
| 4 | Tools & why | log.md scrolling | "Every stage is logged with its model, because in Jua every result explains itself. The music was generated, the voice never." |
| 5 | Difficulties | 2–3 rejected takes side by side | "[Real struggle, e.g. video models kept making her blink; I rejected N takes.]" |
| 6 | Difficulties | [screen] | "[Second real struggle, e.g. finding a photo and someone who could speak truthfully about it.]" |
| 7 | Learned | the silence beat | "[Real lesson, e.g. restraint is the effect — the strongest moment is when the music stops.]" |
| 8 | Better | Jua UI / sleeve | "[Real improvement, e.g. record the testimony first and let the community add names to photos themselves.]" |
| 9 | Payoff | end card | "We can restore the image. We remember the person together." |

Clip prompts for explainer B-roll (if any are generated), one locked STYLE line pasted into every block:
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
