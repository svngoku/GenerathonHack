# Phase 1 log — source + lock set

**Current: Kinshasa 1972 (section at the bottom).** Everything above it is the superseded Brazzaville 1890 run (files moved to `02_source/superseded_brazzaville1890/`).

Format: `item | model | prompt | refs | file | verdict`. Nothing here is in `locked/` until Marty approves.
Research first: `02_source/research.md` (web-search summaries only; full texts blocked by network policy).
Credits before batch: 47,376.

Portrait prompt (prompts.md fictional template, `[DRESS]` filled from research.md; print process changed to albumen per research fact 5):
> Albumen-print studio portrait photograph, Brazzaville, 1890, warm brown monochrome. A woman in her thirties, seated on a wooden chair, three-quarter view, calm direct gaze, wearing a length of patterned trade cloth wrapped as a pagne and a plain simple upper garment. Plain painted studio backdrop. Authentic print wear: faded contrast, fine scratches, a crease across one corner, a slightly torn edge, slight yellowing of the albumen paper. Uninhabited background, untouched by any modern element, text-free. An original fictional person, not a real individual.

| item | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| P1 portrait | seedream_5_pro | portrait prompt | — | `02_source/portrait_v2/seedream_1.jpg` (289a8fb2-7c78-4c63-bc7a-6ec933520a72, 2048x1152) | GOOD — closest to research; light damage only |
| P2 portrait | seedream_5_pro | portrait prompt | — | `02_source/portrait_v2/seedream_2.jpg` (80ab873f-4198-4edc-8add-208b9af110a4) | RECOMMENDED — torn corner + edge tear to restore, large readable face |
| P3 portrait | nano-banana-2 | portrait prompt | — | `02_source/portrait_v2/nano_1.png` (6e8818e5-e6f3-40b0-a7d9-7290bd157585) | OK — heaviest wear; face small; added window + reed mat |
| P4 portrait | nano-banana-2 | portrait prompt | — | `02_source/portrait_v2/nano_2.png` (d2f333a8-e437-466c-9c63-81e5d56a8a96) | REJECT — portrait card on grey canvas; invented headwrap + jewellery |
| hands 1 | nano-banana-2 | prompts.md lock-set template; SKIN/RING/SLEEVE = dark brown skin, no ring, grey cotton cuffs (placeholder choice) | palette | `02_source/lockset/hands_1.png` (629c3ff6-ebf3-4799-855f-11db88507c0d) | REJECT — ambiguous left/right in panel 1; print shows another person |
| hands 2 | nano-banana-2 | same | palette | `02_source/lockset/hands_2.png` (a2b657ca-5dc5-4643-b906-70cff526d9f6) | RECOMMENDED — consistent, 5 fingers each, same sleeves |
| room 1 | nano-banana-2 | room plate, window LEFT, warm late light | palette | `02_source/lockset/room_1.png` (13220472-e809-4055-9b1b-6d48d2708967) | OK — sash window over brick reads European |
| room 2 | nano-banana-2 | same | palette | `02_source/lockset/room_2.png` (737f4ad2-7952-4cc7-89ef-9594d7201653) | RECOMMENDED — simplest; radiator reads European |
| table 1 | nano-banana-2 | top-down table close, light band from LEFT | palette | `02_source/lockset/table_1.png` (e722d263-5d8b-41ca-b90f-10b8002cd059) | OK — cooler grey wood |
| table 2 | nano-banana-2 | same | palette | `02_source/lockset/table_2.png` (ed07bda4-f2f1-45ab-ac3c-5d1b6af07cf0) | RECOMMENDED — warmer, on palette |
| sleeve 1 | nano-banana-2 | blank cream sleeve + pen, top-down | palette | `02_source/lockset/sleeve_1.png` (3675035b-8353-4360-b3c8-1edfb205432a) | OK — pen on left; reads as a card |
| sleeve 2 | nano-banana-2 | same | palette | `02_source/lockset/sleeve_2.png` (c5b82333-4fd7-4b89-bc9e-117853c201ff) | RECOMMENDED — pen on right (right-handed writer); reads as a card |

Palette ref: `01_bible/palette.png` (#9AA3A8 → #D9A35F, paper #F4EAD5), uploaded once; later calls reuse `production/videoassets/629c3ff6-ebf3-4799-855f-11db88507c0d_reference_image_0.png` (temp uploads are single-use).

Open `[TODO: ask Marty]`: hair; how the pagne is worn / any top; studio vs improvised backdrop; brass neck ring; cloth pattern (all four portraits show modern-looking wax-print patterns, unverified for 1890); where the young person's room is (both plates read European); skin tone / ring / sleeve of the young hands.

Superseded: `02_source/portrait_variant_A/B.png`, `03_restore/stage_*`, `locked/original.png`, `locked/restored.png` and the shot-03 work came from the pre-research run. They stay until Marty picks the new portrait, then `locked/` is replaced and phase 3 reruns.


## Kinshasa 1972 redo (Marty: "confirmed, redo for Kinshasa 1972, room in Kinshasa")
Research: `02_source/research.md` (authenticité from Jan 1972; liputa in wax print; wigs/straightening targeted, plaits/braids/headwraps kept; headwrap from same cloth [low-medium]; Studio 3Z opened 1971 in Kitambo). Hands, table, sleeve and palette stay locked; the room is redone.

Portrait prompt (prompts.md fictional template; [DRESS] from research.md; "clearly visible" wear added because the animatic showed the damage didn't read):
> Black-and-white studio portrait photograph, Kinshasa, 1972, in the tradition of Kinshasa studio portraiture. A woman in her thirties, seated on a wooden chair, three-quarter view, calm direct gaze, wearing a wax-print liputa wrapped from waist to ankle, a fitted blouse, and a headwrap cut from the same cloth. Plain painted studio backdrop. Clearly visible authentic print wear: faded contrast, dust specks, fine scratches, a crease across one corner, a slightly torn edge. Silver-gelatin grain, uninhabited background, untouched by any modern element, text-free. An original fictional person, not a real individual.

| item | model | prompt | refs | file | verdict |
|---|---|---|---|---|---|
| K1 portrait | seedream_5_pro | portrait prompt | — | `02_source/portrait_k72/K1_seedream.jpg` (3334cbcf-0ed1-4598-825a-b40642aa02d1, 2048x1152) | RECOMMENDED — follows research, no added jewellery, visible specks/scratches, torn right edge |
| K2 portrait | seedream_5_pro | same | — | `portrait_k72/K2_seedream.jpg` (4577a006-5cdf-4c82-ba5e-dc0b3f743ed0) | GOOD — more frontal, slightly larger face; lighter damage |
| K3 portrait | nano-banana-2 | same | — | `portrait_k72/K3_nano.png` (373fcc09-8c46-4811-8a56-22b48f4b4b43) | GOOD — full matching-cloth set, heaviest wear; adds earrings (unresearched) |
| K4 portrait | nano-banana-2 | same | — | `portrait_k72/K4_nano.png` (a58c3efa-d715-4ad6-b474-167991931601) | REJECT — portrait card on white canvas; invented necklace + bracelets |
| room K1 | nano-banana-2 | room plate: "a modest family home in Kinshasa today", window LEFT, warm late light | palette | `lockset_k72/room_k1.png` (5cc2e44e-d42f-4212-a31e-71c65087aa74) | OK — plausible, more generic (rattan chair, sliding window) |
| room K2 | nano-banana-2 | same | palette | `lockset_k72/room_k2.png` (6d5118d5-2b4b-45dd-8710-d32bf0511289) | RECOMMENDED — barred window, worn plaster, tiled floor; less European. Unsourced details `[TODO: ask Marty]` |
