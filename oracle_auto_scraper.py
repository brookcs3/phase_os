# Oracle Auto Scraper
# Rotates curated search terms, fetches YouTube clips, logs to Oracle DB

import subprocess
import os
import json
import random
from datetime import datetime

from oracle_search_terms import SEARCH_TERMS

CLIP_DIR = "./oracle_clips"
ORACLE_DB = "./oracle_dynamic.json"
MAX_DOWNLOADS = 3

os.makedirs(CLIP_DIR, exist_ok=True)
if not os.path.exists(ORACLE_DB):
    with open(ORACLE_DB, 'w') as f:
        json.dump([], f, indent=2)

def scrape_random_search():
    query = random.choice(SEARCH_TERMS)
    search_term = f"ytsearch{MAX_DOWNLOADS}:{query}"
    print(f"🎧 Searching: {search_term}")
    cmd = [
    "yt-dlp",
    "--extract-audio",
    "--audio-format", "mp3",
    "--output", f"{CLIP_DIR}/%(title).80s.%(ext)s",
    f"ytsearch5:{query}"
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
    print(f"📚 Oracle DB updated with {len(new_entries)} entries")

if __name__ == "__main__":
    scrape_random_search()
    new_entries = scan_downloads()
    update_oracle_db(new_entries)