# Python MCP wrapper install

Use this recipe only when `verifiedx verify --json` returns `recommended.kind = "mcp_py"`.

Docs source: `https://docs.verifiedx.me/sdks/mcp-python`

## Goal

Guard the repo's existing MCP tools directly at the tool boundary.

## Minimal patch

1. Install `verifiedx`.
2. Import `wrap_tool_handler` or `wrap_tool_definition` from `verifiedx`.
3. Boundary protection lives in `wrap_tool_handler()`. Use `wrap_tool_definition()` only to enrich definitions you expose from `listTools()`.
4. If a tool is definitely a durable memory write, pass `policy_scope="memory_write"` instead of relying only on name heuristics.
4. Keep the existing server topology, transport, and orchestration intact.

## Important

- This path is for standalone MCP servers or handlers you own directly.
- If MCP is being surfaced through OpenAI Agents or another higher-level SDK, use that native adapter page instead.
- `wrap_tool_handler()` is a thin adapter over VerifiedX core boundary wrappers. It uses the same preflight, decision-receipt, execution-report, and runtime-loopback path as the rest of the product.
- Your tool names, descriptions, schemas, and params shape remain the source of truth.

## Do not

- build a second MCP server just for VerifiedX
- move business logic out of the existing tool handlers
