# Bounce Logger
# Watches for new audio bounce files and logs them into the current session note

import os
import time
from datetime import datetime

BOUNCE_DIR = os.path.expanduser("~/Music/Bounces")
SESSIONS_DIR = "./unnamed_record/sessions"
EXTENSIONS = [".wav", ".aiff", ".mp3", ".flac"]

LOG_TEMPLATE = "\n## New Bounce [{timestamp}]\n{filename}\n"


def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None
    return os.path.join(SESSIONS_DIR, sessions[0], "notes.md")


def watch_bounces():
    print("🎧 Bounce logger active...")
    seen = set()
    while True:
        for fname in os.listdir(BOUNCE_DIR):
            if not any(fname.lower().endswith(ext) for ext in EXTENSIONS):
                continue
            path = os.path.join(BOUNCE_DIR, fname)
            if path not in seen:
                seen.add(path)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                note_path = find_latest_session()
                if note_path:
                    with open(note_path, 'a') as f:
                        f.write(LOG_TEMPLATE.format(timestamp=timestamp, filename=fname))
                    print(f"📥 Logged bounce: {fname}")
        time.sleep(5)

if __name__ == "__main__":
    watch_bounces()
