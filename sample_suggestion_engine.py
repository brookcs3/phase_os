# Sample Suggestion Engine
# Suggests prompts and sample source ideas based on dynamic phase, tags, session ID

import os
import random
from datetime import datetime

CURRENT_PHASE_FILE = "./current_phase.txt"
FRAGMENT_TAGS = "./fragment_index.md"
SESSIONS_DIR = "./unnamed_record/sessions"
SUGGESTION_FILE = "./sample_prompts.md"

SOURCES = [
    "Obscure VHS audio",
    "Religious field chants",
    "Vintage drum machines",
    "'90s Japanese commercials",
    "Street preacher rants",
    "Shortwave radio sweeps",
    "Home answering machines",
    "Hardcore acapella fragments",
    "Early YouTube monologues",
    "Children’s educational LPs",
    "Rusty metal field recordings"
]

TECHNIQUES = [
    "Granular time-shift",
    "Reverse resynthesis",
    "Bit-depth envelope fold",
    "Multi-layer loop smear",
    "Hard chop delay",
    "Phrase extraction then stretch",
    "Noise-floor preservation",
    "Random-start transient cuts"
]

def get_phase():
    if os.path.exists(CURRENT_PHASE_FILE):
        with open(CURRENT_PHASE_FILE, 'r') as f:
            return f.read().strip()
    return "Unknown"

def get_latest_tags():
    if not os.path.exists(FRAGMENT_TAGS):
        return []
    with open(FRAGMENT_TAGS, 'r') as f:
        return [line.split("Tags:", 1)[-1].strip() for line in f if "Tags:" in line][-3:]

def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    return sessions[0] if sessions else "session_unknown"

def suggest_samples():
    phase = get_phase()
    tags = get_latest_tags()
    session_id = find_latest_session()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    src = random.choice(SOURCES)
    tech = random.choice(TECHNIQUES)

    suggestion = f"""
## Sample Suggestion [{stamp}]
Session: {session_id}
Phase: {phase}
Tags: {', '.join(tags)}

🔊 Source Idea: {src}
🧪 Technique: {tech}
"""

    with open(SUGGESTION_FILE, 'a') as f:
        f.write(suggestion + "\n")

    print(suggestion)

if __name__ == "__main__":
    suggest_samples()
