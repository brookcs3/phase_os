# 🧠 PHASE OS — UNSUPERVISED COGNITIVE ENHANCEMENT PROTOCOL

## 🔧 SYSTEM PRIMER
A recursive operating system for high-intelligence / low-exec-function creatives.
Designed for neuroplasticity, state tracking, burnout recovery, and artifact capture.

## 🌐 CORE STACK
- **Phases**: Generator, Builder, Executor, Recovery
- **AI Assistants**: Dolphin-Mixtral, Context Injector, Reflector Cache
- **Recording Modules**: Voice Memo Logger + Transcriber, Bounce Tracker
- **Sample Oracle**: Curated and live-scraped audio suggestion engine
- **Archival Layer**: Auto backup, weekly digest, version control, vector diffs
- **Web Interfaces**: Tag dashboard, Oracle UI, Digest Viewer

---

## 🔄 PHASE LOOP TABLE

| Phase     | Purpose            | Trigger                          | Tools Activated                                      |
|-----------|--------------------|----------------------------------|-------------------------------------------------------|
| Generator | Divergence / Input | Microdose, hotkey, ritual token | DAW launcher, Context Injection, Sample Oracle, Recorder |
| Builder   | Pattern / Structure| Tag recall, diagram ref          | Journal, Tag Filter, AI Thread, File Router           |
| Executor  | Output / Delivery  | Silence, cold light              | Telemetry, Bounce Logger, Compile / Exporters         |
| Recovery  | Rest / Digest      | Firelight, wind, no screen       | Loop Digest Generator, Archive Exporter, RSS Feed     |

---

## 🎙️ COGNITIVE MEMORY SYSTEM

- **Voice**: Recorded via `mic_preset_router.py`, transcribed with Whisper
- **Tags**: Captured during Generator via `fragment_tagger.py`
- **Reflector**: Updated with session state, tags, and voice transcript
- **Sessions**: Auto-initiated with identity tagging, scratchpad, log linking

---

## 🔊 SAMPLE ORACLE

- Sources: YouTube, Discogs, Blog/RSS Scraping, Curated Playlists
- Classifier: OpenL3 Embedding → Vector Matching
- Interfaces: Web Audio UI, Save + Slice Queue
- Suggestions logged to `oracle_log.md`

---

## ⏳ AUTOMATED SYSTEMS

- `phase_trigger_engine.py`: Launches all context and state modules on phase switch
- `phase_control.py`: Start/stop/status all system processes
- `oracle_scraper_scheduler.py`: Daily clip pulls and digest generation
- `digest_mailer.py` + `oracle_digest_web.py`: Morning dashboard feed
- `archive_exporter.py`: Weekly timestamped system backup

---

## ⚠️ RISK PROTOCOL

- Infinite journaling: cap loops and interleave phases
- Burnout recurrence: enforce Recovery after 3 Executor loops
- Memory distortion: tag hallucinated states vs. actual output

---

## 📁 WORKSPACE

- `unnamed_record/`
  - `/sessions/` — each session time-stamped + scratchpad
  - `/fragments/` — rendered stems and tags
  - `/rituals/` — phase-entry anchors and logs
  - `/archives/` — zipped snapshots, digests

---

## 🛠️ ENTRY

Trigger phase:
```bash
python3 phase_control.py --start all
```

View Oracle:
[http://localhost:7880](http://localhost:7880)

View Digest:
[http://localhost:7881](http://localhost:7881)

Start Session:
```bash
python3 project_initiator.py
```

Voice Log:
⌘ + ⇧ + V → Record, transcribe, reflect, tag, inject.

---

You are now living in the loop.
Let it run you.
Let it log.
Let it build the record underneath you while you walk.

Ready to generate your Phase 1 session identity and begin?
