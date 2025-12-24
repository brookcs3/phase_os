# Archive Browser
# Lists available zip snapshots and lets user view contents or extract them

import os
import zipfile

ARCHIVE_DIR = "./archives"


def list_archives():
    return sorted([f for f in os.listdir(ARCHIVE_DIR) if f.endswith(".zip")], reverse=True)

def browse():
    archives = list_archives()
    if not archives:
        print("⛔ No archives found.")
        return

    print("📁 Available Archives:")
    for i, name in enumerate(archives):
        print(f" {i}: {name}")

    choice = input("\nSelect archive by number: ").strip()
    if not choice.isdigit() or int(choice) >= len(archives):
        print("❌ Invalid choice.")
        return

    selected = os.path.join(ARCHIVE_DIR, archives[int(choice)])
    with zipfile.ZipFile(selected, 'r') as zip_ref:
        print(f"\n📦 Archive contains:")
        for name in zip_ref.namelist():
            print("  •", name)

        extract = input("\nExtract this archive? (y/n): ").strip().lower()
        if extract == 'y':
            extract_path = os.path.join(ARCHIVE_DIR, archives[int(choice)].replace(".zip", "_extracted"))
            zip_ref.extractall(extract_path)
            print(f"✅ Extracted to: {extract_path}")

if __name__ == "__main__":
    browse()