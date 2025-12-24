# Tag Reflector Link
# Appends recent tags from fragment index into the AI reflector cache

import os

TAG_FILE = "./fragment_index.md"
CACHE_FILE = "./reflector_cache.txt"

def extract_recent_tags(n=10):
    if not os.path.exists(TAG_FILE):
        return []
    with open(TAG_FILE, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines[-n:] if "Tags:" in line]

def update_reflector(tags):
    with open(CACHE_FILE, 'a') as f:
        f.write("\n\n# Recent Fragment Tags\n")
        for tag in tags:
            f.write(f"{tag}\n")
    print("🔁 Reflector cache updated with recent tags.")

if __name__ == "__main__":
    recent_tags = extract_recent_tags()
    if recent_tags:
        update_reflector(recent_tags)
    else:
        print("⚠️ No recent tags found.")
