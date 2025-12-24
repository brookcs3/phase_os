# Oracle Playlist Miner
# Searches YouTube for crate-style playlist URLs and saves them to a seed list

import subprocess
import re
import random
from datetime import datetime

SEARCH_TERMS = [
    "rare vinyl funk full album",
    "obscure soul compilation",
    "japanese city pop vinyl playlist",
    "italian horror soundtrack full tape",
    "library music full album",
    "70s gospel soul mix",
    "rare field recording LP",
    "experimental jazz 70s playlist"
]

PLAYLISTS_FILE = "./oracle_playlists.txt"

YDL_TEMPLATE = [
    "yt-dlp",
    "ytsearch10:{}",
    "--flat-playlist",
    "--print", "%(url)s"
]

found = []
print("🔍 Mining playlists from YouTube search...")

for query in random.sample(SEARCH_TERMS, k=3):
    print(f"🔎 Searching: {query}")
    cmd = ["yt-dlp", f"ytsearch10:{query}", "--flat-playlist", "--print", "%(url)s"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    matches = re.findall(r"https://www\.youtube\.com/playlist\?list=[^\s]+", result.stdout)
    found.extend(matches)

if found:
    with open(PLAYLISTS_FILE, 'a') as f:
        for url in found:
            f.write(url + "\n")
    print(f"✅ Mined {len(found)} playlist links saved to {PLAYLISTS_FILE}")
else:
    print("⚠️ No new playlists found.")
