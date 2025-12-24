# Oracle Curator — Single Clip Interaction Tool
# Presents one clip at a time from oracle DB and enforces decision loop

import json
import os
import random
import shutil
from datetime import datetime

ORACLE_DB = "./oracle_dynamic.json"
QUEUE_LOG = "./oracle_curator_log.md"
CLIP_DIR = "./oracle_clips"

if not os.path.exists(ORACLE_DB):
    print("⛔ No oracle DB found.")
    exit()

with open(ORACLE_DB, 'r') as f:
    records = json.load(f)

unlabeled = [r for r in records if not r.get("status")]
if not unlabeled:
    print("✅ All samples have been labeled.")
    exit()

record = random.choice(unlabeled)
clip_path = record['clip']
print(f"🎧 {record['title']}\n\n{clip_path}\n")

os.system(f"afplay '{clip_path}'")

choice = input("Tag this sample as [k]eep / [s]kip / [d]elete: ").strip().lower()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

if choice == 'k':
    record['status'] = "kept"
elif choice == 's':
    record['status'] = "skipped"
elif choice == 'd':
    record['status'] = "deleted"
    if os.path.exists(clip_path):
        os.remove(clip_path)
    print("🗑️ File removed.")
else:
    print("No action taken.")

with open(QUEUE_LOG, 'a') as f:
    f.write(f"[{timestamp}] {record['title']} → {record.get('status', 'unknown')}\n")

with open(ORACLE_DB, 'w') as f:
    json.dump(records, f, indent=2)

print(f"🔁 Oracle DB updated: {record.get('status', 'unknown')}")