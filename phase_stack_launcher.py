# Phase System Stack Launcher (Local Cognitive OS)
# Author: You (with recursive AI reflection)
# Runtime: Python 3.10+

import json
import os
import datetime
import subprocess

PHASES_FILE = "./phases.json"
LOG_DIR = "./phase_logs"
CURRENT_PHASE_FILE = "./current_phase.txt"
AI_PROMPT_FILE = "./ai_context.txt"

os.makedirs(LOG_DIR, exist_ok=True)

def load_phases():
    with open(PHASES_FILE, 'r') as f:
        return json.load(f)['phases']

def log_phase_entry(phase_name):
    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    log_entry = f"[{timestamp}] ENTERED PHASE: {phase_name}\n"
    with open(CURRENT_PHASE_FILE, 'w') as f:
        f.write(phase_name)
    with open(os.path.join(LOG_DIR, f"{phase_name}_{timestamp}.log"), 'w') as f:
        f.write(log_entry)
    print(f"\n🌀 Switched to PHASE: {phase_name}\n")
    with open(AI_PROMPT_FILE, 'w') as f:
        f.write(f"You are currently in Phase: {phase_name}\nRespond accordingly.")

def choose_phase():
    phases = load_phases()
    print("\n🔮 Available Phases:")
    for pid, phase in phases.items():
        print(f" {pid}: {phase['name']} — {phase['intent']}")
    selected = input("\nEnter phase number to enter: ").strip()
    if selected not in phases:
        print("Invalid choice.")
        return None
    phase_name = phases[selected]['name']
    log_phase_entry(phase_name)
    return phase_name

def launch_dolphin_mixtral():
    print("\n✨ Launching Dolphin-Mixtral with Phase context...")
    subprocess.run(["ollama", "run", "dolphin-mixtral"])

if __name__ == "__main__":
    print("\n🧠 Phase System Stack — Cognitive OS")
    phase = choose_phase()
    if phase is not None:
        launch = input("\nLaunch AI Companion with phase context? (y/n): ").strip().lower()
        if launch == 'y':
            launch_dolphin_mixtral()
