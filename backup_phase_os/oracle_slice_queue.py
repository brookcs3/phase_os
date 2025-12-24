# Oracle Slice Queue
# When a sample is saved, queue it for slicing or processing

import os
from datetime import datetime

QUEUE_FILE = "./oracle_slice_queue.md"


def add_to_queue(title, clip_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(QUEUE_FILE, 'a') as f:
        f.write(f"[{timestamp}] {title}\n🎧 {clip_path}\n\n")
    print(f"📥 Queued for slicing: {title}")

if __name__ == "__main__":
    sample_title = input("Sample title: ").strip()
    clip_path = input("Clip path: ").strip()
    if os.path.exists(clip_path):
        add_to_queue(sample_title, clip_path)
    else:
        print("❌ Clip path not found.")
