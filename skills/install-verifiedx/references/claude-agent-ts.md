# claude_agent_ts

- SDK surface: `@verifiedx-core/sdk/claude-agent`
- Minimal seam: wrap the existing Claude query callable with `withVerifiedXClaudeQuery()`

## Apply

1. Install `@verifiedx-core/sdk`.
2. Import `withVerifiedXClaudeQuery`.
3. Create a wrapped query function once and replace direct query calls with it.

## Do not do

- do not rebuild hooks
- do not replace MCP servers
- do not move built-in Claude tools into a fake fallback flow
