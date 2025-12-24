# Phase Mounter
# Maps each phase to a filesystem path and opens it accordingly

import os
import subprocess
import json

CURRENT_PHASE_FILE = "./current_phase.txt"
MOUNT_MAP_FILE = "./phase_mounts.json"

DEFAULT_MOUNTS = {
    "Generator": "~/Projects/Ideas",
    "Builder": "~/Workspaces/Prototypes",
    "Executor": "~/Deliverables",
    "Recovery": "~/Ambient/Logs/Audio"
}

if not os.path.exists(MOUNT_MAP_FILE):
    with open(MOUNT_MAP_FILE, 'w') as f:
        json.dump(DEFAULT_MOUNTS, f, indent=2)

def read_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return None
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()

def mount_path_for_phase(phase):
    with open(MOUNT_MAP_FILE, 'r') as f:
        mapping = json.load(f)
    if phase in mapping:
        return os.path.expanduser(mapping[phase])
    return None

def open_directory(path):
    if os.path.exists(path):
        subprocess.Popen(["open", path])
        print(f"📁 Opened directory: {path}")
    else:
        print(f"❌ Path not found: {path}")

if __name__ == "__main__":
    phase = read_current_phase()
    if phase:
        target = mount_path_for_phase(phase)
        if target:
            open_directory(target)
        else:
            print(f"⚠️ No mount path defined for phase: {phase}")
    else:
        print("⛔ No current phase set.")
