# Wiki Page Template

Use this format for internal wiki/knowledge base pages.

---

## Format

```markdown
# [Page Title]

> **TL;DR:** [One sentence summary]

**Last updated:** [Date]
**Owner:** [Name/Team]
**Status:** Draft | Current | Archived

---

## Overview

[2-3 sentences explaining what this page covers and why it exists]

---

## [Main Content Sections]

### Section 1
[Content organized with clear headers]

### Section 2
[Use bullet points for lists]

### Section 3
[Include tables for comparisons]

---

## Related Pages

- [Link to related page 1]
- [Link to related page 2]

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| [Date] | [What changed] | [Who] |

---

**Questions?** Reach out to [Owner] or post in #[relevant-channel]
```

---

## Example

```markdown
# Voice Agents Enterprise Features

> **TL;DR:** Overview of Voice Agents enterprise capabilities, how to configure them, and what's coming next.

**Last updated:** January 2026
**Owner:** Voice Agents Squad
**Status:** Current

---

## Overview

Wavelength Voice Agents provides AI-powered conversational voice agents for enterprise customer support. This page covers available features, configuration options, and known limitations.

---

## Available Features

### Voice Agent Configuration
Set up and customize AI voice agents for your support workflows.

**How to use:**
1. Navigate to Voice Agents > Create Agent
2. Select a base voice or clone a custom voice
3. Configure guardrails (topics the agent can/cannot discuss)
4. Set latency and quality preferences
5. Test with sample conversations before deploying

**Tips:**
- Start with a pre-built template for common support scenarios
- Always test guardrails with adversarial prompts
- Monitor the first 100 calls closely

### Real-Time Call Monitoring
Monitor live voice agent conversations with latency and quality metrics.

**How to use:**
1. Navigate to Voice Agents > Live Dashboard
2. View active calls, latency (p50/p99), and quality scores
3. Flag calls for human review

---

## Known Limitations

- Current p99 latency is ~780ms (target: sub-300ms by Q1)
- Interruption handling works for short interruptions only
- Voice cloning requires explicit consent verification
- SOC 2 certification in progress (target: March 2026)

---

## What's Coming

- [ ] Sub-300ms latency optimization (Q1)
- [ ] SOC 2 Type II certification (Q1)
- [ ] Advanced guardrails with content filtering (Q1)
- [ ] Multi-language voice agents (Q2)

---

## Related Pages

- [Wavelength Voice Studio](/wiki/voice-studio)
- [Enterprise Security & Compliance](/wiki/enterprise-security)

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| Jan 2026 | Added enterprise features section | Voice Agents squad |
| Nov 2025 | Initial page | Previous PM |

---

**Questions?** Reach out to @voice-agents-squad or post in #voice-agents
```

---

## Tips

- Keep the TL;DR under 20 words
- Update the "Last updated" date when you make changes
- Link to related pages to help discoverability
- Use the changelog for significant updates
- Archive instead of delete when content is outdated
