# Archive Diff Summarizer
# Compares two extracted archives and summarizes changed files and key diffs

import os
import difflib
from datetime import datetime

ARCHIVE_DIR = "./archives"


def select_archive_path(prompt):
    folders = sorted([f for f in os.listdir(ARCHIVE_DIR) if f.endswith("_extracted")], reverse=True)
    if not folders:
        print(f"⛔ No extracted folders in {ARCHIVE_DIR}.")
        return None

    print(f"📁 {prompt}")
    for i, name in enumerate(folders):
        print(f" {i}: {name}")

    choice = input("Select index: ").strip()
    if not choice.isdigit() or int(choice) >= len(folders):
        print("❌ Invalid selection.")
        return None

    return os.path.join(ARCHIVE_DIR, folders[int(choice)])


def compare_files(base_path, new_path):
    differences = []
    for root, _, files in os.walk(new_path):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), new_path)
            new_file = os.path.join(new_path, rel_path)
            base_file = os.path.join(base_path, rel_path)
            if os.path.exists(base_file):
                with open(base_file, 'r', errors='ignore') as bf, open(new_file, 'r', errors='ignore') as nf:
                    base_lines = bf.readlines()
                    new_lines = nf.readlines()
                    diff = list(difflib.unified_diff(base_lines, new_lines, lineterm=''))
                    if diff:
                        differences.append((rel_path, diff))
            else:
                differences.append((rel_path, ["[New file added]"]))
    return differences


def generate_summary(diffs):
    summary_path = f"./archives/summary_{datetime.now().strftime('%Y-%m-%d--%H%M%S')}.md"
    with open(summary_path, 'w') as f:
        f.write(f"# Archive Comparison Summary\n\n")
        for path, changes in diffs:
            f.write(f"## {path}\n")
            for line in changes[:50]:  # limit preview
                f.write(line + "\n")
            f.write("\n---\n\n")
    print(f"📄 Summary written to: {summary_path}")

if __name__ == "__main__":
    old_path = select_archive_path("Select OLDER snapshot:")
    if not old_path:
        exit()
    new_path = select_archive_path("Select NEWER snapshot:")
    if not new_path:
        exit()
    diffs = compare_files(old_path, new_path)
    generate_summary(diffs)