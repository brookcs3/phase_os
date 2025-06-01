# Archive Exporter
# Compresses Phase OS workspace into timestamped zip archive

import os
import shutil
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

    shutil.make_archive(
        base_name=output_path.replace(".zip", ""),
        format='zip',
        root_dir=EXPORT_DIR
    )

    print("✅ Backup complete.")

if __name__ == "__main__":
    archive()