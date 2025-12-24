# Phase OS Dashboard — Status Overview
# Visual terminal UI of all systems and last interaction timestamps

import os
from datetime import datetime
import time

WATCH = {
    "Current Phase": "./current_phase.txt",
    "Last Digest": "./loop_digest_weekly.md",
    "Last Voice Memo": "./unnamed_record/sessions/",
    "Last Moodboard": "./moodboard_log.md",
    "Oracle DB": "./oracle_dynamic.json",
    "Oracle Playlists": "./oracle_playlists.txt",
    "Fragment Index": "./fragment_index.md",
    "Reflector Cache": "./reflector_cache.txt"
}


def get_latest_timestamp(path):
    if not os.path.exists(path):
        return "—"
    if os.path.isdir(path):
        files = [os.path.getmtime(os.path.join(path, f)) for f in os.listdir(path) if f.startswith("session_")]
        return datetime.fromtimestamp(max(files)).strftime("%Y-%m-%d %H:%M") if files else "—"
    return datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M")


def display():
    os.system("clear")
    print("🧠 PHASE OS — SYSTEM DASHBOARD\n")
    for label, path in WATCH.items():
        print(f"{label:20} ⟶ {get_latest_timestamp(path)}")
    print("\n(Refreshes every 15s — Ctrl+C to exit)")

if __name__ == "__main__":
    while True:
        display()
        time.sleep(15)