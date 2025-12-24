# 📘 Phase OS Manual Part 5: `voice_*` Modules

## 🎙️ Purpose

The `voice_*` modules form the **auditory memory interface** of Phase OS. They allow you to speak into the system — to inject ephemeral thought, emotional states, spontaneous tags, or even spoken prompts.

This is not just transcription. It's a way to talk **to** your system, not just use it.

---

## 🧩 Components

### `voice_memo_logger.py`

* **Role**: Record a voice memo, save with timestamp
* **Function**:

  * Captures audio from default input (microphone)
  * Saves `.wav` file to `unnamed_record/sessions/<session>/voice/`
  * Logs filename and timestamp to `fragment_index.md`
* **Use case**: Mark a moment of inspiration while working or walking

---

### `voice_transcriber.py`

* **Role**: Transcribe saved voice memos
* **Function**:

  * Uses `whisper` (or another ASR backend)
  * Writes full transcript to a sidecar `.txt`
  * Appends key moments or quotes into `notes.md`
* **Optional**: Can run nightly or manually

---

### `voice_hotkey.py`

* **Role**: Global hotkey listener
* **Function**:

  * Press `Ctrl + Opt + V` to start recording
  * Press again to stop and auto-save
  * Begins logging session voice instantly

---

### `voice_context_stream.py`

* **Role**: Live text stream from mic input
* **Function**:

  * Creates rolling context stream (useful for journaling or generative AI use)
  * Optional: can inject last sentence into a scratchpad

---

### 📁 File Flow

```
unnamed_record/
└── sessions/
    └── session_<timestamp>/
        ├── voice/
        │   ├── memo_001.wav
        │   └── memo_001.txt
        └── notes.md
```

---

## 🧠 Why It’s Powerful

* Captures ideas that were never typed
* Respects your context — your tone, your emotion, your moment
* Merges voice with form maps and fragments
* Allows you to **speak directly into the record**

---

## 💡 Tips

* Train yourself to tag: "loop idea", "mood map", "vocals only"
* Use `voice_context_stream.py` to keep a meditative rolling transcription
* Review voice log every Recovery phase for unharvested ideas

---

Next up: `sample_*` modules — the REST interface and suggestion engine powering Oracle access.
