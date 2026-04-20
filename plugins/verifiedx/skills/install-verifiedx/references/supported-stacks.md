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
- LangGraph (OpenAI): `https://docs.verifiedx.me/sdks/langgraph-openai`
- LangGraph (Anthropic / Claude): `https://docs.verifiedx.me/sdks/langgraph-anthropic`
- MCP Python: `https://docs.verifiedx.me/sdks/mcp-python`
- MCP TypeScript: `https://docs.verifiedx.me/sdks/mcp-typescript`

If you are stuck, go to `docs.verifiedx.me` and read only the page that matches the seam the repo actually uses. Do not guess another domain.

## Raw runtimes for custom harnesses

Use the raw SDK pages when the repo owns a custom harness and no native adapter already owns the tool loop.

- TypeScript raw runtime:
  - entrypoints: `initVerifiedX()`, `bindHarness()`, `wrapToolCall()`, `wrapMemoryWrite()`, `wrapActionExecute()`
  - read: `raw-typescript-runtime.md`
  - docs: `https://docs.verifiedx.me/sdks/typescript`
- Python raw runtime:
  - entrypoints: `init_verifiedx()`, `install_runtime()`, `bind_harness()`, `wrap_tool_call()`, `wrap_memory_write()`, `wrap_action_execute()`
  - read: `raw-python-runtime.md`
  - docs: `https://docs.verifiedx.me/sdks/python`

These raw-runtime pages are where the docs explain:

- what lower seams are already captured automatically
- when to promote business methods into explicit `llm`, `retrievals`, `actions`, `memories`, or `tools`
- when to use schema and docstring metadata
- how to pass upstream context in composed systems
- what blocked runtime behavior and receipts look like

## Adapter seams

### TypeScript

- `openai_agents_ts`
  - surface: `@verifiedx-core/sdk/openai-agents`
  - minimal seam: `withVerifiedXRunner()`, `withVerifiedXAgent()`, or `run()`
  - docs: `https://docs.verifiedx.me/sdks/openai-agents-sdk`
- `claude_agent_ts`
  - surface: `@verifiedx-core/sdk/claude-agent`
  - minimal seam: `withVerifiedXClaudeQuery()`
  - docs: `https://docs.verifiedx.me/sdks/claude-agent-sdk`
- `langgraph_ts`
  - surface: `@verifiedx-core/sdk/langgraph`
  - minimal seam: `install()` before compilation or `compile()` from the adapter
  - provider-specialized docs:
    - generic: `https://docs.verifiedx.me/sdks/langgraph`
    - OpenAI-backed graphs: `https://docs.verifiedx.me/sdks/langgraph-openai`
    - Anthropic-backed graphs: `https://docs.verifiedx.me/sdks/langgraph-anthropic`
- `vercel_ai_ts`
  - surface: `@verifiedx-core/sdk/vercel-ai`
  - minimal seam: `withVerifiedXGenerateText()`, `withVerifiedXStreamText()`, or `withVerifiedXToolLoopAgent()`
  - docs: `https://docs.verifiedx.me/sdks/vercel-ai`
- `openai_direct_ts`
  - surface: `@verifiedx-core/sdk/openai-direct`
  - minimal seam: `attach()` plus `createToolDispatcher()`
  - docs: `https://docs.verifiedx.me/sdks/openai`
- `anthropic_direct_ts`
  - surface: `@verifiedx-core/sdk/anthropic-direct`
  - minimal seam: `attach()` plus `createToolDispatcher()`
  - docs: `https://docs.verifiedx.me/sdks/anthropic`

### Python

- `openai_agents_py`
  - surface: `verifiedx`
  - minimal seam: `attach_openai_agents_runner()`, `attach_openai_agents_agent()`, `run_openai_agents_sync()`, or `run_openai_agents_streamed()`
  - docs: `https://docs.verifiedx.me/sdks/openai-agents-sdk`
- `claude_agent_py`
  - surface: `verifiedx`
  - minimal seam: `attach_claude_query()` or `claude_query()`
  - docs: `https://docs.verifiedx.me/sdks/claude-agent-sdk`
- `langgraph_py`
  - surface: `verifiedx`
  - minimal seam: `install_langgraph()`, `compile()`, or `attach_langgraph()`
  - provider-specialized docs:
    - generic: `https://docs.verifiedx.me/sdks/langgraph`
    - OpenAI-backed graphs: `https://docs.verifiedx.me/sdks/langgraph-openai`
    - Anthropic-backed graphs: `https://docs.verifiedx.me/sdks/langgraph-anthropic`
- `langchain_py`
  - surface: `verifiedx.langchain`
  - minimal seam: replace the existing `create_agent` import with `verifiedx.langchain.create_agent`
  - docs: there is no dedicated public page today, so use the Python SDK page plus the actual code surface in `verifiedx.langchain`
- `openai_direct_py`
  - surface: `verifiedx`
  - minimal seam: `attach_openai()` plus `create_openai_tool_dispatcher()`
  - docs: `https://docs.verifiedx.me/sdks/openai`
- `anthropic_direct_py`
  - surface: `verifiedx`
  - minimal seam: `attach_anthropic()` plus `create_anthropic_tool_dispatcher()`
  - docs: `https://docs.verifiedx.me/sdks/anthropic`

## Lower seams

- `lower_seam_ts`
  - startup entrypoint: `initVerifiedX()`
  - docs: `https://docs.verifiedx.me/sdks/typescript`
  - read: `lower-seam-ts.md` and `raw-typescript-runtime.md`
  - lower seams already covered in the SDK:
    - `globalThis.fetch` and `undici.fetch`
    - file writes through `node:fs/promises.writeFile`, `appendFile`, `fs.writeFileSync`, and `appendFileSync`
    - `pg.Client.query` and `pg.Pool.query`
    - `amqplib.Channel.publish` and `sendToQueue`
- `lower_seam_py`
  - startup entrypoints: `init_verifiedx()` plus `install_runtime()`
  - docs: `https://docs.verifiedx.me/sdks/python`
  - read: `lower-seam-py.md` and `raw-python-runtime.md`
  - lower seams already covered in the SDK:
    - file writes through `builtins.open` and `aiofiles`
    - HTTP and network calls through `urllib`, `requests`, and `httpx`
    - provider/runtime capture through `OpenAI`, `Anthropic`, and `LiteLLM`
    - AWS runtime client calls through `botocore`
    - database mutations through `sqlite3`, `psycopg`, `psycopg2`, and `SQLAlchemy`
    - queue publishes through `kombu`
    - browser client actions through Playwright

## Explicit wrappers

### MCP-specific wrappers

- `mcp_ts`
  - surface: `@verifiedx-core/sdk/mcp`
  - minimal seam: `wrapMcpTool()`
  - docs: `https://docs.verifiedx.me/sdks/mcp-typescript`
- `mcp_py`
  - surface: `verifiedx`
  - minimal seam: `wrap_tool_handler()` or `wrap_tool_definition()`
  - docs: `https://docs.verifiedx.me/sdks/mcp-python`

Use these MCP pages only for standalone MCP servers or tool handlers you own directly. If MCP is being surfaced through OpenAI Agents or another higher-level SDK, use that native adapter page instead.

### General explicit wrappers and harness promotion

Additional explicit wrappers that may already exist in a repo and should be preserved when they are the cleanest seam:

- TypeScript:
  - `bindHarness()`
  - `wrapToolCall()`
  - `wrapMemoryWrite()`
  - `wrapActionExecute()`
- Python:
  - `bind_harness()`
  - `wrap_tool_call()`
  - `wrap_memory_write()`
  - `wrap_action_execute()`

Read `manual-explicit.md` whenever the repo owns the harness or uses explicit boundary wrappers. That reference explains:

- when to prefer `actions` over `memories` or `tools`
- how the raw runtime promotes business methods into named boundaries
- how schema and docstring metadata sharpen receipts
- how composed-system upstream context should be passed

## Never do this

- redesign the product architecture just to fit VerifiedX
- replace a real lower-seam or explicit-wrapper integration with a noisier adapter path
- invent fallback workflow branches to make VerifiedX look good
- ask the builder to enumerate high-impact actions by hand when the existing seam already exposes them
