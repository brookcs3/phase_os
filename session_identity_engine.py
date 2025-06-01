# Session Identity Engine
# Derives a working identity tag from latest phase, tags, and voice transcript to name the session direction

import os
from datetime import datetime

IDENTITY_FILE = "./current_session_identity.txt"

SESSIONS_DIR = "./unnamed_record/sessions"
FRAGMENT_TAGS = "./fragment_index.md"

def find_latest_session():
    """Return the latest session identifier and path if available."""
    if not os.path.exists(SESSIONS_DIR):
        return None, None
    sessions = sorted(
        [d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")],
        reverse=True,
    )
    if not sessions:
        return None, None
    session_id = sessions[0]
    path = os.path.join(SESSIONS_DIR, session_id)
    return session_id, path

def extract_tags():
    if not os.path.exists(FRAGMENT_TAGS):
        return []
    with open(FRAGMENT_TAGS, 'r') as f:
        lines = [line.strip() for line in f if "Tags:" in line]
    return [line.split("Tags:", 1)[-1].strip() for line in lines[-5:]]

def extract_voice(session_path):
    """Return the latest voice transcription snippet if available."""
    if not os.path.exists(session_path):
        return ""
    txts = sorted(
        [f for f in os.listdir(session_path) if f.startswith("voice_") and f.endswith(".txt")],
        reverse=True,
    )
    if not txts:
        return ""
    with open(os.path.join(session_path, txts[0]), "r") as f:
        return f.read().strip()

def synthesize_identity(voice_snippet, tags):
    parts = []
    if tags:
        keyword = tags[-1].split(",")[0].strip()
        parts.append(keyword)
    if voice_snippet:
        words = voice_snippet.split()
        if words:
            parts.append(words[0].lower())
    time_hash = datetime.now().strftime("%H%M")
    return "_".join(filter(None, parts)) + f"_{time_hash}"

def tag_session_identity():
    session_id, path = find_latest_session()
    if not session_id:
        print("⛔ No session found.")
        return
    tags = extract_tags()
    voice = extract_voice(path)
    identity = synthesize_identity(voice, tags)
    with open(os.path.join(path, "notes.md"), 'a') as f:
        f.write(f"\n## Session Identity\n{identity}\n")

    # Store identity for consumption by other modules
    with open(IDENTITY_FILE, "w") as f:
        f.write(identity)

    print(f"🧬 Session identity tagged: {identity}")

if __name__ == "__main__":
    tag_session_identity()
