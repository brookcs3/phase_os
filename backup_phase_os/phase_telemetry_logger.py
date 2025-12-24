# Phase Telemetry Logger
# Captures time spent in each phase and logs transitions with duration

import os
import time
from datetime import datetime

CURRENT_PHASE_FILE = "./current_phase.txt"
TELEMETRY_LOG = "./phase_telemetry.log"

last_phase = None
start_time = None

def read_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return None
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()

def log_phase_duration(phase, start, end):
    duration = end - start
    with open(TELEMETRY_LOG, 'a') as f:
        f.write(f"[{start.isoformat()}] → [{end.isoformat()}] PHASE: {phase} | Duration: {duration}\n")
    print(f"🧭 Logged {phase} phase — Duration: {duration}")

def run_telemetry():
    global last_phase, start_time
    print("📡 Telemetry logger running...")
    while True:
        current = read_current_phase()
        now = datetime.now()
        if current != last_phase:
            if last_phase and start_time:
                log_phase_duration(last_phase, start_time, now)
            last_phase = current
            start_time = now
        time.sleep(5)

if __name__ == "__main__":
    run_telemetry()
