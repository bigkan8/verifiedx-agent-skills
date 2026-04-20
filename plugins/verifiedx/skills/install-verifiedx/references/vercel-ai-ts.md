# vercel_ai_ts

- SDK surface: `@verifiedx-core/sdk/vercel-ai`
- Minimal seam: wrap `generateText`, `streamText`, or `ToolLoopAgent`
- Docs: `https://docs.verifiedx.me/sdks/vercel-ai`

## Apply

1. Install `@verifiedx-core/sdk`.
2. Import `withVerifiedXGenerateText`, `withVerifiedXStreamText`, or `withVerifiedXToolLoopAgent`.
3. Wrap the existing generation entrypoint that the repo already uses.
4. Keep the existing tool definitions, `onStepFinish`, `experimental_onToolCallStart`, and `experimental_onToolCallFinish` flow intact.

## Do not do

- do not rewrite tools
- do not create a new agent loop
