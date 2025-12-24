# Phase Artifact Logger
# Captures user responses to prompts during each phase

import os
import time
from datetime import datetime

CURRENT_PHASE_FILE = "./current_phase.txt"
PROMPT_FILE = "./ai_context.txt"
ARTIFACT_DIR = "./phase_artifacts"

os.makedirs(ARTIFACT_DIR, exist_ok=True)

def get_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return None
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()

def get_last_prompt():
    if not os.path.exists(PROMPT_FILE):
        return None
    with open(PROMPT_FILE, 'r') as f:
        return f.read().strip()

def write_artifact(phase, prompt, response):
    phase_dir = os.path.join(ARTIFACT_DIR, phase)
    os.makedirs(phase_dir, exist_ok=True)
    timestamp = datetime.now().isoformat().replace(":", "-")
    file_path = os.path.join(phase_dir, f"{timestamp}.md")
    with open(file_path, 'w') as f:
        f.write(f"# Phase: {phase}\n")
        f.write(f"## Prompt:\n{prompt}\n")
        f.write(f"## Response:\n{response}\n")
    print(f"✅ Artifact saved to {file_path}\n")

def run_logger():
    last_prompt = None
    while True:
        phase = get_current_phase()
        prompt = get_last_prompt()
        if prompt and prompt != last_prompt:
            print(f"\n📝 New prompt detected for Phase [{phase}]:\n{prompt}")
            response = input("\nYour response: ")
            write_artifact(phase, prompt, response)
            last_prompt = prompt
        time.sleep(5)

if __name__ == "__main__":
    run_logger()
