# Phase OS Autostart Installer (macOS)
# Ensures Phase Control auto-launches all systems at login

import os
import subprocess

LAUNCH_AGENT_PLIST = os.path.expanduser("~/Library/LaunchAgents/com.phaseos.control.plist")
PYTHON_PATH = subprocess.getoutput("which python3").strip()
PHASE_CONTROL_PATH = os.path.abspath("./phase_control.py")

PLIST_CONTENT = f"""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.phaseos.control</string>
    <key>ProgramArguments</key>
    <array>
        <string>{PYTHON_PATH}</string>
        <string>{PHASE_CONTROL_PATH}</string>
        <string>--start</string>
        <string>all</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/phase_control.out</string>
    <key>StandardErrorPath</key>
    <string>/tmp/phase_control.err</string>
</dict>
</plist>
"""

with open(LAUNCH_AGENT_PLIST, 'w') as f:
    f.write(PLIST_CONTENT)

subprocess.run(["launchctl", "load", LAUNCH_AGENT_PLIST])
print(f"✅ Phase OS autostart configured at login: {LAUNCH_AGENT_PLIST}")
    