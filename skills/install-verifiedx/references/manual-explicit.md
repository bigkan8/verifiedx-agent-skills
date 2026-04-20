# Explicit wrappers and harness promotion

Use this reference when the repo already owns the harness or the cleanest truthful seam is the business method or MCP tool boundary itself.

This is a first-class VerifiedX path. Do not force a repo with a clean explicit seam into a noisier adapter rewrite.

## TypeScript

### Harness promotion

Use `initVerifiedX()` plus `bindHarness(target, { ... })` when the repo already has named methods you want to protect directly.

Supported binding categories:

- `llm`
- `retrievals`
- `actions`
- `memories`
- `tools`

Use the smallest category that matches what the method really does:

- `actions` for high-impact writes such as record mutations, system changes, or messages
- `memories` for durable memory writes
- `tools` for helper wrapping and tool history when the real protected boundary may still be lower in the runtime

### Direct wrappers

- `wrapToolCall()`
- `wrapMemoryWrite()`
- `wrapActionExecute()`
- `wrapMcpTool()`

### Metadata

For `actions`, `memories`, and `tools`, pass `schema` and `docstring` when the repo already has them. That improves boundary context and better receipts without changing the business workflow.

### Composed systems

When the current node is part of a larger workflow, use:

- `setUpstreamContext(payload)`
- `withUpstreamContext(payload, fn)`

Upstream context is supporting workflow context from outside the current node. It is not proof that the current node already executed any local action.

## Python

### Harness promotion

Use `init_verifiedx()` plus `install_runtime()` or `bind_harness(target, { ... })` when the repo already has named methods you want to protect directly.

Supported binding categories:

- `llm`
- `retrievals`
- `actions`
- `memories`
- `tools`

Use the smallest category that matches what the method really does:

- `actions` for high-impact writes such as record mutations, system changes, or messages
- `memories` for durable memory writes
- `tools` for helper wrapping and tool history when the real protected boundary may still be lower in the runtime

### Direct wrappers

- `wrap_tool_call()`
- `wrap_memory_write()`
- `wrap_action_execute()`
- `wrap_tool_handler()`
- `wrap_tool_definition()`

### Metadata

For `actions`, `memories`, and `tools`, pass `schema` and `docstring` when the repo already has them. That improves boundary context and better receipts without changing the business workflow.

### Composed systems

When the current node is part of a larger workflow, use:

- `set_upstream_context(payload)`
- `with_upstream_context(payload)`

Upstream context is supporting workflow context from outside the current node. It is not proof that the current node already executed any local action.

## MCP-specific note

For standalone MCP servers:

- TypeScript boundary protection lives in `wrapMcpTool()`
- Python boundary protection lives in `wrap_tool_handler()`

Definition wrapping is metadata enrichment:

- TypeScript keeps boundary protection at the wrapped handler
- Python `wrap_tool_definition()` enriches exposed definitions, but protection still lives in `wrap_tool_handler()`

## Do not

- create a new orchestration layer just to fit VerifiedX
- move business logic out of the existing handlers if the explicit seam is already clean
- introduce fake fallback lanes instead of using the returned receipt inside the builder's real workflow
