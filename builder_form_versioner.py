# Builder Form Versioner
# Tracks and diffs changes to latest_form_map.md

import os
import hashlib
from datetime import datetime

FORM_PATH = "./unnamed_record/sessions/latest_form_map.md"
ARCHIVE_DIR = "./unnamed_record/sessions/form_versions"
os.makedirs(ARCHIVE_DIR, exist_ok=True)

if not os.path.exists(FORM_PATH):
    print("❌ No form map found.")
    exit()

with open(FORM_PATH, 'r') as f:
    content = f.read()

stamp = datetime.now().strftime("%Y-%m-%d--%H%M%S")
hash_id = hashlib.md5(content.encode()).hexdigest()[:6]
version_file = f"form_{stamp}__{hash_id}.md"
path = os.path.join(ARCHIVE_DIR, version_file)

with open(path, 'w') as f:
    f.write(content)

print(f"📝 Saved form version: {version_file}")