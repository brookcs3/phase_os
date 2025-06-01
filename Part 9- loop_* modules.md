📘 Phase OS Manual Part 9: loop_* Modules

🔁 Purpose

The loop_* modules are responsible for managing your final output layer — tracking bounces, compiling digest summaries, and generating visualizations of your audio structure.

This is how the system learns what you finished.

⸻

🎚️ Core Components

loop_compiler.py
	•	Role: Final bounce cataloger
	•	Function:
	•	Scans your DAW export or bounce folder for new .wav or .mp3 files
	•	Extracts metadata (timestamp, length, file name, session context)
	•	Logs new bounces into a structured digest entry
	•	Output: Updates a master log of completed tracks or fragments

⸻

loop_digest.py
	•	Role: Weekly digest summarizer
	•	Function:
	•	Compiles a .md digest of the week’s most important outputs:
	•	New bounces (via loop_compiler)
	•	Notable tags
	•	Oracle additions
	•	Form map changes
	•	Links to relevant samples, sessions, and exports
	•	Used in: Recovery phase, or on Sunday via digest_scheduler.py

⸻

loop_visualizer.py
	•	Role: Audio structure visualizer
	•	Function:
	•	Loads .wav or .mp3 and renders duration, amplitude plot, section map
	•	Can overlay form map data from builder_form_map_generator
	•	Optionally exports a .png for postmortem review or cover art

⸻

bounce_logger.py
	•	Role: Live bounce detection
	•	Function:
	•	Watches export folders in real-time
	•	Alerts or logs new bounces as they’re created
	•	Purpose: Real-time responsiveness for loop tracking

⸻

📁 Output Sample

loop_digest_weekly.md

# Weekly Loop Digest — 2025-06-01

### New Bounces
- `../bounces/memory-spike-v2.wav` — 3:17
- `../bounces/frag-loop-finale.mp3` — 1:02

### Saved Slices
- 5 Oracle slices saved

### Form Map Version Changes
- Builder structure updated 2 times


⸻

🧠 Why It’s Powerful
	•	Keeps track of what you completed — not just what you started
	•	Surfaces aesthetic and structural momentum over time
	•	Bridges creative activity with reflective context
	•	Can be used for retrospective review, documentation, or sharing

⸻

💡 Tips
	•	Set loop_visualizer.py to generate art for each track
	•	Use loop_digest.py in combination with archive_exporter.py for full historical snapshots
	•	Let bounce logs inform phase transitions (e.g. exit Builder once 2 bounces exist)

⸻

Next: Final section — How all modules interweave as one recursive memory engine.