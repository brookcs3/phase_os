# Phase OS

Phase OS is an experimental toolkit for managing creative sessions as a series of **phases**.  Each phase represents a different mindset (Generator, Builder, Executor, Recovery) and the system launches specific tools or logging utilities as you move between them.

The project began as a collection of scripts to automate personal music workflows.  It now serves as a playground for state-driven automation, sample curation and session archiving.  Every script lives at the repository root and can be run individually, but the typical entry point is `phase_control.py`.

## Features

- **Trigger Engine** – watches `current_phase.txt` and executes commands when you enter a new phase
- **Session Identity** – generates a unique identity for each creative session and logs it
- **Sample Oracle** – scrapes and classifies samples for inspiration
- **Remix Builder** – creates remix sessions and tracks form changes over time
- **Dashboards & Overlays** – small FastAPI apps that surface status and context
- **Archiver** – schedules weekly exports and backups of your work

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The project uses only a handful of Python packages (FastAPI, uvicorn, keyboard, numpy, pillow, soundfile, openl3, tqdm, schedule).  Some modules also rely on audio tools installed separately (a DAW, command line audio utilities, etc.).

## Usage

The central control script manages starting and stopping the various background helpers:

```bash
python phase_control.py --start all     # start daemons
python phase_control.py --status all    # check running services
python phase_control.py --stop all      # stop everything
```

Most helper scripts can also be executed individually for experimentation.

## Development Notes

The repository contains many prototype modules.  The most interesting piece is `phase_trigger_engine.py`.  It reads the current phase from a text file and launches a set of commands defined in `phase_triggers.json`.  This simple polling loop (every ~5 seconds) orchestrates a surprising amount of automation – from opening dashboards to injecting AI context to starting the DAW.

```python
# Simplified from phase_trigger_engine.py
while True:
    phase = read_current_phase()
    if phase != last_phase:
        for cmd in triggers.get(phase, []):
            subprocess.Popen(cmd, shell=True)
        last_phase = phase
    time.sleep(5)
```

## Repository Layout

The root directory contains standalone scripts.  Documentation lives in a series of `Part *` markdown files describing each module family.  A `docs/` folder contains additional notes and an architecture diagram placeholder.

## Next Steps

Phase OS is not packaged for distribution.  Each module is meant to be hacked on directly.  Future work could include:

- Consolidating configuration
- Packaging as an installable module
- Building a UI around phase transitions

