# Sample Oracle v1 API + Similarity Suggestions
# Serves curated vinyl-era clips and suggests matches based on OpenL3 vectors

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
import random
import os
import json
import numpy as np

app = FastAPI()

ORACLE_DB = "./oracle_dynamic.json"
EMBED_FILE = "./oracle_embeddings.json"
app.state.current_clip = None

@app.get("/", response_class=HTMLResponse)
async def oracle_ui():
    with open(ORACLE_DB, 'r') as f:
        records = json.load(f)

    record = random.choice(records)
    clip_path = record['clip']
    suggestion_html = ""

    if os.path.exists(EMBED_FILE):
        with open(EMBED_FILE, 'r') as f:
            vecs = json.load(f)
        if os.path.basename(clip_path) in vecs:
            source_vec = np.array(vecs[os.path.basename(clip_path)])
            matches = []
            for fname, vec in vecs.items():
                if fname == os.path.basename(clip_path):
                    continue
                dist = 1 - np.dot(source_vec, vec) / (np.linalg.norm(source_vec) * np.linalg.norm(vec))
                matches.append((fname, dist))
            top = sorted(matches, key=lambda x: x[1])[:3]
            suggestion_html += "<h3>🔁 Similar Suggestions:</h3><ul>"
            for fname, score in top:
                suggestion_html += f"<li>{fname} (dist {score:.4f})</li>"
            suggestion_html += "</ul>"

    html = f"""
    <html>
    <head><title>Sample Oracle</title></head>
    <body style='background:#111;color:#eee;font-family:sans-serif;padding:2em;'>
        <h1>🔊 Sample Oracle</h1>
        <h2>{record['title']} <small>by {record['artist']} ({record['year']})</small></h2>
        <p><strong>Highlight:</strong> {record['highlight']}</p>
        <p><strong>Suggestion:</strong> {record['suggestion']}</p>
        <audio controls src="/clip"></audio>
        <form method='post' action='/save'>
            <input type='hidden' name='title' value="{record['title']}">
            <input type='hidden' name='artist' value="{record['artist']}">
            <input type='hidden' name='year' value="{record['year']}">
            <input type='hidden' name='highlight' value="{record['highlight']}">
            <input type='hidden' name='suggestion' value="{record['suggestion']}">
            <button type='submit'>💾 Save This Sample</button>
        </form>
        {suggestion_html}
    </body>
    </html>
    """
    app.state.current_clip = clip_path
    return HTMLResponse(html)

@app.get("/clip")
async def serve_clip():
    return FileResponse(app.state.current_clip)

@app.post("/save")
async def save_clip(request: Request):
    form = await request.form()
    title = form['title']
    artist = form['artist']
    year = form['year']
    highlight = form['highlight']
    suggestion = form['suggestion']
    with open("./oracle_log.md", 'a') as f:
        f.write(f"\n## {title} — {artist} ({year})\n• Highlight: {highlight}\n• Suggestion: {suggestion}\n")
    return HTMLResponse("<h2>✅ Sample saved. <a href='/'>Back</a></h2>")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sample_oracle_api:app", host="127.0.0.1", port=7880, reload=True)