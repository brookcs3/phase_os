# Sample Refresh Scheduler
# Runs sample_suggestion_engine daily at 04:00

import subprocess
import schedule
import time


def daily_refresh():
    print("🌅 Generating daily sample suggestions...")
    subprocess.run(["python3", "sample_suggestion_engine.py"])


schedule.every().day.at("04:00").do(daily_refresh)

print("🗓️ Sample suggestion refresh scheduled — Daily at 04:00")

while True:
    schedule.run_pending()
    time.sleep(60)
