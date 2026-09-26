# Model map — Jua (Arcads, verified against external-api.arcads.ai/docs-json, 2026-09-26)

Rule of thumb: **one locked reference set, reused by every model.** Consistency comes from the refs, not from the prompt.

## 0. The lock set (make once, reuse everywhere) → `jua/locked/`
| File | What | Made with |
|---|---|---|
| `original.png` | the photo as found (real scan, or fictional portrait) | scan / image model (§1) |
| `restored.png` | stage 3 of the restoration | §1 restoration |
| `hands_sheet.png` | the younger person's hands: sleeve, ring, skin, nails — 3 angles | nano-banana-2 |
| `room_plate.png` + `table_close.png` | the one room + wooden table, same light direction | nano-banana-2 |
| `sleeve.png` | the blank paper photo sleeve | nano-banana-2 |
| `palette.png` | cool→honey palette swatch (#9AA3A8 → #D9A35F, paper #F4EAD5) | any |

Create one Arcads **project "Jua"** and put every asset in it — Jua's "keep the story together", mirrored in Arcads.

## 1. Image models (`/v2/images/generate`)
| Job | Primary | A/B or fallback | Why (max refs) |
|---|---|---|---|
| Restoration stages 1–3 (edit, identity lock) | **gpt-image-2-5-sunburst** | nano-banana-2 | strongest editor, 16 refs; run each stage on both, keep the one with **less face drift** |
| Optional colour stage | gpt-image-2-5-sunburst | nano-banana-2 | conservative; disclosed on end card |
| Fictional portrait (period B&W, print wear) | **seedream_5_pro** | nano-banana-2 | A/B for authenticity; research dress of [PLACE, YEAR] first |
| Lock set: hands, room, table, sleeve | **nano-banana-2** | gpt-image-2-5-flare | 14 refs → best multi-reference consistency |
| Keyframes (hands + print + table composites) | **nano-banana-2** | gpt-image-2-5-sunburst | refs: original/restored + hands_sheet + table_close |
| Quick mood / thumbnail layout drafts | grok_image | reve_2_1 | fast & cheap; never final |
| — | ~~soul~~ | | 0 refs = no consistency → don't use |

## 2. Video models (`/v2/videos/generate`, `/v1/omni-flash`)
| Job | Primary | Fallback | Why |
|---|---|---|---|
| **Animatic of all 6 shots** (timing & story check before spending) | **grok-video** 480p | seedance-2.0-mini | cheap, 1–15s |
| Shot 01 macro pan over the worn print | **seedance-2.5** (refs: original + table_close) | kling-3.0 | 30 refs keeps the print exact; `audioEnabled` → room tone |
| Shot 02 restoration transitions (optional) | **veo31** start=`original` end=`restored` | kling-3.0 start/end | best temporal consistency; if it invents anything, fall back to crossfades in edit |
| **Shot 03 restrained motion, face locked** | **veo31** startFrame=`restored.png`, 1080p | kling-3.0 (start frame), seedance-2.5 (start frame) | strongest instruction-following → "face does not move" is respected most |
| Shot 04 hands holding print while voice speaks | **seedance-2.5** refs: hands_sheet + restored + room_plate + **testimony audio** | minimax-h3 (accepts ref audio on its own) | the audio ref lets the hands' stillness/pauses follow the real voice |
| Shot 05 hands write the name on the sleeve | **seedance-2.5** start=`sleeve blank` end=`sleeve with name` (name composited from real handwriting) | kling-3.0 | never trust generated lettering — real handwriting overlay in edit |
| Surgical fix on a good take (remove artifact, steady a drifting edge) | **omni-flash** (Gemini Omni Flash, conversational edit) | re-roll | = kit prompt F, for video |
| — | ~~talking-actors / omnihuman / audio_driven~~ | | **forbidden on the portrait** — no one in the photo speaks |

Constraints to remember: seedance-2.5 takes **either** start/end frames **or** reference media per call, not both · 16:9 only via `aspectRatio` (with a start frame it inherits the frame's shape) · durations: seedance-2.5 4–30s, kling-3.0 3–15s, veo31 fixed.

## 3. Sound (`/v1/music/generate`, video `audioEnabled`, voices)
Sound is where the story is rooted. Plan it as three layers:

| Layer | Source | Notes |
|---|---|---|
| **Diegetic** — room tone, paper, sleeve, pen scratch, breath | seedance-2.5 `audioEnabled: true` on shots 01/04/05 | prompt: "natural room sound only, no music, no voices" |
| **Music** — cue A (10–38s) + cue B (58–75s), silence under the voice | **elevenlabs** music, `instrumentalOnly: true`, exact durations 28s and 17s | full score, motif and prompts: **`05_audio/score.md`** |
| Music variations to choose from | suno_v6 (2 tracks per call, same price) | pick by ear, then regenerate the chosen mood in elevenlabs for exact length |
| **Voice** — testimony | **real recording** (non-negotiable in documentary mode) | Arcads captions (if exposed by the MCP) or editor subtitles; names checked by a human |
| Voice — fictional mode only | Arcads voices / imported ElevenLabs voice, disclosed | or better: a consenting person reads `05_audio/script.md` |

Music: see **`jua/05_audio/score.md`** (unfinished motif → silence → motif resolves on the name).

## 4. Order of spend
1. `GET /v1/credits` → check budget.
2. Lock set (§0) → animatic (grok-video) → watch muted: does the story read?
3. Restoration stages (sunburst vs nano-banana-2 A/B) → `restored.png`.
4. Hero shots: 03 (veo31) → 04/05 (seedance-2.5) → 01.
5. Music cues (elevenlabs) cut to the final timing — music last, so it fits the picture.
6. omni-flash fixes only on otherwise-approved takes.
