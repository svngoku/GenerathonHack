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
