# Builder Form Map Generator (prints + injects)
# Generates structure and saves to form map + current scratchpad

import random
from datetime import datetime
import os

SECTIONS = [
    "Intro - texture wash",
    "Verse - looped groove",
    "Chorus - sudden dynamic shift",
    "Bridge - vocal fragment slowdown",
    "Drop - negative space then impact",
    "Outro - reversed melody with silence"
]

MODIFIERS = [
    "Use only slices under 8s",
    "Layer reverb fragments behind new material",
    "Introduce reversed content gradually",
    "End on a field recording",
    "Resample your own bounce halfway through",
    "No drums for first 40 seconds"
]

stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
structure = random.sample(SECTIONS, 4)
modifier = random.choice(MODIFIERS)

map_text = f"""🎼 Builder Form Map — {stamp}

Structure:
- {structure[0]}
- {structure[1]}
- {structure[2]}
- {structure[3]}

Constraint:
→ {modifier}
"""

print("\n" + map_text)

with open("./unnamed_record/sessions/latest_form_map.md", 'w') as f:
    f.write(map_text)

# also inject into most recent session notes
SESSIONS_DIR = "./unnamed_record/sessions"
sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
if sessions:
    latest = os.path.join(SESSIONS_DIR, sessions[0], "notes.md")
    with open(latest, 'a') as f:
        f.write("\n\n## Builder Form Map\n" + map_text + "\n")