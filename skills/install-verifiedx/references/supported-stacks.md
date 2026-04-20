# Supported stacks

Use only the recipe that matches `recommended.kind` from `verifiedx verify --json`.

## Official VerifiedX URLs

- Product and API keys: `https://verifiedx.me`
- Docs home: `https://docs.verifiedx.me`
- Python SDK: `https://docs.verifiedx.me/sdks/python`
- TypeScript SDK: `https://docs.verifiedx.me/sdks/typescript`
- OpenAI Agents SDK: `https://docs.verifiedx.me/sdks/openai-agents-sdk`
- Claude Agent SDK: `https://docs.verifiedx.me/sdks/claude-agent-sdk`
- Vercel AI SDK: `https://docs.verifiedx.me/sdks/vercel-ai`
- LangGraph: `https://docs.verifiedx.me/sdks/langgraph`
- OpenAI direct: `https://docs.verifiedx.me/sdks/openai`
- Anthropic / Claude direct: `https://docs.verifiedx.me/sdks/anthropic`
- MCP Python: `https://docs.verifiedx.me/sdks/mcp-python`
- MCP TypeScript: `https://docs.verifiedx.me/sdks/mcp-typescript`

If you are stuck, go to `docs.verifiedx.me` and read only the page that matches the seam the repo actually uses.

## Raw runtimes for custom harnesses

Use the raw SDK pages when the repo owns a custom harness and no native adapter already owns the tool loop.

- Python SDK: `init_verifiedx()`, `install_runtime()`, `bind_harness()`
- TypeScript SDK: `initVerifiedX()`, `bindHarness()`

These pages also explain the lower-seam capture that is already turned on by default and when to promote business methods into explicit `llm`, `retrievals`, `actions`, `memories`, or `tools`.

## Adapter seams

### TypeScript

- `openai_agents_ts`: `withVerifiedXAgent()`, `withVerifiedXRunner()`, or `run()` from `@verifiedx-core/sdk/openai-agents`
- `claude_agent_ts`: `withVerifiedXClaudeQuery()` from `@verifiedx-core/sdk/claude-agent`
- `langgraph_ts`: `install()` or `compile()` from `@verifiedx-core/sdk/langgraph`
- `vercel_ai_ts`: `withVerifiedXGenerateText()`, `withVerifiedXStreamText()`, or `withVerifiedXToolLoopAgent()` from `@verifiedx-core/sdk/vercel-ai`
- `anthropic_direct_ts`: `attach()` plus `createToolDispatcher()` from `@verifiedx-core/sdk/anthropic-direct`
- `openai_direct_ts`: `attach()` plus `createToolDispatcher()` from `@verifiedx-core/sdk/openai-direct`

### Python

- `langgraph_py`: `install_langgraph()` or `compile()` from `verifiedx`
- `langchain_py`: `create_agent` from `verifiedx.langchain`
- `claude_agent_py`: `attach_claude_query()` or `claude_query()` from `verifiedx`
- `openai_agents_py`: `attach_openai_agents_agent()`, `attach_openai_agents_runner()`, `run_openai_agents_sync()`, or `run_openai_agents_streamed()` from `verifiedx`
- `anthropic_direct_py`: `attach_anthropic()` plus `create_anthropic_tool_dispatcher()` from `verifiedx`
- `openai_direct_py`: `attach_openai()` plus `create_openai_tool_dispatcher()` from `verifiedx`

## Lower seams

- `lower_seam_ts`: startup `initVerifiedX()` from `@verifiedx-core/sdk`, keeping lower-seam fallbacks enabled
- `lower_seam_py`: startup `init_verifiedx()` plus `install_runtime()` from `verifiedx`

Docs make these paths explicit:

- TypeScript lower seams already cover `fetch`, file writes, `pg`, and `amqplib`
- Python lower seams already cover file writes, `aiofiles`, `urllib`, `requests`, `httpx`, `OpenAI`, `Anthropic`, `LiteLLM`, `botocore`, `sqlite3`, `psycopg`, `psycopg2`, `SQLAlchemy`, `kombu`, and Playwright

## Explicit wrappers

- `mcp_ts`: `wrapMcpTool()` from `@verifiedx-core/sdk/mcp`
- `mcp_py`: `wrap_tool_handler()` or `wrap_tool_definition()` from `verifiedx`

Additional explicit wrappers that may already exist in a repo and should be preserved when they are the cleanest seam:

- TypeScript: `bindHarness()`, `wrapToolCall()`, `wrapMemoryWrite()`, `wrapActionExecute()`
- Python: `bind_harness()`, `wrap_tool_call()`, `wrap_memory_write()`, `wrap_action_execute()`

## Never do this

- redesign the product architecture just to fit VerifiedX
- replace a real lower-seam or explicit-wrapper integration with a noisier adapter path
- invent fallback workflow branches to make VerifiedX look good
