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

1. Run the one-shot installer first.
   - `npx -y @verifiedx-core/sdk@latest install --cwd <repo-root>`
   - Agentic install is the default. `--mode standalone` exists only for precision comparison, not as the normal path.
   - If the builder already has a local SDK checkout or preinstalled `verifiedx`, use the local equivalent only when that is clearly the repo's active install path.
2. Read `.verifiedx/install-plan.json` or rerun verify if you need to inspect the seam selection:
   - If `verifiedx` is already installed in the repo environment, run `verifiedx verify --json --cwd <repo-root>`.
   - Otherwise run `npx -y @verifiedx-core/sdk@latest verify --json --cwd <repo-root>`.
3. Read `references/supported-stacks.md`.
4. Read the recipe file that matches `recommended.kind` from the verify output.
   - If the seam is `lower_seam_ts`, also read `references/raw-typescript-runtime.md`.
   - If the seam is `lower_seam_py`, also read `references/raw-python-runtime.md`.
   - If the seam is `mcp_ts` or `mcp_py`, also read `references/manual-explicit.md`.
   - If the repo is a custom harness or already uses `bindHarness()` / `bind_harness()`, also read `references/manual-explicit.md`.
   - If the seam is `langgraph_ts` or `langgraph_py` and the repo uses OpenAI LangGraph providers, also read `references/langgraph-openai.md`.
   - If the seam is `langgraph_ts` or `langgraph_py` and the repo uses Anthropic LangGraph providers, also read `references/langgraph-anthropic.md`.
5. If no supported target is detected:
   - use the raw Python SDK page when the repo is a custom Python harness you own
   - use the raw TypeScript SDK page when the repo is a custom TypeScript harness you own
   - otherwise stop and say so plainly instead of guessing
6. If the one-shot command pauses for explicit manual steering, inspect `.verifiedx/agentic-review.json`, `.verifiedx/agentic-playbook.md`, and `.verifiedx/agentic-runner-prompt.md` before touching repo-owned business methods.
   - Determine topology yourself from the codebase and set `.verifiedx/agentic-review.json` to `single` or `multi_agent`.
   - Never guess topology from names alone.
   - If the repo mixes a native adapter with repo-owned business methods, keep the native seam native and review the business methods separately.
   - The coding agent is responsible for the final repo-native patch placement in the agentic path.
7. Apply only the minimal additive patch for the detected recipe when manual steering is actually needed.
   - Use the exact docs page and local reference file that match the detected seam.
   - For repo-owned custom harness methods, inspect actual repo semantics and actual code effects:
     - keep harmless helpers, retrievals, and collection methods in capture-only surfaces
     - promote only real high-impact mutations into `actions` or `memories`
   - Some tool-like business methods are still the real high-impact boundary. Put those in `actions` when the repo semantics say they are actual mutations.
   - For `multi_agent` systems, do actual orchestration work:
     - wire upstream context at the real parent-to-child boundary
     - keep blocked receipts and runtime loopbacks flowing back to the caller/orchestrator upstream
     - do not stop at classification
   - For native direct adapters, exact local tool execution blocking requires the dispatcher as well as the client attach.
   - Prefer existing schema/docstring metadata when the repo already has it.
8. If manual steering was needed, apply the completed coding-agent review:
   - `npx -y @verifiedx-core/sdk@latest apply-agentic-review --cwd <repo-root>`
   - If the repo exposes the installed CLI, `verifiedx apply-agentic-review --cwd <repo-root>` is fine too.
   - This step validates the repo-native edits and runs the smoke pass. It is not the place to rely on a generic custom-binding inserter.
9. Re-run verification if you need a post-install audit:
   - `verifiedx verify --json --cwd <repo-root>` if the installed environment exposes the CLI
   - otherwise `npx -y @verifiedx-core/sdk@latest verify --json --cwd <repo-root>`
10. Run the repo's own fast validation if it is cheap and already configured.

## Non-Negotiables

- Do not create a new orchestration layer.
- Do not redesign the agent graph.
- Do not add synthetic fallback lanes.
- Do not change the business workflow just to make VerifiedX easier to show.
- Do not ask the user to list "important actions." VerifiedX should integrate at the seam the code already uses.
- Do not guess custom high-impact actions from keywords.
- Do not guess topology either. Decide `single` vs `multi_agent` from the actual orchestration code.
- For raw or mixed custom harnesses, inspect the actual method bodies and repo semantics before routing methods into capture-only or trigger categories.
- Treat all three VerifiedX layers as real:
  - adapter seams
  - lower seams
  - explicit wrappers
- Prefer the least invasive real seam, not the most marketing-friendly one.
- If the repo already uses a lower-seam or explicit-wrapper path, preserve it and harden it instead of forcing an adapter rewrite.
- Never break the builder's working product just to make VerifiedX more visible. Patches must stay lightweight, additive, and reversible.
- Do not silently fall back to standalone install when the agentic path needs help. The only valid fallback is explicit manual continuation of the same agentic review.

## Output

When the install is complete, report:

- detected integration kind
- exact files changed
- package installed
- verification result
- any remaining manual environment setup
