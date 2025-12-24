import os
from datetime import datetime

CURRENT_PHASE_FILE = "./current_phase.txt"
SESSIONS_DIR = "./unnamed_record/sessions"
TAG_INDEX = "./fragment_index.md"
AI_CONTEXT_FILE = "./ai_content.txt"


def read_current_phase():
    if os.path.exists(CURRENT_PHASE_FILE):
        with open(CURRENT_PHASE_FILE, "r") as f:
            return f.read().strip()
    return None


def find_latest_session():
    if not os.path.exists(SESSIONS_DIR):
        return None
    sessions = [d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")]
    if not sessions:
        return None
    latest = sorted(sessions, reverse=True)[0]
    return os.path.join(SESSIONS_DIR, latest)


def get_recent_tags(count=3):
    if not os.path.exists(TAG_INDEX):
        return []
    with open(TAG_INDEX, "r") as f:
        lines = [line.strip() for line in f if "Tags:" in line]
    tags = [line.split("Tags:", 1)[-1].strip() for line in lines[-count:]]
    return tags


def get_latest_voice(session_path):
    txts = [f for f in os.listdir(session_path) if f.startswith("voice_") and f.endswith(".txt")]
    if not txts:
        return None
    latest = sorted(txts, reverse=True)[0]
    with open(os.path.join(session_path, latest), "r") as f:
        return f.readline().strip()


def build_context():
    context_lines = []

    phase = read_current_phase()
    if phase:
        context_lines.append(f"Current phase: {phase}")

    session_path = find_latest_session()
    if session_path:
        notes = os.path.join(session_path, "notes.md")
        if os.path.exists(notes):
            with open(notes, "r") as f:
                first = f.readline().strip()
            context_lines.append(f"Session: {first or os.path.basename(session_path)}")
        voice = get_latest_voice(session_path)
        if voice:
            context_lines.append(f"Latest voice snippet: {voice}")

    tags = get_recent_tags()
    if tags:
        context_lines.append("Recent tags: " + ", ".join(tags))

    timestamp = datetime.now().isoformat()
    with open(AI_CONTEXT_FILE, "w") as f:
        f.write(f"# AI Context [{timestamp}]\n")
        for line in context_lines:
            f.write(line + "\n")

    print(f"✅ AI context written to {AI_CONTEXT_FILE}")


if __name__ == "__main__":
    build_context()
