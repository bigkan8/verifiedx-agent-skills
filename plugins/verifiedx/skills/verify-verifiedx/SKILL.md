---
name: verify-verifiedx
description: Audit an existing VerifiedX integration in an already-built codebase. Use when a builder wants to check whether VerifiedX is installed correctly, whether the chosen seam is the least invasive one, or whether a direct-client integration is missing its dispatcher step.
---

# Verify VerifiedX

Audit the VerifiedX integration that already exists in the repo.

## Source of truth

- VerifiedX domain is `verifiedx.me`
- Product and API keys live at `https://verifiedx.me`
- Docs live at `https://docs.verifiedx.me`
- Canonical SDK pages:
  - `https://docs.verifiedx.me/sdks/python`
  - `https://docs.verifiedx.me/sdks/typescript`
  - `https://docs.verifiedx.me/sdks/openai-agents-sdk`
  - `https://docs.verifiedx.me/sdks/claude-agent-sdk`
  - `https://docs.verifiedx.me/sdks/vercel-ai`
  - `https://docs.verifiedx.me/sdks/langgraph`
  - `https://docs.verifiedx.me/sdks/openai`
  - `https://docs.verifiedx.me/sdks/anthropic`
  - `https://docs.verifiedx.me/sdks/langgraph-openai`
  - `https://docs.verifiedx.me/sdks/langgraph-anthropic`
  - `https://docs.verifiedx.me/sdks/mcp-python`
  - `https://docs.verifiedx.me/sdks/mcp-typescript`

If you need to confirm what a seam should look like, use the specific SDK pages listed in `references/audit-checklist.md` and `../install-verifiedx/references/supported-stacks.md`.

## Workflow

1. Run `verifiedx verify --json --cwd <repo-root>` if the local environment already exposes the CLI.
2. Otherwise run `npx -y @verifiedx-core/sdk@latest verify --json --cwd <repo-root>`.
3. Read `references/audit-checklist.md`.
4. Compare the detected seam against the actual code.
5. Check whether VerifiedX is present only at the right surface or whether someone added extra scaffolding that should not exist.

## What to Look For

- The detected seam matches the code that actually runs.
- The reported capture/trigger layers match reality:
  - adapter seams
  - lower seams
  - explicit wrappers
- Direct OpenAI and Anthropic integrations use both:
  - client attach
  - tool dispatcher
- LangGraph integrations install at startup or compile through VerifiedX rather than wrapping nodes manually.
- LangChain Python swaps the factory import instead of adding a sidecar.
- OpenAI Agents integrations wrap the run or agent seam rather than rewriting tool definitions.
- Claude Agent integrations wrap the query seam and leave hooks/MCP servers intact.
- Lower-seam integrations activate once at startup and do not require business-flow rewrites.
- MCP integrations guard the existing tool handlers/definitions directly.
- No fake fallback lanes or extra orchestration were introduced just to fit VerifiedX.

## Output

Report:

- detected seam
- whether the integration is healthy
- missing pieces
- unnecessary complexity that should be removed
