# Post-Launch Analysis Framework

A layered approach for analyzing A/B tests, feature launches, and post-launch metrics. Work through each layer in order — don't skip to segment breakdowns before checking the headline, and don't declare success based on the headline alone.

---

## The Five Layers

### Layer 1: Headline Results
**What happened at the highest level?**

Start here. Look at the primary metric the experiment was designed to move.

| Question | What to Check |
|----------|---------------|
| Did the primary metric move? | Compare treatment vs. control, or pre vs. post |
| In which direction? | Positive, negative, or flat |
| By how much? | Absolute change and percentage change |
| Is the magnitude meaningful? | A 0.1% improvement might be statistically significant but practically useless |

**Example:**
> Voice Agents Enterprise Beta — Week 4
> - Average latency: 350ms (down from 500ms at launch) — Improving
> - Hallucination rate: 1.8% (down from 3.2%) — Improving
> - Enterprise churn: 5.2% monthly (down from 8%) — Improving
> - Uptime: 99.4% (target: 99.9%) — Below target

### Layer 2: Confidence Check
**Can we trust the numbers?**

| Question | What to Check |
|----------|---------------|
| Is the sample size large enough? | Minimum detectable effect for your sample |
| What's the p-value? | < 0.05 is conventional threshold |
| What's the confidence interval? | Narrow = trustworthy, wide = uncertain |
| How long did the experiment run? | Account for day-of-week effects (minimum 2 full weeks) |
| Are there novelty or primacy effects? | Did the metric change over time during the experiment? |

**Rules of thumb:**
- n < 100 per group: Be very skeptical of any result
- n = 100-1,000: Moderate confidence, look for large effects
- n > 1,000: Higher confidence, can detect smaller effects
- Always check if the effect stabilized or if it's still moving

**Example:**
> Latency improvement: n=4 pilot customers, 28 days of data
> - Sample is small (4 customers) — interpret directionally, not definitively
> - Daily data points (112 total) help, but customer-level n=4 is the constraint
> - Confidence: Medium — trend is clear, but absolute numbers could shift significantly with 1 more customer

### Layer 3: Segment Breakdown
**Is the average hiding something?**

This is where the magic happens. The topline might look modest, but specific segments could be winning big (or losing badly).

| Segment to Check | Why It Matters |
|-----------------|---------------|
| Customer tier (enterprise vs. SMB vs. free) | Enterprise and SMB often have opposite reactions |
| Use case (call center vs. support vs. sales) | Different use cases have different latency sensitivity |
| Geography/timezone | Performance varies by region |
| Tenure (new vs. established) | New customers vs. long-time users behave differently |
| Volume (high-usage vs. low-usage) | Power users vs. casual users |
| Source (organic vs. paid vs. referral) | Acquisition channel affects engagement patterns |

**Example:**
> Topline: Hallucination rate dropped from 3.2% to 1.8% (looks great!)
> Segment analysis:
> - Financial services customers: Dropped from 3.2% to 0.9% (guardrails working perfectly)
> - Healthcare customers: Dropped from 3.2% to 3.0% (barely improved — medical terms not in guardrails)
> - Retail customers: Dropped from 3.2% to 1.5% (solid improvement)
>
> ACTION: Healthcare segment needs domain-specific guardrails. Don't celebrate the topline without fixing this.

### Layer 4: Tradeoff Scan
**Did we improve one thing at the cost of another?**

| Question | What to Check |
|----------|---------------|
| Is the behavior sustained? | Day 1 vs. Day 7 vs. Day 30 retention |
| Are we trading one metric for another? | Did improving latency hurt accuracy? |
| Are the right users affected? | Is the improvement coming from high-value or low-value accounts? |
| Is there a ceiling effect? | Are we approaching diminishing returns? |

**The "gaming" check:**
- Latency improved by skipping guardrails checks? BAD.
- Hallucination rate dropped because we restricted the AI's responses too aggressively? Possible overcorrection.
- Churn rate improved but new sales slowed? Might be fixing retention at the cost of acquisition.

**Example:**
> Latency dropped from 500ms to 350ms (great!)
> But: First-response accuracy dropped from 94% to 91%
> Diagnosis: The speed optimization is truncating some responses before the AI finishes reasoning
> Action: Find the speed-accuracy tradeoff sweet spot, don't blindly optimize for one

### Layer 5: Forward Signals
**What does this data predict about where we'll be next month?**

| Leading Indicator | What It Predicts |
|------------------|-----------------|
| Early usage patterns (Day 1-3) | Long-term engagement and retention |
| Support ticket volume and type | Product quality and user confusion |
| Feature adoption rate | Whether the improvement matters to users |
| NPS / satisfaction changes | Future churn and word-of-mouth |
| Expansion signals (more seats, higher usage) | Revenue growth |

**Example:**
> Leading indicators after 4 weeks of beta:
> - CallVault (churned customer) re-engaged — running test calls (recovery signal)
> - 2 pilot customers asked about adding more phone lines (expansion signal)
> - Support tickets about latency dropped 60% (pain point addressed)
> - New type of support ticket emerging: "How do we configure guardrails for compliance?" (adoption signal — they're going deeper)
> - 1 pilot customer's CSM reported "the team is excited about this" (sentiment signal)

---

## The Analysis Template

For any experiment or launch analysis, work through each layer:

```markdown
## Experiment: [Name]
### Duration: [Start] to [End]
### Primary metric: [What you're measuring]

### Layer 1: Headline Results
- Primary metric: [before] → [after] ([change]%)
- Key secondary metrics: [list with changes]
- Direction: [Positive / Negative / Flat / Mixed]

### Layer 2: Confidence Check
- Sample size: [n]
- Confidence level: [High / Medium / Low]
- Key caveat: [what to be careful about]

### Layer 3: Segment Breakdown
- [Segment A]: [result]
- [Segment B]: [result]
- Surprising finding: [what the average hid]

### Layer 4: Tradeoff Scan
- Are we gaming any metrics? [yes/no, details]
- Metric tradeoffs: [what improved at the cost of what?]
- Sustainability: [is this a lasting improvement?]

### Layer 5: Forward Signals
- Signals of future success: [list]
- Signals of future risk: [list]
- What to monitor next: [list]

### Recommendation
[What to do based on all 5 layers]
```

---

## How to Use This Method

```
Analyze @data/post-launch-metrics.csv using the post-launch analysis
framework in @methods/experiment-analysis.md.

Work through all 5 layers:
1. Headline results — how are the key metrics trending?
2. Confidence check — can we trust these numbers given our sample?
3. Segment breakdown — is the average hiding anything?
4. Tradeoff scan — did improving one metric hurt another?
5. Forward signals — what does this predict for next month?

Compare results to launch criteria from @voice-agents-launch-plan.md.
Give me a go/no-go recommendation for expanding from beta to limited GA.
```

---

## Common Mistakes

| Mistake | Consequence | Fix |
|---------|------------|-----|
| Stopping at Layer 1 | Miss segment-level problems | Always run Layer 3 |
| Declaring significance with small n | False confidence | Be honest about sample size |
| Ignoring metric tradeoffs | Optimize one metric, break another | Always check Layer 4 |
| Not defining success criteria before the experiment | Moving goalposts | Write criteria before launch |
| Celebrating forward signals as proven outcomes | Premature victory | Forward signals predict, they don't prove |

---

*Move through all 5 layers. The headline tells you what happened. The segments tell you who it happened to. The tradeoff scan tells you what it cost. The forward signals tell you where it's headed.*
