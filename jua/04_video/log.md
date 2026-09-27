# Video log — every result explains itself

Format: `shot | model | prompt | refs | file | verdict`. Earlier variant-A work: `superseded_variantA/log.md`.
Credits before phase 2: 47,376.

## Phase 2 — animatic (grok-video 480p, story test only; nothing here is final)
Start frame for 01/03/04: `06_edit/animatic/print_on_table.png` = `locked/original.png` (P2) composited onto `02_source/lockset/table_2.png` locally (no generation). Grok takes a start frame only — no hands/room refs.

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| 01 | grok-video 480p, 10s | MOTION macro glide from torn corner along crease to face; AUDIO room tone, paper, breath; NEGATIVE face movement… | start = print_on_table | asset cede4f19-9d17-4a68-9cca-53fee29dc250 → `06_edit/animatic/grok_01.mp4` (200 cr) | OK for timing; face drifts toward a smile by 8–10s |
| 02 | none (local stills) | original 3s + 3 placeholder stage captions 4s each + wipe back 3s | locked/original.png | `06_edit/animatic/shot_02.mp4` | placeholder — restoration not run yet |
| 03 | grok-video 480p, 10s | prompts.md shot 03 (motion-only + AUDIO + NEGATIVE) | start = print_on_table (via cede4f19 stored start frame) | asset dbaa3095-a2c5-43de-b829-20a7a90bebfb → `grok_03.mp4` (200 cr) | OK for timing; face drifts toward a smile at the close-up |
| 04 | grok-video 480p, 15s + 5s held last frame | hands enter and hold the print; thumb on edge; room sound | start = print_on_table | asset 1c86d283-3584-457b-aa71-028d7f520cca → `grok_04.mp4` (304 cr) | OK for timing; hands light-skinned (no hands ref possible in Grok) |
| 05 | grok-video 480p, 12s | young hand picks up pen, writes one short word; pen scratch | start = `02_source/lockset/sleeve_2.png` | asset 3a27544c-a061-4ec2-99a5-efd302e960f8 → `grok_05.mp4` (240 cr) | OK; nothing legible written; hands light-skinned |
| 06 | none (local) | side by side (restored = placeholder) + end line + fictional disclosure, baked overlay | locked/original.png | `06_edit/animatic/shot_06.mp4` | placeholder |

Assembly: `06_edit/animatic_v01.mp4` (75.04s, 854x480, no music; shot 04 has a baked placeholder subtitle). Phase 2 spend: 944 credits.

## Phase 2 v02 — animatic rebuilt for Kinshasa 1972 (K1 locked)
Previous (P2) animatic and its segments moved to `06_edit/superseded_P2/`. Start frame: `06_edit/animatic/print_on_table.png` = `locked/original.png` (K1) composited on `locked/table_close.png` (local).

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| 01 | grok-video 480p, 10s | as v01 + "smiling" added to NEGATIVE | start = print_on_table (K1) | asset db644c54-6691-455b-ad73-8c989f67fc9c → `grok_01.mp4` (200 cr) | OK for timing; face drifts into a smile by ~9s despite the NEGATIVE |
| 02 | none (local) | as v01 with K1 | locked/original.png | `shot_02.mp4` | placeholder |
| 03 | grok-video 480p, 10s | prompts.md shot 03 + "smiling" in NEGATIVE | start = print_on_table (via db644c54 stored start frame) | asset 13a44a6e-dd0f-47a6-a70a-ecf51d01b05e → `grok_03.mp4` (200 cr) | OK for timing; smiles in the close-up |
| 04 | grok-video 480p, 15s + 5s hold | hands (dark brown skin, grey cuffs) hold the print | same | asset 3709f070-3451-4746-98e3-83dd70bce79d → `grok_04.mp4` (304 cr) | OK — hands now match locked hands_sheet |
| 05 | reused from v01 | — | sleeve | asset 3a27544c-a061-4ec2-99a5-efd302e960f8 → `grok_05.mp4` | OK for timing; hand is light-skinned (mismatch with 04) — real shot 05 uses the lock set |
| 06 | none (local) | as v01 with K1 | locked/original.png | `shot_06.mp4` | placeholder |

Assembly: `06_edit/animatic_v02.mp4` (75.04s, 854x480, no music). Phase 2 v02 spend: 704 credits.

## Phase 2 v03 — consistency fix (Marty: "no consistency at 0:59 … each frame full consistency … direct link with image choices and music")
Rule adopted: **every frame is built from `locked/`.** Faces come only from K1 pixels; hands only from `hands_sheet`; table/sleeve/pen only from the locked plates. v02 Grok takes moved to `06_edit/superseded_v02/`.

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| 01 | none — local pan (Pillow+ffmpeg, `animatic/build_moves.py 01`) | torn edge → face, 10s | `print_on_table.png` (K1 on locked table) | `animatic/move_01.mp4` | KEEP — face = K1 pixels, no drift |
| 03 | none — local push + honey light band (`build_moves.py 03`) | full frame → face, 10s | same | `animatic/move_03.mp4` | KEEP — face = K1 pixels |
| KF04 v1 | nano-banana-2 ×2, generated from refs | hands + print + table from refs | hands_sheet, K1, table_close | `keyframes/v1/kf04_a,b.png` (afbd6fe6…, c8bbdd3d…) | REJECT — print redrawn portrait-format, damage lost |
| KF05 v1 | nano-banana-2 ×2 | hands + pen + print + sleeve from refs | hands_sheet, K1, sleeve | `keyframes/v1/kf05_a,b.png` (232a5f07…, 782ccf18…) | REJECT — print redrawn; b has two pens |
| KF04 v2 | nano-banana-2 ×2, **edit of a locked-pixel base** (`keyframes/base04.png` = K1 on table) | "Change ONLY: add the hands from image 2 … keep the print … pixel-faithful" | base04, hands_sheet | `keyframes/kf04_c.png` (516bf34b-4ff6-4380-aa5b-0840cc8b4a93) KEEP · `kf04_d.png` (a221f43f…) alt | KEEP c — print untouched, locked hands on the edges, face clear |
| KF05 v2 | nano-banana-2 ×2, edit of `keyframes/base05.png` (locked sleeve + pen + K1 print) | "Change ONLY: add the hands … right hand picks up the pen … only one pen" | base05, hands_sheet | `keyframes/kf05_c.png` (1e46eafd-f48c-4432-abb8-855fca7863d5) KEEP · `kf05_d.png` (79637e57…) alt | KEEP c — one pen, locked hands, blank sleeve, K1 print unchanged |
| 04 | grok-video 480p, 15s + 5s hold | thumb moves along the edge; room sound | start = KF04 c | asset f76eba41-5db9-4e2b-b4dd-e14b44f65d6d → `animatic/grok_04.mp4` (304 cr) | KEEP (animatic) — hands consistent; right hand lifts the print corner near the end |
| 05 | grok-video 480p, 12s | hand hesitates, writes one short word; pen scratch | start = KF05 c | asset c43f6a86-e920-4020-aa9e-f0ec5e3025da → `animatic/grok_05.mp4` (240 cr) | KEEP (animatic) — same hands, K1 print unchanged; nothing legible written |

Music link (local only, never uploaded): rough "Pitié" bed from `05_audio/reference/tabu_ley_pitie.mp3` — cue A = song 0:00–0:28 at film 10–38s (2s fade-in, hard cut at 38s); silence 38–58s; cue B = song 3:47–4:04 (its own outro) at film 58–75s (1s fade-out). Picked from a 4s RMS loudness profile (opening = quietest build; ending = the song's own resolution) — **confirm by ear**. End card now credits *Music: Tabu Ley Rochereau, "Pitié"*. Placeholder name overlay "[her name]" at 66.5–70s.

Assembly: `06_edit/animatic_v03.mp4` (75.00s, 854x480). v03 spend: 544 credits.

## Phase 2 v04 — Seedance 2.5 for 04/05, Higgsfield prompt rules, nothing cut at the frame edge
Marty: "try with seedance 2.5 … follow the prompts from the skills of higgsfield … some elements are cut in the middle".
Higgsfield skills read from github.com/higgsfield-ai/skills (`higgsfield-generate/references/prompt-engineering.md`, `media-inputs.md`, `model-catalog.md`): Seedance 2.5 is the default all-purpose video model; use reference mode with the opening frame as a reference; for image-to-video, describe motion only and don't re-describe the frame; prompts under ~200 tokens; phrase positively.
Framing fixes: base frames rebuilt so print, sleeve and pen sit fully inside with margin (`keyframes/base04_v3.png`, `base05_v3.png`); 01 pan re-pathed so her head never leaves frame; 03 push ends headwrap→knees.

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| KF04 v3 | nano-banana-2 ×2, edit of base04_v3 | "Change ONLY: add the two hands … fingertips on the lower corners … whole print fully visible" | base04_v3, hands_sheet | `keyframes/kf04_e.png` (1f01e082-a599-435c-9750-b82866367019) KEEP · `kf04_f.png` (96986bc1…) alt | KEEP e — whole print visible, hands match the lock set |
| KF05 v3 | nano-banana-2 ×2, edit of base05_v3 | "Change ONLY: add the hands … right hand picks up the pen … only one pen" | base05_v3, hands_sheet | `kf05_e.png` (ce993eaf…) REJECT (2 pens) · `kf05_f.png` (dcf5d026-3ec5-4f76-a78d-d98cbe8516c4) KEEP | KEEP f |
| 04 A | seedance-2.5, 20s, 720p, audio on | IMAGE REFERENCES (opening frame, hands, print, table) + IDENTITY LOCK + MOTION (thumb along the edge) + AUDIO + NEGATIVE | kf04_e, hands_sheet, K1, table | asset 6a47453e-c25b-421b-a5f7-8a96ffd05c66 → `04_video/seedance25/shot04_A.mp4` (840 cr) | **KEEP** — whole print in frame, locked hands, print face stable 0→20s, room sound |
| 04 B | same | same | same | asset de7b13c8-9f9f-4495-b135-633cff9748e4 → `shot04_B.mp4` (840 cr) | ALT — equally clean, print framed slightly lower |
| 05 A | seedance-2.5, 12s, 720p, audio on | refs + motion "hesitates, then writes one short word"; NEGATIVE "second pen" | kf05_f, hands_sheet, K1, sleeve | asset 00dac01e-10e1-40d3-bff4-c7b5218f6e47 → `shot05_A.mp4` (504 cr) | REJECT raw — re-added the second pen from the sleeve ref |
| 05 B | same | same | same | asset c6a21778-9561-4dbd-b7ab-0429b83f2ee4 → `shot05_B.mp4` (504 cr) → `shot05_B_penfix.mp4` | **KEEP (fixed)** — same extra pen, removed locally by compositing the keyframe's empty table over that area (static camera); scribble illegible |

Lesson: a sleeve reference that contains a pen gets copied even with "second pen" in NEGATIVE — for the final shot 05 use a sleeve reference without the pen.
Assembly: `06_edit/animatic_v04.mp4` (75.00s), built by `06_edit/animatic/assemble_v04.sh` (local "Pitié" bed as in v03; name placeholder moved clear of the hands). v04 spend: 2,688 credits.

## 3-min extension — beat "inside the photograph" (0:36–0:55)
| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| inside | none — local macro drifts (`04_video/local/inside_photo.py`), 18s, 1920x1080 | face+headwrap → folded hands → liputa → torn edge pulling back to the whole print, 0.5s dissolves | locked/original.png (K1 pixels only) | `04_video/local/shot_inside_photo.mp4` | KEEP — zero drift by construction |

## Cut v05 (2:36) — 3-minute direction, Marty: "approved, keep the script, disclosed AI voice, add others images from the base as 'Souvenir', one ref truly REALISTIC"
`locked/restored.png` = K1 stage 3 (approved). Voice: Arcads TTS (ElevenLabs), disclosed on the end card.

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| voice | Arcads TTS, voice "Elisa" (Young, Calm, FR) ×1 | 05_audio/script.md (hum removed: TTS can't hum) | — | asset 080fcc74-bc95-47a8-bea6-2e918ef3b21c → `05_audio/voice/testimony_elisa.wav` (22s, 8 cr) → paced to 37s (`06_edit/v05/voice_paced.wav`) | **KEEP** — slower, more room for breath |
| voice | Arcads TTS, voice "Gloria" (Young, Calm, FR) | same | — | asset c78686df-93c1-45fd-a76b-12372e5427df → `testimony_gloria.wav` (19s, 8 cr) | ALT — faster, less intimate |
| souvenirs KF | nano-banana-2 ×2, edit of `06_edit/souvenirs/base_souvenirs.png` (K1 + K2 + K3 prints on locked table) | "Change ONLY: make it a true photograph, fully realistic … add the hands from image 2 … keep the three women … pixel-faithful" | base, hands_sheet | `souvenirs/kf_souv_a.png` (afc022db-5683-43a4-b37b-85db461e5274) KEEP · `kf_souv_b.png` (c944c3eb…) | KEEP a — photoreal, grey cuffs kept; b drops the cuffs |
| souvenirs | seedance-2.5 ×2, 12s 720p, audio | IMAGE REFERENCES + IDENTITY LOCK + MOTION (slide the centre print closer, light band) + AUDIO + NEGATIVE | kf_souv_a, hands_sheet, K1 | A: 21b0e5a1-61b5-40e9-a870-7df8ef500e48 → `04_video/seedance25/souvenirs_A.mp4` (504) · B: 7d932c4b-22db-4ac1-aa37-06dae32689e6 (504, still rendering at cut time) | **KEEP A** — all faces frozen, prints stay in frame |
| back of print | seedance-2.5 ×2, 10s | hands turn the print over; back plain, faint illegible pencil | kf04_e, hands_sheet | A: 20e4cddf-8088-42e6-b12a-544d6c741974 → `back_A.mp4` (420) · B: be592a0e-9e73-4711-88c5-19b5c4ef7d79 → `back_B.mp4` (420) | **KEEP A** — her face visible mid-turn, blank back; B flatter |
| room | seedance-2.5 ×2, 8s | static, sunlight shifts across the table, distant Kinshasa | locked room_plate (K2) | A: 3d398e9a-d578-41a9-973a-e7bd725e9cd2 → `room_A.mp4` (336) · B: 5cc3fdea-5caf-4950-a81d-1bd2cc6f9ac5 → `room_B.mp4` (336) | **KEEP A** — light moves; B similar |
| name | none — baked handwriting (Caveat, OFL, `06_edit/v05/OFL_caveat.txt`) on shot05_B_penfix, revealed with the pen, only on paper pixels | "Mama Nzeba" | — | `06_edit/v05/shot05_named.mp4` | KEEP — no generated lettering |
| locals | Pillow+ffmpeg | restoration beat (stages + captions + wipe), 1080p moves 01/03, inside-photo, slow push on restored face, side by side, end card | locked/ only | `06_edit/v05/*.py` | KEEP |

Assembly: `06_edit/cut_v05.mp4` (2:36, 1920x1080, 48 kHz, loudnorm −14 LUFS), rebuilt by `06_edit/v05/build_v05.sh`. "Pitié" (local only): song 0:00–1:16 at 0:10–1:26, silence under the voice 1:26–2:03, song 3:31–4:04 at 2:03–2:36. Spend this round: ~3,030 credits.

## Round v06 (Marty: African-accented voice, scenes linked to the "Pitié" lyrics, smooth 1:21→1:27)
| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| voice catalogue | Arcads `list_voices` (499 female voices) | metadata has no accent field; 16 French voices, all standard names | — | `scratchpad` only | no voice is labelled African-accented. The Gemini accent check (`analyze_media`) failed server-side 5×, with "audio too large" and then URL-fetch timeouts, and was refunded |
| voice tests | Arcads TTS ×5 (ElevenLabs): Amara, Thandiwe, Nia, Lerato, Zanele (English-catalogue voices reading the French script) | script.md, French | — | `05_audio/voice/accent_tests/tts_*.wav` + `accent_tests_5voices.mp3` (order as listed, ~14 s each). Assets 836c5948, 71a0027d, 7d49956d, 9d65286d, 2280dd75 (8 cr each) | **for Marty's ear**. None is Congolese by design. Marty proposes his ElevenLabs voice **Monique**, who says "Kobosana te" well |
| voice-id test | Arcads TTS with an ElevenLabs voice id that is NOT in the Arcads list (premade 21m00Tcm4TlvDq8ikWAM) | "Kobosana te." | — | asset 88520ae2 (8 cr) | works: any ElevenLabs voice id can be passed. **Waiting for Monique's voice id** |
| lyric map | local Whisper large-v3-turbo (sherpa-onnx, GitHub release); the song never leaves the container | — | reference mp3 | `05_audio/pitie_lyrics_map.md` | line timings ±1 s; cue A moved to song 0:06→film 0:10 so the lines land on their scenes |
| room bridge | Pillow+ffmpeg (no generation) | room_A + 8.8 s hold, one slow push-in 1.0→1.3× to the table | room_A | `06_edit/v06/room_push.mp4` | KEEP |

Assembly: `06_edit/cut_v06_voiceElisa.mp4` (2:45.5, 1080p, −14.4 LUFS), rebuilt by `06_edit/v06/build_v06.py <voice> <out>` from `timeline.json` + `lyric_caps.json`.
- **Dissolves:** 0:38 (1 s), 0:56 (1.2 s), 1:08 (1 s), 1:18 (1.5 s), **1:32.5 (3 s)**, 1:53.5 and 2:11.5 (1.5 s). The hard cuts from 0:00 to 0:38 are kept, as approved.
- **Music:** "Pitié" cue A runs over film 0:10–1:36 and fades out under "je fais ton avenir". About 1 s of silence follows, then the voice at 1:37. Cue B (song 2:05.5) enters at 2:13 on "Pitié toi mon amour", as the name is written.
- **Voice:** placeholder, the v05 Elisa take (metropolitan French), to be replaced by the accented voice. The swap is a rebuild with a new `voice_paced` file (`v06/pace_voice.py`, one TTS file per line placed at the subtitle times). Spend this round: 48 credits.

## Round v07: Marty asked for "the name written by the video model" plus a final collage ("try both, I pick")
**Rule exception:** CLAUDE.md forbids generated lettering. Marty chose to test an override against the hybrid. The override take is kept only if every letter is right. The end card discloses it.

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| name A (override) | seedance-2.5, 12s 720p, audio | IMAGE REFERENCES + IDENTITY LOCK + MOTION "writes the name 'Mama Nzeba' in neat cursive dark-blue ink … spelled exactly M-a-m-a N-z-e-b-a" + NEGATIVE (no second pen, no other letters) | kf05_f, hands_sheet, K1 (no sleeve ref) | b461988f-1425-4249-bc9a-037845fe48d1 → `04_video/seedance25/name_A_override.mp4` (504) | **CANDIDATE**: final frame reads "Mama Nzeba" (cursive capital N); print face stable; one pen |
| name B (mime, for the hybrid) | same, "pen glides just above the surface … no ink, no letters" | same | same | 51153bc0-8f8d-4b67-9442-dde1248d6953 → `name_B_mime.mp4` (504) | REJECT: wrote pencil gibberish anyway; erase + bake attempt (`name_hybrid.py`) left patches because exposure drifts. The v06 hybrid (`06_edit/v05/shot05_named.mp4`) remains the hybrid option |
| collage base | Pillow over locked table (colour-matched to the shot-05 table): original, restored, K2, K3, sleeve with baked Caveat name | — | locked/*, K2, K3 | `06_edit/collage/base_collage.png` | base |
| collage KF | nano-banana-2 ×2, edit of base: "Change ONLY the realism … pixel-faithful … same handwriting" | — | base | a: 64e5a73b… (turned prints sepia) REJECT · b: 7d6c6217… → faces slightly redrawn → `relock.py` pastes the locked print pixels back (tone-matched, feathered) → `kf_collage_b_locked.png` | **KEEP b (re-locked)** |
| collage | seedance-2.5 ×2, 10s, audio: slow pull-back, window light drifts, nothing moves | IMAGE REFERENCES + IDENTITY LOCK + NEGATIVE | kf_collage_b_locked | A: 40707173-4282-48be-9d3f-1c9dbea70831 → `collage_A.mp4` (420) · B: a0ff2639-2cc6-49c8-8e5c-a0d0e61c538a → `collage_B.mp4` (420) | **KEEP A** (from 1.5 s every print is inside the frame; light sweep); B pulls back into a dark floor. Local fallback: `06_edit/collage/collage_local.mp4` |

Comparison for Marty: `04_video/seedance25/name_compare_A_vs_hybrid.mp4`. Spend this round: 2,352 credits.

## Round v08: voice with an African accent (ElevenLabs MCP)
| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| voice check | ElevenLabs `creative_list_voices` | Marty's voice id vDyhpISvKaEsK9QtEFlO | — | — | it is **"Dolamade"**, labelled en-nigerian (an English voice). The library search for female `fr-african` voices found Fatou (Vza9yt3uSx3RXnRx6YfI), Aquilas, Mar, Ropako |
| testimony | ElevenLabs eleven_v3 ×2 per voice (flow czR8p6OzVq5lDhs8ExEH), script.md with v3 tags [softly] [pause] [hums softly] [small laugh] [long pause] [breathes] | — | Dolamade, Fatou | `05_audio/voice/v08/dolamade_1,2.mp3`, `fatou_1,2.mp3` (~415 EL credits each) | Local Whisper check: **dolamade_1 KEEP** (clean; "tout bas" slightly swallowed) · dolamade_2 REJECT ("Kobosana te" garbled) · **fatou_1 KEEP, chosen for the film** (francophone African accent; every word clear) · fatou_2 REJECT ("Roche-Roe") |
| pacing | `06_edit/v06/pace_take.py` | one continuous take; only the gaps between lines move, to the film's line grid; subtitle times rewritten from the real audio | — | `voice_paced_fatou.wav` / `_dolamade.wav` + `subs_*.json` | the voice is 5.5 dB louder than Elisa, so voice_gain drops from 3.5 to 1.85 |

Assembly: `06_edit/cut_v08_fatou.mp4` (main) and `cut_v08_dolamade.mp4` (the voice Marty asked for), built with `TIMELINE=timeline_v08.json SUBS=subs_<voice>.json build_v06.py voice_paced_<voice>.wav`.

## Round v09: the face comes alive at 1:53–2:12 (Marty: "make her smile and eyes blinking")
**Rule exception:** CLAUDE.md says nobody in the photograph moves their face. Marty overrode it. The end card now says: "Her blink and smile: AI animation of the restored portrait (Kling 3.0 Pro)."

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| face 20 s ×2 | seedance-2.5, 720p, no audio | IMAGE REFERENCES + IDENTITY LOCK + blink, then a closed-lip smile | kf_face (a crop of locked/restored), restored.png | A 78b48db7… / B 8b0c12ed… → `06_edit/face_anim/face_A,B.mp4` (840 each) | REJECT both: they start from the full print (ref 2), push in, and end on a rounder, different face |
| face 10 s ×2 | seedance-2.5, only kf_face as reference | same, still camera | kf_face | 5bf356f5… (still rendering, unused) · 997627ef… → `face10_D.mp4` (420 each) | REJECT: Seedance 2.5 does not use image 1 as the first frame; it re-frames and re-draws her from frame 0 |
| face 10 s ×2 | **kling-3.0-pro**, true start frame = kf_face | "photograph quietly comes to life … blinks slowly once … small, tender closed-lip smile … no talking, no teeth, no camera move" | start frame kf_face | A 080ccdbc-6de9-4123-870b-d0000ccc5050 → `kling_A.mp4` · B d54b59c8-e5f3-43bf-8a31-54fe1aaf468d → `kling_B.mp4` (400 each, 1080p) | **KEEP A** (warmer smile; same woman). B is the subtler alternative, closest to the locked face |
| face beat | local composite `face_anim/face_alive.py` | locked pixels for 9.5 s (push 1.00→1.03), then Kling A at 1.03 | kf_face | `face_anim/face_alive.mp4` (19.5 s) | the join is invisible (Δ 2.96 vs 2.27 between ordinary frames). The blink falls on "Cette photo…" and the smile builds to "On s'en souvient, Mama" |

Spend this round: 3,320 credits.

## Round v10: a deeper 1:19–1:30 ("the scene doesn't look deep enough")
| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| return home | seedance-2.5 ×2, 16s 720p, audio | evening; a slow dolly-in from the doorway; the granddaughter, seen only from behind in a grey long-sleeved top, walks in holding the print, lays it on the table by the window and sits; the camera ends above her shoulder on the photo. Audio: footsteps, chair, distant Kinshasa evening | room plate (room_A ref 0), hands_sheet, K1 | A 2769e5ca-6e48-4db0-9f76-f8e6d7bf2b9d → `04_video/seedance25/return_A.mp4` · B aebbb56c-1ab9-4ac0-8623-0b174c5c48dd → `return_B.mp4` (672 each) | **KEEP B**: pale grey top matches the hands in shot 04; her face is never shown; ends on the photo, which motivates the dissolve to the overhead hands. A REJECT: she wears a wax-print wrap and then a headwrap, so she reads as Mama Nzeba, which breaks continuity |

It replaces `room_push` in `timeline_v10.json`, playing under the lyric *Le soir je vais revenir… je fais ton avenir*. Spend this round: 1,344 credits.

## Round v11: continuity from 1:32 to 2:15 ("changing to the old hands-on-table scene is too rude"); music ducked, not cut
| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| holds the photo | seedance-2.5 ×2, 22s 720p, audio; opening frame = the **last frame of return_B**, so the scene continues | over her shoulder at dusk she lifts the print into the last window light, her thumb traces the edge; the camera drifts in until the print fills the frame. IDENTITY LOCK on the print; her face never shown | return_B last frame, K1, hands_sheet | A 44f32307-aea2-45b9-8a9c-571426a076f0 → `hold_A.mp4` · B d6a1e59b-6ba0-443c-882e-fd42d883f955 → `hold_B.mp4` (924 each) | **KEEP B**: continuous with return_B; ends with the print filling the frame, which leads into the face beat. The print is the worn original, warm in the backlight, and does not move. A is similar but ends less close |
| music | local | "Pitié" is one continuous cue from 0:10 (song 0:06) to the end; it dips from 0.5 to 0.11 (−13 dB) over 1:31–1:35, stays under the voice, and returns over 2:11–2:14 | — | `timeline_v11.json` (cue_a.duck) | replaces the stop at 1:36 and the separate cue B |

The old overhead shot04 (hands on the old table) is no longer used. Timeline: return_B → cut → hold_B → 2.5 s dissolve → face_alive. Spend this round: 1,848 credits.

## Round v12: one continuous dusk world from 0:56 to 2:33; no animated portrait; the collage fits the frame; more emotion in the voice
Marty's notes:
- "same for 0:56–1:17";
- "1:53–2:10: not the animated photo, a frame of the woman touching the photo";
- "2:11–2:32 still the old generation and the Mama Nzeba picture is cut";
- "the audio misses emotions and has blanks".

The Kling blink-and-smile beat has been **removed**, so the portrait never moves again. The end-card line about it is gone.

Prompts from here on follow the Higgsfield "Seedance 2.5" structure:
- SCENE CONTEXT
- ACTIVE REFERENCES (@image1 = opening frame, "100% match")
- FIRST FRAME & BLOCKING
- FORMAT
- OPTICS
- CAMERA
- ACTION BEATS with timings
- PHYSICS
- LIGHTING
- AUDIO
- LOCKS

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| trunk / souvenirs (S0) | seedance-2.5 ×2, 24s 720p, audio | kneels by an old metal trunk at dusk and unties a bundle of photos; looks at two portraits (K2, K3), stops on Mama Nzeba's, turns it to the plain back, presses it to her chest; over her shoulder, face never shown | room plate, hands_sheet, K2, K3, K1 | A 0a898462-2c11-465c-8845-ae136e1bddcd → `trunk_A.mp4` · B a300a915-7c1f-472d-9ac1-028bfabb5514 → `trunk_B.mp4` (1,008 each) | **KEEP A**: the same plaster wall with barred-window dusk shadows and the same grey top as return and hold; she goes through the bundle, turns one print to its plain back, and ends holding Mama Nzeba's portrait close. B REJECT: a different, darker trunk room, and it falls almost to black in the last 2 s |
| touch (S1) | seedance-2.5 ×2, 20s 720p, audio; opening frame = **last frame of hold_B** | lowers the print onto the table; her fingertips touch the face in the photograph and linger; left hand to the heart; the camera drifts down | hold_B_last, K1, hands_sheet | A 55e35dc2-09c2-45af-8809-238dfd56c17c → `touch_A.mp4` · B 63bd8bdc-3ddf-4168-8fe4-4327e0656890 → `touch_B.mp4` (840 each) | **KEEP A**: frame 0 is nearly identical to hold_B's last frame, so the cut is invisible; her fingertips rest on the face in the print for about 12 s. The print keeps its face. Note: the forearm at the end is bare and soft-focus. B REJECT: jumps to a wider window framing, and the print's face is barely readable on the table |
| name (S2) | seedance-2.5 ×2, 14s 720p, audio; opening frame = **last frame of touch_A**; Higgsfield structure | picks up a dark-blue fountain pen and writes "Mama Nzeba" (spelled M-a-m-a N-z-e-b-a) on the white strip below the portrait; the whole print stays in frame | touch_A_last, K1, hands_sheet | A ef6068d8-b8e0-444f-8718-98d19a3ede43 → `name12_A.mp4` · B f56d5b7d-4e30-4e8b-be8e-0792751d0a97 → `name12_B.mp4` (588 each) | Both spell **M-a-m-a N-z-e-b-a** correctly, checked on the last frame. **KEEP B**: large, readable cursive with the whole print in frame, so it reads with the sound off; it joins with a 1 s dissolve because its opening angle differs slightly. A: seamless continuation of touch_A, but the name is tiny on a small label |
| family (S3) | seedance-2.5 ×2, 12s 720p, audio; opening frame = **last frame of name12_B**; Higgsfield structure | sets the pen down and lays two other family portraits on either side of the named one; hands withdraw; the camera cranes back so every print sits fully inside the frame | name12_B_last, K2, K3, K1 (reused as `production/videoassets/0a898462…_reference_image_2/3/4.png`) | A 9d026d67-e209-4286-8b8c-8579a336ddeb → `family12_A.mp4` · B dc62dd40-9d1a-4b3f-9a01-ef09062cdc7a → `family12_B.mp4` (504 each) | **KEEP A**: the last frame shows three prints side by side on the dusk table, all fully in frame, "Mama Nzeba" readable, her portrait uncovered. This replaces the old collage, whose left print was cut by the frame edge. B REJECT: the other prints cover Mama Nzeba's face |

**Audio (v12):**
- Voice: Fatou's emotional take `fatou_emo_1` (eleven_v3 with [softly], [hums softly], [voice breaking]), paced onto the same line grid (`pace_take.py fatou_emo`), gain 1.7.
- Music:
  - "Pitié" now starts at 0:04 on the song's own intro, so film = song + 4 is kept and the old 0–10 s digital silence is gone.
  - Under the voice it sits at 0.24 (it was 0.11).
  - A sidechain compressor keyed by the voice dips it only while she speaks, so it swells back in her pauses.
  - Fix: the sidechain key is padded (`apad`), otherwise the music stopped when the voice file ended (2:13).
- A brown-noise room-tone bed at −34 dB runs under everything, so there is never digital silence.

**Timeline v12** (`06_edit/v06/timeline_v12.json`, 2:51): trunk_A (0:56) → return_B → hold_B (played through its 22.0 s frame) → cut → touch_A → 1 s dissolve → name12_B → cut → family12_A (its last frame is held about 3 s so the full arrangement reads) → end card v12. The face_alive beat and its end-card line are removed.

Spend this round: 2×1,008 + 2×840 + 2×588 + 2×504 = 5,880 credits.

## Round v13: the forgotten box, a family moving house (Marty's restructure, 27 Sept)
Story: `01_bible/story_v13.md`.
- **Place:** Kinshasa, Bandalungwa, chosen by Claude as Marty allowed.
- **Portrait:** stays 1972, in its wax pagne (Marty).
- **Language:** French with Lingala words.
- **Voice:** the testimony is kept, spoken by the mother.

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| characters | nano-banana-2 ×2, 16:9 | character sheet: mother (about 35, pale grey long-sleeved top, wax wrap) and son (about 8, mustard T-shirt) | hands_sheet | a 311944fc… (has text labels) · **b 9030b328-5fdf-4e66-ab55-5f5721b537ee** → `01_bible/family/chars_b.png` | **KEEP b**: no labels; passed as @image1 to every family shot |
| mother's line | ElevenLabs eleven_v3, Fatou `Vza9yt3uSx3RXnRx6YfI` ×2 | « [surprised, softly] Ah… ça ! C'est ta tante qui nous l'avait donnée. [sighs] Tu sais, chez nous… on a si peu de photos. Moi, j'en ai qu'une de moi petite. » | — | **take 1** → `05_audio/voice/v13/mother_tante_1.mp3` (10.9 s) | Whisper confirms the text; used as Seedance reference audio for lip-sync |
| find | seedance-2.5 ×2, 18s, audio | moving day; the boy pulls a rusty tin box from the storeroom: « Maman, regarde ! Il y a une boîte… c'est quoi ? »; opens it, turns the photo over: blank back, « Y a rien d'écrit… » | chars_b, room plate, original | **A 19f529b8…** → `04_video/v13/find_A.mp4` · B 4de98b9f… | **KEEP A**: wide shot, mother packing in the background, blank back clearly shown. Whisper hears one possible stray background phrase at 7–10 s, so that stretch is lowered to 0.12 (`find_A_fix.mp4`). B: tighter, works too |
| aunt | seedance-2.5 ×2, 14s, reference audio = mother_tante_1 | the mother kneels, takes the photo, speaks (lip-synced) | chars_b, room plate, original, audio | A 1ab76a02… · **B 1e04667a…** → `tante_B.mp4` | **KEEP B**: tender, a little sad, matches "on a si peu de photos". A: smiles through the line |
| joy | seedance-2.5 ×2, 12s, audio | she photographs the print; the phone shows the restored face; boy: « Waouh ! On voit son visage ! »; laughter, hug | chars_b, original, restored print | A 91348848… (still rendering, unused) · **B be566eab…** → `joy_B.mp4` | **KEEP B**: the restored face on the phone, the boy's delight, the hug. This is the joy beat |
| album | seedance-2.5 ×2, 16s, audio | the boy mounts the portrait with photo corners in the old family album and writes "Mama Nzeba" | chars_b, K1, K2, K3 | **A ca7de8b4…** → `album_A.mp4` · B fa796286… | **KEEP A**: last frame reads **Mama Nzeba**, checked letter by letter, under her portrait in the album. B REJECT: the name is written upside down and unreadable |
| wall | seedance-2.5 ×2, 14s, audio | new home: they hang the framed portraits, Mama Nzeba in the centre; boy: « Mbote, Mama Nzeba ! » | chars_b, K1, K2, K3 | **A 37b341da…** → `wall_A.mp4` · B dd817b20… (still rendering, unused) | **KEEP A**: three framed portraits fully in frame, mother and son looking up at them. Whisper hears "Bonne… Mama Zéba", so check the "Mbote" by ear |

The mother's other lines are the testimony (`fatou_emo_1`), over return_B, hold_B and touch_A: the dusk scenes whose hands and grey top are hers.

## Round v14: into her memory (0:44–1:02), in colour, with hard cuts (Marty, 27 Sept)
**Rule exception, asked for by Marty:** Mama Nzeba is shown alive, in colour, as the mother's memory. The photograph itself is never altered. The end card says: "Her memories, in colour: imagined by AI (Seedance 2.5) from the family's words; colours are imagined."

The content comes only from the testimony, with nothing added:
- the portrait being taken ("so that we would remember her face");
- on Sundays, the headwrap tied in front of the mirror while she hums;
- the charcoal fire and the soap.

The little girl in yellow is the mother as a child.

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| memory ×2 | seedance-2.5, 15s, 3 shots with hard cuts, colour | 1972 studio, same pose as the portrait, the flash, a smile; then about 25 years later, in front of the mirror with the little girl; then the charcoal brazier, her hand on the little girl's cheek | K1 restored, K1 alternate | A 07e993e7… · **B f6ae6206…** → `04_video/v13/memory_B.mp4` (630 each) | **KEEP B**: the first shot is the portrait's exact pose in colour, so cutting from the black-and-white portrait reads as "the photo becomes memory"; same face across all three shots. A REJECT: its first shot stays black-and-white, which means the photograph itself moves |
| studio (backup) | seedance-2.5, 12s | 1972 studio, two shots | K1 | e26fd667… (still rendering, unused) | — |
| portrait in | local `portrait_in.py` | 3 s on the locked restored portrait (black-and-white, untouched), push 1.00 to 1.05 | locked/restored.png | `06_edit/v06/portrait_in.mp4` | hard cut in, hard cut out |

Timeline v14: joy → cut → portrait_in (44–47) → cut → memory_B (47–62) → cut → return_B. "Pitié" plays continuously; its first line, "Pitié toi mon amour", lands on the brazier shot.

## Round v15: hard cuts only, matched pixel by pixel (Marty: "des bons matching cuts, pixel par pixel… hard cuts pour les changements de point")
All dissolves have been removed; every transition is a hard cut (`timeline_v15.json`, all `xin` 0).

How the matching works:
- **Automatic (`06_edit/v06/matchcut.py`):**
  - For each cut, it compares the last outgoing frame with the first incoming frame, using normalised cross-correlation on edge maps (numpy FFT).
  - It searches a zoom box from 1.0× to 2.0× on either side.
  - When a match is found, one side pushes in (outgoing) or opens zoomed and eases back (incoming) over 1.25 s, so that the two frames coincide at the cut.
  - Results are in `matchcut_report.json`.
- **By hand (`matchcut_manual.py`):** object match cuts on the print of Mama Nzeba.

| cut | plain → matched correlation | kept |
|---|---|---|
| portrait_in → memory | 0.30 → **0.73** | yes: same pose and size, only the colour changes |
| hold → touch | 0.58 → **0.74** | yes |
| touch → album | hand-set box | yes: the print on the table lands where the boy mounts the print in the album |
| album → wall | hand-set box | yes: album push-in on her print; her face lands on the framed portrait's axis |
| tante → joy, return → hold | false match (a 2× zoom onto empty table or cheek) | no: plain hard cuts |
| the others (different places) | below 0.25 | plain hard cuts |
