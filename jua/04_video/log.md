# Video log — every result explains itself

Format: `shot | model | prompt | refs | file | verdict`. Rule for 03: reject any take where the face moves or changes.
Shot 03 prompt (P03) = prompts.md "Shot 03" block. Variants noted per row. Rejected MP4s are not in git (138 MB); re-download by Arcads asset ID.

| shot | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| 03 | kling-3.0 (Arcads `generate_video`), 6s, 16:9 | P03 verbatim | start = `locked/restored.png` | asset 0550a51e-1076-4ef6-88ee-6208b6d18411 (`rejected/shot_03_kling_takeA.mp4`, not in git) | REJECT — by 6s face longer, cheeks narrower, eyes reshaped; no table rendered |
| 03 | kling-3.0, 6s, 16:9 | P03 verbatim | start = `locked/restored.png` | asset 46485905-f0ec-429c-864f-7c57715219f4 (`rejected/shot_03_kling_takeB.mp4`) | REJECT — face narrower, nose and eyes changed, new skin creases |
| 03 | seedance-1.5, 6s, 1080p | P03 minus "lies on a wooden table" + "ending exactly on the end frame; face stays pixel-identical" | start = `restored.png`, end = `03_restore/shot03_endframe_crop.png` (digital crop, no generation) | asset 79c2f4ff-6ed0-47a6-9ebd-6dd39879712b (`rejected/shot_03_seedance_takeA.mp4`) | REJECT — nasolabial lines added from frame 0, looks older |
| 03 | seedance-1.5, 6s, 1080p | same as above | same as above | asset 87ee77c1-62fd-48ae-9f81-03c47434f594 (`rejected/shot_03_seedance_takeB.mp4`) | REJECT — same added lines, older |
| 03 | veo31, 1080p (8s, fixed) | P03 minus table sentence + "face stays identical"; start+end frame refused (INVALID_END_FRAME), so start only | start = `restored.png` | asset 9d0dff2f-dc5c-4a95-a01b-ad4c13f737e9 (`rejected/shot_03_veo31_takeA.mp4`) | REJECT — invents film-strip sprocket borders (~1–2s); face drifts in close-up (nose, forehead) |
| 03 | veo31, 1080p (8s) | same as above | same as above | asset fcf2d339-7a66-4955-a6fb-77a36d860bbc (`rejected/shot_03_veo31_takeB.mp4`) | REJECT — colourises the print (warm brown, blue cast on face); face changes in close-up |
| 03 | none — shotlist fallback "digital push + light-leak", rendered locally (Pillow + ffmpeg), 6s, 1920x1080, 24 fps | ease-in push from full frame to crop (487,0)–(2413,1075); honey #D9A35F light band left→right | `locked/restored.png` only | `04_video/shot_03_digital_push.mp4` | CANDIDATE — face pixel-identical by construction; no table (no locked table plate yet) |

Evidence: `04_video/shot_03_face_check.jpg` (last-frame face of every take vs `restored.png`), `rejected/kling_face_drift.jpg`.
Credits spent on shot 03: Kling 2×272, Seedance 2×120, Veo 2×800 = 2,384.
