# Socratic Questioning Method for PRDs

A structured interview framework to pressure-test your thinking before writing a PRD. Ask Claude to interview you using these 5 lenses. Answer honestly — vague answers get follow-up pushback.

---

## Lens 1: Problem Definition

Ask these questions to validate that the problem is real, specific, and worth solving.

- Who exactly feels this pain? (Be specific — not "users" but "VP of Ops at enterprises with 500+ daily call volume")
- How often do they feel it? (Daily? Weekly? Only during onboarding?)
- How severely does it affect them? (Annoyance? Revenue loss? Churn trigger?)
- What's the cost of NOT solving this? (Quantify: lost ARR, wasted hours, churn rate)
- How do users solve this today? (Workarounds, competitors, manual processes)
- What evidence do we have that this is a real problem? (Interviews, data, support tickets, churn reasons)

**Red flags to probe:**
- "Everyone wants this" → Who specifically? How do you know?
- "It's obvious" → Obvious to whom? What data supports this?
- "Competitors have it" → Do our users actually need it, or is this feature envy?

---

## Lens 2: Solution Fitness

Ask these questions to stress-test the proposed solution.

- Why THIS solution? What alternatives did you consider?
- What's the simplest version that would solve 80% of the problem?
- What are you assuming about user behavior that might be wrong?
- What's the riskiest assumption? How would you test it?
- If an engineer said "this will take 3x longer than you think," what would you cut?
- Is this a vitamin (nice-to-have) or a painkiller (must-have)?

**Red flags to probe:**
- Jumping to a complex solution without considering simpler options
- No mention of alternatives considered
- Solution designed for the loudest customer, not the most common need

---

## Lens 3: Measurable Outcomes

Ask these questions to define what "winning" looks like.

- How will you know this worked? What metric moves?
- What's the specific target? (Not "improve retention" but "reduce enterprise churn from 8% to 5% within 90 days")
- What would indicate failure? At what point do you pull the plug?
- What does "good enough for v1" look like?
- How long after launch until you can measure success?
- What leading indicators will you track before the lagging metric moves?

**Red flags to probe:**
- No measurable success criteria
- Success defined as "ship it" rather than "achieve outcome"
- No failure criteria or kill switch

---

## Lens 4: Boundaries & Tradeoffs

Ask these questions to surface hidden risks and hard boundaries.

- What's the biggest technical risk?
- What are we explicitly NOT doing? Why?
- If you had half the engineering time, what would you cut?
- What dependencies exist? (Other teams, third parties, infrastructure)
- Are there security, compliance, or legal implications?
- What's the opportunity cost? (What are we NOT building by building this?)

**Red flags to probe:**
- "No constraints" → There are always constraints
- Ignoring engineering capacity or technical debt
- No mention of what's out of scope

---

## Lens 5: Timing & Alignment

Ask these questions to confirm this is the right thing to build right now.

- Why now? What changed to make this urgent?
- How does this connect to our quarterly OKRs?
- Does this serve our target customer segment, or a different one?
- What would a competitor do if we shipped this? Would it matter?
- If we could only ship 3 things this quarter, would this be one of them?
- Does this strengthen our moat or just keep up with competitors?

**Red flags to probe:**
- Building because a single customer asked (vs. a pattern of demand)
- "The CEO wants it" without strategic justification
- No connection to OKRs or company strategy

---

## How to Use This Method

### Option 1: Claude Interviews You

```
I want to write a PRD for [feature]. Before we start writing,
interview me using the Socratic questioning method in @methods/socratic-questioning.md.

Ask one category at a time. Wait for my answers before moving on.
Push back if my answers are vague or hand-wavy.
```

### Option 2: Claude Reviews a Draft PRD

```
Review @[prd-file] using the Socratic questioning framework
in @methods/socratic-questioning.md.

For each category, identify:
- Questions the PRD answers well
- Questions the PRD leaves unanswered
- Where the reasoning is weak or assumes too much
```

---

*Adapted for PM workflows. Use before every PRD, feature brief, or strategic decision.*
