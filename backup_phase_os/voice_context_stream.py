# Voice Context Stream
# Appends latest voice transcript to reflector cache for AI integration

import os

SESSIONS_DIR = "./unnamed_record/sessions"
CACHE_FILE = "./reflector_cache.txt"

def find_latest_transcript():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    if not sessions:
        return None, None
    session_path = os.path.join(SESSIONS_DIR, sessions[0])
    transcripts = sorted([f for f in os.listdir(session_path) if f.endswith(".txt") and f.startswith("voice_")], reverse=True)
    if not transcripts:
        return None, None
    return os.path.join(session_path, transcripts[0]), sessions[0]

def inject_to_reflector():
    txt_path, session_id = find_latest_transcript()
    if not txt_path:
        print("⚠️ No voice transcript found.")
        return

    with open(txt_path, 'r') as f:
        content = f.read().strip()

    with open(CACHE_FILE, 'a') as out:
        out.write(f"\n\n# Voice Memo [{session_id}]\n{content}\n")

    print(f"🧠 Transcript injected into reflector: {txt_path}")

if __name__ == "__main__":
    inject_to_reflector()