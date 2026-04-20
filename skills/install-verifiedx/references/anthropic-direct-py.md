# anthropic_direct_py

- SDK surface: `attach_anthropic()` and `create_anthropic_tool_dispatcher()` from `verifiedx`
- Minimal seam: attach the existing Anthropic client and dispatch local tool uses through the VerifiedX dispatcher
- Docs: `https://docs.verifiedx.me/sdks/anthropic`

## Apply

1. Install `verifiedx`.
2. Import `attach_anthropic` and `create_anthropic_tool_dispatcher`.
3. Wrap the existing Anthropic client with `attach_anthropic(client, verifiedx=vx)`.
4. Replace direct local tool handler execution with the dispatcher inside the existing Claude Messages loop.
5. Keep the existing assistant message and tool-result message flow intact.

## Important

`attach_anthropic()` alone is not enough for local tool execution blocking. The dispatcher is required for the exact handler boundary.
