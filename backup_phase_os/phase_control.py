# Phase OS Control Switch
# Master control to start, stop, or check status of core systems

import subprocess
import sys
import os

SERVICES = {
    "daemon": "phase_daemon.py",
    "logger": "artifact_logger.py",
    "telemetry": "phase_telemetry_logger.py",
    "trigger": "phase_trigger_engine.py",
    "beacon": "phase_beacon.py",
    "record": "record_trigger.py",
    "bounce": "bounce_logger.py"
}

PID_DIR = "./.pids"
os.makedirs(PID_DIR, exist_ok=True)

def get_pid_path(name):
    return os.path.join(PID_DIR, f"{name}.pid")

def start(name, script):
    pid_path = get_pid_path(name)
    if os.path.exists(pid_path):
        print(f"⚠️  {name} already running")
        return
    process = subprocess.Popen(["python3", script])
    with open(pid_path, 'w') as f:
        f.write(str(process.pid))
    print(f"✅ Started {name} [{process.pid}]")

def stop(name):
    pid_path = get_pid_path(name)
    if not os.path.exists(pid_path):
        print(f"⛔ {name} not running")
        return
    with open(pid_path, 'r') as f:
        pid = int(f.read().strip())
    try:
        os.kill(pid, 9)
        os.remove(pid_path)
        print(f"🛑 Stopped {name}")
    except Exception as e:
        print(f"❌ Failed to stop {name}: {e}")

def status(name):
    pid_path = get_pid_path(name)
    if os.path.exists(pid_path):
        with open(pid_path, 'r') as f:
            pid = f.read().strip()
        print(f"🔵 {name} running (PID: {pid})")
    else:
        print(f"⚪ {name} not running")

def main():
    if len(sys.argv) < 2:
        print("Usage: phase_control.py [--start|--stop|--status|--restart] [all|service]")
        return
    cmd = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else "all"
    for name, script in SERVICES.items():
        if target != "all" and target != name:
            continue
        if cmd == "--start":
            start(name, script)
        elif cmd == "--stop":
            stop(name)
        elif cmd == "--status":
            status(name)
        elif cmd == "--restart":
            stop(name)
            start(name, script)

if __name__ == "__main__":
    main()