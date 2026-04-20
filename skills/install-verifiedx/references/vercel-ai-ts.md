# vercel_ai_ts

- SDK surface: `@verifiedx-core/sdk/vercel-ai`
- Minimal seam: wrap `generateText`, `streamText`, or `ToolLoopAgent`

## Apply

1. Install `@verifiedx-core/sdk`.
2. Import `withVerifiedXGenerateText`, `withVerifiedXStreamText`, or `withVerifiedXToolLoopAgent`.
3. Wrap the existing generation entrypoint.

## Do not do

- do not rewrite tools
- do not create a new agent loop
