#!/usr/bin/env bash
# Media (images, video, audio) lives in the Hugging Face bucket, not in git.
# Git keeps only text: brief, bible, prompts, shotlist, QC logs.
#
#   scripts/assets.sh push      upload project/ media to the bucket
#   scripts/assets.sh pull      download bucket media into project/
#   scripts/assets.sh status    dry-run both directions
#   scripts/assets.sh migrate   push, verify, then untrack media from git
#
# Needs HF_TOKEN with WRITE access for push/migrate (connector OAuth is read-only).
set -euo pipefail
cd "$(dirname "$0")/.."

BUCKET="${HF_BUCKET:-hf://buckets/Svngoku/generathon-tech-arcads}/project"
LOCAL=project
MEDIA=(--include '*.png' --include '*.jpg' --include '*.jpeg' --include '*.webp'
       --include '*.mp4' --include '*.mov' --include '*.webm'
       --include '*.wav' --include '*.mp3' --include '*.m4a'
       --exclude '*')

command -v hf >/dev/null || pip install -q -U huggingface_hub

case "${1:-status}" in
  push)   hf sync "$LOCAL" "$BUCKET" "${MEDIA[@]}" ;;
  pull)   hf sync "$BUCKET" "$LOCAL" "${MEDIA[@]}" ;;
  status) echo "## local -> bucket"; hf sync "$LOCAL" "$BUCKET" "${MEDIA[@]}" --dry-run
          echo "## bucket -> local"; hf sync "$BUCKET" "$LOCAL" "${MEDIA[@]}" --dry-run ;;
  migrate)
    hf sync "$LOCAL" "$BUCKET" "${MEDIA[@]}"
    pending=$(hf sync "$LOCAL" "$BUCKET" "${MEDIA[@]}" --dry-run | grep -c '"upload"' || true)
    if [ "$pending" != "0" ]; then echo "verify failed: $pending files still differ" >&2; exit 1; fi
    git ls-files -z project | grep -zE '\.(png|jpe?g|webp|mp4|mov|webm|wav|mp3|m4a)$' \
      | xargs -0 -r git rm --cached --quiet
    echo "media untracked from git; commit the removal" ;;
  *) echo "usage: $0 {push|pull|status|migrate}" >&2; exit 2 ;;
esac
