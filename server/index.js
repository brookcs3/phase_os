import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

const server = new McpServer({ name: "remote-workspace", version: "0.1.0" });

const css = readFileSync(resolve("web/dist/remote-widget.css"), "utf8");
const js = readFileSync(resolve("web/dist/remote-widget.js"), "utf8");

server.registerResource(
  "remote-workspace-widget",
  "ui://widget/remote-workspace.html",
  {},
  async () => ({
    contents: [
      {
        uri: "ui://widget/remote-workspace.html",
        mimeType: "text/html+skybridge",
        text: `
<div id="remote-widget-root"></div>
<style>${css}</style>
<script type="module">${js}</script>
        `.trim(),
        _meta: {
          "openai/widgetPrefersBorder": true,
          "openai/widgetDescription": "Displays the remote workspace prompt so builders can copy or refresh it.",
          "openai/widgetCSP": {
            connect_domains: [],
            resource_domains: ["https://*.oaistatic.com"],
          },
        },
      },
    ],
  })
);

const loadPrompt = () => readFileSync(resolve("prompt/PROMPT.md"), "utf8");

server.registerTool(
  "remote_workspace_prompt",
  {
    title: "Show remote workspace prompt",
    description: "Returns the terminal-first prompt for cloning repos and running code with the MCP server.",
    inputSchema: {
      type: "object",
      properties: {
        workspaceGoal: { type: "string", description: "Goal or task to anchor the prompt" },
      },
      required: [],
      additionalProperties: false,
    },
    _meta: {
      "openai/outputTemplate": "ui://widget/remote-workspace.html",
      "openai/toolInvocation/invoking": "Loading remote workspace prompt…",
      "openai/toolInvocation/invoked": "Remote workspace prompt ready.",
      "openai/widgetAccessible": true,
    },
  },
  async ({ workspaceGoal = "" }) => {
    const prompt = loadPrompt();

    return {
      structuredContent: {
        prompt,
        workspaceGoal,
      },
      content: [
        {
          type: "text",
          text: workspaceGoal
            ? `Remote workspace prompt prepared for goal: ${workspaceGoal}`
            : "Remote workspace prompt prepared.",
        },
      ],
      _meta: {
        prompt,
        workspaceGoal,
      },
    };
  }
);

const PORT = Number(process.env.PORT || 3000);
server.listen({ port: PORT, host: "0.0.0.0" });
console.log(`MCP server listening on http://0.0.0.0:${PORT}/mcp`);
