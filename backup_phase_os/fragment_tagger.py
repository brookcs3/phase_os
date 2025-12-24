# Fragment Tagger
# Prompts user to tag fragments created in the current session

import os
from datetime import datetime

SESSIONS_DIR = "./unnamed_record/sessions"
TAG_FILE = "./fragment_index.md"

def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None
    return os.path.join(SESSIONS_DIR, sessions[0], "notes.md"), sessions[0]

def tag_fragment():
    note_path, session_id = find_latest_session()
    if not note_path:
        print("⛔ No session found.")
        return

    print("🎛️ Tag your latest fragment(s):")
    tag_input = input("Enter tags (comma-separated): ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(note_path, 'a') as f:
        f.write(f"\n## Fragment Tags [{timestamp}]\n{tag_input}\n")

    with open(TAG_FILE, 'a') as idx:
        idx.write(f"[{timestamp}] Session: {session_id} — Tags: {tag_input}\n")

    print("✅ Tags added.")

if __name__ == "__main__":
    tag_fragment()