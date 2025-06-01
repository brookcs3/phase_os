# Session Identity Logger
# Appends current session ID to scratchpad + logbook

import os
from datetime import datetime

SESSIONS_DIR = "./unnamed_record/sessions"
LOGBOOK = "./unnamed_record/logbook.md"

session_identity = "rusted_i_1300"

def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None, None
    sid = sessions[0]
    return sid, os.path.join(SESSIONS_DIR, sid)

sid, path = find_latest_session()
if path:
    notes = os.path.join(path, "notes.md")
    with open(notes, 'a') as f:
        f.write(f"\n## Auto Identity\n{session_identity}\n")
    with open(LOGBOOK, 'a') as f:
        f.write(f"[{datetime.now().isoformat()}] → {session_identity} → {sid}\n")
    print(f"✅ Session '{session_identity}' logged under: {sid}")
else:
    print("⛔ No active session found.")
