# Builder Form Map Generator (prints + injects + versions)
# Generates structure, saves to scratchpad, and snapshots version

import random
from datetime import datetime
import os
import hashlib

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

form_path = "./unnamed_record/sessions/latest_form_map.md"
with open(form_path, 'w') as f:
    f.write(map_text)

# Inject into session notes
SESSIONS_DIR = "./unnamed_record/sessions"
sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
if sessions:
    latest = os.path.join(SESSIONS_DIR, sessions[0], "notes.md")
    with open(latest, 'a') as f:
        f.write("\n\n## Builder Form Map\n" + map_text + "\n")

# Auto-version
ARCHIVE_DIR = os.path.join(SESSIONS_DIR, "form_versions")
os.makedirs(ARCHIVE_DIR, exist_ok=True)

hash_id = hashlib.md5(map_text.encode()).hexdigest()[:6]
stamp_id = datetime.now().strftime("%Y-%m-%d--%H%M%S")
version_path = os.path.join(ARCHIVE_DIR, f"form_{stamp_id}__{hash_id}.md")
with open(version_path, 'w') as f:
    f.write(map_text)
print(f"📌 Versioned form map: {version_path}")
