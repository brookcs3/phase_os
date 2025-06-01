# Oracle Seed Engine
# Scrapes YouTube playlists for vinyl archive content and builds a starter DB

import subprocess
import os
import json
from datetime import datetime

PLAYLISTS = [
    # Add more vinyl-themed playlist links here
    "https://www.youtube.com/playlist?list=PL5E1C4554C04C79DD",  # Sample: obscure funk vinyl rips
    "https://www.youtube.com/playlist?list=PLk2C_fmFww40pUqC8k98IuVo0xr7Oyoxr"   # Sample: deep crate psych/funk
]

ORACLE_DB = "./oracle_dynamic.json"
CLIP_DIR = "./oracle_clips"

os.makedirs(CLIP_DIR, exist_ok=True)
if not os.path.exists(ORACLE_DB):
    with open(ORACLE_DB, 'w') as f:
        json.dump([], f, indent=2)

def scrape_playlist(url):
    print(f"📼 Scraping: {url}")
    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--playlist-end", "5",
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
            "highlight": "Find a weird moment manually",
            "suggestion": "Try hard slicing then layering it into a non-rhythmic pattern"
        })
    return entries


def update_oracle_db(new_entries):
    with open(ORACLE_DB, 'r') as f:
        existing = json.load(f)
    merged = existing + [e for e in new_entries if e not in existing]
    with open(ORACLE_DB, 'w') as f:
        json.dump(merged, f, indent=2)
    print(f"🧠 Oracle DB updated with {len(new_entries)} new entries.")

if __name__ == "__main__":
    for url in PLAYLISTS:
        scrape_playlist(url)
    new_entries = scan_downloads()
    update_oracle_db(new_entries)
