# Oracle Remix Session Launcher
# Loads all saved fragments from log and prepares a remix session folder

import os
import shutil
import re
from datetime import datetime

FRAG_INDEX = "./fragment_index.md"
REMIX_DIR = f"./remix_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
SLICE_DIR = "./oracle_slices"

def extract_fragment_paths():
    if not os.path.exists(FRAG_INDEX):
        return []
    with open(FRAG_INDEX, 'r') as f:
        lines = f.readlines()
    paths = [line.strip() for line in lines if line.startswith("Audio: ")]
    return [line.replace("Audio: ", "").strip() for line in paths if os.path.exists(line.replace("Audio: ", "").strip())]

def build_remix_session():
    os.makedirs(REMIX_DIR, exist_ok=True)
    fragments = extract_fragment_paths()
    for path in fragments:
        basename = os.path.basename(path)
        shutil.copy(path, os.path.join(REMIX_DIR, basename))
    print(f"🎛️ Remix session created at: {REMIX_DIR}")
    print(f"🔗 Included {len(fragments)} fragments")

if __name__ == "__main__":
    build_remix_session()
