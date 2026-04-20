# openai_direct_py

- SDK surface: `attach_openai()` and `create_openai_tool_dispatcher()` from `verifiedx`
- Minimal seam: attach the existing OpenAI client and dispatch local tool calls through the VerifiedX dispatcher
- Docs: `https://docs.verifiedx.me/sdks/openai`

## Apply

1. Install `verifiedx`.
2. Import `attach_openai` and `create_openai_tool_dispatcher`.
3. Wrap the existing OpenAI client with `attach_openai(client, verifiedx=vx)`.
4. Replace direct local tool handler execution with the dispatcher inside the existing `responses` or `chat` loop.

## Important

`attach_openai()` alone is not enough for local tool execution blocking. The dispatcher is required for the exact handler boundary.
