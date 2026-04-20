# Audit checklist

## Universal

- `verifiedx verify --json` returns a supported `recommended.kind`
- `verifiedx verify --json` reports the right capture/trigger layer for the repo:
  - `adapter`
  - `lower_seam`
  - `explicit_wrapper`
- `.verifiedx/install-plan.json` exists if the repo was initialized with `verifiedx init --write`
- env placeholders or real env vars exist for:
  - `VERIFIEDX_API_KEY`
  - `VERIFIEDX_AGENT_ID`
  - `VERIFIEDX_SOURCE_SYSTEM`

## Direct clients

For `openai_direct_*` and `anthropic_direct_*`, attach alone is not enough. The code should also route local tool execution through the VerifiedX dispatcher.

## LangGraph

The repo should install or compile through the LangGraph adapter. It should not wrap individual nodes manually to simulate support.

## LangChain Python

The clean seam is the `create_agent` factory replacement from `verifiedx.langchain`.

## Claude Agent SDK

The clean seam is the query wrapper. Hooks, MCP servers, and built-in tools should stay in the builder's own workflow.

## OpenAI Agents

The clean seam is the runner or agent surface. Tool implementations and handoffs should not be rewritten just to fit VerifiedX.

## Lower seams

Startup install should be enough:

- TypeScript: `initVerifiedX()` with lower-seam fallbacks
- Python: `init_verifiedx()` plus `install_runtime()`

If the repo uses this layer, it should not have been rewritten into a fake adapter demo.

## MCP / explicit wrappers

MCP integrations should wrap the existing handler or definition:

- TypeScript: `wrapMcpTool()`
- Python: `wrap_tool_handler()` or `wrap_tool_definition()`

Custom explicit wrapper repos should preserve the builder's own harness/tool surface instead of introducing a new orchestration layer.
