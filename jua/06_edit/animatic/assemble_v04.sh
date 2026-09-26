#!/usr/bin/env bash
# Animatic v04: 01/03 local moves over locked K1, 02/06 locked stills, 04/05 Seedance 2.5 takes,
# rough local "Pitié" bed (never uploaded). Usage: ./assemble_v04.sh <take04.mp4> <take05.mp4>
set -euo pipefail
cd "$(dirname "$0")"
F=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
N="scale=854:480:force_original_aspect_ratio=decrease,pad=854:480:(ow-iw)/2:(oh-ih)/2,fps=24,format=yuv420p"
A="aresample=48000,aformat=channel_layouts=stereo"
$F -loglevel error -y -i move_01.mp4 -vf "fps=24,format=yuv420p" -af "$A" -t 10 -c:v libx264 -crf 20 -c:a aac seg_01.mp4
$F -loglevel error -y -i shot_02.mp4 -vf "fps=24,format=yuv420p" -af "$A" -t 18 -c:v libx264 -crf 20 -c:a aac seg_02.mp4
$F -loglevel error -y -i move_03.mp4 -vf "fps=24,format=yuv420p" -af "$A" -t 10 -c:v libx264 -crf 20 -c:a aac seg_03.mp4
$F -loglevel error -y -i "$1" -i sub_04.png -filter_complex "[0:v:0]$N,tpad=stop_mode=clone:stop_duration=5[v];[v][1:v]overlay=0:0,format=yuv420p[o];[0:a:0]$A,apad[a]" -map "[o]" -map "[a]" -t 20 -c:v libx264 -crf 20 -c:a aac seg_04.mp4
$F -loglevel error -y -i "$2" -loop 1 -i name_05.png -filter_complex "[0:v:0]$N,tpad=stop_mode=clone:stop_duration=3[v];[v][1:v]overlay=0:0:enable='gte(t,8.5)',format=yuv420p[o];[0:a:0]$A,apad[a]" -map "[o]" -map "[a]" -t 12 -c:v libx264 -crf 20 -c:a aac seg_05.mp4
$F -loglevel error -y -i shot_06.mp4 -vf "fps=24,format=yuv420p" -af "$A" -t 5 -c:v libx264 -crf 20 -c:a aac seg_06.mp4
printf "file 'seg_%s.mp4'\n" 01 02 03 04 05 06 > list.txt
$F -loglevel error -y -f concat -safe 0 -i list.txt -c:v libx264 -crf 20 -c:a aac -ar 48000 -t 75 picture.mp4
P=../../05_audio/reference/tabu_ley_pitie.mp3
$F -loglevel error -y -i picture.mp4 -ss 0 -t 28 -i $P -ss 227 -t 17 -i $P -filter_complex "[1:a]$A,volume=0.55,afade=t=in:d=2,adelay=10000|10000[m1];[2:a]$A,volume=0.55,afade=t=in:d=1,afade=t=out:st=16:d=1,adelay=58000|58000[m2];[0:a]$A[d];[d][m1][m2]amix=inputs=3:normalize=0:duration=first[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t 75 ../animatic_v04.mp4
rm -f picture.mp4
