# Digest Scheduler
# Runs weekly digest generator, mailer, and backup every Sunday at 10am

import schedule
import time
import subprocess

def run_weekly_digest():
    print("🗂️ Running weekly digest generation...")
    subprocess.run(["python3", "loop_digest.py"])
    print("📨 Sending digest email...")
    subprocess.run(["python3", "digest_mailer.py"])
    print("📦 Archiving Phase OS snapshot...")
    subprocess.run(["python3", "archive_exporter.py"])

schedule.every().sunday.at("10:00").do(run_weekly_digest)

print("📅 Digest scheduler active: runs every Sunday at 10:00")
while True:
    schedule.run_pending()
    time.sleep(60)
