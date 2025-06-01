# Oracle Sample Classifier (Option 2)
# Extracts audio embeddings from sample clips and logs them for future similarity matching

import os
import numpy as np
import soundfile as sf
import openl3
from tqdm import tqdm
import json

CLIP_DIR = "./oracle_clips"
EMBED_FILE = "./oracle_embeddings.json"

if not os.path.exists(CLIP_DIR):
    print("⛔ No clip directory found.")
    exit()

os.makedirs("./oracle_vectors", exist_ok=True)

existing = set()
if os.path.exists(EMBED_FILE):
    with open(EMBED_FILE, 'r') as f:
        existing = set(json.load(f).keys())

embeddings = {}
print("🔎 Classifying sample embeddings...")

for fname in tqdm(os.listdir(CLIP_DIR)):
    if not fname.endswith(".mp3") or fname in existing:
        continue

    try:
        audio, sr = sf.read(os.path.join(CLIP_DIR, fname))
        emb, _ = openl3.get_audio_embedding(audio, sr, content_type="music", embedding_size=512)
        vec = np.mean(emb, axis=0).tolist()
        embeddings[fname] = vec
    except Exception as e:
        print(f"❌ Failed on {fname}: {e}")

if embeddings:
    if os.path.exists(EMBED_FILE):
        with open(EMBED_FILE, 'r') as f:
            full = json.load(f)
    else:
        full = {}
    full.update(embeddings)
    with open(EMBED_FILE, 'w') as f:
        json.dump(full, f, indent=2)
    print(f"✅ {len(embeddings)} new embeddings stored in: {EMBED_FILE}")
