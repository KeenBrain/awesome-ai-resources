# Voice Agents Enterprise - Product Requirements Document (WIP)

> **Status:** DRAFT - heavily incomplete
> **Author:** Jordan Machado (PM, All Product Lines... for now)
> **Last updated:** 2025-11-14 (2:47 AM... again)
> **Reviewers:** Priya Chandrasekaran (CTO), Amara Osei (Head of Voice AI), TBD legal
>
> NOTES TO SELF: I know this is messy. I'm managing four product lines and something has to give.
> If you're reading this and I'm no longer at the company, I'm sorry. I tried to get help.
> The Voice Agents stuff is the most urgent because we're losing enterprise deals NOW.
> -- Jordan

---

## 1. Executive Summary

Voice Agents is Wavelength's enterprise conversational AI product, enabling companies to deploy AI-powered voice agents for customer support, sales, and internal operations. We launched the initial version 9 months ago and have ~35 customers, but we are hemorrhaging enterprise pipeline due to **latency issues**, **lack of security certifications**, and a **pricing model that even our own sales team can't explain**.

This PRD outlines the requirements for **Voice Agents Enterprise** -- a dedicated tier targeting companies with 500+ support agents, strict compliance needs, and high-volume call centers.

{{QUESTION: Should this be a separate product or an enterprise tier of Voice Agents? Priya and I disagreed on this in our last 1:1. She wants a unified codebase. I think the requirements diverge too much. Need to resolve before eng sprint planning on Dec 2.}}

---

## 2. Customer Problem

### 2.1 The Latency Problem

Our current Voice Agents architecture routes through a shared inference pipeline. Average response latency is **~800ms** from end-of-user-speech to beginning-of-agent-speech. For context:

- Human conversational turn-taking gap: ~200ms
- Anything above 400ms feels "robotic" to callers
- Our primary competitor (ElevenLabs Agents) claims sub-300ms
- Amazon Connect + Bedrock is marketing sub-200ms (unverified)

> **Derek Okafor, VP of Engineering, CallVault (churned Q3):**
> "Look, the voice quality was genuinely impressive -- best we'd tested. But when there's an 800-millisecond gap every time a customer asks a question, it doesn't matter how good the voice sounds. Our callers were saying 'hello? are you still there?' on 40% of calls. We moved to a competitor in six weeks. I told your sales team this was the issue in our QBR and nothing changed for two quarters."

> **Derek (follow-up email, Oct 3):**
> "The other thing that killed us was hallucination on policy questions. The agent confidently told a customer their subscription had a 90-day refund window. Our policy is 30 days. That one call cost us $12,000 in goodwill credits. We need deterministic responses for anything involving money or policy, and your system doesn't support guardrails at that level."

CallVault was a $180K ARR account. Their churn was flagged in the Q3 board deck.

### 2.2 The Pricing Confusion

Our pricing across the four product lines is a Frankenstein:

| Product | Pricing Model | Unit |
|---------|--------------|------|
| Voice Studio | Per character | $0.000015/char (nano-dollars, basically) |
| Soundscape | Per minute of audio + per sound effect | $0.08/min + $0.25/sound |
| Voice Agents | Per minute of conversation | $0.12/min |
| Open Voice | Free tier + usage-based | Free to 10K chars, then $0.00002/char |

> **Marcus Webb, Senior AE:**
> "I was on a call with TeleCorp last month -- a $400K annual deal. The CFO asked me to explain how Voice Agents pricing compares to our Voice Studio pricing and why one is per-character and the other is per-minute. I tried to draw it on a whiteboard and I confused MYSELF. She said 'if your own team can't explain this, how are we supposed to budget for it?' We lost that deal to ElevenLabs, who just has three simple tiers. Four hundred thousand dollars because of a pricing page."

> **Marcus (Slack, #sales-feedback, Oct 22):**
> "Another one gone. Meridian Financial wanted to start with Voice Agents but also wanted Voice Studio for their IVR prompts. When I quoted them two completely different pricing models for what they see as 'the same AI voice thing,' they asked if we were actually two different companies. Not joking."

### 2.3 The Security Gap

No SOC 2 Type II. No HIPAA BAA. No data residency options.

For enterprise contact centers, this is table stakes. We can't even get into procurement review at most F500 companies.

{{QUESTION: Priya mentioned we could fast-track SOC 2 Type II with Vanta in ~3 months. Is that realistic? The audit alone takes 6-8 weeks and we haven't even started the readiness assessment. LEGAL: can we guarantee voice isolation per customer?? Our current architecture shares inference across tenants.}}

TODO: Get timeline from Priya on SOC 2 readiness
TODO: Map out data residency requirements for top 10 enterprise prospects
TODO: Talk to legal about multi-tenant voice data implications

---

## 3. Proposed Solution

### 3.1 Overview

Voice Agents Enterprise will be a dedicated enterprise tier featuring:

1. **Sub-200ms latency** via dedicated inference endpoints (TODO: ask Priya about model latency targets -- she mentioned a new streaming architecture in standup but I missed the details because I was in a Soundscape incident call at the same time)
2. **SOC 2 Type II compliance** (TODO: realistic timeline?)
3. **Simplified enterprise pricing** (TODO: pricing recommendation -- see separate pricing analysis doc)
4. **Guardrails engine** for policy-compliant responses (TODO: is this the "Sentinel" project Amara's team prototyped? Need to check if it's production-ready)
5. **Tenant isolation** for voice data (TODO: LEGAL: can we guarantee voice isolation per customer??)

### 3.2 Technical Architecture

NOTES TO SELF: I started writing this section three times and deleted it. I don't have enough context on Priya's infra plans. She keeps rescheduling our deep-dive because of the Soundscape legal fire. Just parking the high-level bullets.

- Dedicated inference cluster per enterprise customer (or per cohort?)
- Streaming token generation (speculative decoding? Amara mentioned this)
- Edge deployment option for latency-sensitive regions
- {{QUESTION: should we build a separate model for Voice Agents or fine-tune the base model? Amara's team says fine-tuning is 2 months, new model is 6+ months. But a fine-tuned model might not hit latency targets.}}

TODO: Full technical architecture section after deep-dive with Priya (rescheduled to... TBD)
TODO: Latency benchmarks from Amara's team
TODO: Infrastructure cost modeling -- dedicated endpoints are expensive, need to validate unit economics

### 3.3 Guardrails Engine

The hallucination problem Derek flagged is critical. We need:

- Policy document ingestion (upload your refund policy, the agent follows it deterministically)
- Confidence scoring with fallback to human agent
- Prohibited response patterns (never quote specific dollar amounts unless from approved source)
- Audit trail for every agent response

TODO: Review Amara's "Sentinel" prototype
TODO: How does this interact with the base model? Do we need a separate classification step?

NOTES TO SELF: This is actually the feature that could differentiate us. ElevenLabs doesn't have anything like this. If we nail guardrails + low latency, we have a real moat. But I can't get eng time allocated because everyone is firefighting the Soundscape music copyright mess.

---

## 4. Competitive Analysis

TODO: competitive analysis

I started this and it's in a Google Doc somewhere. Key competitors:

- **ElevenLabs** - just raised $80M, their agent product is gaining fast. Simple pricing, good latency, weaker on customization.
- **Play.ht** - strong on voice quality, less focused on enterprise agents
- **Amazon (Connect + Bedrock)** - the 800lb gorilla. Not great voice quality but they have compliance, scale, and every enterprise already has AWS.
- **Bland AI** - phone agent focused, aggressive on pricing
- **Retell AI** - developer-focused, good DX but limited enterprise features

{{QUESTION: How do we position against Amazon? They'll always win on compliance and scale. We need to win on voice quality + customization + guardrails. Is that enough?}}

TODO: Feature comparison matrix
TODO: Pricing comparison (see pricing analysis doc)
TODO: Win/loss analysis from last two quarters

---

## 5. Security Requirements

TODO: security requirements

The basics I know we need:
- SOC 2 Type II
- HIPAA BAA (for healthcare contact centers -- huge market)
- GDPR compliance (we probably already have this? need to check)
- Data residency (US, EU, APAC at minimum)
- Voice data encryption at rest and in transit
- Tenant isolation (this is the big one -- our current shared architecture doesn't support it)
- PII redaction in call transcripts
- Role-based access control

NOTES TO SELF: I asked legal for a security requirements doc three weeks ago. Nothing. They're consumed by the Soundscape/Universal Music lawsuit. I get it, but we're losing enterprise deals every week we don't have SOC 2.

TODO: Engage external security consultant?
TODO: Customer-facing security whitepaper
TODO: Penetration test -- when was our last one? Do we even do those?

---

## 6. Success Metrics

| Metric | Current | Target | Notes |
|--------|---------|--------|-------|
| Response latency (p50) | 800ms | {{TARGET: sub-200ms? sub-300ms? need Priya's input}} | Critical for enterprise adoption |
| Response latency (p95) | 1,400ms | {{TARGET: ??}} | |
| Enterprise pipeline | $1.2M | {{TARGET: ??}} | Need data from Marcus |
| Enterprise win rate | 18% | {{TARGET: ??}} | Abysmal right now |
| Enterprise churn | 22% quarterly | {{TARGET: sub-5%?}} | CallVault, TeleCorp, others |
| Hallucination rate | ~4.2% of responses | {{TARGET: sub-0.5%?}} | Per Amara's eval suite |
| SOC 2 certification | None | Certified | Binary -- either we have it or we don't |
| Time to deploy (new customer) | ~6 weeks | {{TARGET: sub-2 weeks?}} | Onboarding is a mess too |
| CSAT (caller satisfaction) | Not measured | {{TARGET: ??}} | TODO: We don't even measure this. How? |

NOTES TO SELF: Half these metrics don't have baselines because we don't have proper instrumentation. Added "implement observability" to Q1 OKRs but it keeps getting deprioritized.

---

## 7. Pricing Recommendation

TODO: pricing recommendation (see separate pricing analysis doc)

Quick thoughts:
- Enterprise tier should be annual contract, not usage-based
- Minimum commit of $50K/year? $100K/year?
- Need to include dedicated support + SLA
- Platform fee + usage component?
- {{QUESTION: Should Voice Agents Enterprise pricing be decoupled from the rest of the platform? Or should enterprise customers get access to all products?}}

See: pricing-model-analysis.md (also WIP, sorry)

---

## 8. Timeline & Milestones

| Phase | Target Date | Deliverable | Status |
|-------|------------|-------------|--------|
| Phase 0: Security foundation | Q1 2026 | SOC 2 readiness assessment, begin audit | NOT STARTED |
| Phase 1: Latency improvements | Q1 2026 | Sub-400ms p50 via streaming architecture | BLOCKED (eng resources on Soundscape compliance) |
| Phase 2: Guardrails MVP | Q1-Q2 2026 | Sentinel prototype in production | NOT STARTED |
| Phase 3: Enterprise tier launch | Q2 2026 | Full enterprise offering | DEPENDENT ON PHASES 0-2 |
| Phase 4: Advanced features | Q3 2026 | Multi-agent, analytics, custom models | WISHLIST |

NOTES TO SELF: This timeline is optimistic and I know it. Phase 1 alone could take a full quarter if Priya's streaming architecture doesn't pan out. And we still have 2 engineers pulled onto Soundscape compliance tooling with no return date. I flagged this in the last leadership meeting and Raj (CEO) said "we'll figure it out." That's not a plan.

---

## 9. Open Questions

1. Should we build a separate model for Voice Agents or fine-tune the base? (Owner: Amara -- no answer yet)
2. Can we guarantee tenant-level voice data isolation with current infra? (Owner: Priya -- no answer yet)
3. What's the realistic SOC 2 Type II timeline? (Owner: Legal/Ops -- no answer yet, legal is drowning)
4. How do we price Voice Agents Enterprise without cannibalizing Voice Studio revenue? (Owner: Jordan/Marcus -- in progress, see pricing doc)
5. Should we pause Voice Agents sales until we fix latency? Marcus says no, we'll lose market presence. I think we're burning trust. (Owner: Raj -- hasn't weighed in)
6. The deepfake incident in September -- has this been fully resolved? Are we at risk of another one? How does this affect enterprise trust? (Owner: Legal/Trust & Safety -- TODO: follow up)
7. If we move to dedicated inference endpoints for enterprise, what's the cost per customer? Can we maintain margins? (Owner: Priya/Finance -- TODO)
8. Is our voice cloning technology legally defensible after the Universal Music lawsuit? (Owner: Legal -- they won't answer this until settlement is done)

---

## 10. Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Latency improvements don't hit sub-200ms | High | Critical | TODO: fallback plan? |
| SOC 2 timeline slips | High | High | TODO: parallel path? |
| More legal incidents (deepfakes, copyright) | Medium | Critical | TODO: what is our content policy? |
| Eng resources stay diverted to Soundscape | High | High | TODO: escalate to Raj (again) |
| ElevenLabs launches enterprise features first | Medium | High | TODO: competitive response plan |
| Pricing simplification causes revenue dip | Medium | Medium | TODO: model the impact |

---

## Appendix A: Customer Quotes (Unprocessed)

Dumping these here so I don't lose them. Need to organize.

**Sarah Levine, Head of CX, NovaPay:**
"We ran a pilot for three weeks. Your voice quality blew away Amazon Connect. But then our infosec team asked for your SOC 2 report and that was the end of the conversation. Literally -- they said 'call us when you have it.'"

**Derek Okafor (CallVault, post-churn interview):**
"I want to be honest with you because I actually liked working with your team. The product has incredible potential. But potential doesn't help me hit my SLA. My agents need sub-second response times and zero hallucination on policy questions. You're at 800ms average and 4% hallucination. That's not close enough."

**Anonymous (NPS survey, Q3):**
"Pricing is bizarre. We're paying per minute for agents but our other team is paying per character for voice studio. When we asked for a unified invoice it took 3 weeks."

**Yuki Tanaka, CTO, ReachOut Health:**
"HIPAA is non-negotiable. I told your sales team this on the first call. They said it was 'on the roadmap.' That was five months ago."

---

## Appendix B: Internal Notes

- 2 engineers from Voice Agents team reassigned to Soundscape compliance tooling (Nov 1). No return date given. This is killing our velocity.
- Amara's team ran latency experiments with speculative decoding -- got to 340ms in lab conditions. Promising but not production-ready. (See: #eng-voice-agents Slack, Oct 28)
- The deepfake incident in September (someone used our API to generate a fake CEO earnings call) was contained but exposed gaps in our usage monitoring. Trust & Safety is a team of 1 (!!).
- Raj wants Voice Agents Enterprise to be the "hero product" at our Series B pitch in Q2. No pressure.

---

*Last saved: Nov 14, 2025, 2:47 AM*
*Jordan's note: If Priya is reading this, I'm sorry it's incomplete. I'll have a better draft after Thanksgiving. Assuming nothing else catches fire.*
