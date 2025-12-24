# Oracle Remix Browser
# UI for browsing and auditioning most recent remix session

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

ROOT = "./"
REMIX_BASE = "remix_session_"

@app.get("/", response_class=HTMLResponse)
async def browse():
    dirs = sorted([d for d in os.listdir(ROOT) if d.startswith(REMIX_BASE)], reverse=True)
    if not dirs:
        return HTMLResponse("<h2>No remix sessions found.</h2>")
    latest = os.path.join(ROOT, dirs[0])
    files = [f for f in os.listdir(latest) if f.endswith(".wav") or f.endswith(".mp3")]
    html = f"<html><body style='background:#111;color:#eee;font-family:sans-serif;padding:2em;'>"
    html += f"<h1>🎛️ Remix Session Browser: {dirs[0]}</h1>"
    for f in sorted(files):
        html += f"<p><strong>{f}</strong><br><audio controls src='/remix/{f}'></audio></p>"
    html += "</body></html>"
    return HTMLResponse(html)

@app.get("/remix/{name}")
async def stream(name: str):
    dirs = sorted([d for d in os.listdir(ROOT) if d.startswith(REMIX_BASE)], reverse=True)
    if not dirs:
        return HTMLResponse("No remix folder.")
    latest = os.path.join(ROOT, dirs[0])
    return FileResponse(os.path.join(latest, name))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("remix_browser:app", host="127.0.0.1", port=7892, reload=True)
