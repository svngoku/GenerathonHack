# Phase 1 log — source + lock set (full redo, new phase order)

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
