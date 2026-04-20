# TypeScript MCP wrapper install

Use this recipe only when `verifiedx verify --json` returns `recommended.kind = "mcp_ts"`.

## Goal

Guard the repo's existing MCP tools directly at the tool boundary.

## Minimal patch

1. Install `@verifiedx-core/sdk`.
2. Import `wrapMcpTool` from `@verifiedx-core/sdk/mcp`.
3. Wrap the existing MCP tool handler or definition where it is registered.
4. Keep the existing server topology, transport, and orchestration intact.

## Do not

- build a second MCP server just for VerifiedX
- move business logic out of the existing tool handlers
