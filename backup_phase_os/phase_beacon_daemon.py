# Beacon Daemon Scheduler (macOS)
# Runs phase_beacon.py in the background using launchctl

import os
import subprocess

LAUNCH_AGENT_PLIST = os.path.expanduser("~/Library/LaunchAgents/com.phaseos.beacon.plist")
PYTHON_PATH = subprocess.getoutput("which python3").strip()
PHASE_BEACON_PATH = os.path.abspath("./phase_beacon.py")

PLIST_CONTENT = f"""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.phaseos.beacon</string>
    <key>ProgramArguments</key>
    <array>
        <string>{PYTHON_PATH}</string>
        <string>{PHASE_BEACON_PATH}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StartInterval</key>
    <integer>60</integer>
    <key>StandardOutPath</key>
    <string>/tmp/phase_beacon.out</string>
    <key>StandardErrorPath</key>
    <string>/tmp/phase_beacon.err</string>
</dict>
</plist>
"""

with open(LAUNCH_AGENT_PLIST, 'w') as f:
    f.write(PLIST_CONTENT)

subprocess.run(["launchctl", "load", LAUNCH_AGENT_PLIST])
print(f"✅ Phase beacon daemon installed and loaded: {LAUNCH_AGENT_PLIST}")
