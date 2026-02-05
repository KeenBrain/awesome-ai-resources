"""
Configuration
=============
Centralized settings for the voice agent service.
In production these would be loaded from a config service or env vars.
"""

# ---------------------------------------------------------------------------
# Latency targets
# ---------------------------------------------------------------------------
CURRENT_LATENCY_TIMEOUT_MS = 800   # What we ship today
TARGET_LATENCY_MS = 200            # Where we need to be for enterprise SLAs

# ---------------------------------------------------------------------------
# Model settings
# ---------------------------------------------------------------------------
MODEL_NAME = "claude-voice-v2"
MODEL_MAX_TOKENS = 256             # Keep responses concise for voice
MODEL_TEMPERATURE = 0.3            # Low temp for factual, consistent answers
MODEL_STREAMING_ENABLED = True     # Stream tokens for lower time-to-first-byte

# ---------------------------------------------------------------------------
# Enterprise tenant configurations
# ---------------------------------------------------------------------------
TENANT_CONFIGS = {
    "acme-corp": {
        "display_name": "Acme Corporation",
        "tier": "enterprise",
        "custom_greeting": "Thank you for calling Acme support.",
        "max_turns": 20,
    },
    "globex-inc": {
        "display_name": "Globex Inc.",
        "tier": "enterprise",
        "custom_greeting": "Welcome to Globex customer service.",
        "max_turns": 15,
    },
    "initech": {
        "display_name": "Initech",
        "tier": "standard",
        "custom_greeting": None,  # Uses default greeting
        "max_turns": 10,
    },
}

# TODO: Add per-tenant guardrail configuration - enterprise customers need custom rules
# For example, Acme wants to block discussion of their ongoing lawsuit,
# and Globex needs a custom PII filter for their internal employee IDs.
# This is currently blocked on the guardrails engine supporting tenant-aware rules.
