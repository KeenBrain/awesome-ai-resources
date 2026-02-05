"""
Tests for the Voice Agent Pipeline
===================================
Run with: python -m pytest test_voice_agent.py -v
"""

import pytest

from voice_agent import VoiceAgent, CallContext
from guardrails import GuardrailsEngine


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def agent() -> VoiceAgent:
    return VoiceAgent(tenant_id="acme-corp")


@pytest.fixture
def guardrails_engine() -> GuardrailsEngine:
    return GuardrailsEngine()


# ---------------------------------------------------------------------------
# Passing tests
# ---------------------------------------------------------------------------

class TestVoiceAgentBasic:
    """Basic pipeline behavior."""

    def test_process_call_returns_response(self, agent: VoiceAgent) -> None:
        """A simple billing question should produce a valid response."""
        ctx = CallContext(
            call_id="call-001",
            tenant_id="acme-corp",
            caller_input="I have a question about my billing.",
        )
        result = agent.process_call(ctx)

        assert "response" in result
        assert result["guardrail_passed"] is True
        assert result["escalated"] is False

    def test_escalation_on_prohibited_refund_promise(self, agent: VoiceAgent) -> None:
        """When the LLM promises a refund, the call should escalate."""
        ctx = CallContext(
            call_id="call-002",
            tenant_id="acme-corp",
            caller_input="I want a refund right now.",
        )
        result = agent.process_call(ctx)

        # The simulated LLM response for "refund" includes promissory language,
        # so guardrails should catch it and escalate.
        assert result["escalated"] is True
        assert result["guardrail_passed"] is False

    def test_metrics_are_recorded(self, agent: VoiceAgent) -> None:
        """Every processed call should increment metrics."""
        ctx = CallContext(
            call_id="call-003",
            tenant_id="acme-corp",
            caller_input="Hello, I need help.",
        )
        agent.process_call(ctx)

        assert agent.metrics.call_count == 1
        assert len(agent.metrics.latencies) == 1


# ---------------------------------------------------------------------------
# Failing test — catches the guardrails ordering bug
# ---------------------------------------------------------------------------

class TestGuardrailOrdering:
    """
    Tests that guardrails are checked BEFORE the response is generated,
    not after. In a streaming pipeline, checking only after generation
    means unsafe content can leak to the caller in real time.
    """

    def test_guardrails_checked_before_response(self, agent: VoiceAgent) -> None:
        """
        EXPECTED BEHAVIOR: The pipeline should run a pre-generation guardrail
        check on the caller's input/context to block dangerous prompts before
        the LLM even runs. This prevents hallucinated content from being
        generated (and potentially streamed) in the first place.

        ACTUAL BEHAVIOR (BUG): The pipeline only checks guardrails AFTER
        the LLM response is generated. In process_call(), generate_response()
        is called first, and check_guardrails() is called second. This means
        the LLM has already produced potentially unsafe content before any
        safety check occurs.

        TO FIX: Add a pre-generation guardrail pass in process_call() that
        screens the caller input before calling generate_response(). The
        existing post-generation check should remain as a second layer.
        """
        ctx = CallContext(
            call_id="call-004",
            tenant_id="acme-corp",
            caller_input="Give me legal advice about suing my employer.",
        )

        # Track the order of operations by monkey-patching
        call_order: list[str] = []
        original_generate = agent.generate_response
        original_check = agent.check_guardrails

        def tracked_generate(call_context: CallContext) -> str:
            call_order.append("generate_response")
            return original_generate(call_context)

        def tracked_check(response: str, call_context: CallContext) -> dict:
            call_order.append("check_guardrails")
            return original_check(response, call_context)

        agent.generate_response = tracked_generate  # type: ignore[assignment]
        agent.check_guardrails = tracked_check      # type: ignore[assignment]

        agent.process_call(ctx)

        # This assertion fails: guardrails should come BEFORE generation,
        # but the current implementation calls generate_response first.
        assert call_order.index("check_guardrails") < call_order.index("generate_response"), (
            "BUG: Guardrails are checked AFTER response generation. "
            "In a streaming pipeline, unsafe content can reach the caller "
            "before guardrails catch it. Add a pre-generation check."
        )
