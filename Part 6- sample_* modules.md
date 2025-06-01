📘 Phase OS Manual Part 6: sample_* Modules

🎧 Purpose

The sample_* modules are the API and intelligence surface for your Oracle data.

They exist to:
	•	Serve audio fragments to external tools
	•	Recommend samples based on tags, usage, and context
	•	Act as the bridge between your stored material and real-time interfaces

⸻

🌐 Core Components

sample_oracle_api.py
	•	Role: RESTful API wrapper for Oracle data
	•	Routes:
	•	/samples → returns all active Oracle entries
	•	/samples/tags/{tag} → returns entries filtered by tag
	•	/samples/random → returns a single random approved fragment
	•	Backend: FastAPI
	•	Purpose: Enables external tools, dashboards, and DAWs to query Oracle content

⸻

sample_suggestion_engine.py
	•	Role: Intelligent surface
	•	Function:
	•	Parses fragment_index.md, oracle_dynamic.json, and voice/context metadata
	•	Suggests next samples based on:
	•	Most-used tags
	•	Least-used tags
	•	Recently saved fragments
	•	Phase-aware biases (e.g., Generator prefers ambient samples)
	•	Can be expanded into real-time recommender

⸻

📁 Output Files
	•	suggested_samples.md (optional): Inline or session-local sample picks
	•	/samples/random?phase=Builder (API expansion): Scoped entropy

⸻

🧠 Why It’s Powerful
	•	Turns your archive into a living library
	•	Surfaces what you’ve forgotten you saved
	•	Enables external tools (browser, sampler, AI DAW) to access your personal material
	•	Paves the way for contextual sample injection into downstream tools

⸻

💡 Tips
	•	Use sample_oracle_api.py to plug fragments into Ableton, TidalCycles, SuperCollider
	•	Combine with voice_context_stream.py for semantic filtering (e.g. “Show me all hiss samples tagged anxiety”)
	•	Run as background API server for other modules to ping

⸻

Next: tag_* module family — memory reflection, annotation, and dashboard layers.