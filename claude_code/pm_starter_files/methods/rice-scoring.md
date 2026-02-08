# RICE Scoring Framework

A quantitative prioritization method for ranking features, projects, or backlog items. Score each item on four dimensions, then calculate a composite score.

---

## The Formula

```
RICE Score = (Reach × Impact × Confidence) / Effort
```

---

## The Four Dimensions

### Reach
**How many users/accounts will this affect in a defined time period?**

| Score | Definition | Example |
|-------|-----------|---------|
| 10,000+ | Affects all or nearly all users | Core latency improvement |
| 5,000-10,000 | Affects most users | Notification system redesign |
| 1,000-5,000 | Affects a significant segment | Enterprise admin dashboard |
| 100-1,000 | Affects a small segment | API-only feature for developers |
| <100 | Affects very few users | Custom integration for one account |

**How to estimate:**
- Use product analytics (DAU/MAU for the affected area)
- Count the number of accounts that have requested this
- Look at support ticket volume related to this pain point
- Use funnel data to count users who reach the relevant step

### Impact
**How much will this move the target metric per user affected?**

| Score | Definition | Example |
|-------|-----------|---------|
| 3 | Massive impact | Reduces churn by 50%+ for affected users |
| 2 | High impact | Reduces churn by 20-50% for affected users |
| 1 | Medium impact | Reduces churn by 5-20% for affected users |
| 0.5 | Low impact | Slight improvement, hard to measure |
| 0.25 | Minimal impact | Nice-to-have, no measurable metric change |

**How to estimate:**
- Use historical data from similar features
- Reference user research (% who said this would change their behavior)
- Look at competitor data (what happened when they shipped this?)
- Start with 1 (medium) if you truly don't know

### Confidence
**How sure are you about your Reach and Impact estimates?**

| Score | Definition | Evidence Required |
|-------|-----------|-------------------|
| 100% | High confidence | Have data: analytics, user research, A/B test results |
| 80% | Medium confidence | Have some data: customer interviews, competitor benchmarks |
| 50% | Low confidence | Mostly intuition, limited supporting data |
| 20% | Moonshot | Speculation, no supporting data |

**The honesty check:**
- If you haven't talked to users about this, confidence is at most 50%
- If you have data but from a different segment, discount by 20%
- If the feature is unprecedented (no comparable), cap at 50%

### Effort
**How many person-months of engineering, design, and PM time?**

| Score | Definition | Example |
|-------|-----------|---------|
| 0.5 | Half a person-month | Config change, small UI tweak |
| 1 | One person-month | Simple feature, one engineer |
| 2 | Two person-months | Medium feature, 1-2 engineers |
| 5 | Five person-months | Large feature, full team sprint |
| 10 | Ten person-months | Major initiative, multi-sprint |
| 20+ | Twenty+ person-months | Platform-level change |

**How to estimate:**
- Ask your tech lead for a t-shirt size, then convert
- Include design time (typically 20-30% of eng estimate)
- Include PM time (writing specs, testing, launch coordination)
- Add 30% buffer for unknowns (always)

---

## Scoring Example

| Item | Reach | Impact | Confidence | Effort | RICE Score |
|------|-------|--------|-----------|--------|------------|
| Latency to sub-400ms | 5,000 | 3 | 80% | 10 | 1,200 |
| SOC 2 Type I | 500 | 3 | 100% | 5 | 300 |
| Per-tenant guardrails | 2,000 | 2 | 80% | 3 | 1,067 |
| Multi-language support | 1,000 | 2 | 50% | 8 | 125 |
| Dark mode | 8,000 | 0.25 | 80% | 1 | 1,600 |

**Interpretation:** Dark mode scores highest on RICE because it's high reach, low effort. But it doesn't serve the strategic priority (enterprise reliability). This is why RICE is a starting point, not the final answer — you need a strategic alignment overlay.

---

## Strategic Alignment Overlay

After RICE scoring, flag items that are strategically important even if the RICE score is low:

| Flag | Meaning | Example |
|------|---------|---------|
| **STRATEGIC** | Aligns with OKRs even if RICE is modest | SOC 2 (blocks enterprise deals) |
| **DEPENDENCY** | Other high-RICE items depend on this | Infrastructure upgrade |
| **RETENTION** | Directly tied to churn data | Latency optimization |
| **COMPETITIVE** | Competitors have it, we're losing deals without it | Enterprise admin controls |

---

## How to Use This Method

```
Score the items in @data/feature-requests.csv using the RICE framework
in @methods/rice-scoring.md.

For each item:
1. Estimate Reach from @data/usage-metrics.csv
2. Estimate Impact from @data/churn-analysis.csv and @research/ interviews
3. Assess Confidence based on available evidence
4. Estimate Effort (ask me if unclear)

Add strategic alignment flags where relevant.
Rank by RICE score, then note where strategic importance overrides the score.
```

---

*RICE was created by Sean McBride at Intercom. Use it as a starting framework, not a replacement for judgment.*
