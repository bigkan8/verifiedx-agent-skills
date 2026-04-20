# Python MCP wrapper install

Use this recipe only when `verifiedx verify --json` returns `recommended.kind = "mcp_py"`.

## Goal

Guard the repo's existing MCP tools directly at the tool boundary.

## Minimal patch

1. Install `verifiedx`.
2. Import `wrap_tool_handler` or `wrap_tool_definition` from `verifiedx`.
3. Wrap the existing MCP tool handler or definition at registration time.
4. Keep the existing server topology, transport, and orchestration intact.

## Do not

- build a second MCP server just for VerifiedX
- move business logic out of the existing tool handlers
