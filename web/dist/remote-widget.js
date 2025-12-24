const root = document.getElementById("remote-widget-root");
const state = window.openai || {};
const toolOutput = state.toolOutput || {};
const promptText = toolOutput.prompt || "Request a prompt from the MCP tool to see it here.";
const workspaceGoal = toolOutput.workspaceGoal || "";

function render() {
  root.innerHTML = `
    <section class="widget">
      <header>
        <p class="eyebrow">Remote Workspace Prompt</p>
        <h1>Bootstrap a clean coding session</h1>
        <p class="lede">Designed for cloning repos, running commands, and iterating transparently.</p>
      </header>
      <div class="panel">
        <div class="panel-row">
          <div>
            <p class="label">Stated goal</p>
            <p class="value">${workspaceGoal || "(use the tool to pass a goal)"}</p>
          </div>
          <button class="ghost" onclick="window.openai?.callTool?.('remote_workspace_prompt', { workspaceGoal: '${workspaceGoal.replace(/'/g, "\\'")}' })">Refresh prompt</button>
        </div>
        <p class="label">Prompt</p>
        <pre class="prompt">${promptText}</pre>
      </div>
    </section>
  `;

  state.notifyIntrinsicHeight?.();
}

render();
