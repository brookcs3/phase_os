# ChatGPT Remote Workspace App

This repository reboots the workspace into a minimal ChatGPT app scaffold designed for terminal-first workflows. The included prompt teaches ChatGPT how to clone GitHub repositories, download artifacts, run code, and report progress while staying aligned with MCP widget flows.

## What changed
- All previous files now live in `./backup_phase_os/` for safekeeping.
- A new prompt (`prompt/PROMPT.md`) defines the operating rules for remote-terminal work.
- A lightweight MCP server (`server/index.js`) exposes the prompt through a `remote_workspace_prompt` tool and serves a widget template.
- A simple widget bundle in `web/dist/` renders the prompt and allows refreshes inside ChatGPT.

## Project layout
```
chatgpt-remote-workspace-app/
├─ prompt/PROMPT.md          # The canonical remote-terminal prompt
├─ server/index.js           # MCP server registering the widget + tool
├─ web/dist/remote-widget.*  # Inlineable HTML/CSS/JS used by the widget template
└─ backup_phase_os/          # Archived prior contents of the directory
```

## Running locally
1. Install dependencies (network access may be required):
   ```bash
   npm install
   ```
2. Start the MCP server:
   ```bash
   npm start
   ```
3. Point MCP Inspector or ChatGPT dev mode to `http://localhost:3000/mcp` to exercise the `remote_workspace_prompt` tool.

If dependency installation is blocked by registry access, you can still read the prompt directly from `prompt/PROMPT.md` and wire it into your own server stack.

## Prompt overview
The prompt emphasizes:
- Clear goals and workspace hygiene
- Quick repository pulls and reproducible commands
- Careful edits guided by project documentation
- Honest testing and transparent summaries

Use it as a starting point for any conversation that requires cloning, running, or inspecting code with the remote terminal.
