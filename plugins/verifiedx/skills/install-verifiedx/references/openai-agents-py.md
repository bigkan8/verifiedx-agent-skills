# openai_agents_py

- SDK surface: `attach_openai_agents_agent()`, `attach_openai_agents_runner()`, `run_openai_agents_sync()`, or `run_openai_agents_streamed()` from `verifiedx`
- Minimal seam: wrap the current runner or agent surface
- Docs: `https://docs.verifiedx.me/sdks/openai-agents-sdk`

## Apply

1. Install `verifiedx`.
2. Import the matching VerifiedX OpenAI Agents helper.
3. Replace the run or attach surface without changing tools or handoffs.

## Do not do

- do not rewrite tool definitions
- do not redesign the agent graph
