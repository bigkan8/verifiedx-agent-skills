# langgraph_ts

- SDK surface: `@verifiedx-core/sdk/langgraph`
- Minimal seam: call `install()` before graph compilation or import `compile()` from the adapter

## Apply

1. Install `@verifiedx-core/sdk`.
2. Import `install` or `compile` from `@verifiedx-core/sdk/langgraph`.
3. Activate VerifiedX before `StateGraph.compile()`.

## What the adapter really does

- patches `StateGraph.compile`
- patches `StructuredTool.call`
- patches `ToolNode.runTool`

Do not wrap every node manually.
