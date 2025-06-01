# Session Artifact Linker
# Adds DAW project file path to the session notes for cross-traceability

import os
from datetime import datetime

SESSIONS_DIR = "./unnamed_record/sessions"
DAW_PROJECT_PATH = os.path.expanduser("~/Music/Logic/CurrentSession.logicx")


def find_latest_session():
    if not os.path.exists(SESSIONS_DIR):
        return None
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None
    return os.path.join(SESSIONS_DIR, sessions[0], "notes.md")


def append_daw_link(note_path):
    with open(note_path, 'a') as f:
        f.write(f"\n## Linked Project\n{DAW_PROJECT_PATH}\n")
    print(f"🔗 Linked DAW session to {note_path}")

if __name__ == "__main__":
    latest_note = find_latest_session()
    if latest_note and os.path.exists(DAW_PROJECT_PATH):
        append_daw_link(latest_note)
    else:
        print("⚠️ No session note or project path found.")
