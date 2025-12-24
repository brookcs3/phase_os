# Loop Visualizer (Terminal Timeline View)
# Parses phase telemetry and shows duration-based timeline per day

import os
from datetime import datetime, timedelta

TELEMETRY_LOG = "./phase_telemetry.log"
SEGMENT_WIDTH = 3
DAY_WIDTH = 80

COLORS = {
    "Generator": "\033[95m",
    "Builder": "\033[94m",
    "Executor": "\033[92m",
    "Recovery": "\033[93m",
    "END": "\033[0m"
}

def parse_log():
    if not os.path.exists(TELEMETRY_LOG):
        print("No telemetry log found.")
        return []

    entries = []
    with open(TELEMETRY_LOG, 'r') as f:
        for line in f:
            if "PHASE" not in line:
                continue
            parts = line.strip().split(" PHASE: ")
            time_parts = parts[0].split(" → ")
            phase = parts[1].split(" | ")[0].strip()
            start = datetime.fromisoformat(time_parts[0][1:])
            end = datetime.fromisoformat(time_parts[1][1:])
            duration = end - start
            entries.append({"phase": phase, "start": start, "end": end, "duration": duration})
    return entries

def group_by_day(entries):
    days = {}
    for entry in entries:
        day = entry["start"].date()
        if day not in days:
            days[day] = []
        days[day].append(entry)
    return days

def render_day(day, blocks):
    total_minutes = sum(int(e['duration'].total_seconds() // 60) for e in blocks)
    scale = max(1, total_minutes / DAY_WIDTH)
    print(f"\n{day.strftime('%A, %Y-%m-%d')}:\n")
    line = ""
    for entry in blocks:
        length = max(1, int(entry['duration'].total_seconds() // 60 // scale))
        color = COLORS.get(entry['phase'], '')
        label = entry['phase'][0] * length
        line += f"{color}{label}{COLORS['END']}"
    print(line)

def visualize():
    entries = parse_log()
    grouped = group_by_day(entries)
    for day in sorted(grouped.keys()):
        render_day(day, grouped[day])

if __name__ == "__main__":
    visualize()
