# 📘 Phase OS Manual Part 2: `oracle_*` Modules

## 🔮 Purpose

The `oracle_*` modules form the **Sample Oracle** — a subsystem dedicated to discovering, curating, slicing, and archiving audio fragments. It acts as your external memory, cultural informant, and texture recommender. The Oracle is intentionally frictional: you must engage with each sample to save it.

This system is your memory scaffolder — not a bulk scraper.

---

## 📂 Components Overview

### 🗃️ Discovery + Ingestion

#### `oracle_playlist_miner.py`

* **Role**: Mines YouTube for crate-digging-style playlists
* **Method**: Uses `yt-dlp` to run `ytsearch10:` with smart queries like "rare vinyl mix", stores found playlists in `oracle_playlists.txt`

#### `oracle_weekly_playlist_job.py`

* **Role**: Scheduled job to refresh Oracle content weekly
* **Function**: Combines `playlist_miner.py` + `seed_engine.py`
* **Schedule**: Sunday 2 AM (via `digest_scheduler.py`)

#### `oracle_seed_engine.py`

* **Role**: Downloads audio from playlists into `oracle_clips/`
* **Function**: Pulls top 3 tracks from each playlist
* **Output**: Updates `oracle_dynamic.json` (sample metadata store)

#### `oracle_auto_scraper.py`

* **Role**: Alt mode to perform `ytsearch3:` queries from `oracle_search_terms.py`
* **Purpose**: Query-tuned scraper that fetches short samples based on themes

#### `oracle_search_terms.py`

* **Role**: Centralized bank of terms like "glitch choir", "dusty breakbeat"
* **Function**: Provides entropy to search-based scraping

---

## 🎧 Curation UI

#### `oracle_curator_ui.py`

* **Role**: Web app to play each scraped sample and log user decision
* **Flow**:

  1. Sample loads with metadata
  2. User clicks: 💾 Save / 🗑️ Delete / ⏭️ Next
  3. On Save → redirect to waveform editor

#### `oracle_wave_editor.html`

* **Role**: Web-based waveform visualizer + region slicer
* **Function**:

  * User drags start/end
  * On Export → slice saved to `oracle_slices/`
  * Triggers slice logger

---

## 📝 Logging + Visual Memory

#### `oracle_slice_logger.py`

* **Role**: Logs last exported slice into `fragment_index.md`
* **Fields**: session ID, timestamp, path

#### `oracle_slice_visual_logger.py`

* **Role**: Captures screenshot at time of slice and logs with audio
* **Output**: stored in `oracle_slices_visual/`

#### `oracle_remix_session.py`

* **Role**: Copies all logged slices into fresh `remix_session_*` folder
* **Invoked by**: Builder phase

---

## 📊 Browsers + Reflections

#### `oracle_fragment_browser.py`

* **Role**: Web UI that displays all saved slices with screenshots
* **Usage**: Used during Recovery phase for reflection

#### `oracle_moodboard_generator.py`

* **Role**: Random prompt generator during Generator phase
* **Function**: Combines themes, textures, verbs, forms into a stylized prompt

---

## 🧠 What Makes It Powerful

* Forces mindful interaction with each sample
* Embeds voice + vision in every fragment
* Reuses your own saved history as raw material
* Fully integrated with your session + identity context

## 💡 Tips

* Set your own `oracle_search_terms.py` themes
* Clip only what speaks to the mood
* Use `oracle_fragment_browser.py` to spot aesthetic drift
* Re-seed Oracle weekly via `digest_scheduler`

---

Next up: `builder_*` module system — form map logic, versioning, and track structure memory.
