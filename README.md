# VerifiedX Agent Skills

Public install surfaces for adding VerifiedX to an existing codebase through the smallest real capture/trigger seam.

This repo does not re-implement VerifiedX. It teaches coding agents how to:

1. inspect a repo with `verifiedx verify`
2. read the repo's actual capture/trigger layer shape
3. choose the least invasive supported VerifiedX seam
4. apply only the minimal patch for that seam
5. validate that the app still works

Builders already have systems. VerifiedX should fit those systems in a few lines, not force them to redesign their product around a demo harness.

## VerifiedX domains

- Product and API keys: [https://verifiedx.me](https://verifiedx.me)
- Docs: [https://docs.verifiedx.me](https://docs.verifiedx.me)

If an agent gets stuck, it should use `docs.verifiedx.me` and pick the specific SDK page that matches the repo instead of guessing.

## What This Repo Ships

- Agent Skills standard skills for install and audit flows
- Codex plugin packaging
- Claude Code custom marketplace packaging
- Cursor custom marketplace packaging

## Current public SDKs

- TypeScript: `@verifiedx-core/sdk@0.1.18`
- Python: `verifiedx==0.1.9`

## Canonical SDK pages

- Python SDK: [https://docs.verifiedx.me/sdks/python](https://docs.verifiedx.me/sdks/python)
- TypeScript SDK: [https://docs.verifiedx.me/sdks/typescript](https://docs.verifiedx.me/sdks/typescript)
- OpenAI Agents SDK: [https://docs.verifiedx.me/sdks/openai-agents-sdk](https://docs.verifiedx.me/sdks/openai-agents-sdk)
- Claude Agent SDK: [https://docs.verifiedx.me/sdks/claude-agent-sdk](https://docs.verifiedx.me/sdks/claude-agent-sdk)
- Vercel AI SDK: [https://docs.verifiedx.me/sdks/vercel-ai](https://docs.verifiedx.me/sdks/vercel-ai)
- LangGraph: [https://docs.verifiedx.me/sdks/langgraph](https://docs.verifiedx.me/sdks/langgraph)
- OpenAI direct: [https://docs.verifiedx.me/sdks/openai](https://docs.verifiedx.me/sdks/openai)
- Anthropic / Claude direct: [https://docs.verifiedx.me/sdks/anthropic](https://docs.verifiedx.me/sdks/anthropic)
- LangGraph (OpenAI): [https://docs.verifiedx.me/sdks/langgraph-openai](https://docs.verifiedx.me/sdks/langgraph-openai)
- LangGraph (Anthropic / Claude): [https://docs.verifiedx.me/sdks/langgraph-anthropic](https://docs.verifiedx.me/sdks/langgraph-anthropic)
- MCP Python: [https://docs.verifiedx.me/sdks/mcp-python](https://docs.verifiedx.me/sdks/mcp-python)
- MCP TypeScript: [https://docs.verifiedx.me/sdks/mcp-typescript](https://docs.verifiedx.me/sdks/mcp-typescript)

## VerifiedX capture/trigger layers

### 1. Adapter seams

Use the framework-native adapter when the repo already runs through one:

- TypeScript OpenAI Agents
- TypeScript Claude Agent SDK
- TypeScript LangGraph
- TypeScript Vercel AI SDK
- TypeScript Anthropic direct
- TypeScript OpenAI direct
- Python LangGraph
- Python LangChain
- Python Claude Agent SDK
- Python OpenAI Agents
- Python Anthropic direct
- Python OpenAI direct

Provider-specialized LangGraph docs are also covered:

- OpenAI-backed graphs: `langgraph-openai`
- Anthropic-backed graphs: `langgraph-anthropic`

### 2. Lower seams

Use the lower-seam runtime install when the repo mainly crosses trust boundaries through transport/runtime surfaces rather than a supported agent adapter:

- TypeScript startup install via `initVerifiedX()` with lower-seam fallbacks
- Python startup install via `init_verifiedx()` plus `install_runtime()`

These paths cover real lower-level seams already in the SDKs, including HTTP, DB, queue, browser, cloud, and file-write interception where supported.

### 3. Explicit wrappers

Use explicit wrapping when the repo exposes MCP tools or a custom harness and the cleanest seam is the specific action/memory/tool boundary itself:

- TypeScript `wrapMcpTool()`, `bindHarness()`, `wrapToolCall()`, `wrapMemoryWrite()`, `wrapActionExecute()`
- Python `wrap_tool_handler()`, `wrap_tool_definition()`, `bind_harness()`, `wrap_tool_call()`, `wrap_memory_write()`, `wrap_action_execute()`

For custom harnesses, the skills repo now also points agents at the raw runtime details the public docs provide:

- lower-seam defaults already captured automatically
- explicit binding categories `llm`, `retrievals`, `actions`, `memories`, and `tools`
- schema and docstring metadata
- composed-system upstream context
- runtime blocked-result and receipt behavior

## Install Surfaces

### skills.sh / Agent Skills

```bash
npx skills add bigkan8/verifiedx-agent-skills
```

Then tell the agent: `Install VerifiedX into this repo.`

### Cursor

Use Cursor's plugin install flow with this repo as the source, then ask:

```text
Install VerifiedX into this repo.
```

The packaged plugin lives in `cursor/verifiedx`.

### Claude Code

Add this repo as a custom plugin marketplace, install the `verifiedx` plugin, then ask:

```text
Install VerifiedX into this repo.
```

The packaged plugin lives in `claude/verifiedx`.

### Codex

Install the skills from this repo or add the packaged Codex plugin, then ask:

```text
Install VerifiedX into this repo.
```

The packaged plugin lives in `plugins/verifiedx`.

## How The Install Flow Works

The install skill:

1. runs `verifiedx verify --json` or an ephemeral `npx @verifiedx-core/sdk` probe
2. reads the recommended integration kind and the detected capture/trigger layers
3. installs the correct SDK package
4. runs `verifiedx init --write`
5. applies only the minimal code change for the detected seam
6. re-runs verification and the repo's own quick validation

It does not:

- scaffold a new system
- ask the builder to enumerate guarded actions
- invent fallback lanes to make VerifiedX look good
- rewrite the product architecture
- downgrade a real lower-seam or explicit-wrapper integration just because the evals happened to use adapters

## Repository Layout

- `skills/`: canonical Agent Skills source of truth
- `plugins/verifiedx/`: Codex plugin packaging
- `claude/verifiedx/`: Claude Code plugin packaging
- `cursor/verifiedx/`: Cursor plugin packaging
- `scripts/validate_repo.py`: packaging validation

## Validate

```bash
python scripts/validate_repo.py
```
