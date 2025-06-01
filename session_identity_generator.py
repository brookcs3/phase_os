# Session Identity Generator
# Dynamically names sessions from fragments + tags

from datetime import datetime
import random

# These would ideally be pulled from your live tag and voice logs
# but here we initialize with sample seed data

tags = [
    "fractured bassline, hiss-layered drums",
    "ritual break, midtempo loop",
    "reverbed vocal snap",
    "rusted sample texture, ambient debris"
]

voice_fragments = [
    "I want it to feel like something broken but alive.",
    "Don’t loop it clean—smear it like memory.",
    "The silence is more important than the drop.",
    "It should glitch like it’s haunted."
]

prefix = random.choice(tags).split(",")[0].strip().split()[0]
trigger = random.choice(voice_fragments).split()[0].lower()
stamp = datetime.now().strftime("%H%M")

session_identity = f"{prefix}_{trigger}_{stamp}"
print(f"🧬 Generated Session Identity: {session_identity}")
