from pathlib import Path
from collections import Counter
from openpyxl import Workbook
DATA=[{"id":"RFI-1","project":"ProjectA","status":"Open"},{"id":"RFI-2","project":"ProjectA","status":"Closed"},{"id":"RFI-3","project":"ProjectB","status":"Open"}]
def export_summary(output_path: Path):
    counts = Counter([d["status"] for d in DATA])
    wb = Workbook(); ws = wb.active; ws.title="Summary"; ws.append(["Status","Count"])
    for k,v in sorted(counts.items()): ws.append([k,v])
    wb.save(output_path)
def main():
    out = Path("summary.xlsx"); export_summary(out); print(f"Wrote {out.resolve()}")
if __name__ == "__main__": main()
