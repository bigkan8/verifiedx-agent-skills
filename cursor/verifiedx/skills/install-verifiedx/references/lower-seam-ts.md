# TypeScript lower-seam install

Use this recipe only when `verifiedx verify --json` returns `recommended.kind = "lower_seam_ts"`.

Docs source: `https://docs.verifiedx.me/sdks/typescript`

## Goal

Activate VerifiedX once at startup and let the SDK patch supported lower seams already used by the app, including fetch, pg, amqplib, and file writes.

## Minimal patch

1. Install `@verifiedx-core/sdk`.
2. Import `initVerifiedX` from `@verifiedx-core/sdk`.
3. Call `await initVerifiedX()` once during startup.
4. Leave the app's own business logic untouched.

## Covered seams

- `globalThis.fetch` and `undici.fetch`
- `node:fs/promises.writeFile` and `appendFile`
- `fs.writeFileSync` and `appendFileSync`
- `pg.Client.query` and `pg.Pool.query`
- `amqplib.Channel.publish` and `sendToQueue`

If the repo needs business-level named boundaries instead of only these transport/runtime seams, also read `raw-typescript-runtime.md`.

## Do not

- wrap every callsite manually if the startup lower-seam install is enough
- create a fake orchestrator or fallback workflow
- turn off lower-seam fallbacks unless the repo already has a stronger native adapter seam in place
