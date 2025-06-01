# Phase Companion Daemon
# Watches current phase and injects prompts or nudges accordingly

import time
import os
from datetime import datetime

CURRENT_PHASE_FILE = "./current_phase.txt"
LOG_FILE = "./daemon_log.txt"
PROMPT_FILE = "./ai_context.txt"

last_phase = None

PROMPTS = {
    "Generator": [
        "What pattern are you unraveling right now?",
        "Leave behind one fragment. A sentence, a symbol, a sketch.",
        "What loop are you caught in that you didn’t notice until now?"
    ],
    "Executor": [
        "What are you delivering today? One clean unit.",
        "Close a loop. Pick one. It doesn’t have to be the right one.",
        "Where are you holding back? Ship past it."
    ],
    "Recovery": [
        "Stop typing. Listen. Reset your signal.",
        "What silence can you log right now?",
        "If this is the end of a loop, what did it leave behind?"
    ],
    "Builder": [
        "Which two fragments want to connect today?",
        "Turn sketches into prototypes. What’s the spine?",
        "Can you collapse one idea into a system?"
    ]
}

def read_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return None
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()

def write_prompt(phase, prompt):
    timestamp = datetime.now().isoformat()
    with open(PROMPT_FILE, 'w') as f:
        f.write(f"[{timestamp}] Phase: {phase}\n{prompt}\n")
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{timestamp}] Phase: {phase} >> {prompt}\n")
    print(f"\n🧭 Phase Nudge [{phase}]: {prompt}\n")

def loop():
    global last_phase
    while True:
        current_phase = read_phase()
        if current_phase and current_phase != last_phase:
            last_phase = current_phase
            if current_phase in PROMPTS:
                prompt = PROMPTS[current_phase][datetime.now().second % len(PROMPTS[current_phase])]
                write_prompt(current_phase, prompt)
        time.sleep(10)

if __name__ == "__main__":
    loop()
