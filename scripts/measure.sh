#!/usr/bin/env bash
set -euo pipefail
mkdir -p docs
OUT="docs/metrics.md"
count_routes_py(){ grep -R -E '@app\.(get|post|put|delete|patch)\(' "$1" 2>/dev/null | wc -l | tr -d ' '; }
count_routes_ts(){ grep -R -E '\.get\(|\.post\(|\.put\(|\.delete\(' "$1" 2>/dev/null | wc -l | tr -d ' '; }
loc(){
python - <<'PY'
import os
exts={'.py':'Python','.ts':'TypeScript','.js':'JavaScript','.md':'Markdown','.sh':'Shell','.yml':'YAML'}
exclude_dirs = {'.git','staging','docs','.github','node_modules','venv','.venv','dist','build','coverage','.pytest_cache'}
tot={}
for r,ds,fs in os.walk('.'):
  ds[:] = [d for d in ds if d not in exclude_dirs]
  for f in fs:
    p=os.path.join(r,f); e=os.path.splitext(f)[1]
    if e in exts:
      try: c=sum(1 for _ in open(p,'r',encoding='utf-8',errors='ignore'))
      except: c=0
      tot[exts[e]]=tot.get(exts[e],0)+c
for k in sorted(tot): print(f"- {k}: {tot[k]}")
PY
}
echo "# metrics" > "$OUT"
echo "" >> "$OUT"
echo "## endpoints" >> "$OUT"
echo "- apm-agent-backend: $(count_routes_py apm-agent-backend/src)" >> "$OUT"
echo "- rag-system: $(count_routes_py rag-system/src)" >> "$OUT"
echo "- procore-mcp-gateway: $(count_routes_ts procore-mcp-gateway/src)" >> "$OUT"
echo "" >> "$OUT"
echo "## loc" >> "$OUT"
loc >> "$OUT"
echo "" >> "$OUT"
echo "## tests" >> "$OUT"
find . -maxdepth 3 -type d -name tests -not -path "./staging/*" -not -path "./.git/*" -not -path "./docs/*" -not -path "./node_modules/*" -print | sed 's#^#- #' >> "$OUT"
echo "" >> "$OUT"
echo "Wrote $OUT"
