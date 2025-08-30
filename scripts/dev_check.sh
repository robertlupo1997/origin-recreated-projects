#!/usr/bin/env bash
set -euo pipefail

echo "== Secret scan =="
# focus on real credential patterns (assignments/bearer), not ordinary words
PAT_ASSIGN='(?i)\b(secret_key|api_token|api[-_]?key|client_secret|client_id|password)\b\s*[:=]'
PAT_BEARER='(?i)\bbearer\s+[A-Za-z0-9._\-]{16,}'
PAT_AUTH='(?i)\bauthorization\s*[:=]'

if command -v rg >/dev/null 2>&1; then
  HITS="$(rg -n -i -e "$PAT_ASSIGN" -e "$PAT_BEARER" -e "$PAT_AUTH" -- . \
    --glob '!.git/**' --glob '!staging/**' --glob '!docs/**' --glob '!.github/**' \
    --glob '!scripts/**' --glob '!node_modules/**' --glob '!venv/**' --glob '!.venv/**' \
    --glob '!dist/**' --glob '!build/**' --glob '!coverage/**' --glob '!.pytest_cache/**' \
    --glob '!**/*.env' --glob '!**/.dev.vars' || true)"
else
  HITS="$(grep -RIn -E 'secret_key|api_token|api[-_]?key|client_secret|client_id|password|Bearer [A-Za-z0-9._\-]{16,}|Authorization[:=]' . \
    --exclude-dir=.git --exclude-dir=staging --exclude-dir=docs --exclude-dir=.github \
    --exclude-dir=scripts --exclude-dir=node_modules --exclude-dir=venv --exclude-dir=.venv \
    --exclude-dir=dist --exclude-dir=build --exclude-dir=coverage --exclude-dir=.pytest_cache \
    --exclude='*.env' --exclude='.dev.vars' || true)"
fi

if [ -n "${HITS}" ]; then
  echo "Risk hits:"; echo "$HITS"; exit 2
else
  echo "No risk hits."
fi

echo; echo "== Metrics =="
bash scripts/measure.sh
sed -n '1,80p' docs/metrics.md || true
