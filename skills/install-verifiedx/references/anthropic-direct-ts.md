# anthropic_direct_ts

- SDK surface: `@verifiedx-core/sdk/anthropic-direct`
- Minimal seam: `attach()` the Anthropic client and dispatch local tool uses through `createToolDispatcher()`

## Apply

1. Install `@verifiedx-core/sdk`.
2. Import `attach` and `createToolDispatcher`.
3. Wrap the existing Anthropic client with `attach(client, { verifiedx })`.
4. Replace direct local tool handler execution with the dispatcher.

## Important

`attach()` alone is not enough for local tool execution blocking. The dispatcher is required for the exact handler boundary.
