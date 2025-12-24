# Voice Query Tool
# Search all voice memo transcripts by keyword or phrase

import os

SESSIONS_DIR = "./unnamed_record/sessions"


def collect_transcripts():
    results = []
    for session in sorted(os.listdir(SESSIONS_DIR)):
        session_path = os.path.join(SESSIONS_DIR, session)
        if not os.path.isdir(session_path):
            continue
        for file in os.listdir(session_path):
            if file.startswith("voice_") and file.endswith(".txt"):
                full_path = os.path.join(session_path, file)
                with open(full_path, 'r') as f:
                    text = f.read()
                    results.append((session, file, text))
    return results

def search_voice():
    query = input("🔍 Enter search term: ").lower().strip()
    results = collect_transcripts()
    found = [(s, f, t) for (s, f, t) in results if query in t.lower()]

    if not found:
        print("❌ No matches found.")
        return

    print("\n📂 Matches:\n")
    for session, filename, text in found:
        print(f"Session: {session}\nFile: {filename}\n---\n{text.strip()}\n{'-'*40}\n")

if __name__ == "__main__":
    search_voice()