# openai_direct_ts

- SDK surface: `@verifiedx-core/sdk/openai-direct`
- Minimal seam: `attach()` the OpenAI client and dispatch local tool calls through `createToolDispatcher()`

## Apply

1. Install `@verifiedx-core/sdk`.
2. Import `attach` and `createToolDispatcher`.
3. Wrap the existing OpenAI client with `attach(client, { verifiedx })`.
4. Replace direct local tool handler execution with the dispatcher.

## Important

`attach()` records the request surface. The dispatcher is what guards the exact local handler execution.
