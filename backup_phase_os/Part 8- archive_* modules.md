📘 Phase OS Manual Part 8: archive_* Modules

🗂️ Purpose

The archive_* modules form Phase OS’s temporal memory and export layer.

They handle:
	•	Full system snapshots
	•	Weekly digest exports
	•	Difference detection between system states
	•	External sharing of your creative state

This is how your loop gets frozen in time.

⸻

🧱 Core Components

archive_exporter.py
	•	Role: Backs up system snapshot (focused)
	•	Function:
	•	Archives system metadata, session logs, but excludes heavy .wav and .zip
	•	Outputs: archives/phase_backup_<timestamp>.zip
	•	Use Case: Reliable incremental backups without overload

⸻

phase_os_exporter.py
	•	Role: Full system exporter
	•	Function:
	•	Zips the entire system, including scripts, dashboards, and README
	•	Designed for full migration / versioned clone
	•	Trigger: Run manually or from digest_scheduler.py

⸻

archive_browser.py
	•	Role: Explore past exports
	•	Function:
	•	Lists all past archive files
	•	Lets you diff, open, or mark one for recovery
	•	Status: CLI-first, extendable to web

⸻

archive_diff_summarizer.py
	•	Role: Compare two zip exports
	•	Function:
	•	Unzips, hashes contents
	•	Reports any changed scripts, logs, or data between backups
	•	Diff-like functionality for scaffolds

⸻

digest_scheduler.py
	•	Role: Weekly job controller
	•	Function:
	•	Runs every Sunday at 10:00am (via schedule)
	•	Executes:
	•	Digest generation
	•	Playlist refresh
	•	Oracle seed
	•	Archive export
	•	Phase OS export
	•	Manifest write
	•	Purpose: Ensures memory is captured on a fixed rhythm

⸻

📁 Output Tree

archives/
├── phase_backup_2025-06-01--1032__scaffold_commit.zip
├── phase_os_export_2025-06-01--1034.zip
README.md
record_scaffold_manifest.md


⸻

🧠 Why It’s Powerful
	•	Guarantees no creative memory is lost
	•	Enables rollback to past states (aesthetic + structural)
	•	Facilitates cloning your environment across machines
	•	Can be used as submission proof, audit trail, or versioned release deck

⸻

💡 Tips
	•	Pair archive diffs with builder_form_diff_viewer to see creative + config delta
	•	Add README.md or a human memo to each zip before sharing externally
	•	Use with phase_autostart.py for bootstrapping remote recovery

⸻

Next up: loop_* modules — bounce tracking, digest compiling, and waveform visualization.