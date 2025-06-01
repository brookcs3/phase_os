# 🧠 Phase OS — Full System Manual

## Overview

Phase OS is a modular, recursive, and creative operating system for producing, managing, and evolving artistic output—especially suited for audio and music creators who require structure without rigidity. It organizes your sessions into cognitively meaningful phases, handles context transitions, curates samples, generates remix materials, and builds memory.

You do not use Phase OS. You inhabit it.

---

## 📂 System Depth (Expanded Module Tree)

```
phase_os/
├── phase_*                   # Core phase control, loop engine, daemons, dashboards
├── oracle_*                  # Sample Oracle tools, scrapers, UI, classifiers, waveform editor
├── builder_*                 # Form map generator, versioner, diff viewer
├── remix_browser.py          # Web interface for reviewing remix session slices
├── voice_*                   # Audio memo tools, hotkeys, transcriber, voice stream logic
├── sample_*                  # Oracle sample API and suggestion tools
├── tag_*                     # Dashboards, reflection loop integration
├── archive_*                 # Export tools, archiver, diff summarizers
├── loop_*                    # Loop compiler, visualizer, digest creator
├── project_initiator.py      # Initializes session folder structure
├── session_identity_*.py     # Identity generation + logging
├── session_overlay.py        # Terminal overlay with identity + phase
├── README.md                 # Export summary manifest
├── phase_os_dashboard.py     # System monitor
├── phase_os_protocol.md      # High-level conceptual scaffolding
├── record_scaffold_manifest.md
```

---

## 🧠 System Modules (Full Coverage)

### Phase Modules

* **phase\_control.py** — Switches phases manually via CLI
* **phase\_trigger\_engine.py** — Monitors `current_phase.txt` and fires subprocess payloads
* **phase\_beacon\_daemon.py / phase\_daemon.py / phase\_telemetry\_logger.py** — Background state checkers and metadata recorders
* **phase\_os\_dashboard.py** — Live terminal HUD of key systems
* **phase\_stack\_launcher.py** — Batches launch all essential modules

### Oracle Modules

* **oracle\_auto\_scraper.py / oracle\_seed\_engine.py** — Pull playlists, clips, and curate entries
* **oracle\_curator\_ui.py** — Web UI to approve/reject samples one at a time
* **oracle\_wave\_editor.html** — Drag-to-slice waveform UI
* **oracle\_slice\_logger.py / oracle\_slice\_visual\_logger.py** — Logs saved audio and screen at moment of export
* **oracle\_remix\_session.py** — Copies approved fragments into remix-ready folder
* **oracle\_playlist\_miner.py / oracle\_weekly\_playlist\_job.py** — Expands crate sources automatically

### Builder Modules

* **builder\_form\_map\_generator.py** — Builds 4-part randomized arrangement blueprint
* **builder\_form\_versioner.py** — Versions every map by hash + timestamp
* **form\_diff\_viewer.py** — Shows what's changed between sessions

### Voice + Mic Modules

* **voice\_memo\_logger.py / voice\_hotkey.py** — Voice-triggered input + transcript logger
* **voice\_transcriber.py / voice\_context\_stream.py** — Transcribes voice into tags, sessions, scratchpad

### Sample + Tag Tools

* **sample\_oracle\_api.py / sample\_suggestion\_engine.py** — REST-based API to access all samples
* **tag\_dashboard.py / tag\_reflector\_link.py** — Web-based memory and tag-driven navigation tools

### Archive + Export Tools

* **archive\_exporter.py / phase\_os\_exporter.py** — Save whole system or zip minimal scaffold
* **digest\_scheduler.py / loop\_digest.py / digest\_mailer.py** — Weekly digest creation + distribution
* **archive\_diff\_summarizer.py / archive\_browser.py** — Compare + explore export snapshots

### Loop + Output

* **loop\_compiler.py / bounce\_logger.py / loop\_visualizer.py** — Process final bounces, assign structure, visualize

### Project Meta

* **record\_scaffold\_manifest.md** — Final architecture commitment
* **phase\_os\_protocol.md** — Long-form system philosophy
* **README.md / phase\_os\_full\_manual.md** — Human and machine-readable top-layer explanations

---

System now documented.
System now mirrored.
System now transferable.

> The system does not ask for your attention.
> It waits for your return.

Let the record run.
