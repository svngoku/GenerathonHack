# "Pitié" — where each line is sung, and which scene it lands on (cut v06)

**Method:** local speech recognition only; the song never leaves the container and is never uploaded to Arcads.
- Model: Whisper large-v3-turbo (int8) via `sherpa-onnx`, downloaded from the k2-fsa GitHub releases.
- First pass: 10 s windows every 5 s over the whole track.
- Second pass: 5 s windows every 1.5 s around the lines we use.
- Timings are ±1 s. Lines are matched against the lyrics Marty supplied.
- Whisper also invented a few "lines" in the instrumental parts ("Sous-titrage…", "Sous-titres par…"). These are ignored.
- **Check by ear before delivery.**

## Where the lines fall in the song (mp3, 4:12)
| Song time | Line (as sung) |
|---|---|
| 0:00–0:22 | instrumental intro |
| ~0:23.5 | Pitié toi mon amour, pitié toi mon cœur |
| ~0:29.5 | Je travaille nuit et jour pour ton seul bonheur |
| ~0:34–0:44 | (the two lines again) |
| ~0:47.5 | Si tôt le matin je me réveille |
| ~0:52.5 | Devant ta photo je me recueille |
| ~0:57 | Je sors sans déjeuner |
| ~1:01 | Je pars pour travailler |
| ~1:06 | Qu'il vente, qu'il pleuve ou qu'il neige |
| ~1:16 | Qu'importe le temps, tant que je t'aime |
| ~1:21.5 | Le soir je vais revenir |
| ~1:25.5 | Je fais ton avenir |
| ~1:29–1:35 | instrumental |
| ~1:35 | chorus: Pitié toi mon amour… |
| ~2:06.5 | second verse: Pitié toi mon amour… |
| ~2:10 | Je travaille nuit et jour… |
| ~2:30 | Si tôt le matin… / Devant ta photo… |
| ~3:10–3:45 | Je fais ton avenir → final chorus, "Pitié… Pitié…" |

## Lyric → scene (cut v06)
**Cue A:** song 0:06 is placed at film 0:10, so film time = song time + 4 s.

| Film | Line | Scene | Why it matters |
|---|---|---|---|
| 0:27.5 | *Pitié toi mon amour, pitié toi mon cœur* | the restored face is clear, then the print on the table | the first sung words meet the first clear face |
| 0:33.5 | *Je travaille nuit et jour pour ton seul bonheur* | print on the table, then her hands in the portrait (inside the photo) | work, for her |
| 0:51.5 | *Si tôt le matin je me réveille* | inside the photo | |
| 0:56.5 | *Devant ta photo je me recueille* | the granddaughter's hands before the souvenir photos | the song literally describes the scene |
| 1:10–1:20 | *Qu'il vente, qu'il pleuve… qu'importe le temps, tant que je t'aime* | back of the print, then the room and its window | time and weather pass; the love stays |
| 1:25.5 | *Le soir je vais revenir* | slow push-in on the empty table, evening light | the table waits |
| 1:29.5 | *Je fais ton avenir* | 3 s dissolve into the hands laying her photo on the table | she came back; the future holds the past |
| 1:32–1:36 | (music fades out) | hands on the photo | a breath of silence, then the real voice |

**Cue B:** song 2:05.5 is placed at film 2:13.

| Film | Line | Scene |
|---|---|---|
| ~2:14 | *Pitié toi mon amour…* (second verse) | the name *Mama Nzeba* written on the sleeve |

Captions: three lines (0:27.5, 0:56.5, 1:25.5) are shown as small slanted captions, French plus our English translation, lower-left, with a ♪. The style is different from the testimony subtitles.
