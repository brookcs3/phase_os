# Tag Search Dashboard + Voice Query
# Serves a searchable interface for fragment_index.md and voice transcripts

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI()

TAG_FILE = "./fragment_index.md"
SESSIONS_DIR = "./unnamed_record/sessions"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    query = request.query_params.get("q", "").lower()

    tag_results = []
    if os.path.exists(TAG_FILE):
        with open(TAG_FILE, 'r') as f:
            tag_lines = [line.strip() for line in f if line.strip()]
        tag_results = [line for line in tag_lines if query in line.lower()] if query else tag_lines

    voice_results = []
    for session in sorted(os.listdir(SESSIONS_DIR)):
        session_path = os.path.join(SESSIONS_DIR, session)
        if not os.path.isdir(session_path):
            continue
        for file in os.listdir(session_path):
            if file.startswith("voice_") and file.endswith(".txt"):
                full_path = os.path.join(session_path, file)
                with open(full_path, 'r') as f:
                    text = f.read().strip()
                    if (not query) or (query in text.lower()):
                        voice_results.append((session, file, text))

    html = f"""
    <html>
    <head><title>Fragment + Voice Search</title></head>
    <body style='font-family:sans-serif;padding:2em;background:#111;color:#eee;'>
        <h1>🔍 Loop Query Interface</h1>
        <form method='get'>
            <input type='text' name='q' placeholder='Search tags or voice...' style='width:300px;'>
            <button type='submit'>Search</button>
        </form>

        <h2>🏷️ Fragment Tags</h2>
        <pre>{chr(10).join(tag_results)}</pre>

        <h2>🎙️ Voice Transcripts</h2>
        <div>
    """
    for session, file, content in voice_results:
        html += f"<h4>{session} — {file}</h4><pre>{content}</pre><hr>"
    html += "</div></body></html>"

    return HTMLResponse(html)

if __name__ == "__main__":
    uvicorn.run("tag_dashboard:app", host="127.0.0.1", port=7870, reload=True)
