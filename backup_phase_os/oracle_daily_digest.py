# Oracle Daily Digest
# Generates a morning summary of new Oracle entries in HTML or Markdown

import os
import json
from datetime import datetime

ORACLE_DB = "./oracle_dynamic.json"
DIGEST_FILE = "./oracle_digest_today.md"


def load_entries():
    if not os.path.exists(ORACLE_DB):
        return []
    with open(ORACLE_DB, 'r') as f:
        return json.load(f)

def filter_today(entries):
    today = datetime.now().strftime("%Y-%m-%d")
    return [e for e in entries if today in e['clip']]

def generate_digest():
    entries = load_entries()
    today_entries = filter_today(entries)
    if not today_entries:
        print("📭 No new entries today.")
        return

    with open(DIGEST_FILE, 'w') as f:
        f.write(f"# Oracle Daily Digest — {datetime.now().strftime('%Y-%m-%d')}\n\n")
        for e in today_entries:
            f.write(f"## {e['title']}\n")
            f.write(f"• Highlight: {e['highlight']}\n")
            f.write(f"• Suggestion: {e['suggestion']}\n")
            f.write(f"• File: {e['clip']}\n\n")

    print(f"📓 Digest written: {DIGEST_FILE}")

if __name__ == "__main__":
    generate_digest()
