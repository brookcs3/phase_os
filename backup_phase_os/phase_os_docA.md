
⸻
1. phase_control.py
	•	Purpose: Acts as the central controller for Phase OS, managing the transition between different phases of the creative process.
	•	Functionality:
	•	Monitors the current phase (e.g., Generator, Builder, Recovery).
	•	Triggers corresponding scripts and tools associated with each phase.
	•	Rationale: Centralizing phase management ensures a structured workflow, reducing manual intervention and maintaining consistency. ￼

⸻

2. phase_trigger_engine.py
	•	Purpose: Automates the execution of specific scripts when transitioning between phases.
	•	Functionality:
	•	Reads the current phase from a designated file.
	•	Executes a predefined set of scripts associated with that phase.
	•	Rationale: Automating script execution minimizes the risk of human error and ensures that all necessary tools are activated during phase transitions.

⸻

3. builder_form_map_generator.py
	•	Purpose: Generates a structural blueprint for a music track during the Builder phase.
	•	Functionality:
	•	Randomly selects sections (e.g., Intro, Verse, Chorus) to form a track structure.
	•	Applies modifiers to introduce creative constraints.
	•	Saves the structure to latest_form_map.md and appends it to the current session’s notes.
	•	Rationale: Providing a randomized yet structured form map encourages creativity while maintaining a coherent track structure.

⸻

4. builder_form_versioner.py
	•	Purpose: Maintains version control of form maps to track the evolution of a track’s structure.
	•	Functionality:
	•	Computes a hash of the current form map.
	•	Saves the form map with a timestamp and hash to a versioned directory.
	•	Rationale: Versioning allows for retrospective analysis of structural changes and facilitates reverting to previous versions if needed.

⸻

5. form_diff_viewer.py
	•	Purpose: Displays differences between the two most recent form map versions.
	•	Functionality:
	•	Reads the last two saved form maps.
	•	Uses a unified diff to highlight changes.
	•	Rationale: Visualizing changes aids in understanding the evolution of a track’s structure and supports informed decision-making.

⸻

6. phase_os_exporter.py
	•	Purpose: Creates a compressed archive of the entire Phase OS system for backup or transfer.
	•	Functionality:
	•	Zips the Phase OS directory, excluding specified files and directories.
	•	Names the archive with a timestamp for easy identification.
	•	Rationale: Regular backups safeguard against data loss and facilitate system migration or sharing.

⸻

7. phase_os_manifest_writer.py
	•	Purpose: Generates a README file summarizing the contents and functionalities of the Phase OS system.
	•	Functionality:
	•	Creates a markdown file detailing each component and its purpose.
	•	Includes a timestamp to indicate the last update.
	•	Rationale: Providing clear documentation enhances usability, especially when sharing the system with others or revisiting after a hiatus.

⸻

8. digest_scheduler.py
	•	Purpose: Automates weekly maintenance tasks, including generating digests, refreshing playlists, and exporting the system.
	•	Functionality:
	•	Schedules tasks to run at specified times (e.g., every Sunday at 10:00 AM).
	•	Executes scripts for digest generation, email dispatch, playlist updates, and system export.
	•	Rationale: Automating routine tasks ensures consistency, saves time, and keeps the system up-to-date with minimal manual intervention.
