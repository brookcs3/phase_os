# Oracle Slice Logger (Hotkey Auto-Trigger)
# Monitors export folder and logs final slices with timestamp and session tag

import os
from datetime import datetime
import shutil
import keyboard
import time

EXPORT_DIR = "./oracle_slices"
SESSIONS_DIR = "./unnamed_record/sessions"
SLICE_LOG = "./fragment_index.md"
HOTKEY = "ctrl+alt+s"

os.makedirs(EXPORT_DIR, exist_ok=True)


def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    return sessions[0] if sessions else "session_unknown"

def monitor_and_log():
    files = [f for f in os.listdir(EXPORT_DIR) if f.endswith(".wav") or f.endswith(".mp3")]
    if not files:
        print("📭 No new slices found.")
        return

    latest = max(files, key=lambda x: os.path.getmtime(os.path.join(EXPORT_DIR, x)))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    session = find_latest_session()
    path = os.path.join(EXPORT_DIR, latest)

    with open(SLICE_LOG, 'a') as log:
        log.write(f"[{timestamp}] SLICE: {latest} (session: {session})\n{path}\n\n")

    print(f"✅ Logged slice: {latest} under session {session}")

print(f"🎚️ Slice logger active — press {HOTKEY} to log latest export")
keyboard.add_hotkey(HOTKEY, monitor_and_log)
keyboard.wait()
