# Phase Loop Compiler
# Merges artifacts, phase logs, and daemon prompts into a single narrative snapshot

import os
from datetime import datetime

CURRENT_PHASE_FILE = "./current_phase.txt"
LOG_DIR = "./phase_logs"
ARTIFACT_DIR = "./phase_artifacts"
DAEMON_LOG = "./daemon_log.txt"
OUTPUT_DIR = "./compiled_loops"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_current_phase():
    if not os.path.exists(CURRENT_PHASE_FILE):
        return None
    with open(CURRENT_PHASE_FILE, 'r') as f:
        return f.read().strip()

def collect_files(directory, filter_ext=None):
    entries = []
    for root, _, files in os.walk(directory):
        for file in sorted(files):
            if not filter_ext or file.endswith(filter_ext):
                with open(os.path.join(root, file), 'r') as f:
                    entries.append((file, f.read().strip()))
    return entries

def compile_loop():
    phase = get_current_phase()
    if not phase:
        print("No active phase found.")
        return

    timestamp = datetime.now().isoformat().replace(":", "-")
    output_file = os.path.join(OUTPUT_DIR, f"loop_{phase}_{timestamp}.md")

    with open(output_file, 'w') as out:
        out.write(f"# Phase Loop Summary: {phase}\n\n")

        out.write("## 🔹 Phase Entry Logs\n\n")
        logs = collect_files(LOG_DIR)
        for fname, content in logs:
            if phase in fname:
                out.write(f"### {fname}\n{content}\n\n")

        out.write("## 🔸 Daemon Nudges\n\n")
        if os.path.exists(DAEMON_LOG):
            with open(DAEMON_LOG, 'r') as f:
                lines = [line for line in f.readlines() if f"Phase: {phase}" in line]
                out.writelines(lines)
                out.write("\n")

        out.write("## 📝 Artifacts\n\n")
        artifacts = collect_files(os.path.join(ARTIFACT_DIR, phase), filter_ext=".md")
        for fname, content in artifacts:
            out.write(f"### {fname}\n{content}\n\n")

    print(f"✅ Compiled loop saved to {output_file}")

if __name__ == "__main__":
    compile_loop()
