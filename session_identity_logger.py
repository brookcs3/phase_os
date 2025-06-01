# Session Identity Logger
# Appends current session ID to scratchpad + logbook

import os
from datetime import datetime

SESSIONS_DIR = "./unnamed_record/sessions"
LOGBOOK = "./unnamed_record/logbook.md"
IDENTITY_FILE = "./current_session_identity.txt"

def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None, None
    sid = sessions[0]
    return sid, os.path.join(SESSIONS_DIR, sid)

def read_identity():
    if not os.path.exists(IDENTITY_FILE):
        return None
    with open(IDENTITY_FILE, "r") as f:
        return f.read().strip()

sid, path = find_latest_session()
identity = read_identity()

if path and identity:
    notes = os.path.join(path, "notes.md")
    with open(notes, 'a') as f:
        f.write(f"\n## Auto Identity\n{identity}\n")
    with open(LOGBOOK, 'a') as f:
        f.write(f"[{datetime.now().isoformat()}] → {identity} → {sid}\n")
    print(f"✅ Session '{identity}' logged under: {sid}")
elif not path:
    print("⛔ No active session found.")
else:
    print("⛔ No session identity generated.")

