# Prompts — Jua

## Shot 03 — restrained motion (UmoJua image-to-video, or Arcads Kling/Veo)
Input: `locked/restored.png` (only with photo owner's permission to upload).
```
CONSTRAINTS: Render ONLY what is described. The person in the photograph does NOT move: no blinking, no smiling, no lip or head movement, no change in expression or identity. No added text, props, color, or background changes.
Duration 6s, 16:9. The photograph lies on a wooden table. Slow, steady camera push-in toward the face. A soft band of warm window light moves slowly from left to right across the print. Paper grain and edges stay stable. One continuous shot, no cuts.
```
Roll 2 variants; reject any take where the face changes.

## Fictional mode only — generated portrait → `locked/original.png`
```
Black-and-white studio portrait photograph, [FICTIONAL PLACE], [YEAR]. A woman in her thirties, seated, three-quarter view, calm direct gaze, [HEADWRAP / CLOTHING TYPICAL OF THAT PLACE AND DECADE — research, don't guess]. Plain painted studio backdrop. Authentic print wear: faded contrast, fine scratches, a crease across one corner, slightly torn edge. Silver-gelatin grain. No text, no watermark, no modern elements. An original fictional person, not a real individual.
```
Then run it through UmoJua for the restoration exactly as you would a real photo.

## Fictional mode only — hands on table B-roll (Arcads image/video)
```
CONSTRAINTS: Live motion video. Render ONLY what is described. No text, logos, or extra objects.
Top-down, 16:9, warm late daylight on a worn wooden table. A young person's hands slide an old black-and-white portrait print out of a paper sleeve and lay it flat. Natural hand anatomy, five fingers each. Static camera. 5s.
```

## Captions (Arcads captions/translate)
Source: witness audio from shot 04. Output: burned-in EN subtitles + FR version. Check every word of the name and place by ear with the witness — never trust auto-transcription of names.

## Critic pass (kit prompt H, extended)
```
Review this cut against the brief. Score 0–5: emotional readability muted, honesty (original visible, no invented facts, face unaltered in motion), first 3 seconds, testimony clarity. List blocking issues + the smallest fix.
```
