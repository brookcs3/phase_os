# Oracle Seed Engine (patched)
# Rotates from dynamically mined playlist file

import subprocess
import os
import json
from datetime import datetime

PLAYLIST_SOURCE = "./oracle_playlists.txt"
ORACLE_DB = "./oracle_dynamic.json"
CLIP_DIR = "./oracle_clips"

os.makedirs(CLIP_DIR, exist_ok=True)
if not os.path.exists(ORACLE_DB):
    with open(ORACLE_DB, 'w') as f:
        json.dump([], f, indent=2)

def load_playlists():
    if not os.path.exists(PLAYLIST_SOURCE):
        print("⚠️ No playlist file found.")
        return []
    with open(PLAYLIST_SOURCE, 'r') as f:
        return [line.strip() for line in f if line.strip().startswith("https://")]

def scrape_playlist(url):
    print(f"📼 Scraping: {url}")
    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--playlist-end", "3",
        "--output", f"{CLIP_DIR}/%(title).80s.%(ext)s",
        url
    ]
    subprocess.run(cmd)

def scan_downloads():
    entries = []
    for fname in os.listdir(CLIP_DIR):
        if not fname.endswith(".mp3"):
            continue
        path = os.path.join(CLIP_DIR, fname)
        entries.append({
            "title": fname.replace(".mp3", ""),
            "artist": "Unknown",
            "year": "Unknown",
            "clip": path,
            "highlight": "Listen and slice",
            "suggestion": "Explore loopable vocal/drum textures"
        })
    return entries

def update_oracle_db(new_entries):
    with open(ORACLE_DB, 'r') as f:
        existing = json.load(f)
    merged = existing + [e for e in new_entries if e not in existing]
    with open(ORACLE_DB, 'w') as f:
        json.dump(merged, f, indent=2)
    print(f"🧠 Oracle DB updated with {len(new_entries)} entries.")

if __name__ == "__main__":
    playlists = load_playlists()
    if playlists:
        for url in playlists[:2]:
            scrape_playlist(url)
    else:
        print("⚠️ No playlists to scrape.")
    new_entries = scan_downloads()
    update_oracle_db(new_entries)