#!/usr/bin/env bash
# Cut v05 (~2:36, 1920x1080, 24fps). Every picture comes from locked/ refs (local moves) or Seedance 2.5 takes built on them.
# Audio: diegetic clip sound + disclosed AI voice (Elisa, ElevenLabs via Arcads) + local "Pitié" edit (never uploaded).
set -euo pipefail
cd "$(dirname "$0")"
F=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
SD=../../04_video/seedance25
V="scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=24,format=yuv420p"
A="aresample=48000,aformat=channel_layouts=stereo"
seg(){ # seg <n> <src> <dur> <has_audio 0/1> [volume]
  if [ "$4" = 1 ]; then $F -loglevel error -y -i "$2" -map 0:v:0 -map 0:a:0 -vf "$V,tpad=stop_mode=clone:stop_duration=5" -af "$A,volume=${5:-0.6},apad" -t "$3" -c:v libx264 -crf 18 -c:a aac -b:a 192k s$1.mp4
  else $F -loglevel error -y -i "$2" -f lavfi -i anullsrc=r=48000:cl=stereo -map 0:v:0 -map 1:a -vf "$V,tpad=stop_mode=clone:stop_duration=5" -t "$3" -c:v libx264 -crf 18 -c:a aac -b:a 192k s$1.mp4; fi; }
seg 01 move_01.mp4 10 0
seg 02 shot02_restoration.mp4 18 0
seg 03 move_03.mp4 10 0
seg 04 ../../04_video/local/shot_inside_photo.mp4 18 0
seg 05 $SD/souvenirs_A.mp4 12 1 0.5
seg 06 $SD/back_A.mp4 10 1 0.6
seg 07 $SD/room_A.mp4 8 1 0.6
seg 08 $SD/shot04_A.mp4 20 1 0.35
seg 09 local_face.mp4 16 0
seg 10 shot05_named.mp4 12 1 0.6
seg 11 local_side.mp4 12 0
seg 12 local_end.mp4 10 0
printf "file 's%s.mp4'\n" 01 02 03 04 05 06 07 08 09 10 11 12 > list.txt
$F -loglevel error -y -f concat -safe 0 -i list.txt -c copy concat.mp4
# subtitles (voice starts at 86s; subs.json times are relative to voice_paced.wav)
VO=86
IN=""; FC="[0:v]null[v0]"; i=0
for row in $(python3 -c "import json;[print(f'{a}:{b}') for a,b,_ in json.load(open('subs.json'))]"); do
  a=${row%%:*}; b=${row##*:}; s=$(python3 -c "print($VO+$a)"); e=$(python3 -c "print($VO+$b)")
  IN="$IN -i sub_$i.png"; FC="$FC;[v$i][$((i+1)):v]overlay=0:0:enable='between(t,$s,$e)'[v$((i+1))]"; i=$((i+1)); done
P=../../05_audio/reference/tabu_ley_pitie.mp3
$F -loglevel error -y -i concat.mp4 $IN -i voice_paced.wav -ss 0 -t 76 -i $P -ss 211 -t 33 -i $P -filter_complex "$FC;\
[$((i+1)):a]$A,highpass=f=90,aecho=0.8:0.4:35:0.15,volume=3.5,adelay=${VO}000|${VO}000[vo];\
[$((i+2)):a]$A,volume=0.5,afade=t=in:d=2,afade=t=out:st=74.5:d=1.5,adelay=10000|10000[m1];\
[$((i+3)):a]$A,volume=0.5,afade=t=in:d=1.5,afade=t=out:st=31:d=2,adelay=123000|123000[m2];\
[0:a]$A[d];[d][vo][m1][m2]amix=inputs=4:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map "[v$i]" -map "[a]" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -t 156 ../cut_v05.mp4
rm -f concat.mp4 s[0-9][0-9].mp4
