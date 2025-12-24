# Voice Memo Transcriber
# Converts latest voice memo to text using OpenAI Whisper CLI

import os
import subprocess
from datetime import datetime

SESSIONS_DIR = "./unnamed_record/sessions"


def find_latest_voice(session_path):
    files = sorted([f for f in os.listdir(session_path) if f.startswith("voice_") and f.endswith(".m4a")], reverse=True)
    if not files:
        return None
    return os.path.join(session_path, files[0])

def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None
    return os.path.join(SESSIONS_DIR, sessions[0])

def transcribe():
    session_path = find_latest_session()
    if not session_path:
        print("⛔ No session found.")
        return
    memo_path = find_latest_voice(session_path)
    if not memo_path:
        print("⚠️ No voice memo found.")
        return

    print(f"🔊 Transcribing: {memo_path}")
    subprocess.run(["whisper", memo_path, "--language", "en", "--model", "base", "--output_format", "txt"])

    txt_file = memo_path.replace(".m4a", ".txt")
    if os.path.exists(txt_file):
        with open(txt_file, 'r') as tf:
            transcript = tf.read().strip()
        with open(os.path.join(session_path, "notes.md"), 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"\n## Voice Memo Transcript [{timestamp}]\n{transcript}\n")
        print("✅ Transcript appended to session notes.")
    else:
        print("❌ Transcription file not found.")

if __name__ == "__main__":
    transcribe()
