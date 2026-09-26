# Agent prompts — Jua, phase by phase

`CLAUDE.md` holds the rules, so these prompts are short. Paste one phase at a time; each ends at a checkpoint where you approve or redirect. Replace every `[…]`.

---

## 0 · Kickoff (paste once per new session)
```
git pull. Read CLAUDE.md and every file it lists, in order (official_rules.md overrides everything). Then reply with:
1. the story in two sentences,
2. the mode you'll run (DOCUMENTARY / FICTIONAL) and what's missing for it,
3. the Arcads tools you discovered and the credits balance,
4. the phase plan with an estimated credit cost per phase.
Don't generate anything yet.

Mode: [DOCUMENTARY — original scan is jua/02_source/original.png; owner and witness gave permission]
   or [FICTIONAL — place: ___, year: ___]
Emotion (we choose it): BELONGING  [or another → apply the matching row in brief.md first]
```

## 1 · Source + lock set
```
Phase 1. Create the Arcads project "Jua".
[DOCUMENTARY] Copy jua/02_source/original.png → jua/locked/original.png untouched.
[FICTIONAL] Research period-accurate dress and studio-portrait conventions for [PLACE, YEAR] and write 5 bullet facts with sources in jua/02_source/research.md. Then generate the portrait with prompts.md (seedream_5_pro vs nano-banana-2, 2 each) → jua/02_source/.
Then build the lock set from model_map.md §0 with nano-banana-2: hands_sheet, room_plate, table_close, sleeve (2 variants each).
CHECKPOINT: show me everything as a grid with a one-line verdict each. I'll pick what goes into locked/.
```

## 2 · Animatic (the story test)
```
Phase 2. Make a grok-video 480p animatic of all 6 shots following shotlist.csv timings, using the approved lock set as references. Assemble it in order into jua/06_edit/animatic_v01.mp4 (ffmpeg concat) with no music.
CHECKPOINT: tell me what a muted stranger would understand at 10s, 38s, 58s and 75s. Flag any beat that doesn't read.
```

## 3 · Restoration (Jua's before/after)
```
Phase 3. Run the 4-stage restoration from prompts.md on locked/original.png. Each stage: gpt-image-2-5-sunburst AND nano-banana-2, both from the previous approved stage. Log every call in jua/03_restore/log.md.
After each stage compare the face with the previous stage (eyes, nose, mouth, jaw, hairline) and keep the one with less drift. Skip stage 4 (colour) unless I say "colour".
CHECKPOINT: show original → stage 1 → 2 → 3 side by side with the model for each. On my "approved", copy stage 3 → locked/restored.png.
```

## 4 · Hero shots (one at a time)
```
Phase 4 — shot [03 / 04 / 05 / 01]. Follow model_map.md §2 for the model, refs and constraints, and prompts.md for the wording, with the Seedance guards. 2 variants in parallel.
Shot 03: veo31, startFrame = locked/restored.png. Reject any take where the face moves.
Shot 04: seedance-2.5, refs = hands_sheet + restored + room_plate + jua/05_audio/testimony.[m4a] (audio ref), audioEnabled, "natural room sound only, no music, no voices".
Shot 05: seedance-2.5, start = sleeve blank, end = sleeve with the name area empty (I'll composite real handwriting).
Shot 01: seedance-2.5, refs = original + table_close, macro pan, audioEnabled.
Log in jua/04_video/log.md, update shotlist.csv status.
CHECKPOINT: both takes + one-line verdict + which one you'd keep.
```
Fix a nearly-good take:
```
Use omni-flash on jua/04_video/shot_[NN]_v[XX].mp4: [exact problem, e.g. "the print edge warps at 4s — keep everything else identical"]. Save as _v[XX]b.
```

## 5 · Testimony + subtitles
```
Phase 5. [DOCUMENTARY] Transcribe jua/05_audio/testimony.[m4a]. Write jua/05_audio/subtitles_en.srt and _fr.srt timed to 38–58s. Mark every name, place and non-English word as [CHECK] — don't guess spellings. Use Arcads captions if the MCP exposes them; otherwise produce the SRT.
[FICTIONAL] Draft jua/05_audio/script.md: 3–4 plain, spoken-sounding sentences — her name, the place, ONE sensory detail (a smell, a song she hummed, the fabric she wore, a sound from her kitchen). No grand claims, no narration. A consenting person will say it in the room — recorded with room acoustics and breath, not close-mic studio.
[BOTH] Remind me: record the witness in the room, keep the breaths and pauses, and ask whether she used to hum or sing something — record that too (score.md cue B).
CHECKPOINT: show me the text.
```

## 6 · Score
```
Phase 6. Follow jua/05_audio/score.md. Primary: edit Tabu Ley "Pitié" locally from jua/05_audio/reference/ (cue A 28s, silence, cue B 17s → music_edit.md). Backup: original score in the same spirit, 1970s Kinshasa rumba guitar.
For the backup: audition cue A and cue B with suno_v6 (1 call each = 2 tracks), and B straight after A must sound like the same player.
CHECKPOINT: give me the "Pitié" excerpt timestamps + the 4 backup auditions with a one-line description each. After I pick, render the backup finals with elevenlabs at exactly 28s and 17s → 05_audio/music/, and log everything in licenses.
```

## 7 · Assembly
```
Phase 7. Build jua/06_edit/cut_v01.mp4 with ffmpeg, 16:9 1080p, 75s, following shotlist.csv:
- shot 02: restoration stages as 3s crossfades, corner caption "stage N · step · model" (small serif, 60% opacity), one wipe back to the original
- music: "Pitié" excerpts (cue A 10–38s, hard cut to silence at 38s, cue B 58–75s, ≤1s fade out), end-card credit "Music: Tabu Ley Rochereau, 'Pitié'"; ALSO export the backup cut with the original score
- testimony audio 38–58s with burned-in EN subtitles
- end card 70–75s: "We can restore the image. We remember the person together." + disclosure line(s) required by brief.md
- loudness: -14 LUFS integrated
Write the exact ffmpeg commands to jua/06_edit/build.sh so the cut can be rebuilt.
CHECKPOINT: send the cut + a muted-viewing verdict per beat.
```

## 8 · Critic pass
```
Phase 8. Critic pass on jua/06_edit/cut_v[NN].mp4 against brief.md and CLAUDE.md. For each check give PASS / PARTIAL / FAIL + a one-line reason:
1. restoration accuracy — face identical across original → stages → motion shot
2. motion restraint — no blink, mouth or head movement in shot 03
3. no invented facts — every name, place and detail traces to the witness or research.md
4. no generated lettering — the name is real handwriting or a baked overlay
5. sound — silence starts on the first breath at 38s; the motif resolves at the handoff
6. muted readability at 10s / 38s / 58s / 75s
7. disclosures present (fictional / colour) as brief.md requires
8. first 3 seconds make you want to keep watching
List only FAIL/PARTIAL items, each with the smallest fix and its credit cost.
```

## 9 · Delivery
```
Phase 9. Final QA from generathon-emotion-ad-production-kit.md §6. Then, following jua/delivery/explainer_thumbnail.md:
- Thumbnail: pitch me 5 concepts (A–E), generate my pick (2 variants), bake any text afterwards, run the thumbnail QA → jua/delivery/thumbnail.png
- Face cam explainer (≤ 60s, 8 required items): pull my real challenges, wins and lessons from the log.md files and rejected takes, list them for me to confirm (don't invent any), fill the 8 script blocks (~150 words), and export the pipeline node-graph cutaway
Fill jua/delivery/submission.md with the final YouTube link [URL] and explainer link [URL]. Commit, push, and give me the exact form fields to paste.
```

---

## Quick replies at any checkpoint
`approved` · `lock it` · `redo [shot] — [one precise change]` · `A/B again with [model]` · `too much — simpler` · `credits?` · `stop`
