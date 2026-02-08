# Rumelt's Strategy Kernel Framework

A framework for developing real product strategy — not goals, not wish lists, not feature roadmaps, but actual strategic choices with tradeoffs.

Adapted from Richard Rumelt's *Good Strategy Bad Strategy*, simplified for PM workflows.

---

## The Three Parts

Every real strategy has exactly three components:

### 1. Diagnosis
**What's the challenge or opportunity?**

The diagnosis is your honest assessment of what's happening. Not what you wish was happening. Not the marketing spin. The truth.

**Good diagnosis characteristics:**
- Identifies the critical challenge (not 10 challenges — the ONE that matters most)
- Based on evidence (data, research, customer feedback)
- Explains WHY this is the critical challenge
- Simplifies complexity into a clear picture

**Example (Wavelength Voice Agents):**
> "Enterprise customers are churning at 8% monthly primarily because our voice agent latency (800ms p99) is 4x slower than what they need for production call centers. The product was built for interactive demos, not enterprise-grade phone automation. Our growth is masking a retention crisis — we're filling a leaky bucket."

**Bad diagnosis examples:**
- "We need to grow revenue" (that's a goal, not a diagnosis)
- "The market is competitive" (too vague)
- "We have lots of opportunities" (not a challenge)

### 2. Direction
**What's our overall approach?**

The direction answers two questions:
- **WHERE to compete:** Which segment, use case, market?
- **HOW to win:** What approach will we take?

**Good direction characteristics:**
- Makes a clear choice (what you're doing AND what you're NOT doing)
- Creates advantage by focusing resources
- Is specific enough to guide decisions but broad enough to allow flexibility
- Involves a real tradeoff (if it doesn't hurt to say "no" to something, it's not a strategy)

**Example (Wavelength Voice Agents):**
> "We will focus exclusively on enterprise reliability for Q1-Q2 — fixing the foundation (latency, compliance, guardrails) before adding capabilities. We will WIN by combining our voice quality advantage with enterprise-grade reliability, targeting the call center segment specifically. We will NOT pursue creator features, new product lines, or market expansion until the enterprise foundation is solid."

**Bad direction examples:**
- "Be the best voice AI platform" (no tradeoff)
- "Delight customers" (not specific)
- "Grow 50% year over year" (that's a target, not a direction)

### 3. Action Plan
**What specific steps will we take?**

The action plan is the sequenced, coordinated set of initiatives that implement your direction. "Coordinated" is the key word — the actions should reinforce each other, not pull in different directions.

**Good action plan characteristics:**
- Specific and actionable (not vague intentions)
- Sequenced correctly (dependencies are explicit)
- Reinforce each other (not a random list)
- Resource-realistic (you can actually do them)

**Example (Wavelength Voice Agents):**
> 1. **Q1 Sprint 1-3:** Latency optimization — target sub-400ms p99 (team of 4 engineers)
> 2. **Q1 Sprint 1-4:** SOC 2 Type I audit — hire compliance consultant, remediation (1 engineer + external)
> 3. **Q1 Sprint 4-6:** Per-tenant guardrail configuration — eliminate hallucination risk for enterprise (2 engineers)
> 4. **Q1-Q2:** Enterprise pricing tier — committed volume, SLA guarantees, dedicated support
> 5. **Q2:** CRM integrations (Salesforce, Zendesk) — after reliability foundation is solid
>
> **Explicitly NOT doing in Q1-Q2:**
> - Multi-language support (deferred to Q3)
> - Creator-focused features (deferred indefinitely)
> - New voice cloning capabilities
> - Open Voice model expansion

---

## The Strategy Test

### Test 1: Can your competitor copy your strategy statement?

If yes, it's not a strategy. "Be the best" isn't a strategy because anyone can say it. "Focus exclusively on enterprise call centers with sub-200ms latency and SOC 2 compliance" is harder to copy because it requires specific investment and tradeoffs.

### Test 2: Does it say what you're NOT doing?

A strategy without "no" isn't a strategy. What are you giving up? What customers are you disappointing? What features are you deferring?

### Test 3: Would a smart person disagree?

If everyone agrees with your strategy, it probably isn't making a real choice. Real strategies have reasonable counter-arguments. (Use the devil's advocate method to find them.)

### Test 4: Are the actions coordinated?

Do the actions reinforce each other, or are they a random list? Latency improvement + SOC 2 + enterprise pricing = coordinated enterprise strategy. Latency improvement + new music features + mobile app = scattered list with no coherence.

---

## Strategy vs. Not Strategy

| NOT a Strategy | IS a Strategy |
|----------------|---------------|
| "Grow enterprise revenue 50%" | "Focus exclusively on the call center segment, sacrificing broader enterprise features, because that's where latency matters most and our voice quality provides a differentiated advantage" |
| "Be the best voice AI platform" | "Win on voice quality + agent intelligence, concede pure latency speed to Cartesia, and beat ElevenLabs on compliance" |
| "Improve customer satisfaction" | "Fix the top 3 churn drivers before building any new capabilities, even if it means zero new features for 2 quarters" |
| "Innovate in AI" | "Invest in pre-generation guardrails (not post-generation) because preventing hallucinations is more valuable to enterprise customers than catching them after the fact" |

---

## Strategic Decision Areas

When developing your strategy, you're making choices in these areas. Each one involves a real tradeoff — there's no "right" answer, only the answer that's right for your situation.

| Decision Area | The Question | Example Options |
|---------------|-------------|-----------------|
| **Segment Focus** | Who do we serve first? Who do we deprioritize? | Go deep on one segment / spread across many / partner for coverage |
| **Competitive Posture** | How do we respond to competitors? | Race them feature-for-feature / find a different angle / ignore and focus on our users |
| **Revenue Model** | How do we capture value? | Premium tiers / usage-based / land-and-expand / subsidize for growth |
| **AI Scope** | What role does AI play in our product? | AI IS the product / AI enhances an existing product / AI targets specific workflows |
| **Pace vs. Safety** | How fast do we move? How much risk do we absorb? | Move fast and iterate / deliberate and defensible / wait and learn from the market |

For each decision, document: what you chose, what you rejected, and why the tradeoff was worth it.

---

## How to Use This Method

### Full Strategy Development

```
Develop a product strategy for Voice Agents using Rumelt's Strategy
Kernel framework in @methods/rumelt-strategy-kernel.md.

Use these inputs:
- @state-of-voice-agents.md (current situation)
- @competitive-analysis.md (competitive landscape)
- @data/churn-analysis.csv (the problem in numbers)
- @okrs-q1.md (company priorities)

For each of the three components (Diagnosis, Direction, Action Plan):
- Be specific, not generic
- Include real numbers and evidence
- Make explicit tradeoffs

Then run the 4 strategy tests. Does it pass?
```

### Strategy Review

```
Review @voice-agents-product-strategy.md against Rumelt's Strategy
Kernel framework in @methods/rumelt-strategy-kernel.md.

- Does the diagnosis identify the CRITICAL challenge?
- Does the direction make a real choice with a real tradeoff?
- Are the actions actually coordinated (reinforcing each other)?
- Does it pass all 4 strategy tests?

Where it fails, suggest specific improvements.
```

---

*Strategy is the art of choosing what NOT to do. If your strategy doesn't make you uncomfortable about what you're leaving on the table, it's not a strategy yet.*
