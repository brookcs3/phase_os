# Archive Exporter
# Compresses Phase OS workspace into timestamped zip archive

import os
import shutil
from zipfile import ZipFile
from datetime import datetime

EXPORT_ROOT = "./archives"
EXPORT_DIR = "./"
IGNORE_DIRS = {"__pycache__", ".pids", ".git", "archives"}

os.makedirs(EXPORT_ROOT, exist_ok=True)

def archive():
    stamp = datetime.now().strftime("%Y-%m-%d--%H%M%S") + "__scaffold_commit"
    output_name = f"phase_backup_{stamp}.zip"
    output_path = os.path.join(EXPORT_ROOT, output_name)
    print(f"📦 Creating archive: {output_path}")

    with ZipFile(output_path, 'w') as zipf:
        for root, dirs, files in os.walk(EXPORT_DIR):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                if any(ignored in root for ignored in IGNORE_DIRS):
                    continue
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, EXPORT_DIR)
                zipf.write(abs_path, rel_path)

    print("✅ Backup complete.")

if __name__ == "__main__":
    archive()
