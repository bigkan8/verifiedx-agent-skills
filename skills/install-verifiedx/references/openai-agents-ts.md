# openai_agents_ts

- SDK surface: `@verifiedx-core/sdk/openai-agents`
- Minimal seam: wrap the existing runner or agent entrypoint

## Apply

1. Install `@verifiedx-core/sdk`.
2. Import `withVerifiedXAgent`, `withVerifiedXRunner`, or `run` from `@verifiedx-core/sdk/openai-agents`.
3. Replace the existing run surface with the VerifiedX wrapper.

## Do not do

- do not rewrite tool definitions
- do not change handoffs
- do not create a new orchestration layer
