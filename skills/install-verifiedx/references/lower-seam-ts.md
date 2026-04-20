# TypeScript lower-seam install

Use this recipe only when `verifiedx verify --json` returns `recommended.kind = "lower_seam_ts"`.

## Goal

Activate VerifiedX once at startup and let the SDK patch supported lower seams already used by the app, including fetch, pg, amqplib, and file writes.

## Minimal patch

1. Install `@verifiedx-core/sdk`.
2. Import `initVerifiedX` from `@verifiedx-core/sdk`.
3. Call `await initVerifiedX()` once during startup.
4. Leave the app's own business logic untouched.

## Do not

- wrap every callsite manually if the startup lower-seam install is enough
- create a fake orchestrator or fallback workflow
- turn off lower-seam fallbacks unless the repo already has a stronger native adapter seam in place
