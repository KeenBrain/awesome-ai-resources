"""
Guardrails Engine
=================
Validates agent responses against safety policies before they reach callers.
Checks for prohibited topics, PII exposure, and enterprise-specific rules.

Each validation returns a dict: {"passed": bool, "reason": str | None}
"""

import re
from datetime import datetime, timezone
from typing import Optional


# Topics the agent must never make promises or give advice about.
PROHIBITED_TOPICS = [
    "refund",          # Agent must not promise refunds — only humans can authorize
    "legal advice",    # Liability risk — must escalate to legal
    "medical advice",  # Safety risk — must escalate to medical professional
    "competitor",      # Brand policy — never mention competitor products
]


class GuardrailsEngine:
    """
    Stateless validation engine. Each method performs a single check
    and returns a pass/fail result with an explanation.
    """

    def __init__(self) -> None:
        self.violation_log: list[dict] = []

    def validate_response(self, response: str, tenant_id: str) -> dict:
        """
        Runs all guardrail checks on a response. Returns on the first failure.

        Args:
            response: The LLM-generated text to validate.
            tenant_id: The enterprise tenant for tenant-specific rules.

        Returns:
            {"passed": True} or {"passed": False, "reason": "..."}
        """
        # Check 1: Prohibited topics
        topic_check = self.check_prohibited_topics(response)
        if not topic_check["passed"]:
            self.log_violation(tenant_id, "prohibited_topic", topic_check["reason"])
            return topic_check

        # Check 2: PII exposure
        pii_check = self.check_pii_exposure(response)
        if not pii_check["passed"]:
            self.log_violation(tenant_id, "pii_exposure", pii_check["reason"])
            return pii_check

        return {"passed": True, "reason": None}

    def check_prohibited_topics(self, response: str) -> dict:
        """
        Scans the response for language that touches prohibited topics.
        Uses keyword matching — a production system would use a classifier.
        """
        response_lower = response.lower()
        for topic in PROHIBITED_TOPICS:
            # Look for the topic keyword combined with promise-like language
            if topic in response_lower:
                promise_patterns = [
                    "will process", "i can confirm", "guaranteed",
                    "we promise", "absolutely", "i recommend",
                    "you should", "take this medication",
                ]
                for pattern in promise_patterns:
                    if pattern in response_lower:
                        return {
                            "passed": False,
                            "reason": f"Prohibited topic detected: '{topic}' with promissory language '{pattern}'",
                        }
        return {"passed": True, "reason": None}

    def check_pii_exposure(self, response: str) -> dict:
        """
        Checks whether the response accidentally leaks PII like phone
        numbers, SSNs, or credit card numbers.

        Known limitation: The phone number regex only matches US-formatted
        numbers (e.g., 555-123-4567 or (555) 123-4567). International
        formats like +44 20 7946 0958 or +91-9876543210 are NOT caught.
        """
        # US phone number pattern only — misses international formats
        phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

        # SSN pattern
        ssn_pattern = r"\d{3}-\d{2}-\d{4}"

        # Credit card pattern (basic)
        cc_pattern = r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}"

        for label, pattern in [
            ("phone number", phone_pattern),
            ("SSN", ssn_pattern),
            ("credit card", cc_pattern),
        ]:
            if re.search(pattern, response):
                return {
                    "passed": False,
                    "reason": f"PII detected in response: {label}",
                }

        return {"passed": True, "reason": None}

    def log_violation(self, tenant_id: str, violation_type: str, detail: Optional[str]) -> None:
        """Records a guardrail violation for audit and compliance."""
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tenant_id": tenant_id,
            "type": violation_type,
            "detail": detail,
        }
        self.violation_log.append(entry)
