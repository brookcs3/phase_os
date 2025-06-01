# Mic Preset Router
# Routes ffmpeg mic settings based on current phase

import os
from datetime import datetime
import subprocess
import json

CURRENT_PHASE_FILE = "./current_phase.txt"
SESSIONS_DIR = "./unnamed_record/sessions"
PRESET_FILE = "./mic_presets.json"
DEFAULT_DURATION = 30

DEFAULT_PRESETS = {
    "Generator": ["-f", "avfoundation", "-i", ":0", "-acodec", "aac"],
    "Builder": ["-f", "avfoundation", "-i", ":0", "-acodec", "aac", "-ar", "44100"],
    "Executor": ["-f", "avfoundation", "-i", ":0", "-acodec", "aac", "-b:a", "64k"],
    "Recovery": ["-f", "avfoundation", "-i", ":0", "-af", "aecho=0.8:0.88:60:0.4"]
}

if not os.path.exists(PRESET_FILE):
    with open(PRESET_FILE, 'w') as f:
        json.dump(DEFAULT_PRESETS, f, indent=2)

def get_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return "Generator"
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()

def get_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    return os.path.join(SESSIONS_DIR, sessions[0]) if sessions else None

def run_record():
    phase = get_phase()
    session = get_session()
    if not session:
        print("⛔ No active session.")
        return
    filename = f"voice_{datetime.now().strftime('%Y-%m-%d--%H%M%S')}.m4a"
    filepath = os.path.join(session, filename)

    with open(PRESET_FILE, 'r') as f:
        presets = json.load(f)
    args = presets.get(phase, DEFAULT_PRESETS["Generator"])

    print(f"🎤 Recording memo ({phase} preset) to {filepath}...")
    subprocess.run(["ffmpeg"] + args + ["-t", str(DEFAULT_DURATION), filepath])

    with open(os.path.join(session, "notes.md"), 'a') as f:
        f.write(f"\n## Voice Memo ({phase})\n{filename}\n")

    subprocess.run(["python3", "voice_transcriber.py"])

if __name__ == "__main__":
    run_record()
