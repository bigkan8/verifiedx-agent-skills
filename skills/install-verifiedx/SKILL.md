---
name: install-verifiedx
description: Install VerifiedX into an existing codebase through the smallest supported seam. Use when a builder asks to add VerifiedX, guard high-impact actions, protect a production agent workflow, or integrate VerifiedX into an already-built app without redesigning the system.
---

# Install VerifiedX

Install VerifiedX into the repo that is already in front of you. Do not scaffold a new app, do not invent a fallback workflow, and do not ask the builder to enumerate guarded actions by hand.

## Source of truth

- VerifiedX domain is `verifiedx.me`
- Get API keys at `https://verifiedx.me`
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

If you get stuck, go to `https://docs.verifiedx.me` and pick the exact SDK page from `references/supported-stacks.md`. Never guess another domain such as `.com` or `.io`.

## Core Rule

VerifiedX must fit the builder's existing architecture in a few lines. Always choose the least invasive supported seam that already exists in the codebase.

## Workflow

1. Detect the repo's best VerifiedX seam first.
   - If `verifiedx` is already installed in the repo environment, run `verifiedx verify --json --cwd <repo-root>`.
   - Otherwise run `npx -y @verifiedx-core/sdk@latest verify --json --cwd <repo-root>`.
2. Read `references/supported-stacks.md`.
3. Read the recipe file that matches `recommended.kind` from the verify output.
   - If the seam is `lower_seam_ts`, also read `references/raw-typescript-runtime.md`.
   - If the seam is `lower_seam_py`, also read `references/raw-python-runtime.md`.
   - If the seam is `mcp_ts` or `mcp_py`, also read `references/manual-explicit.md`.
   - If the repo is a custom harness or already uses `bindHarness()` / `bind_harness()`, also read `references/manual-explicit.md`.
   - If the seam is `langgraph_ts` or `langgraph_py` and the repo uses OpenAI LangGraph providers, also read `references/langgraph-openai.md`.
   - If the seam is `langgraph_ts` or `langgraph_py` and the repo uses Anthropic LangGraph providers, also read `references/langgraph-anthropic.md`.
4. If no supported target is detected:
   - use the raw Python SDK page when the repo is a custom Python harness you own
   - use the raw TypeScript SDK page when the repo is a custom TypeScript harness you own
   - otherwise stop and say so plainly instead of guessing
5. Install the SDK package using `recommended.install_command`.
6. Run `npx -y @verifiedx-core/sdk@latest init --write --json --cwd <repo-root>` to generate `.verifiedx/install-plan.json` and env placeholders.
7. Apply only the minimal patch for the detected recipe.
8. Re-run verification:
   - `verifiedx verify --json --cwd <repo-root>` if the installed environment exposes the CLI
   - otherwise `npx -y @verifiedx-core/sdk@latest verify --json --cwd <repo-root>`
9. Run the repo's own fast validation if it is cheap and already configured.

## Non-Negotiables

- Do not create a new orchestration layer.
- Do not redesign the agent graph.
- Do not add synthetic fallback lanes.
- Do not change the business workflow just to make VerifiedX easier to show.
- Do not ask the user to list "important actions." VerifiedX should integrate at the seam the code already uses.
- Treat all three VerifiedX layers as real:
  - adapter seams
  - lower seams
  - explicit wrappers
- Prefer the least invasive real seam, not the most marketing-friendly one.
- If the repo already uses a lower-seam or explicit-wrapper path, preserve it and harden it instead of forcing an adapter rewrite.

## Output

When the install is complete, report:

- detected integration kind
- exact files changed
- package installed
- verification result
- any remaining manual environment setup
