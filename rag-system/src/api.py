from fastapi import FastAPI, Query
import csv
from pathlib import Path
app = FastAPI(title="RAG System Demo", version="0.1.0")
DOCS=[]
@app.on_event("startup")
def load():
    p=Path(__file__).resolve().parent.parent/"db"/"synthetic"/"sample_docs.csv"
    with p.open("r", encoding="utf-8") as f:
        DOCS[:]=list(csv.DictReader(f))
@app.get("/health") 
def health(): return {"status":"ok","count":len(DOCS)}
@app.get("/search")
def search(q: str = Query(..., min_length=1)):
    ql=q.lower(); scored=[]
    for d in DOCS:
        txt=f"{d['project']} {d['content']}".lower()
        score=1.0 if ql in txt else 0.2
        scored.append({"id":d["id"],"project":d["project"],"excerpt":d["content"],"score":score})
    scored.sort(key=lambda x:x["score"], reverse=True)
    return {"hits": scored[:3]}
