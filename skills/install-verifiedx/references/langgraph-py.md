# langgraph_py

- SDK surface: `verifiedx.install_langgraph` or `verifiedx.compile`
- Minimal seam: install once before compilation or compile through VerifiedX
- Docs:
  - generic: `https://docs.verifiedx.me/sdks/langgraph`
  - OpenAI-backed graphs: `https://docs.verifiedx.me/sdks/langgraph-openai`
  - Anthropic-backed graphs: `https://docs.verifiedx.me/sdks/langgraph-anthropic`

## Apply

1. Install `verifiedx`.
2. Import `install_langgraph` or `compile` from `verifiedx`.
3. Activate VerifiedX before compiling the graph.
4. If the repo uses `langchain_openai`, also read `langgraph-openai.md`.
5. If the repo uses `langchain_anthropic`, also read `langgraph-anthropic.md`.

## What the adapter really does

- patches `StateGraph.add_node`
- patches `StateGraph.compile`
- patches LangGraph tool invocation
- wraps the checkpointer and store
- preserves the graph topology and provider wiring

Do not wrap every node manually.
