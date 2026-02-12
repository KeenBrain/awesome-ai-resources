# Prioritize Features (RICE Scoring)

Read both insight reports and apply RICE scoring to rank all identified features.

## Instructions

1. **Read both insight files**:
   - `output/interview-insights.md` (qualitative data)
   - `output/analytics-insights.md` (quantitative data)

2. **Identify all candidate features** from both reports. Each feature should be a concrete, implementable improvement mapped to specific code files.

3. **Apply RICE scoring** to each feature:

### Reach (1-10)
Derived from analytics data:
- How many users are affected? (from feature_usage views, error counts)
- What % of DAU encounters this issue?
- Score: 10 = affects >50% of users, 1 = affects <5%

### Impact (1-10)
Derived from interview severity + analytics impact:
- How severe is the pain point? (critical=10, high=8, medium=5, low=2)
- What's the abandonment/error rate?
- Does it affect conversion funnel?

### Confidence (1-10)
Based on evidence strength:
- How many data sources confirm this? (interviews + analytics = high)
- How many interview participants mentioned it?
- Is the analytics signal clear and unambiguous?
- Score: 10 = 4+ interviews + strong analytics, 5 = mixed signals, 1 = single weak signal

### Effort (1-10, lower = less effort = better)
Based on code scope:
- How many files need to change?
- Is it a new feature or fixing existing code?
- Complexity estimate
- Score: 1 = single simple file change, 10 = major architectural change

### RICE Score = (Reach × Impact × Confidence) / Effort

4. **Tag each feature** with:
   - Files to modify (specific component paths)
   - Whether features overlap (can't be implemented in parallel if they touch the same files)
   - Implementation approach (brief)

5. **Select top 3 non-overlapping features** for implementation — these should touch different files so they can be implemented by parallel coding agents.

6. **Write the output** to `output/prioritized-features.md`:

```markdown
# Feature Prioritization Report
Generated: [timestamp]

## RICE Scoring Summary

| Rank | Feature | Reach | Impact | Confidence | Effort | RICE Score | Files |
|------|---------|-------|--------|------------|--------|------------|-------|
| 1 | [name] | X | X | X | X | XX.X | [files] |
| [etc.] | | | | | | | |

## Top 5 Features (Detailed)

### #1: [Feature Name] — RICE: XX.X
**Files**: [list of files to modify]
**Evidence**:
- Interview: [summary of qualitative evidence]
- Analytics: [summary of quantitative evidence]
**Implementation Approach**: [brief description]
**Overlaps with**: [other features touching same files, or "None"]

[Repeat for top 5...]

## Selected for Implementation (Top 3 Non-Overlapping)
1. [Feature] → [files] — Agent 1
2. [Feature] → [files] — Agent 2
3. [Feature] → [files] — Agent 3

## Deferred Features
[Features ranked 4+ with brief reasoning for deferral]
```

7. **Verify** the output file was written successfully.
