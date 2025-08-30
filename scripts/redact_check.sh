#!/usr/bin/env bash
set -euo pipefail
PAT='secret|token|apikey|api_key|client_secret|client_id|password|bearer|authorization|PROCORE|OPENAI|AWS|GCP|AZURE'
if command -v rg >/dev/null 2>&1; then
  rg -n -i -e "$PAT" -- . --glob '!.git' --glob '!**/.env' --glob '!**/.dev.vars' || true
else
  grep -RIn -E "$PAT" . --exclude-dir=.git --exclude="*.env" --exclude="*.dev.vars" || true
fi