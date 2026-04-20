# TypeScript MCP wrapper install

Use this recipe only when `verifiedx verify --json` returns `recommended.kind = "mcp_ts"`.

Docs source: `https://docs.verifiedx.me/sdks/mcp-typescript`

## Goal

Guard the repo's existing MCP tools directly at the tool boundary.

## Minimal patch

1. Install `@verifiedx-core/sdk`.
2. Import `wrapMcpTool` from `@verifiedx-core/sdk/mcp`.
3. Wrap the existing MCP tool handler where it is registered.
4. If a tool is definitely a durable memory write, pass `policyScope: "memory_write"` instead of relying only on name heuristics.
4. Keep the existing server topology, transport, and orchestration intact.

## Important

- This path is for standalone MCP servers or handlers you own directly.
- If MCP is being surfaced through OpenAI Agents or another higher-level SDK, use that native adapter page instead.
- `wrapMcpTool()` is a thin adapter over VerifiedX core boundary wrappers. It uses the same preflight, decision-receipt, execution-report, and runtime-loopback path as the rest of the product.
- Your tool names, descriptions, schemas, and params shape remain the source of truth.

## Do not

- build a second MCP server just for VerifiedX
- move business logic out of the existing tool handlers
