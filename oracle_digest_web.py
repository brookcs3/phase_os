# Oracle Digest Web Viewer
# Serves latest daily digest markdown in a clean browser format

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import markdown
import os

app = FastAPI()
DIGEST_FILE = "./oracle_digest_today.md"

@app.get("/", response_class=HTMLResponse)
async def view_digest():
    if not os.path.exists(DIGEST_FILE):
        return HTMLResponse("<h2>No Oracle digest found yet.</h2>")
    with open(DIGEST_FILE, 'r') as f:
        content = f.read()
    html = markdown.markdown(content)
    page = f"""
    <html>
    <head><title>Oracle Digest</title></head>
    <body style='font-family:sans-serif;background:#111;color:#eee;padding:2em;'>
        <h1>📓 Daily Oracle Digest</h1>
        {html}
    </body>
    </html>
    """
    return HTMLResponse(page)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("oracle_digest_web:app", host="127.0.0.1", port=7881, reload=True)