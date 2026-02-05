# AI Product Evaluation

*Every AI product needs evals. If you can't measure it, you can't ship it.*

*Owner: [Name] | Date: [Date] | Model/Feature: [Name + version]*

---

## What We're Evaluating

- **Feature / model:** [Name and version]
- **Scope:** [What specifically is being tested — e.g., "Voice cloning accuracy on English-language samples under 60 seconds"]
- **Why now:** [What triggered this eval — new model, pre-launch gate, regression check]

## Success Criteria

*Define pass/fail BEFORE you run the eval. Don't move the goalposts after.*

| Criteria | Threshold | Priority |
|----------|-----------|----------|
| [e.g., Accuracy] | >= [X]% | Must-hit |
| [e.g., Latency p95] | < [X] ms | Must-hit |
| [e.g., Cost per request] | < $[X] | Target |
| [e.g., User satisfaction] | >= [X]/5 | Target |

---

## Test Cases

| # | Scenario | Input | Expected Output | Actual Output | Pass/Fail |
|---|---------|-------|----------------|---------------|-----------|
| 1 | [Happy path] | | | | |
| 2 | [Variation] | | | | |
| 3 | [Boundary case] | | | | |
| 4 | [Different persona/accent/style] | | | | |
| 5 | [Adversarial input] | | | | |

*Minimum recommended: 20+ test cases for any production-bound eval. Table above is a starting sample.*

## Edge Cases

*Inputs or scenarios that are uncommon but important to handle correctly.*

- [Edge case 1 — e.g., "Empty audio file"]
- [Edge case 2 — e.g., "Background music louder than speech"]
- [Edge case 3 — e.g., "Non-English input when English is expected"]

## Failure Modes Observed

*What went wrong? Categorize the failures.*

| Failure Type | Frequency | Severity | Example |
|-------------|-----------|----------|---------|
| [e.g., Hallucinated words] | [X / N cases] | High / Med / Low | [Brief description] |
| [e.g., Truncated output] | | | |
| [e.g., Latency spike] | | | |

---

## Quantitative Results

| Metric | Result | Target | Pass/Fail |
|--------|--------|--------|-----------|
| Accuracy (overall) | | | |
| Accuracy (edge cases) | | | |
| Latency — p50 | | | |
| Latency — p95 | | | |
| Cost per request | | | |
| Error rate | | | |

## Qualitative Assessment

*Human judgment matters for AI products. Summarize what reviewers observed.*

- **Output quality:** [Summary — e.g., "Natural-sounding 85% of the time, robotic on longer passages"]
- **Consistency:** [Does it produce similar quality across runs?]
- **User experience gaps:** [Anything that feels off even if metrics pass?]

---

## Recommendations

- **Ship / Don't ship / Ship with caveats:** [Clear recommendation]
- **Key blockers (if any):** [What must be fixed before launch]
- **Acceptable trade-offs:** [What we're okay living with for now]

## Next Steps

- [ ] [Action item — e.g., "Retrain on edge case dataset"]
- [ ] [Action item — e.g., "Add monitoring for failure mode X"]
- [ ] [Action item — e.g., "Schedule follow-up eval for v2"]
- [ ] [Action item — e.g., "Set up automated regression eval in CI"]

---

*Evals are not one-time events. Schedule recurring evals for any AI feature in production.*
