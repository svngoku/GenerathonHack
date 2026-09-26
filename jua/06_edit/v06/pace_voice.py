# Place one TTS file per testimony line at the subtitle start times (v05/subs.json) -> voice_paced_<name>.wav (37.5 s).
# Each line is trimmed of leading/trailing silence, so the pauses are ours (breath, silence) and the subtitles stay in sync.
# Usage: python3 pace_voice.py <name> line0.wav line1.wav ... line6.wav
import sys, json, subprocess, numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); SR = 48000
subs = json.load(open("../v05/subs.json"))
name, files = sys.argv[1], sys.argv[2:]
assert len(files) == len(subs), (len(files), len(subs))
def load(f):
    raw = subprocess.run([FF, "-loglevel", "error", "-i", f, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)
out = np.zeros(int(37.5 * SR), np.float32)
for (a, b, txt), f in zip(subs, files):
    y = load(f); env = np.convolve(np.abs(y), np.ones(480) / 480, "same"); on = np.where(env > 0.01)[0]
    y = y[max(on[0] - 1200, 0): on[-1] + 2400]
    i = int(a * SR); n = min(len(y), len(out) - i); out[i:i + n] += y[:n]
    print(f"{a:5.1f}s  {len(y)/SR:4.1f}s (sub {b-a:4.1f}s)  {txt[:50]}")
subprocess.run([FF, "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", f"voice_paced_{name}.wav"], input=out.tobytes(), check=True)
