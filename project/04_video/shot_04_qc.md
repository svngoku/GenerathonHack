# Shot 04 — generation log & continuity QC

Emotion: **COMFORT** (brief default; no official re-skin received). Status: **review** — awaiting director sign-off before shots 01–03, 05, 06.

## Assets (Arcads asset IDs — reuse as `production/videoassets/<id>.png` in referenceImages)
| File | Model | Arcads asset | QC |
|---|---|---|---|
| 02_refs/character/amara_sheet.png | nano-banana-2 | 85978de4-a4ec-4ba7-88bf-57fcb47c2d23 | PASS (v2). v1 rejected: came out as an illustration, not photoreal. Note: reads slightly older than 34. |
| 02_refs/product/mug_master.png | nano-banana-2 | a6cf6393-513d-4916-883e-7e7e9ccdd0af | PASS — handle right, thumb dimple, raw clay ring, no text |
| 02_refs/locations/kitchen_wide.png | nano-banana-2 | 3e2fe48c-b04f-4cd5-9430-478955fcb571 | PASS — window left, curtain, counter L→R, kettle, pothos, blue-grey |
| 02_refs/locations/kitchen_close.png | nano-banana-2 (ref: wide) | 02b0c755-a079-473f-9758-cf21d76852e3 | PASS — same counter/window/kettle/pothos |
| 03_stills/shot_04_start.png | nano-banana-2 (refs: sheet, mug, close) | aa64a64b-1430-4671-9a7f-d3f11ef99cdf | PASS (v2). v1 rejected: handle/dimple hidden, left hand had no arm/sleeve. |
| 03_stills/shot_04_end.png | nano-banana-2 (edit of start, prompt F) | e7a11daf-ee20-4354-ab61-1e053090d5ac | PASS — amber ray upper-left→lower-right, steam gold, geometry locked. Steam slightly flame-like. |
| 04_video/shot_04_v01.mp4 | Seedance 1.5, start+end frame, 6s, 1080x1920 | 2b691acd-6a91-4d7e-9ec7-3f584fa91751 | PASS — **selected**. Mug stays planted, gradual warm-up. Watch 4.3–4.8s: hands briefly open off the mug. |
| 04_video/shot_04_v02.mp4 | Seedance 1.5, start+end frame, 6s, 1080x1920 | 02deeb84-fa45-4e8a-ab73-aa9959799569 | PASS w/ note — mug lifts off counter 2–3.5s; steam white and tall at 4.5s. |

Both videos carry a generated audio track — mute in edit.

## Continuity checklist (shot 04)
- [x] Window on the left; sun falls upper-left → lower-right (end frame + both takes)
- [x] Mug handle faces right, thumb dimple visible (start/end: right thumb on dimple)
- [x] Cardigan on, both sleeves visible (scrubs not in frame)
- [x] Two hands, five fingers each — checked frames 0/36/60/72/84/108/125/144 of both takes
- [x] No generated text or logos

## Edit suggestions
- v01: if the 4.3–4.8s hand release reads wrong, trim to 0–4.2s and cross-dissolve into the end still, or speed-ramp.
- Fallback (shotlist): crossfade start→end + light leak.

## Workflow note
The Arcads MCP server cannot read local paths in this container. Pass prior outputs by S3 key (`production/videoassets/<asset-id>.png`) instead.
