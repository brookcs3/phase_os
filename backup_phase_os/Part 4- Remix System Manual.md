# 📘 Phase OS Manual Part 4: Remix System

## 🎛️ Purpose

The Remix System in Phase OS is where your **archived memory becomes new music**.

It activates during the **Builder** phase and works by collecting every curated and sliced fragment you've saved — then compiling them into a ready-to-use session folder. This is not a loop pack. This is a mirror of your aesthetic history.

---

## 🔁 Core Components

### `oracle_remix_session.py`

* **Role**: Fragment compiler
* **Function**:

  * Scans `fragment_index.md` for all approved slices
  * Copies those audio files into a timestamped folder (e.g. `remix_session_20250601_1342/`)
  * Filters only `.wav` and `.mp3` paths that still exist
* **Invoked**:

  * Automatically during Builder phase
  * Manually runnable if needed
* **Why it matters**: Ensures only your saved sonic decisions become remix material

---

### `remix_browser.py`

* **Role**: Local remix UI
* **Function**:

  * Scans latest `remix_session_*` folder
  * Displays all fragments in a scrollable HTML browser
  * Allows preview of all audio without opening your DAW
* **URL**: [http://localhost:7892](http://localhost:7892)
* **Triggers**:

  * Auto-opens during Builder phase alongside `oracle_remix_session.py`

---

### 📁 File Flow

```
oracle_slices/
  └── [fragments]
fragment_index.md
  └── Audio: ./oracle_slices/voice_flare_1044.wav
oracle_remix_session.py
  └── remix_session_20250601_1342/
        ├── voice_flare_1044.wav
        ├── hiss_bridge_clip_1033.wav
```

---

## 🧠 Why It's Powerful

* You no longer remix from sample packs — you remix **from yourself**
* It links your curation, your editing, your visual memory into one workspace
* It allows **generative feedback loops** (you remix a remix of your own memory)

---

## 💡 Tips

* Run multiple remix sessions and compare how your creative intent evolves
* Create symbolic links from remix folder into DAW project for traceability
* Combine with `builder_form_map_generator.py` to structure your remix based on moodboard logic

---

Next up: `voice_*` modules — how spoken input, hotkeys, and transcripts become structured memory.
