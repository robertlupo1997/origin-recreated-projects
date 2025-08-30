from fastapi import FastAPI
app = FastAPI(title="APM Agent Backend", version="0.1.0")
PROJECTS=[{"id":1,"name":"ProjectA"},{"id":2,"name":"ProjectB"}]
RFIS=[{"id":101,"project_id":1,"title":"RFI-101"},{"id":102,"project_id":2,"title":"RFI-102"}]
@app.get("/health") 
def health(): return {"status":"ok"}
@app.get("/projects") 
def projects(): return {"projects":PROJECTS}
@app.get("/rfis") 
def rfis(): return {"rfis":RFIS}
