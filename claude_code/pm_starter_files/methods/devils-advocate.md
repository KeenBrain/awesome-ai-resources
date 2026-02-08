# Devil's Advocate Method

A structured pressure-testing framework for strategic decisions, PRDs, roadmaps, and pitches. The goal is to surface weaknesses BEFORE stakeholders, competitors, or reality do.

---

## Core Principle

> Every weakness you find proactively is a surprise you prevent in a review meeting, a board presentation, or a customer call.

Every decision has downsides. Every plan has blind spots. The devil's advocate method forces you to confront them proactively.

---

## The 4-Question Framework

For each decision, choice, or plan, answer these four questions:

### 1. What's the strongest argument AGAINST this?

Not a straw man. The BEST version of the counter-argument. If a smart, informed person disagreed with you, what would they say?

**Example:**
- Decision: "Focus on enterprise reliability over new features"
- Devil's advocate: "Your creator segment made you who you are. Neglecting them for 2 quarters while chasing enterprise could destroy your community, kill your word-of-mouth engine, and hand ElevenLabs your most vocal advocates."

### 2. What assumption could be wrong?

Every plan is built on assumptions. Which one, if wrong, would invalidate the entire approach?

**Example:**
- Assumption: "Fixing latency will reduce enterprise churn by 40%"
- What if wrong: "What if latency is the stated reason but the real reason is the hallucination incidents? What if customers blame latency because it's concrete, but they'd churn anyway because they don't trust the AI?"

### 3. What would a competitor do to exploit this?

If your competitor knew your strategy, how would they attack?

**Example:**
- Strategy: "Invest 4 engineers in latency optimization for one quarter"
- Competitor exploit: "ElevenLabs could ship sub-100ms latency PLUS SOC 2 during the same quarter, making your 400ms target look like a participation trophy."

### 4. Under what conditions should we reverse this decision?

Define the kill switch. What signal would tell you this was wrong?

**Example:**
- Kill switch: "If after 6 weeks of latency work, we haven't achieved measurable improvement below 500ms, we stop and reassess the architectural approach."

---

## When to Use the Devil's Advocate

| Situation | How to Apply |
|-----------|-------------|
| **Before writing a PRD** | Challenge the problem statement and proposed solution |
| **After making strategic choices** | Pressure-test each of your 5 strategic decisions |
| **Before an executive pitch** | Anticipate the hardest questions |
| **During roadmap planning** | Challenge prioritization and sequencing |
| **Before a launch** | Identify failure modes and rollback triggers |
| **After a competitive analysis** | Challenge your "where we win" assumptions |

---

## The Multi-Perspective Devil's Advocate

For maximum value, run the devil's advocate from multiple perspectives:

### The Skeptical Engineer
- "Is this technically feasible in the stated timeline?"
- "What technical debt are we creating?"
- "What's the GPU cost of this approach at scale?"

### The Churned Customer
- "I already left. What would you need to show me to come back?"
- "Your competitor already solved my problem. Why would I switch back?"
- "I don't trust your AI after the hallucination incident. How do you rebuild trust?"

### The Board Member
- "What's the ROI? Show me the numbers."
- "How does this compare to investing the same resources elsewhere?"
- "What's the competitive moat here? Can ElevenLabs copy this in 3 months?"

### The Burned-Out Engineer
- "We've been promised 'just one more quarter of infrastructure work' before. Why should I believe this time is different?"
- "Half the team is interviewing elsewhere. Does this plan account for attrition?"
- "This timeline assumes zero surprises. When has that ever happened?"

---

## How to Use This Method

### For Strategic Decisions

```
Here are my strategic choices for Voice Agents:

1. Focus on enterprise call centers (not creators or podcasters)
2. Fix latency and reliability before adding features
3. Enterprise pricing tier with committed volume
4. SOC 2 and compliance before new capabilities
5. Deliberate pace — no rushing after the hallucination incident

Play devil's advocate using @methods/devils-advocate.md.

For each choice:
1. Strongest argument against
2. Assumption that could be wrong
3. How a competitor would exploit this
4. Conditions to reverse the decision

Be ruthless. Don't hold back.
```

### For PRD Review

```
Review @voice-agents-enterprise-prd.md using the devil's advocate
framework in @methods/devils-advocate.md.

For the overall approach AND for each major requirement:
- What's the strongest objection?
- What assumption is shakiest?
- What would the churned customer say?
```

### For Pitch Rehearsal

```
I'm pitching @executive-pitch-latency.md to my VP tomorrow.

Using @methods/devils-advocate.md, give me:
- The 5 hardest questions my VP will ask
- The weakest part of my argument
- The number or claim most likely to be challenged
- Suggested responses for each
```

---

## Output Format

For each decision or claim, provide:

```
DECISION: [What you decided]

DEVIL'S ADVOCATE:
1. STRONGEST COUNTER-ARGUMENT: [Best case against]
2. WEAKEST ASSUMPTION: [What could be wrong]
3. COMPETITOR EXPLOIT: [How they'd attack]
4. KILL SWITCH: [When to reverse]

VERDICT: [Is the decision still sound? What should be adjusted?]
```

---

## The Meta-Lesson

The devil's advocate isn't about being negative. It's about being prepared.

Every concern you surface here is one fewer surprise in a review meeting, one fewer blind spot in your strategy, and one more reason stakeholders trust your judgment.

The PM who says "Here are the risks, and here's how we're mitigating them" is infinitely more credible than the PM who says "This plan is perfect."

---

*Run this method on every major decision. The 5 minutes it takes will save you hours of rework.*
