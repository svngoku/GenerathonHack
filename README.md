# Jua — More Than a Photograph

**Generathon #2 · Three Minutes to Move — Short Film · Challenge: "Limbic Narration, Not Just a Voice-Over"**
Marty Niongolo · 75s · 16:9 · made entirely in Arcads

> **AI can restore a face. Only people can give back a name.**

## The film
An old family photograph from [PLACE, YEAR]: cracked, faded, the woman in it unknown. We watch it being restored, stage by stage, until her face is clear again, and then the film stops showing off. The music cuts. In the silence, someone who knew her says her name and remembers one small, sensory thing about her. A younger hand writes that name on the photo sleeve, and the melody that could never finish finally resolves. The film ends on the original and the restoration side by side: the AI version never replaces the real one.

**Emotional arc (our choice): absence → curiosity → belonging.**
**End line:** *"We can restore the image. We remember the person together."*

## Why it answers the challenge: limbic narration
No narrator, no explaining voice-over. The story reaches the emotional brain through the senses:
- **Sound:** paper and room tone → a four-note motif that never resolves → total silence on a breath → the motif resolves under the pen.
- **Touch:** a thumb on the print's edge, a pen that hesitates before writing.
- **Memory:** the only words are the witness's, spoken inside the room, with a sensory detail (a smell, a song, a fabric), not facts read from a script.

## Why it matters: Jua
Jua (umojua.com) is a workspace to *make, restore, and keep the story together* for African heritage images, where *every result explains itself*. The film is Jua's thesis: restoration technology is powerful, and it must stay honest. It repairs, it doesn't invent. Each restoration stage appears on screen with the model that made it.

## How it's made (AI technical mastery)
| Layer | Arcads models |
|---|---|
| Consistency | one locked reference set (print, hands, room, sleeve) + an identity-lock clause in every prompt |
| Restoration in 4 stages | gpt-image-2.5 (sunburst) A/B nano-banana-2, each stage edits the previous one, face drift rejected |
| Frozen-face motion | veo31 from the restored still: camera and light move, she never does |
| Hands, room, native sound | seedance-2.5 with up to 30 image refs + the real testimony as an audio reference |
| Score | Suno v6 auditions → ElevenLabs cues at exact length (28s + 17s), one instrument from the photo's place |
| Animatic & fixes | grok-video previz, omni-flash surgical edits |

## Honesty rules
Nothing about her is invented: name, place and memory come from a real person (or the film is labelled a fictional proof of concept). Nobody in the photo moves their face or speaks. No generated lettering. Colour, if used, is disclosed. The original is always shown.

## Deliverables
1. Main film, 75s (limit 3 min) → YouTube, unlisted
2. Face cam explainer, ≤ 60s, covering inspiration, what, how, challenges, proud of, learned, next, tools
3. Thumbnail: original vs restored, a pen over the blank sleeve

Soft deadline **Sun 13:30**, hard **14:00** · Live screening Sun 17:30 + public vote.

## Repo map
`CLAUDE.md` agent rules · `jua/00_brief/` official rules, Jua context, brief · `jua/01_bible/` shot list, visual bible, prompts, model map · `jua/05_audio/score.md` music · `jua/AGENT_PROMPTS.md` phase-by-phase prompts · `jua/delivery/` form, explainer, thumbnail
