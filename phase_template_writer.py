# Phase Template Writer
# Creates a new daily scratchpad file in the phase directory with starter content

import os
from datetime import datetime
import json

CURRENT_PHASE_FILE = "./current_phase.txt"
MOUNT_MAP_FILE = "./phase_mounts.json"

TEMPLATE = {
    "header": "# Phase Scratchpad\n",
    "structure": [
        "## Intent",
        "Write the core intention for this session.",
        "\n## Immediate Fragments",
        "List anything raw you need to catch now.",
        "\n## Live Notes",
        "Freeform zone. No pressure.\n"
    ]
}

def read_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return None
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()

def mount_path_for_phase(phase):
    if not os.path.exists(MOUNT_MAP_FILE):
        return None
    with open(MOUNT_MAP_FILE, 'r') as f:
        mapping = json.load(f)
    if phase in mapping:
        return os.path.expanduser(mapping[phase])
    return None

def create_template_file(base_path, phase):
    date_tag = datetime.now().strftime("%Y-%m-%d--%H%M")
    filename = f"scratchpad_{phase}_{date_tag}.md"
    full_path = os.path.join(base_path, filename)

    with open(full_path, 'w') as f:
        f.write(TEMPLATE["header"])
        for section in TEMPLATE["structure"]:
            f.write(section + "\n")

    print(f"📝 Created phase scratchpad: {full_path}")
    return full_path

if __name__ == "__main__":
    phase = read_current_phase()
    if phase:
        base = mount_path_for_phase(phase)
        if base:
            os.makedirs(base, exist_ok=True)
            create_template_file(base, phase)
        else:
            print("⚠️ No mount path found for phase.")
    else:
        print("⛔ No active phase detected.")
