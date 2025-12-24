# 📘 Phase OS Manual Part 3: `builder_*` Modules

## 🧩 Purpose

The `builder_*` modules form the structural intelligence layer of Phase OS. They operate during the **Builder** phase, where raw fragments are organized, remixed, and arranged into coherent sonic forms.

The system doesn’t just store samples — it remembers how you build with them.

---

## 📂 Components Overview

### `builder_form_map_generator.py`

* **Role**: Generates a randomized but musically aware track blueprint
* **Output**:

  * 4 structural sections (Intro, Verse, etc.)
  * A creative constraint (e.g., "no drums for 40 seconds")
* **Writes to**:

  * `latest_form_map.md`
  * Appends to current session’s `notes.md`
* **Triggers**:

  * During Builder phase (via `phase_trigger_engine.py`)

---

### `builder_form_versioner.py`

* **Role**: Snapshots every form map
* **Output**: Saves file as `form_YYYY-MM-DD--HHMMSS__HASH.md` in `form_versions/`
* **Purpose**:

  * Ensures version control of evolving track arrangements
  * Creates a breadcrumb trail of ideas

---

### `form_diff_viewer.py`

* **Role**: Shows the difference between the two most recent form versions
* **Function**:

  * Unified diff viewer in terminal
  * Helps surface shifts in aesthetic direction
* **Invoked Automatically**:

  * At start of Builder phase

---

### 📁 Related Folder Structure

```
unnamed_record/
└── sessions/
    ├── session_<timestamp>/
    │   └── notes.md
    └── form_versions/
        ├── form_2025-06-01--1532__92c1a2.md
        └── form_2025-06-01--1621__4bf731.md
```

Each form is not just saved, but versioned like code.

---

## 🧠 What Makes It Powerful

* 🎼 Gives you a starting structure for every session
* 🧬 Remembers how your structure evolved
* 🧠 Encourages constraint-based creativity
* 🔍 Lets you visualize change, not just generate ideas

This subsystem turns the **form** of your music into a trackable, editable, and **differential artifact.**

---

## 💡 Tips

* Run `form_diff_viewer.py` manually to analyze evolution between versions
* Edit `builder_form_map_generator.py` to bias toward your favorite structures
* Use form maps as AI prompt anchors or DAW import templates

---

Next up: **Remix System Manual** — how Phase OS assembles your saved fragments into a remix-ready workspace.
