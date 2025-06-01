# AI Reflector Cache Builder
# Extracts high-response prompt patterns from compiled loops

import os
import re
from collections import defaultdict, Counter

COMPILED_DIR = "./compiled_loops"
CACHE_FILE = "./reflector_cache.txt"

PROMPT_RE = re.compile(r"## Prompt:\n(.*?)\n## Response:", re.DOTALL)

def extract_prompts():
    prompt_counter = Counter()
    for fname in os.listdir(COMPILED_DIR):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(COMPILED_DIR, fname)
        with open(path, 'r') as f:
            text = f.read()
            matches = PROMPT_RE.findall(text)
            for match in matches:
                clean = match.strip().replace("\n", " ")
                prompt_counter[clean] += 1
    return prompt_counter

def write_cache(prompt_counter):
    with open(CACHE_FILE, 'w') as f:
        f.write("# Reflector Memory Cache\n")
        f.write("Most engaged prompt types:\n\n")
        for prompt, count in prompt_counter.most_common(20):
            f.write(f"- ({count}) {prompt}\n")
    print(f"✅ Reflector cache written to {CACHE_FILE}")

if __name__ == "__main__":
    prompts = extract_prompts()
    write_cache(prompts)
