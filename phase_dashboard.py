# Phase Web Dashboard (FastAPI)
# Serves a simple page showing current phase, logs, and hot trigger buttons

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

CURRENT_PHASE_FILE = "./current_phase.txt"
PHASES_FILE = "./phases.json"

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    current = open(CURRENT_PHASE_FILE).read().strip() if os.path.exists(CURRENT_PHASE_FILE) else "None"
    phase_html = f"<h2>Current Phase: <span style='color: #22aa88'>{current}</span></h2>"

    buttons = ""
    import json
    with open(PHASES_FILE, 'r') as f:
        phases = json.load(f)['phases']
        for pid, phase in phases.items():
            buttons += f"<form action='/set/{pid}' method='post' style='display:inline-block;margin:5px;'>"
            buttons += f"<button style='padding:10px;background:#444;color:white;border:none;'>{phase['name']}</button>"
            buttons += "</form>"

    html = f"""
    <html>
    <head><title>Phase Dashboard</title></head>
    <body style='font-family:sans-serif;background:#111;color:#eee;padding:2em;'>
        <h1>🧠 Phase OS</h1>
        {phase_html}
        <div>{buttons}</div>
    </body>
    </html>
    """
    return HTMLResponse(html)

@app.post("/set/{phase_id}")
async def set_phase(phase_id: str):
    with open(PHASES_FILE, 'r') as f:
        phases = json.load(f)['phases']
    if phase_id in phases:
        with open(CURRENT_PHASE_FILE, 'w') as f:
            f.write(phases[phase_id]['name'])
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    uvicorn.run("phase_dashboard:app", host="127.0.0.1", port=7860, reload=True)
