---
name: install-verifiedx
description: Install VerifiedX into an existing codebase through the smallest supported seam. Use when a builder asks to add VerifiedX, guard high-impact actions, protect a production agent workflow, or integrate VerifiedX into an already-built app without redesigning the system.
---

# Install VerifiedX

Install VerifiedX into the repo that is already in front of you. Do not scaffold a new app, do not invent a fallback workflow, and do not ask the builder to enumerate guarded actions by hand.

## Core Rule

VerifiedX must fit the builder's existing architecture in a few lines. Always choose the least invasive supported seam that already exists in the codebase.

## Workflow

1. Detect the repo's best VerifiedX seam first.
   - If `verifiedx` is already installed in the repo environment, run `verifiedx verify --json --cwd <repo-root>`.
   - Otherwise run `npx -y @verifiedx-core/sdk@latest verify --json --cwd <repo-root>`.
2. Read `references/supported-stacks.md`.
3. Read only the recipe file that matches `recommended.kind` from the verify output.
4. If no supported target is detected, stop and say so plainly instead of guessing.
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
