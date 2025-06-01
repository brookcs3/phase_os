# Phase OS Manifest Writer
# Creates a README.md with summary of the system for export inclusion

from datetime import datetime

stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
manifest = f"""# 🧠 Phase OS — System Export Manifest

**Generated:** {stamp}

This archive includes:

- 🌀 Phase Engine (trigger-based state loop)
- 🧬 Session Identity Generator + Logger
- 🎛️ Sample Oracle + Curator + Wave Editor
- 🔁 Fragment Logger, Visual Logger, Slice Queue
- 🎼 Builder Form Generator + Versioner + Diff Viewer
- 🗂️ Digest Generator, Mailer, and Auto Backup
- 🧩 Remix Session Creator + Browser
- 📊 Dashboard + Overlay Interface
- 📦 Weekly Archiver + Export Scheduler

All files are versioned by phase and linked to recorded sessions.
Use `phase_control.py` to start the loop.

Ready to reboot your mind. Ready to record itself.
"""

with open("./README.md", "w") as f:
    f.write(manifest)

print("📄 Export manifest written: README.md")