# Extract Analytics Insights

Query the SQLite analytics database and extract data-driven product insights.

## Instructions

1. **Connect to the SQLite database** at `data/analytics/product_analytics.db` using the sqlite MCP server.

2. **Run these analytical queries**:

### Usage Patterns
- Daily active users trend (last 90 days) — is it growing?
- Average session duration by device type
- Peak usage hours/days
- Feature usage distribution (views, clicks per feature)

### Error & Abandonment Analysis
- Features with highest error counts
- Features with highest abandonment rates
- Error trends over time — getting worse?

### Funnel Conversion
- Conversion rate at each stage (signup → onboarding → activation → active → paid)
- Where is the biggest drop-off?
- Funnel completion by time cohort

### NPS Analysis
- Overall NPS score
- NPS by segment (free, pro, enterprise)
- Distribution of scores (promoters vs detractors vs passives)
- Common themes in NPS comments

### Revenue & Growth
- MRR trend
- New signups trend
- Churn rate trend
- Revenue per user segment

3. **Write the output** to `output/analytics-insights.md` with this structure:

```markdown
# Analytics Insights Report
Generated: [timestamp]
Data range: [start] to [end]

## Executive Summary
[Top 3-4 data-driven findings]

## Key Metrics
| Metric | Value | Trend |
|--------|-------|-------|
| DAU | X | +Y% |
| [etc.] | | |

## Critical Findings

### 1. [Finding Title]
**Data**: [specific numbers from queries]
**Impact**: [what this means for the product]
**Related Feature**: [component name if applicable]

[Repeat for each finding...]

## Feature Health Scorecard
| Feature | Views | Errors | Abandon Rate | Health |
|---------|-------|--------|--------------|--------|
| [name] | X | Y | Z% | 🔴/🟡/🟢 |

## Funnel Analysis
[Stage-by-stage breakdown with conversion rates]

## NPS Breakdown
[By segment with scores and key comments]

## Recommendations
[Data-driven recommendations ranked by impact]
```

4. **Verify** the output file was written successfully.
