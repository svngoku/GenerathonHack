# Generathon #2 — agent instructions

Deadlines: **Sun 2026-09-27 — soft 13:30 (stop & upload), hard 14:00** (internal cutoff 12:00). Active project: **`jua/`** — "Jua — More Than a Photograph", track **Three Minutes to Move — Short Film**, challenge **"Limbic Narration, Not Just a Voice-Over"**, 75s, 16:9.

## Read first, in order
0. `jua/00_brief/official_rules.md` — organizers' rules, deliverables, judging (overrides everything)
1. `jua/00_brief/jua_context.md` — what Jua is and how it shapes the story
2. `jua/00_brief/brief.md` — arc, mode, honesty rules, emotion variants
3. `jua/01_bible/model_map.md` — which Arcads model does which job (verified API limits)
4. `jua/01_bible/shotlist.csv`, `visual_bible.md`, `prompts.md`
5. `jua/05_audio/score.md` — the music tells the story too (motif resolves when the name is written)

Phase-by-phase prompts: `jua/AGENT_PROMPTS.md` (0 kickoff → 9 delivery).

## The story in one line
AI restores a face; only people can give back a name. **Absence → curiosity → belonging.** The climax is a real human voice, never an AI effect.

## Hard rules (stop and ask rather than break one)
- **No narrator / voice-over.** The only spoken words are the witness's, inside the scene (limbic narration: breath, touch, silence, a sensory memory).
- **Afro-rooted and specific:** Kinshasa, Lingala, Congolese rumba ("Pitié"), the Kinshasa studio-portrait tradition; see `jua_context.md` § Afro roots. Never generic "African".
- **Never invent** a name, place, date, clothing fact or biography. Unknown → `[TODO: ask Marty]`.
- **Restore, never re-create:** each restoration stage takes the previous stage as input; reject any output where the face drifts.
- **Nobody in the photograph moves their face or speaks.** Talking-actor / omnihuman / audio_driven models are forbidden on the portrait.
- No generated lettering — names and titles are real handwriting or baked overlays (method in prompts.md, shot 05).
- Follow the 6 prompt rules and the IDENTITY LOCK at the top of `jua/01_bible/prompts.md` in every generation.
- Original is shown before and beside the restoration, never replaced by it. Colour, if used, is disclosed.
- **Honesty gate (TypeSafe):** before any text ships (subtitles, end card, explainer, submission), run `jua/tools/honesty_check.py` — every factual sentence must come back `verified` against the transcript / research / logs. Needs `TYPESAFE_API_KEY`.
- Fictional mode → end card: "Fictional proof of concept. No real person is depicted."

## How to work
- Use the Arcads MCP (discover tools live; the `arcads:media-router` skill helps). Check credits before each batch.
- Every final-candidate generation: **2 variants in parallel**, then pick with a one-line verdict each.
- Consistency comes from `jua/locked/` — pass the same reference set to every call. Promote an asset to `locked/` only after Marty approves it.
- Log every generation in `jua/03_restore/log.md` (restoration) or `jua/04_video/log.md` (video): `shot | model | prompt | refs | file | verdict`.
- Save outputs to the folder named in `shotlist.csv`; update its `status` column (`todo → draft → approved`).
- **Checkpoints — stop and show Marty:** after the animatic, after restoration stages, after each hero shot, after music. Don't run ahead.
- Commit + push after each checkpoint (`feat(jua): shot 03 takes v01-v02`). Keep each video file < 100 MB.

## Definition of done
Muted, a stranger reads: worn photo → face becomes clear → a name is written. With sound: the music stops and a real voice says who she was. `jua/delivery/submission.md` filled, YouTube link unlisted and playable, **face cam explainer ≤ 60s covering all 8 items** (inspiration, what, how, challenges, proud of, learned, next, tools).
