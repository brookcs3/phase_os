# Oracle Moodboard Generator
# Creates and appends sonic prompts to session notes and global moodboard log

import random
from datetime import datetime
import os

SESSIONS_DIR = "./unnamed_record/sessions"
MOOD_LOG = "./moodboard_log.md"

def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    return os.path.join(SESSIONS_DIR, sessions[0]) if sessions else None

themes = [
    "broken machine anthem", "memory glitched prayer", "tape-smeared grief loop",
    "drone for unspoken language", "rituals lost in radio fog", "detuned hope signal",
    "percussive anxiety burst", "echo of forgotten rave", "monotonic joy decay"
]

textures = [
    "grimy horns", "dead vinyl crackle", "field tape hiss", "glitched choir",
    "shortwave sweeps", "low fidelity piano thumps", "static-covered breakbeats"
]

verbs = [
    "stretched", "granulated", "choked", "decomposed", "reversed", "smeared",
    "fractured", "drained", "lowpassed", "compressed to oblivion"
]

structure = [
    "no drums, just rising loops", "loops that forget themselves", 
    "breaks that implode on entry", "samples that never fully start",
    "only sound and feedback, no beat", "vocal that loops too late"
]

stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
theme = random.choice(themes)
texture = random.choice(textures)
action = random.choice(verbs)
form = random.choice(structure)

prompt = f"""🎧 Sonic Moodboard — {stamp}

Theme: {theme}
Source Texture: {texture}, {action}
Form: {form}\n"""

print(prompt)

latest = find_latest_session()
if latest:
    with open(os.path.join(latest, "notes.md"), 'a') as f:
        f.write(f"\n## Sonic Moodboard\n{prompt}\n")
with open(MOOD_LOG, 'a') as log:
    log.write(f"{prompt}\n")
