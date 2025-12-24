# Phase OS Exporter
# Creates a compressed archive of the entire Phase OS system

import os
from zipfile import ZipFile
from datetime import datetime

EXPORT_ROOT = "./archives"
EXPORT_DIR = "./"
IGNORE_DIRS = {"__pycache__", ".pids", ".git", "archives"}


def export_system():
    os.makedirs(EXPORT_ROOT, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d--%H%M%S")
    output_name = f"phase_os_export_{stamp}.zip"
    output_path = os.path.join(EXPORT_ROOT, output_name)
    print(f"🧠 Creating full export: {output_path}")

    with ZipFile(output_path, 'w') as zipf:
        for root, dirs, files in os.walk(EXPORT_DIR):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                if any(ignored in root for ignored in IGNORE_DIRS):
                    continue
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, EXPORT_DIR)
                zipf.write(abs_path, rel_path)

    print("✅ Full system export complete.")


if __name__ == "__main__":
    export_system()
