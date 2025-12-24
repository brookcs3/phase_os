# Oracle Weekly Playlist Job
# Runs playlist mining and seeding once per week

import subprocess
import schedule
import time


def run_playlist_refresh():
    print("📡 Mining new playlists...")
    subprocess.run(["python3", "oracle_playlist_miner.py"])
    print("📼 Seeding Oracle from updated playlist pool...")
    subprocess.run(["python3", "oracle_seed_engine.py"])

schedule.every().monday.at("02:00").do(run_playlist_refresh)

print("🗓️ Oracle playlist refresh job scheduled — Every Monday at 02:00")
while True:
    schedule.run_pending()
    time.sleep(60)