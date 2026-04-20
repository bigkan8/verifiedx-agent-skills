# langchain_py

- SDK surface: `verifiedx.langchain.create_agent`
- Minimal seam: replace the factory import

## Apply

1. Install `verifiedx`.
2. Replace `from langchain.agents import create_agent` with `from verifiedx.langchain import create_agent`.
3. Keep the same model, tools, and middleware arguments unless there is a direct conflict.

## Important

This is the only LangChain install path this repo treats as first-class. Do not invent a sidecar wrapper around LangChain.
