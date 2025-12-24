# Builder Form Diff Viewer
# Compares the last two saved form maps and prints a diff

import os
import difflib

ARCHIVE_DIR = "./unnamed_record/sessions/form_versions"
versions = sorted([f for f in os.listdir(ARCHIVE_DIR) if f.endswith(".md")], reverse=True)

if len(versions) < 2:
    print("❌ Not enough form versions to diff.")
    exit()

v1_path = os.path.join(ARCHIVE_DIR, versions[1])
v2_path = os.path.join(ARCHIVE_DIR, versions[0])

with open(v1_path, 'r') as f:
    old = f.readlines()
with open(v2_path, 'r') as f:
    new = f.readlines()

diff = difflib.unified_diff(old, new, fromfile=versions[1], tofile=versions[0])
print("\n📊 Diff between last two form maps:\n")
print("".join(diff))
