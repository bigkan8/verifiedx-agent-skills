# langgraph_ts

- SDK surface: `@verifiedx-core/sdk/langgraph`
- Minimal seam: call `install()` before graph compilation or import `compile()` from the adapter
- Docs:
  - generic: `https://docs.verifiedx.me/sdks/langgraph`
  - OpenAI-backed graphs: `https://docs.verifiedx.me/sdks/langgraph-openai`
  - Anthropic-backed graphs: `https://docs.verifiedx.me/sdks/langgraph-anthropic`

## Apply

1. Install `@verifiedx-core/sdk`.
2. Import `install` or `compile` from `@verifiedx-core/sdk/langgraph`.
3. Activate VerifiedX before `StateGraph.compile()`.
4. If the repo uses `@langchain/openai`, also read `langgraph-openai.md`.
5. If the repo uses `@langchain/anthropic`, also read `langgraph-anthropic.md`.

## What the adapter really does

- patches `StateGraph.compile`
- patches `StructuredTool.call`
- patches `ToolNode.runTool`
- preserves the existing graph topology, store, checkpointer, and tool registry

Do not wrap every node manually.
