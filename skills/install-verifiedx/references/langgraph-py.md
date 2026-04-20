# langgraph_py

- SDK surface: `verifiedx.install_langgraph` or `verifiedx.compile`
- Minimal seam: install once before compilation or compile through VerifiedX

## Apply

1. Install `verifiedx`.
2. Import `install_langgraph` or `compile` from `verifiedx`.
3. Activate VerifiedX before compiling the graph.

## What the adapter really does

- patches `StateGraph.add_node`
- patches `StateGraph.compile`
- patches LangGraph tool invocation
- wraps the checkpointer and store

Do not wrap every node manually.
