# claude_agent_py

- SDK surface: `attach_claude_query()` or `claude_query()` from `verifiedx`
- Minimal seam: wrap the existing Claude Agent SDK query surface

## Apply

1. Install `verifiedx`.
2. Import `attach_claude_query` or `claude_query`.
3. Replace direct query calls with the wrapped VerifiedX query surface.

## Do not do

- do not rebuild hooks
- do not replace MCP servers
- do not move built-in tools into a fake fallback design
