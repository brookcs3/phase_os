# Session Overlay
# Displays current session identity and moodboard in a persistent terminal banner

import os
import time

SESSIONS_DIR = "./unnamed_record/sessions"


def get_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None
    return os.path.join(SESSIONS_DIR, sessions[0], "notes.md")


def extract_last_block(note_path, header):
    if not os.path.exists(note_path):
        return None
    with open(note_path, 'r') as f:
        lines = f.readlines()
    block = []
    capturing = False
    for line in reversed(lines):
        if line.strip().startswith("## ") and capturing:
            break
        if header in line:
            capturing = True
        if capturing:
            block.insert(0, line.strip())
    return "\n".join(block) if block else None


def show_overlay():
    while True:
        os.system("clear")
        note_path = get_latest_session()
        identity = extract_last_block(note_path, "Session Identity")
        mood = extract_last_block(note_path, "Sonic Moodboard")

        print("🧬 PHASE OS — SESSION OVERLAY\n")
        if identity:
            print(identity + "\n")
        if mood:
            print(mood + "\n")
        print("(press Ctrl+C to exit)")
        time.sleep(10)

if __name__ == "__main__":
    show_overlay()
