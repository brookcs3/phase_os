# Oracle Slice Visual Logger
# Captures screenshot on slice export and logs next to audio fragment

import os
import shutil
from datetime import datetime
from PIL import ImageGrab

EXPORT_DIR = "./oracle_slices"
VISUAL_DIR = "./oracle_slices_visual"
SESSIONS_DIR = "./unnamed_record/sessions"
SLICE_LOG = "./fragment_index.md"

os.makedirs(VISUAL_DIR, exist_ok=True)


def find_latest_session():
    sessions = sorted([d for d in os.listdir(SESSIONS_DIR) if d.startswith("session_")], reverse=True)
    return sessions[0] if sessions else "session_unknown"

def log_with_visual():
    files = [f for f in os.listdir(EXPORT_DIR) if f.endswith(".wav") or f.endswith(".mp3")]
    if not files:
        print("📭 No slices found.")
        return

    latest = max(files, key=lambda x: os.path.getmtime(os.path.join(EXPORT_DIR, x)))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    session = find_latest_session()
    path = os.path.join(EXPORT_DIR, latest)

    shot_name = latest.replace(".wav", ".png").replace(".mp3", ".png")
    shot_path = os.path.join(VISUAL_DIR, shot_name)
    ImageGrab.grab().save(shot_path)

    with open(SLICE_LOG, 'a') as log:
        log.write(f"[{timestamp}] SLICE: {latest} (session: {session})\n")
        log.write(f"Audio: {path}\nVisual: {shot_path}\n\n")

    print(f"🖼️ Logged with screenshot: {shot_name}")

if __name__ == "__main__":
    log_with_visual()
