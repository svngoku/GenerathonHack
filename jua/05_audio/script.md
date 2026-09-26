# Testimony script — FICTIONAL (draft for Marty's approval)

Marty (2026-09-26): "Whatever the name, we are trying to share deep emotion … follow the Pitié vibe … refer to any African woman." → The name and memories below are **invented for the fictional proof of concept**, written by the agent, approved by Marty. The end card already says: *"Fictional proof of concept. No real person is depicted."* Nothing here refers to a real person.

## Who speaks
A granddaughter, today, in the Kinshasa room, holding the print (the young hands in shots 04–05 are hers). Spoken, not read: pauses, breath, a small laugh. Recorded in the room (not close-mic). **A consenting person records it** (preferred); disclosed synthetic voice only as a fallback (model_map §3).

## Her name (fictional)
**Mama Nzeba** — a name widely used in Congo (DRC), plain and warm. `[Marty: keep / change]`

## Script (~40 s, French with a few Lingala words; subtitles EN)
Lingala words marked `[CHECK]` — to be checked with a Lingala speaker; never trust these from a model.

> *(breath)*
> C'est Mama Nzeba. Ma grand-mère.
> *(pause)*
> Le dimanche, elle attachait son foulard devant le miroir… et elle chantait Rochereau, tout bas. *Pitié…* *(she hums two notes, stops)*
> Elle sentait le savon de Marseille et le charbon de bois.
> *(small laugh)* Elle disait toujours : « **Kobosana te** » — n'oublie pas. `[CHECK]`
> *(long pause)*
> Cette photo… elle l'a faite pour qu'on se souvienne de son visage.
> *(breath)* On s'en souvient, Mama.

**EN subtitles**
> This is Mama Nzeba. My grandmother.
> On Sundays she tied her headwrap in front of the mirror… and sang Rochereau, very softly. "Pitié…"
> She smelled of Marseille soap and charcoal.
> She always said: "Kobosana te" — don't forget.
> This photo… she had it taken so we would remember her face.
> We remember, Mama.

## Why these details (consistency with the film)
- **The headwrap** is the one she wears in the locked portrait (K1) — the memory matches the picture.
- **Rochereau / "Pitié"** ties her memory to the film's music: the song is *hers*. When "Pitié" returns under the name, it comes from her memory (brief § limbic narration).
- **Soap and charcoal**: a smell, not a fact — sensory, ordinary, no biography.
- **"Kobosana te"** (don't forget) is the film's thesis in her own words — and the reason the name is written on the sleeve.
- No dates, jobs, places beyond Kinshasa, or life events are invented.

## Voice as built (cut v08)
- **Disclosed synthetic voice:** ElevenLabs eleven_v3. The end card says "Voice: AI-generated".
- **Main voice:** Fatou (ElevenLabs library, `fr-african`, "a French-speaking African woman").
- **Alternative:** Dolamade, the voice Marty asked for. It is an English voice with a Nigerian accent, so its French sounds anglophone West African, not Kinshasa.
- **Still open:** no Congolese (Lingala-accented) voice exists in the library. A consenting Kinshasa speaker remains the best option. "Kobosana te" still needs checking by a Lingala speaker `[CHECK]`.

## Voice as built (cut v12)
The voice is Fatou's **emotional** take, `05_audio/voice/v08/fatou_emo_1.mp3` (ElevenLabs eleven_v3).
- The same words, with performance tags: [softly], [hums softly] on "Pitié", and [voice breaking] on "N'oublie pas".
- It is paced onto the same line grid with `06_edit/v06/pace_take.py fatou_emo`; subtitles are in `subs_fatou_emo.json`.
- The second take, `fatou_emo_2`, is not used.
- Music stays under the voice at 0.24, with a sidechain dip only while she speaks, so the pauses breathe with "Pitié" instead of falling silent.
