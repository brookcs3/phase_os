# Voice Memo Hotkey Binder
# Binds a global hotkey to launch phase-aware voice memo recorder with feedback and AI stream injection

import keyboard
import subprocess

HOTKEY = "cmd+shift+v"

print(f"🎚️ Voice memo hotkey active: {HOTKEY}")
keyboard.add_hotkey(HOTKEY, lambda: [
    subprocess.Popen(["python3", "voice_feedback_overlay.py"]),
    subprocess.Popen(["python3", "voice_context_stream.py"])
])
keyboard.wait()