# Oracle Curator UI (with Waveform Redirect)
# After saving, redirect to waveform editor for manual slicing

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
import os
import json
import random
from datetime import datetime

app = FastAPI()

ORACLE_DB = "./oracle_dynamic.json"
CURATION_LOG = "./oracle_curation_log.md"

@app.get("/", response_class=HTMLResponse)
async def curate():
    with open(ORACLE_DB, 'r') as f:
        entries = json.load(f)
    entries = [e for e in entries if os.path.exists(e['clip'])]
    if not entries:
        return HTMLResponse("<h2>No clips available.</h2>")
    sample = random.choice(entries)
    app.state.current = sample
    clip_path = sample['clip']
    html = f"""
    <html><body style='background:#111;color:#eee;font-family:sans-serif;padding:2em;'>
        <h1>🧠 Oracle Curator</h1>
        <h2>{sample['title']}</h2>
        <p><strong>Highlight:</strong> {sample['highlight']}</p>
        <p><strong>Suggestion:</strong> {sample['suggestion']}</p>
        <audio controls src='/clip'></audio>
        <form action='/action' method='post'>
            <input type='hidden' name='clip' value='{clip_path}'>
            <button name='decision' value='save'>💾 Save</button>
            <button name='decision' value='delete'>🗑️ Delete</button>
            <button name='decision' value='next'>⏭️ Next</button>
        </form>
    </body></html>
    """
    return HTMLResponse(html)

@app.get("/clip")
async def stream_clip():
    return FileResponse(app.state.current['clip'])

@app.post("/action")
async def handle(decision: str = Form(...), clip: str = Form(...)):
    sample = app.state.current
    if decision == "save":
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(CURATION_LOG, 'a') as f:
            f.write(f"[{stamp}] SAVED: {sample['title']}\n{sample['clip']}\n\n")
        return RedirectResponse(url="/waveform?clip=" + clip, status_code=303)
    elif decision == "delete":
        os.remove(sample['clip'])
    return RedirectResponse("/", status_code=303)

@app.get("/waveform", response_class=HTMLResponse)
async def waveform_redirect(clip: str):
    file_name = os.path.basename(clip)
    return HTMLResponse(f"""
    <html><body style='background:#000;color:#eee;padding:2em;font-family:sans-serif;'>
        <h2>🔊 Launching Wave Editor...</h2>
        <script>
            window.location.href = '/oracle_wave_editor.html';
        </script>
    </body></html>
    """)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("oracle_curator_ui:app", host="127.0.0.1", port=7890, reload=True)
