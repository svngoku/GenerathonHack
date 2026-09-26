#!/usr/bin/env python3
"""Cut v06 (~2:44, 1920x1080, 24 fps). Same pictures as v05 (locked/ refs + Seedance 2.5 takes), plus:
- dissolves instead of hard cuts from 0:38 on (0:00-0:38 kept as approved);
- 1:18-1:34 room beat rebuilt: room_A + one slow push-in to the table (room_push.py), 3 s dissolve into the hands;
- "Pitié" cue A placed so its lines land on the matching scenes (lyric map: 05_audio/pitie_lyrics_map.md);
- music fades out under "je fais ton avenir" as the hands arrive; a breath of silence; then the voice;
- cue B returns on "Pitié toi mon amour" as the name is written;
- lyric captions (lyric_caps.json) + testimony subtitles (subs.json, relative to the voice start).
Usage: python3 build_v06.py <voice_paced.wav> <out.mp4>
The song is only read locally (never uploaded)."""
import json, subprocess, sys, os
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
VOICE, OUT = sys.argv[1], sys.argv[2]
SD, V5 = "../../04_video/seedance25", "../v05"
P = "../../05_audio/reference/tabu_ley_pitie.mp3"
T = json.load(open(os.environ.get("TIMELINE", "timeline.json")))
B, SEG, VO, CUE_A, CUE_B = T["bounds"], T["segments"], T["voice_start"], T["cue_a"], T["cue_b"]
sh = lambda c: subprocess.run(c, check=True)
X = lambda k: 0 if k == 0 else max(SEG[k]["xin"], 1 / 24)   # a hard cut is a 1-frame fade (xfade needs overlap)
def dur(f): return float(subprocess.run([FF, "-i", f], capture_output=True, text=True).stderr.split("Duration: ")[1].split(",")[0].split(":")[2]) + 60 * float(subprocess.run([FF, "-i", f], capture_output=True, text=True).stderr.split("Duration: ")[1].split(",")[0].split(":")[1])

SKIP = os.environ.get("SKIP_SEGS") == "1" and os.path.exists("picture.mp4")
# 1) normalise each segment to its extended length (nominal + half of each neighbouring dissolve)
Vf = "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=24,format=yuv420p"
starts, lens = [], []
for k, s in enumerate(SEG):
    din = X(k); dout = X(k + 1) if k + 1 < len(SEG) else 0
    st = B[k] - din / 2; ln = (B[k + 1] - B[k]) + din / 2 + dout / 2
    starts.append(st); lens.append(ln)
    src = s["src"].replace("$SD", SD).replace("$V5", V5)
    speed = s.get("speed", 1.0)
    vf = f"setpts={speed}*PTS,{Vf},tpad=stop_mode=clone:stop_duration=8"
    if not SKIP: sh([FF, "-loglevel", "error", "-y", "-i", src, "-an", "-vf", vf, "-t", f"{ln:.3f}", "-c:v", "libx264", "-crf", "16", "-preset", "fast", f"g{k:02d}.mp4"])
    if s.get("vol") and not SKIP:
        af = f"atempo={1/speed:.4f}," if speed != 1.0 else ""
        sh([FF, "-loglevel", "error", "-y", "-i", src, "-vn", "-af", f"{af}aresample=48000,aformat=channel_layouts=stereo,volume={s['vol']},apad", "-t", f"{ln:.3f}", f"g{k:02d}.wav"])

# 2) picture: chained xfade (a 0-length transition is a straight cut, done with a 1-frame fade)
inp, fc, last = [], [], "[0:v]"
for k in range(len(SEG)): inp += ["-i", f"g{k:02d}.mp4"]
for k in range(1, len(SEG)):
    d = X(k); off = B[k] - d / 2
    fc.append(f"{last}[{k}:v]xfade=transition=fade:duration={d:.3f}:offset={off:.3f}[x{k}]"); last = f"[x{k}]"
if not SKIP: sh([FF, "-loglevel", "error", "-y", *inp, "-filter_complex", ";".join(fc), "-map", last, "-c:v", "libx264", "-crf", "16", "-preset", "fast", "picture.mp4"])
for k in range(len(SEG)): print(f"seg {k:2d} {SEG[k]['name']:12s} start {starts[k]:7.3f} len {lens[k]:6.3f} file {dur(f'g{k:02d}.mp4'):6.2f}")
print("picture.mp4", dur("picture.mp4")); assert abs(dur("picture.mp4") - B[-1]) < 0.2

# 3) overlays (own pass, video only): each PNG cropped to its text box, looped at 24 fps, alpha-faded, shifted in time
from PIL import Image
subs = json.load(open(os.environ.get("SUBS", f"{V5}/subs.json"))); caps = json.load(open("lyric_caps.json"))
ov = [(f"{V5}/sub_{i}.png", VO + a, VO + b, 0.25) for i, (a, b, _) in enumerate(subs)]
ov += [(f"lyr_{i}.png", c["t0"], c["t1"], 0.6) for i, c in enumerate(caps)]
ov += [(n["png"], n["t0"], n["t1"], 0.6) for n in T.get("notes", [])]
inp, fc, last = ["-i", "picture.mp4"], [], "[0:v]"
for i, (png, a, b, f) in enumerate(ov):
    im = Image.open(png); x0, y0, x1, y1 = im.getbbox(); x0 -= x0 % 2; y0 -= y0 % 2
    x1 += x1 % 2; y1 += y1 % 2; im.crop((x0, y0, x1, y1)).save(f"ov_{i}.png")
    inp += ["-framerate", "24", "-loop", "1", "-t", f"{b - a:.3f}", "-itsoffset", f"{a:.3f}", "-i", f"ov_{i}.png"]
    fc.append(f"[{i+1}:v]format=yuva420p,fade=t=in:st={a:.3f}:d={f}:alpha=1,fade=t=out:st={b-f:.3f}:d={f}:alpha=1[o{i}]")
    fc.append(f"{last}[o{i}]overlay={x0}:{y0}:eof_action=pass:format=yuv420[v{i}]"); last = f"[v{i}]"
sh([FF, "-loglevel", "error", "-stats", "-y", *inp, "-filter_complex", ";".join(fc), "-map", last, "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "overlaid.mp4"])
print("overlaid.mp4", dur("overlaid.mp4"))

# 4) audio (own pass): diegetic clip sound (placed, fades matching the dissolves) + voice + two Pitié cues
ai, fc, amix = [], [], []
for k, s in enumerate(SEG):
    if not s.get("vol"): continue
    din = X(k) or 0.05; dout = (X(k + 1) if k + 1 < len(SEG) else 0) or 0.05
    j = len(ai) // 2; ai += ["-i", f"g{k:02d}.wav"]
    ms = int(starts[k] * 1000)
    fc.append(f"[{j}:a]afade=t=in:d={din:.3f},afade=t=out:st={lens[k]-dout:.3f}:d={dout:.3f},adelay={ms}|{ms}[d{k}]"); amix.append(f"[d{k}]")
j = len(ai) // 2
ai += ["-i", VOICE]; ms = int(VO * 1000)
fc.append(f"[{j}:a]aresample=48000,aformat=channel_layouts=stereo,highpass=f=90,aecho=0.8:0.4:35:0.15,volume={T['voice_gain']},adelay={ms}|{ms},asplit=2[vo][vosc]"); amix.append("[vo]")
for n, c in (("ma", CUE_A), ("mb", CUE_B)):
    if not c: continue
    j += 1; ai += ["-ss", str(c["song_in"]), "-t", str(c["dur"]), "-i", P]; ms = int(c["film_at"] * 1000)
    # optional ducking: [[film_t, gain], ...] linearly interpolated (keeps the music under the voice instead of stopping it)
    if c.get("duck"):
        pts = [(ft - c["film_at"], g) for ft, g in c["duck"]]; e = str(pts[0][1])
        for (t0, g0), (t1, g1) in zip(pts, pts[1:]):
            e = f"if(gte(t,{t0}),{g0}+({g1}-{g0})*min(1,(t-{t0})/{max(t1-t0,0.01)}),{e})"
        vol = f"volume='{e}':eval=frame"
    else: vol = f"volume={c['vol']}"
    fc.append(f"[{j}:a]aresample=48000,aformat=channel_layouts=stereo,{vol},afade=t=in:d={c['fade_in']},afade=t=out:st={c['dur']-c['fade_out']}:d={c['fade_out']},adelay={ms}|{ms}[{n}]"); amix.append(f"[{n}]")
TOTAL = B[-1]
if T.get("sidechain") and "[ma]" in amix:
    amix.remove("[ma]"); fc.append(f"[vosc]apad[vosk];[ma][vosk]sidechaincompress=threshold=0.015:ratio=6:attack=120:release=1100:makeup=1[mad]"); amix.append("[mad]")
else:
    fc.append("[vosc]anullsink")
# optional room-tone bed (never digital silence): very low brown noise, low-passed, over [from, to]
if T.get("roomtone"):
    a, b, g = T["roomtone"]; ms = int(a * 1000)
    fc.append(f"anoisesrc=color=brown:sample_rate=48000:amplitude=1:duration={b-a},lowpass=f=700,volume={g},afade=t=in:d=2,afade=t=out:st={b-a-2}:d=2,aformat=channel_layouts=stereo,adelay={ms}|{ms}[rt]"); amix.append("[rt]")
fc.append(f"{''.join(amix)}amix=inputs={len(amix)}:normalize=0,apad=whole_dur={TOTAL},atrim=0:{TOTAL},loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]")
sh([FF, "-loglevel", "error", "-y", *ai, "-filter_complex", ";".join(fc), "-map", "[a]", "-ar", "48000", "-t", str(TOTAL), "mix.wav"])

# 5) mux
sh([FF, "-loglevel", "error", "-y", "-i", "overlaid.mp4", "-i", "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(TOTAL), OUT])
print(OUT, dur(OUT))
for f in os.listdir("."):
    if f.startswith("g") and f[1:3].isdigit() and f.endswith((".mp4", ".wav")) and not os.environ.get("KEEP"): os.remove(f)
for f in (("overlaid.mp4", "mix.wav") if os.environ.get("KEEP") else ("picture.mp4", "overlaid.mp4", "mix.wav")): os.remove(f)
for f in os.listdir("."):
    if f.startswith("ov_") and f.endswith(".png"): os.remove(f)
print("built", OUT, TOTAL, "s")
