import os
from datetime import datetime

SESSIONS_DIR = "./unnamed_record/sessions"


def start_session():
    os.makedirs(SESSIONS_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d--%H%M%S")
    session_path = os.path.join(SESSIONS_DIR, f"session_{stamp}")
    os.makedirs(session_path, exist_ok=True)

    notes_path = os.path.join(session_path, "notes.md")
    with open(notes_path, "w") as f:
        f.write(f"# Session {stamp}\n")

    print(f"🆕 Session created: {session_path}")
    return session_path


if __name__ == "__main__":
    start_session()
