# 📘 Phase OS Manual Part 1: `phase_*` Modules

## 🌀 Purpose

The `phase_*` modules are the backbone of Phase OS. They orchestrate transitions, track cognitive states, and determine which tools should launch or log activity based on your current phase (Generator, Builder, Executor, Recovery).

Every other system plugs into this layer. It is the **conductor** of your recursive loop.

---

## 📂 Components Overview

### `phase_control.py`

* **Role**: Manual phase switcher (CLI entrypoint)
* **Function**: Prompts user to select a phase by ID, logs selection, and sets current phase to `current_phase.txt`
* **Invokes**: `log_phase_entry()`, updates session state

---

### `phase_trigger_engine.py`

* **Role**: Main automation loop (daemon-style)
* **Function**: Constantly watches `current_phase.txt`. On phase change:

  * Launches subprocesses listed under each phase
  * Runs contextual injectors, dashboards, remixers, etc.
  * Writes `.last_triggered_phase` for memory tracking
* **Pattern**: Event-driven, polling every 5s

---

### `phase_template_writer.py`

* **Role**: Scratchpad initializer
* **Function**: On entering a new phase, generates default session notes with headers for mood, phase, identity, tasks
* **Location**: Writes into `./unnamed_record/sessions/<session>/notes.md`

---

### `phase_daemon.py` / `phase_beacon_daemon.py`

* **Role**: Background watchers (deprecated or experimental)
* **Function**: Track CPU, memory, or session drift
* **Notes**: Optional if telemetry isn't required

---

### `phase_telemetry_logger.py`

* **Role**: Writes session heartbeat data
* **Function**: Logs timestamp, active phase, session name, identity, and module status to disk every X minutes
* **Output**: Used to review system usage and temporal pacing

---

### `phase_os_dashboard.py`

* **Role**: CLI interface for system status
* **Function**: Displays last activity time of each major file: moodboard, digest, sample, etc.
* **Output**: Refreshes every 15s. Optional, but used in Recovery.

---

### `phase_stack_launcher.py`

* **Role**: Launches entire stack from CLI
* **Function**: Used in emergencies or resets. Invokes all launchable modules at once.

---

### `phase_hotkey_binder.py` *(optional)*

* **Role**: Links phase transitions to global keybinds
* **Function**: Could be used to bind Ctrl+Opt+1 → Generator, Ctrl+Opt+2 → Builder, etc.

---

## 🧠 What Makes It Powerful

* 💡 It externalizes state: you don't have to remember what you were doing.
* 🔁 It enforces creative rhythm: each phase has a purpose and its own tools.
* ⚡ It's extendable: add new phases or new triggers without rewriting the engine.
* 🧬 It integrates identity, time, and structure without needing a UI.

## 🚀 Recommended Usage

* Run `phase_control.py` at the start of a session.
* Leave `phase_trigger_engine.py` running in the background.
* Customize `phase_triggers.json` to include your custom scripts, aliases, or routines per phase.

---

Next up: `oracle_*` modules.
