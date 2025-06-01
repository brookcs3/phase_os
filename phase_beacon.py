# Phase Reminder Beacon
# Sends macOS notifications every 30 minutes with phase and intent

import time
import json
import os
import subprocess

CURRENT_PHASE_FILE = "./current_phase.txt"
PHASES_FILE = "./phases.json"
INTERVAL_MINUTES = 30


def read_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return None
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()


def load_phases():
    with open(PHASES_FILE, 'r') as f:
        return json.load(f)['phases']


def send_notification(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])


def run_beacon():
    print(f"🔔 Phase beacon active (every {INTERVAL_MINUTES} min)")
    while True:
        phase = read_current_phase()
        if not phase:
            time.sleep(INTERVAL_MINUTES * 60)
            continue

        phases = load_phases()
        matched = None
        for pid, info in phases.items():
            if info['name'] == phase:
                matched = info
                break

        if matched:
            intent = matched.get("intent", "No intent set.")
            send_notification(f"Phase: {phase}", intent)
        else:
            send_notification("Phase OS", f"Unrecognized phase: {phase}")

        time.sleep(INTERVAL_MINUTES * 60)


if __name__ == "__main__":
    run_beacon()
