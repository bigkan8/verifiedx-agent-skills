# Raw Python runtime

Use this path when the repo owns a custom Python harness and no native adapter already owns the tool loop.

Docs source: `https://docs.verifiedx.me/sdks/python`

## Best for

- custom Python harnesses you already own
- repos where the truthful seam is your own business methods
- lower-seam installs that need clearer business-level names and receipts

## Smallest truthful delta

1. Install `verifiedx`.
2. Call `init_verifiedx()`.
3. For the fewest lines, use `install_runtime(target, ...)`.
4. If the process owns multiple nodes or you want lower-seam patching earlier in startup, use `install_runtime()` once and `bind_harness(target, ...)` later.

## What lower seams already cover

Calling `install_runtime()` already turns on lower-seam capture for:

- file writes through `builtins.open`
- async file writes through `aiofiles`
- HTTP and network calls through `urllib`, `requests`, and `httpx`
- provider/runtime capture for `OpenAI`, `Anthropic`, and `LiteLLM`
- AWS runtime client calls through `botocore`
- database mutations through `sqlite3`, `psycopg`, `psycopg2`, and `SQLAlchemy`
- queue publishes through `kombu`
- browser client actions through Playwright

That means you do not need to enumerate every low-level side effect for VerifiedX to start working.

## When to bind methods explicitly

Use `bind_harness()` when you want your own named boundary instead of only the lower seam. The runtime supports these categories:

- `llm`
  - model call methods such as `call_model`
- `retrievals`
  - reads and lookups that provide context
  - use `external_retrieval` only for weaker outside context such as public web search
- `actions`
  - high-impact side effects such as record mutations, system changes, internal or external messages, webhooks, and other writes
- `memories`
  - durable memory writes
- `tools`
  - general helper wrapping and tool history when the real protected boundary may still be caught lower in the runtime

Use the smallest category that matches what the method really does.

## Explicit wrapper entrypoints

If the repo already uses wrapper-style boundaries instead of a single bind call, preserve that shape:

- `wrap_tool_call()`
- `wrap_memory_write()`
- `wrap_action_execute()`

Do not force a custom harness into an adapter-shaped rewrite.

## Metadata

For `actions`, `memories`, and `tools`, add `schema` and `docstring` when the repo already has that information. It improves boundary context and produces better receipts without changing the business flow.

## Composed systems

If the current node is part of a larger workflow, pass upstream context with:

- `set_upstream_context(payload)`
- `with_upstream_context(payload)`

Upstream context is supporting workflow context from outside the current node. It is not proof that the current node already executed any local action.

## Runtime behavior

Protected boundaries can return:

- `allow`
- `allow_with_warning`
- `replan_required`
- `goal_fail_terminal`

If a boundary is blocked, the side effect does not execute. The wrapped method returns a structured blocked result with the decision receipt. Keep the builder's workflow intact and let it use the receipt locally or upstream instead of inventing new fallback lanes.
