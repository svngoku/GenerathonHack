# Pace ONE continuous TTS take (eleven_v3, natural delivery) onto the film's line grid.
# Each line keeps its own audio (breaths, hum, pauses inside it); only the gaps between lines are changed,
# so every line starts where the picture expects it. Writes voice_paced_<name>.wav + subs_<name>.json
# (subtitle times = where the audio really is; the subtitle PNGs are the v05 ones, same text).
# Line cuts were found by silence detection + local Whisper labels (see 04_video/log.md, round v08).
import sys, json, subprocess, numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); SR = 48000
START = [1.5, 5.4, 13.9, 17.2, 19.8, 26.8, 34.6]      # line starts relative to the voice (unchanged film grid)
TAKES = {
  # name: list of (src_from, src_to, line_start_index, [(sub_index, frac_from, frac_to), ...])
  "dolamade": ("../../05_audio/voice/v08/dolamade_1.mp3", [
      (0.00, 2.75, 0, [(0, 0, 1)]),
      (4.05, 9.05, 1, [(1, 0, 1)]),
      (9.30, 14.35, 2, [(2, 0, 0.62), (3, 0.62, 1)]),        # "Pitié…" + savon/charbon read as one breath
      (14.70, 18.40, 4, [(4, 0, 1)]),
      (19.70, 23.35, 5, [(5, 0, 1)]),
      (23.35, 24.60, 6, [(6, 0, 1)]),
  ]),
  "fatou": ("../../05_audio/voice/v08/fatou_1.mp3", [
      (0.10, 3.40, 0, [(0, 0, 1)]),
      (4.85, 10.75, 1, [(1, 0, 1)]),
      (11.90, 15.70, 2, [(2, 0, 1)]),
      (15.75, 17.05, 3, [(3, 0, 1)]),
      (17.80, 22.45, 4, [(4, 0, 1)]),
      (23.70, 27.75, 5, [(5, 0, 1)]),
      (28.35, 29.44, 6, [(6, 0, 1)]),
  ]),
}
name = sys.argv[1]; src, lines = TAKES[name]
y = np.frombuffer(subprocess.run([FF, "-loglevel", "error", "-i", src, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True).stdout, np.float32)
out = np.zeros(int(37.5 * SR), np.float32); subs = [None] * 7; cursor = 0.0
for a, b, li, sl in lines:
    seg = y[int(a * SR): int(b * SR)].copy(); n = len(seg); f = int(0.03 * SR)
    seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)          # click-free edges
    t0 = max(START[li], cursor + 0.35); i = int(t0 * SR); out[i:i + n] += seg[:len(out) - i]
    cursor = t0 + n / SR
    for si, fa, fb in sl: subs[si] = [round(t0 + fa * n / SR, 2), round(t0 + fb * n / SR, 2)]
    print(f"line {li}: src {a:5.2f}-{b:5.2f} -> {t0:5.2f}-{cursor:5.2f}")
old = json.load(open("../v05/subs.json"))
json.dump([[s[0], s[1], o[2]] for s, o in zip(subs, old)], open(f"subs_{name}.json", "w"), ensure_ascii=False)
subprocess.run([FF, "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", f"voice_paced_{name}.wav"], input=out.tobytes(), check=True)
