# Explicit wrapper surfaces

These are real VerifiedX integration surfaces even when they are not the default automatic install path.

## TypeScript

- `bindHarness()`
- `wrapToolCall()`
- `wrapMemoryWrite()`
- `wrapActionExecute()`
- `wrapMcpTool()`

## Python

- `bind_harness()`
- `wrap_tool_call()`
- `wrap_memory_write()`
- `wrap_action_execute()`
- `wrap_tool_handler()`
- `wrap_tool_definition()`

Use these only when the repo has a custom runtime or tool surface where the explicit boundary is the least invasive seam. Do not force them on top of a cleaner native adapter or lower-seam install.
