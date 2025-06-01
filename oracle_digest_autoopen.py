# Oracle Digest Autoopen
# Opens the daily digest web UI at startup each day

import webbrowser
import subprocess
import time
import schedule

def start_server():
    print("🌐 Launching Oracle Digest Web Server...")
    subprocess.Popen(["uvicorn", "oracle_digest_web:app", "--port", "7881", "--reload"])
    time.sleep(2)
    webbrowser.open("http://localhost:7881")

def launch_daily():
    schedule.every().day.at("08:00").do(start_server)
    print("🕗 Oracle digest will launch daily at 08:00")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    start_server()
