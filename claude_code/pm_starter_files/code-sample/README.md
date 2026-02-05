# Voice Agents API

Handles real-time voice agent conversations for enterprise customers.

## Key Components

- **Voice Processing Pipeline** (`voice_agent.py`) — Orchestrates the end-to-end call flow: receives caller input, generates agent responses via LLM, applies safety guardrails, and handles escalation to human agents when needed.
- **Guardrails Engine** (`guardrails.py`) — Validates every agent response against prohibited-topic rules and PII-exposure checks before it reaches the caller. Logs violations for compliance review.
- **Conversation Manager** — Maintains session state, turn history, and context window for multi-turn conversations (not yet extracted into its own module).
- **Metrics Collector** (`metrics.py`) — Tracks call volume, latency percentiles, hallucination counts, and escalation rates. Powers the ops dashboard.
- **Configuration** (`config.py`) — Centralized settings for latency targets, model parameters, and per-tenant overrides.

## Architecture

```
Caller --> Voice Pipeline --> LLM --> Guardrails --> Response --> Caller
                                        |
                                   Escalation (if needed)
```

## Running Tests

```bash
python -m pytest test_voice_agent.py -v
```

## Current Status

- Latency P99: ~800ms (target: 200ms)
- Guardrails coverage: 4 prohibited-topic categories
- Enterprise tenants: 3 active
