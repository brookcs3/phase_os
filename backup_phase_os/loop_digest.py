# Weekly Loop Digest
# Compiles a markdown report of all sessions, tags, and bounces from the past 7 days

import os
from datetime import datetime, timedelta

SESSIONS_DIR = "./unnamed_record/sessions"
TAG_FILE = "./fragment_index.md"
TELEMETRY_LOG = "./phase_telemetry.log"
DIGEST_PATH = "./loop_digest_weekly.md"

cutoff = datetime.now() - timedelta(days=7)

def collect_sessions():
    output = []
    for session in sorted(os.listdir(SESSIONS_DIR)):
        path = os.path.join(SESSIONS_DIR, session, "notes.md")
        if not os.path.exists(path):
            continue
        timestamp = session.replace("session_", "")
        try:
            session_time = datetime.strptime(timestamp, "%Y-%m-%d--%H%M%S")
        except:
            continue
        if session_time >= cutoff:
            with open(path, 'r') as f:
                output.append((session_time, f.read()))
    return output

def collect_tags():
    if not os.path.exists(TAG_FILE):
        return []
    with open(TAG_FILE, 'r') as f:
        lines = [line for line in f.readlines() if line.strip()]
    return [line for line in lines if datetime.strptime(line[1:20], "%Y-%m-%d %H:%M") >= cutoff]

def collect_telemetry():
    if not os.path.exists(TELEMETRY_LOG):
        return []
    with open(TELEMETRY_LOG, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip() and datetime.fromisoformat(line[1:20]) >= cutoff]

def generate_digest():
    sessions = collect_sessions()
    tags = collect_tags()
    telemetry = collect_telemetry()

    with open(DIGEST_PATH, 'w') as f:
        f.write(f"# Weekly Loop Digest — {datetime.now().strftime('%Y-%m-%d')}\n\n")

        f.write("## 🧠 Session Notes\n\n")
        for ts, content in sessions:
            f.write(f"### Session {ts.isoformat()}\n{content}\n\n")

        f.write("## 🏷️ Fragment Tags\n\n")
        for tag in tags:
            f.write(f"{tag}\n")

        f.write("\n## ⏳ Phase Timeline\n\n")
        for line in telemetry:
            f.write(f"{line}\n")

    print(f"📄 Digest generated: {DIGEST_PATH}")

if __name__ == "__main__":
    generate_digest()
