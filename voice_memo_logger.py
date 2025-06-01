# Voice Memo Logger
# Records a short voice memo and links it to the current session

import os
import subprocess
from datetime import datetime

SESSIONS_DIR = "./unnamed_record/sessions"
MEMO_DURATION = 30  # seconds


def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None
    return os.path.join(SESSIONS_DIR, sessions[0])


def record_memo():
    session_path = find_latest_session()
    if not session_path:
        print("⛔ No session found.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d--%H%M%S")
    filename = f"voice_{timestamp}.m4a"
    filepath = os.path.join(session_path, filename)

    print(f"🎙️ Recording voice memo for {MEMO_DURATION} seconds...")
    subprocess.run([
        "ffmpeg",
        "-f", "avfoundation",
        "-i", ":0",
        "-t", str(MEMO_DURATION),
        filepath
    ])

    notes_path = os.path.join(session_path, "notes.md")
    with open(notes_path, 'a') as f:
        f.write(f"\n## Voice Memo [{timestamp}]\n{filename}\n")

    print(f"✅ Voice memo saved and linked: {filepath}")
    subprocess.run(["python3", "voice_transcriber.py"])

if __name__ == "__main__":
    record_memo()
