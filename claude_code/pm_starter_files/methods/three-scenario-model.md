# Three-Scenario Impact Model

Never present a single estimate. Always present three scenarios to account for uncertainty and build stakeholder confidence.

---

## The Three Scenarios

| Scenario | Assumption Level | Framing | Use For |
|----------|-----------------|---------|---------|
| **Conservative** | Cautious — things go worse than expected | "Even in the downside case, the investment pays for itself" | Risk mitigation, budget justification |
| **Expected** | Reasonable middle ground | "Our best estimate based on available data" | Planning, resource allocation, timelines |
| **Aggressive** | Favorable — things go better than expected | "If adoption exceeds expectations, the upside is..." | Stretch goals, investor narratives, upside framing |

---

## Sizing the Opportunity

To build a credible business case, you need to quantify what's at stake:

```
Revenue at Risk = Affected Accounts × Problem Rate × Attribution % × Revenue per Account
```

### Breaking Down Each Component

**Affected Accounts:** How many accounts are in the zone of impact?
- Source: Product analytics, CRM data, segment counts
- Example: 150 enterprise Voice Agents accounts

**Problem Rate:** What's the current rate of the negative behavior you're trying to fix?
- Source: Funnel data, engagement metrics, churn data
- Example: 8% monthly enterprise churn rate

**Attribution %:** What percentage of that problem is caused by the specific issue you're addressing?
- Source: Exit interviews, support tickets, survey data
- Example: 65% of churned accounts cite latency as primary reason

**Revenue per Account:** What's each account worth?
- Source: Revenue data, LTV calculations, contract values
- Example: Average enterprise account = $24K ARR

Then apply a **recovery rate** (how much of the problem you expect to fix) — and that's where the three scenarios come in.

---

## Lift Estimation Sources (Ranked by Reliability)

| Rank | Source | Reliability | When to Use |
|------|--------|-------------|-------------|
| 1 | **Your own historical data** | Highest | You've shipped something similar before and measured the impact |
| 2 | **User research** | High | Customers told you this would change their behavior (discount by 40% for self-report bias) |
| 3 | **Competitor benchmarks** | Medium | A competitor shipped this and you have data on their results |
| 4 | **Industry benchmarks** | Medium-Low | Published research on similar changes in similar products |
| 5 | **Expert judgment** | Lowest | Your best guess based on experience (be honest about this) |

### Applying Scenarios to Lift Estimates

| Source of Estimate | Conservative | Expected | Aggressive |
|-------------------|-------------|----------|------------|
| Historical data | 0.6x of past result | 1.0x of past result | 1.4x of past result |
| User research | 0.3x of stated intent | 0.5x of stated intent | 0.7x of stated intent |
| Competitor benchmark | 0.5x of their result | 0.8x of their result | 1.0x of their result |
| Expert judgment | 0.5x of your estimate | 1.0x of your estimate | 1.5x of your estimate |

---

## Worked Example: Latency Optimization

**Context:** Wavelength Voice Agents, 150 enterprise accounts, 8% monthly churn, top churn reason is 800ms latency.

### Inputs

| Component | Value | Source |
|-----------|-------|--------|
| Users Affected | 150 enterprise accounts | CRM data |
| Current Churn Rate | 8% monthly | @data/churn-analysis.csv |
| Churn attributed to latency | 65% of churned accounts cite latency | Exit interviews |
| Latency-driven churn rate | 5.2% monthly (8% × 65%) | Calculated |
| Value per account | $24K ARR | Revenue data |
| Investment required | 4 engineers × 1 quarter | Engineering estimate |

### Lift Estimates

| Scenario | Churn Recovery Rate | Source |
|----------|-------------------|--------|
| Conservative | 20% recovery of latency-driven churn | Expert judgment — minimum expected from any improvement |
| Expected | 40% recovery | User research — 72% said they'd reconsider if latency dropped below 400ms (discounted by 45% for self-report bias) |
| Aggressive | 60% recovery | Competitor benchmark — ElevenLabs saw ~60% enterprise churn reduction after latency improvements |

### Results

| Scenario | Monthly Churn Saved | Annual ARR Recovered | ROI vs. Investment |
|----------|--------------------|--------------------|-------------------|
| **Conservative** | 150 × 5.2% × 20% = 1.56 accounts/mo | 1.56 × $24K × 12 = **$449K** | 2.2x |
| **Expected** | 150 × 5.2% × 40% = 3.12 accounts/mo | 3.12 × $24K × 12 = **$898K** | 4.5x |
| **Aggressive** | 150 × 5.2% × 60% = 4.68 accounts/mo | 4.68 × $24K × 12 = **$1.35M** | 6.7x |

**Investment cost:** 4 engineers × $200K fully-loaded annual × 0.25 (one quarter) = $200K

### The Pitch

> "Even in the conservative scenario, the latency optimization project recovers $449K in ARR — a 2.2x return on the $200K investment. In our expected scenario, we recover $898K. The cost of doing nothing: we continue losing $1.87M annually to latency-driven churn."

---

## How to Use This Method

### For Impact Estimation

```
Build a three-scenario impact model for [feature/project].

Use the framework in @methods/three-scenario-model.md.
Pull data from:
- @data/churn-analysis.csv (churn rates, revenue at risk)
- @data/usage-metrics.csv (user counts, engagement data)
- @research/ (user research for lift estimates)

Show conservative, expected, and aggressive scenarios.
Calculate ROI for each scenario against the estimated investment.
```

### For Executive Pitches

```
Using the three-scenario model in @methods/three-scenario-model.md,
build the financial case for [project].

Lead with: "Even in the worst case, this pays for itself."
Show all three scenarios.
Compare to the cost of doing nothing.
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Only showing the aggressive case | Always lead with conservative — it builds trust |
| Using one source for lift estimate | Triangulate from multiple sources |
| Ignoring self-report bias | Discount user-stated intent by 40-60% |
| Forgetting opportunity cost | Include what you're NOT doing |
| Precise-seeming numbers from vague inputs | Be honest: "We estimate..." not "The data shows..." |

---

*Present all three scenarios. Let the decision-maker choose which one to plan for. Your job is to give them an honest range, not a false sense of precision.*
