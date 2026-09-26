# Jua context — what the film is really about

Production runs 100% in **Arcads**. This file keeps the knowledge of **Jua** (umojua.com) so every generation is prompted in Jua's spirit and the story stays true to what Jua is.

## What Jua is (from umojua.com)
- Tagline: **"Make, restore, and keep the story together."**
- Principle: **"Every result explains itself"** — each output keeps its model, size and processing details.
- Audience: African artists, heritage preservationists, creatives working with African histories and futures.
- Tools:
  - **Studio** — multi-model generation (Nano Banana 2, GPT Image 2, Krea 2 Turbo, Flux 2 Pro, Grok) with one prompt composer and a creative history that keeps "the brief, source images, and finished outputs together".
  - **Upscale** — archive photo restoration with before/after comparison, target-resolution upscaling, metadata preserved; output can go on to recreation, video, or download.
  - **Gallery** — curated work incl. an original FLUX LoRA collection (fashion, architecture, everyday life, afrofuturism).

## Jua → Arcads mapping (how we reproduce it)
| Jua step | Arcads equivalent | Rule borrowed from Jua |
|---|---|---|
| Upscale: restore archive photo | image edit with Nano Banana Edit / GPT Image 2, in **stages** | before/after always visible |
| Upscale: target resolution | Arcads upscale tool (if exposed) or highest-res edit output | keep original framing, no crop |
| Metadata preserved | we log model + prompt + stage per output in `03_restore/log.md` and show it on screen in shot 02 | **every result explains itself** |
| Output → video | image-to-video (Kling / Veo / Seedance) from `locked/restored.png` | motion only where it doesn't invent |
| Studio creative history | this repo: brief → sources → outputs in one place | keep the story together |

## How Jua shapes the story
1. **Shot 02 = Jua's before/after.** Stages appear with a small caption in the corner: `stage 2 · crack repair · Nano Banana Edit`. That is "every result explains itself" made visible — and it's honest about the AI.
2. **The AI is a restorer, not an author.** Jua restores; people remember. The film's climax is a human voice, which matches "keep the story together".
3. **Say it plainly in the explainer:** "This is the pipeline I'm building in Jua; for the hackathon I ran it with the same models inside Arcads."
4. **Never** let a generated detail pass as archival fact — Jua's value is trust in the archive.
