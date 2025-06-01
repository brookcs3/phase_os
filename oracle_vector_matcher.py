# Oracle Vector Matcher
# Recommends clips similar to a selected source clip based on OpenL3 embedding similarity

import json
import numpy as np
import os

EMBED_FILE = "./oracle_embeddings.json"
CLIP_DIR = "./oracle_clips"

with open(EMBED_FILE, 'r') as f:
    embeddings = json.load(f)

filenames = list(embeddings.keys())

print("📂 Available Clips:")
for i, fname in enumerate(filenames):
    print(f" {i}: {fname}")

choice = input("\nSelect clip index to find similar: ").strip()
if not choice.isdigit() or int(choice) >= len(filenames):
    print("❌ Invalid selection.")
    exit()

source = filenames[int(choice)]
src_vec = np.array(embeddings[source])

def cosine_dist(a, b):
    a = np.array(a)
    b = np.array(b)
    return 1 - np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

scores = []
for fname, vec in embeddings.items():
    if fname == source:
        continue
    dist = cosine_dist(src_vec, vec)
    scores.append((fname, dist))

matches = sorted(scores, key=lambda x: x[1])[:5]

print(f"\n🔁 Similar to {source}:")
for fname, dist in matches:
    print(f" • {fname} (distance: {dist:.4f})")
