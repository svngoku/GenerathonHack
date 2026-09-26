# Filled prompts — First Light (generate in this order)

Arcads MCP routing: stills → an image model with references (Nano Banana), motion → image-to-video with start/end frames (Seedance / Kling / Veo). Upload refs first; upload paths expire in ~10 min.

## Arcads skills → kit stages (plugin `arcads@arcads`, project scope)

| Kit stage | Skill | Use it for | Needs |
|---|---|---|---|
| §3A Concept / references | `/arcads:spy-competitor-ads` | pull winning mug / ceramics / cozy-lifestyle ads from Meta Ad Library as mood refs → `02_refs/` | browser MCP (Chrome/Playwright) |
| §4 Shot 01 hook | `/arcads:clone-hook` | analyze a proven 0–4s opening, re-shoot its structure with Amara + mug (Seedance 2.0, 2 variants) | source video (or chains spy) + mug master |
| Social cutdowns / poster | `/arcads:clone-static-ad` | turn `locked/hero_frame.png` into a static ad layout (3 variants) | reference static ad + mug master |
| §3C–G every still & shot | `arcads:media-router` (auto) | any "generate/edit/upscale/caption/voice-over" → picks the live Arcads tool, uploads, polls, downloads | Arcads MCP authenticated |

Rights check (kit §6): competitor ads are structure references only — never ship their footage, faces, logos or music.

## Seedance guards (prepend to every motion prompt)
```
CONSTRAINTS: Every shot is live motion video — people and steam move naturally; no frozen frames. Render ONLY what is explicitly described below. Do NOT add any text, captions, logos, watermarks, props or graphics not described.
```
Always roll **2 variants** in parallel; keep the better take as `_v01`, the other as `_v02`.

## 1. Character sheet → `02_refs/character/amara_sheet.png`
```
CHARACTER REFERENCE SHEET: One consistent original character: Amara, 34-year-old Black woman, short natural coils, tired eyes, small gold stud earrings, faded teal nurse scrubs under an oversized grey knit cardigan, white socks. Neutral plain background. Three panels: waist-up front, full-body front, full-body back. Same face, hairstyle, proportions and outfit in every panel. Even soft light, natural skin texture. No labels or extra people.
```

## 2. Product master → `02_refs/product/mug_master.png`
```
PRODUCT MASTER: One physical hand-thrown stoneware mug, ~9cm tall, slightly irregular cylinder, matte sand-beige glaze, unglazed raw clay ring at the base, single loop handle with a shallow thumb dimple, handle facing right. Isolated three-quarter view on a neutral backdrop; clean product photography. Keep proportions mechanically plausible. No text, logos, extra parts, or duplicate product.
```

## 3. Location plate → `02_refs/locations/kitchen_wide.png`, `kitchen_close.png`
```
LOCATION PLATE: Empty small studio-apartment kitchen corner, 5th floor, window on the LEFT facing east with a thin linen curtain, wooden counter running left to right, electric kettle, one pothos plant. Pre-dawn: only cold blue-grey ambient light (#2B3A4A). Medium-wide frame, 9:16. No people, no product, no text. Room for a foreground subject. Then a second matching close angle on the counter, same layout.
```

## 4. Shot 04 keyframes (do this before anything else)
```
Use reference 1 ONLY for character identity; reference 2 ONLY for product design; reference 3 ONLY for environment. Close-up, 9:16: Amara's two hands wrapped around the mug on the wooden counter, cardigan sleeves visible. START: cold blue-grey light, faint steam barely visible, fingers tense. END: a single warm amber sun ray (#E8A45C) through the curtain gap from upper-left hits the steam, which glows gold; fingers relaxed. Shallow depth of field. Preserve identities and geometry; exactly two hands, five fingers each; no text or extra props.
```

## 5. Shot 04 motion
```
START FRAME: shot_04_start.png. END FRAME: shot_04_end.png. Duration: 6s. One continuous static shot. Subject performs ONE action: slowly tightens both hands around the mug and exhales. First half: cold blue room, faint steam. At 3s a sun ray enters from the upper-left. Last frame: steam glows gold, hands relaxed. Keep hands, mug silhouette, background and perspective stable. No cuts, morphing, new objects, text or camera movement.
```

## 6. Shot 05 reaction
```
Use reference 1 ONLY for identity, reference 3 ONLY for environment. Medium close-up, 9:16, slow push-in: Amara holding the mug near her chest, eyes closing, long exhale, shoulders dropping, faint smile. Warm amber sunlight from the left now fills the room (#F2C98A). Natural skin texture, shallow DOF. Same face, cardigan and earrings as reference. No text.
```

## 7. Hero end frame → `locked/hero_frame.png`
```
The ceramic mug in sharp focus, lower third, matching the product master exactly, steam glowing in warm amber morning light. Behind it, softly out of focus, Amara curled on the window seat, eyes closed, faint smile. Palette cream and amber (#F2C98A, #FFF1DC). Clean negative space in the upper third for a tagline added in edit. No generated lettering or logos.
```

Shots 01–03: reuse prompt D of the kit with the shot list framing. Corrections and review: kit prompts F and H verbatim.
