# Score — Jua (Arcads `/v1/music/generate`: suno_v6 to audition, elevenlabs for exact-length finals)

## The musical idea
A **four-note motif that never finishes** while she is unknown. It stops completely when the real voice speaks. When the name is written, the motif **returns and finally lands on its last note**. The melody finds its home when she gets her name back.

Keep A and B the same instrument, **key and tempo** so they sound like one piece: **D minor → D major, 60 BPM**.

## Cue sheet (synced to shotlist.csv)
| Time | Shot | Music | Story job |
|---|---|---|---|
| 0–10s | 01 unknown image | **none** — room tone, paper | absence; silence makes the viewer lean in |
| 10–38s | 02–03 restoration + movement | **Cue A "Searching"** (28s) — motif enters on the first stage reveal, one soft note per stage | curiosity; the face appears, the tune can't resolve |
| 38–58s | 04 the voice | **total silence** (music hard-cuts on the first breath) | the only thing that matters is the person speaking |
| 58–75s | 05–06 handoff + side by side | **Cue B "Belonging"** (17s) — enters when the pen touches the sleeve; resolves on the held last note under the side-by-side | belonging; the motif completes |

## Instrument: rooted in the photo's place (pick one, never mix regions)
| Place | Instrument |
|---|---|
| Kinshasa / Congo basin | likembe (thumb piano) or clean solo rumba guitar |
| Mali, Senegal, Gambia, Guinea | kora |
| Zimbabwe | mbira |
| Ethiopia | krar or masenqo |
| Ghana | seperewa or gyil |
| Unsure | ask Marty — don't default to a "generic African" sound |

## Prompts
**Audition (suno_v6, `instrumentalOnly: true`, nbGenerations 1 = 2 tracks, duration 30):**
```
Solo [INSTRUMENT] from [PLACE], intimate close-mic recording, D minor, 60 BPM. A simple four-note motif that repeats but never resolves, long pauses between phrases, like someone trying to remember a face. Sparse, hesitant, warm room ambience. No drums, no bass, no vocals, no build, no cinematic swell.
```
```
Solo [INSTRUMENT] from [PLACE], intimate close-mic, D major, 60 BPM. The same simple four-note motif, now completed: it finally lands on its home note. A second, softer line of the same instrument joins. Gentle, grateful, unhurried; ends on one long held note that rings out. No drums, no bass, no vocals, no swell.
```
**Finals (elevenlabs, `instrumentalOnly: true`, exact `duration`):** reuse the chosen audition's wording → Cue A `duration: 28`, Cue B `duration: 17`. Save as `05_audio/music/cue_a_v01.mp3`, `cue_b_v01.mp3`.

**Optional (only if it serves the story):** a wordless hum over cue B — suno_v6, `instrumentalOnly: false`, lyrics `[Hummed melody, no words]`. Never generate lyrics in a real language: a model would get it wrong and it would sound invented.

## Checks before locking
- [ ] A and B sound like the same player on the same instrument (play B straight after A)
- [ ] Cue A doesn't swell into the voice; the cut to silence at 38s feels like a held breath
- [ ] Cue B ends at 75s on the held note (fade ≤ 1s)
- [ ] Mix: voice clear with nothing under it; music around -20 LUFS short-term under room tone; export master at -14 LUFS integrated (YouTube)
- [ ] Log both cues in `05_audio/licenses.md`: model, prompt, date, "generated via Arcads — [plan] terms"
