# Archive Exporter
# Compresses Phase OS workspace into timestamped zip archive

import os
import shutil
from datetime import datetime

EXPORT_ROOT = "./archives"
EXPORT_DIR = "./"
IGNORE_DIRS = ["__pycache__", ".pids", ".git", "archives"]

os.makedirs(EXPORT_ROOT, exist_ok=True)

def archive():
    stamp = datetime.now().strftime("%Y-%m-%d--%H%M%S")
    output_name = f"phase_backup_{stamp}.zip"
    output_path = os.path.join(EXPORT_ROOT, output_name)
    print(f"📦 Creating archive: {output_path}")
    shutil.make_archive(output_path.replace(".zip", ""), 'zip', EXPORT_DIR, logger=print_filter)
    print("✅ Backup complete.")

def print_filter(path, names):
    for name in names[:]:
        if name in IGNORE_DIRS:
            names.remove(name)
    return names

if __name__ == "__main__":
    archive()
