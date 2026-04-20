# Python lower-seam install

Use this recipe only when `verifiedx verify --json` returns `recommended.kind = "lower_seam_py"`.

## Goal

Activate VerifiedX once at startup and let the SDK patch supported lower seams already used by the app, including requests/httpx, DB connectors, queues, browser automation, and supported cloud/runtime seams.

## Minimal patch

1. Install `verifiedx`.
2. Import `init_verifiedx` from `verifiedx`.
3. Create one runtime with `vx = init_verifiedx()`.
4. Call `vx.install_runtime()` once during startup.
5. Leave the app's own business logic untouched.

## Do not

- wrap every function manually if the runtime install already covers the seam
- add demo-only workflow branches
- restructure the app around VerifiedX
