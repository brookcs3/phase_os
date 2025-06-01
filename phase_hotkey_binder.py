# Phase Hotkey Binder (Mac only)
# Binds global hotkeys to switch phases via keyboard shortcuts

import keyboard
import json
import os

PHASES_FILE = "./phases.json"
CURRENT_PHASE_FILE = "./current_phase.txt"

with open(PHASES_FILE, 'r') as f:
    PHASES = json.load(f)['phases']

HOTKEYS = {
    'cmd+alt+1': '1',
    'cmd+alt+2': '2',
    'cmd+alt+3': '3',
    'cmd+alt+4': '4'
}

def switch_phase(phase_id):
    if phase_id not in PHASES:
        print(f"Unknown phase ID: {phase_id}")
        return
    name = PHASES[phase_id]['name']
    with open(CURRENT_PHASE_FILE, 'w') as f:
        f.write(name)
    print(f"🌐 Switched to phase: {name} (via hotkey)")

def bind_hotkeys():
    for combo, phase_id in HOTKEYS.items():
        keyboard.add_hotkey(combo, lambda pid=phase_id: switch_phase(pid))
    print("🎛️ Hotkeys bound: ⌘⌥1-4 → switch phases")
    keyboard.wait()

if __name__ == "__main__":
    bind_hotkeys()
