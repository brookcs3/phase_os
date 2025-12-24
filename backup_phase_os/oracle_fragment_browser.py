# Oracle Fragment Browser
# Displays audio+visual pairings from fragment_index.md as an HTML scrollable log

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import re

app = FastAPI()
INDEX_FILE = "./fragment_index.md"

@app.get("/", response_class=HTMLResponse)
async def browse():
    if not os.path.exists(INDEX_FILE):
        return HTMLResponse("<h2>No fragments found.</h2>")

    with open(INDEX_FILE, 'r') as f:
        content = f.read()

    entries = re.findall(r"\[(.*?)\] SLICE: (.*?) \(session: (.*?)\)\\nAudio: (.*?)\\nVisual: (.*?)", content.replace("\n", "\\n"))
    html = """
    <html><body style='background:#111;color:#eee;font-family:sans-serif;padding:2em;'>
    <h1>🎛️ Oracle Fragment Browser</h1>
    <div style='display:flex;flex-direction:column;gap:2em;'>
    """
    for stamp, name, session, audio, visual in entries[::-1]:
        audio_rel = audio.replace("./", "/")
        visual_rel = visual.replace("./", "/")
        html += f"""
        <div style='border:1px solid #444;padding:1em;'>
            <h3>{name}</h3>
            <p>{stamp} • <code>{session}</code></p>
            <audio controls src='{audio_rel}'></audio><br>
            <img src='{visual_rel}' width='480' style='margin-top:1em;'>
        </div>
        """
    html += "</div></body></html>"
    return HTMLResponse(html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("oracle_fragment_browser:app", host="127.0.0.1", port=7891, reload=True)
