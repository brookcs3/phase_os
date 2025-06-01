# Phase Trigger Engine
# Executes pre-defined actions upon phase entry

import json
import os
import subprocess
import time

TRIGGERS_FILE = "./phase_triggers.json"
CURRENT_PHASE_FILE = "./current_phase.txt"
TRIGGER_STATE_FILE = "./.last_triggered_phase"

if not os.path.exists(TRIGGERS_FILE):
    with open(TRIGGERS_FILE, 'w') as f:
        json.dump({}, f)

def load_triggers():
    with open(TRIGGERS_FILE, 'r') as f:
        return json.load(f)

def read_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return None
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()

def read_last_triggered():
    if not os.path.exists(TRIGGER_STATE_FILE):
        return None
    with open(TRIGGER_STATE_FILE, 'r') as f:
        return f.read().strip()

def write_last_triggered(phase):
    with open(TRIGGER_STATE_FILE, 'w') as f:
        f.write(phase)

def execute_commands(commands):
    for cmd in commands:
        print(f"⚡ Triggering: {cmd}")
        subprocess.Popen(cmd, shell=True)
    print("🔁 Injecting updated cognitive context to AI...")
    subprocess.Popen(["python3", "context_injector.py"])

def trigger_phase_actions():
    triggers = load_triggers()
    current = read_current_phase()
    last = read_last_triggered()
    if current and current != last:
        if current in triggers:
            execute_commands(triggers[current])
        else:
            execute_commands([])
        write_last_triggered(current)

def run_loop():
    print("⏳ Trigger engine active...")
    while True:
        trigger_phase_actions()
        time.sleep(5)

if __name__ == "__main__":
    run_loop()
