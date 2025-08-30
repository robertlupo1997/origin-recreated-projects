from pathlib import Path
from src.rfi_export import export_summary
def test_export_writes_file(tmp_path: Path):
    out = tmp_path/"summary.xlsx"; export_summary(out)
    assert out.exists() and out.stat().st_size>0
