# Oracle Scraper Scheduler
# Runs oracle_auto_scraper and oracle_daily_digest each day at 3:00 AM

import schedule
import time
import subprocess

def run_oracle_scrape():
    print("🌙 Running Oracle auto-scraper...")
    subprocess.run(["python3", "oracle_auto_scraper.py"])
    print("📝 Generating Oracle digest...")
    subprocess.run(["python3", "oracle_daily_digest.py"])

schedule.every().day.at("03:00").do(run_oracle_scrape)

print("🗓️ Oracle scrape scheduler active — Daily at 03:00 AM")
while True:
    schedule.run_pending()
    time.sleep(60)
