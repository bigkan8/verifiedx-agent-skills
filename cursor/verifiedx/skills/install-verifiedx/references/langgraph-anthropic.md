# LangGraph with Anthropic providers

Use this reference when the repo already uses LangGraph and the model provider is Claude through:

- `langchain_anthropic`
- `@langchain/anthropic`

Docs source: `https://docs.verifiedx.me/sdks/langgraph-anthropic`

## Real seam

This is still the LangGraph adapter seam, not the raw Anthropic direct seam.

- TypeScript: `@verifiedx-core/sdk/langgraph`
- Python: `install_langgraph()` or `compile()` from `verifiedx`

## What to preserve

- `StateGraph` topology
- existing nodes
- `ToolNode`
- stores
- checkpointers
- provider model wiring through LangGraph and LangChain

Do not drop down to `anthropic-direct` inside the graph unless the repo actually owns a separate Claude Messages tool loop outside LangGraph.
