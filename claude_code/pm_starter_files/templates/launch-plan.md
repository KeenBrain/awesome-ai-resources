# Launch Plan

*Owner: [Name] | Launch date: [Date] | Status: Planning / Ready / Launched*

---

## Launch Overview

- **What:** [Feature/product name — one sentence description]
- **When:** [Target launch date and time, with timezone]
- **Why:** [Business goal this launch supports]
- **Who:** [Target users — be specific]

## Launch Tier

*Tier determines the level of coordination and comms required.*

| Tier | Description | This Launch |
|------|------------|-------------|
| **P0** | Major launch. Full cross-functional coordination, external comms, exec visibility. | [ ] |
| **P1** | Notable launch. Targeted comms, key stakeholder alignment. | [ ] |
| **P2** | Minor launch. Internal awareness, changelog update, no external push. | [ ] |

## Target Audience

- **Primary:** [Who benefits most]
- **Secondary:** [Who else is affected]
- **Internal stakeholders:** [Support, sales, etc. who need to know]

## Launch Goals & Success Metrics

| Goal | Metric | Target (7-day) | Target (30-day) |
|------|--------|---------------|-----------------|
| [e.g., Adoption] | [e.g., % of MAU using feature] | | |
| [e.g., Quality] | [e.g., Error rate < X%] | | |
| [e.g., Satisfaction] | [e.g., Thumbs-up rate] | | |

---

## Pre-Launch Checklist — 2 Weeks Out

- [ ] Feature complete and QA'd
- [ ] AI evals passing success criteria (link to [ai-eval.md])
- [ ] Analytics / tracking instrumented and verified
- [ ] Feature flag configured for staged rollout
- [ ] Support team briefed with FAQ doc
- [ ] Release notes drafted (link to [release-notes.md])
- [ ] External comms approved (blog, email, social)
- [ ] Legal / compliance review (if applicable)
- [ ] Rollback procedure documented and tested
- [ ] Load testing complete (if applicable)

## Launch Day Plan

| Time | Action | DRI | Channel |
|------|--------|-----|---------|
| [T-1h] | Final go/no-go check | [Name] | [Slack channel] |
| [T-0] | Flip feature flag — [X]% rollout | [Name] | |
| [T+15m] | Verify dashboards, check error rates | [Name] | |
| [T+1h] | Expand to [X]% if metrics healthy | [Name] | |
| [T+1h] | Publish external comms | [Name] | |
| [T+2h] | Monitor support queue | [Name] | |
| [T+4h] | Status check — expand or hold | [Name] | |
| [EOD] | Launch day retro / async update | [Name] | |

## Post-Launch Monitoring — First 48 Hours

| Metric | Threshold for Concern | Alert Owner |
|--------|----------------------|-------------|
| Error rate | > [X]% | [Name] |
| Latency p95 | > [X] ms | [Name] |
| Support tickets | > [X] per hour | [Name] |
| [Feature-specific metric] | [Threshold] | [Name] |

## Rollback Plan

- **Trigger:** [Under what conditions do we roll back?]
- **Mechanism:** [Feature flag off / revert deploy / etc.]
- **DRI:** [Name]
- **Estimated rollback time:** [X minutes]
- **User communication if rolled back:** [What do we tell users?]

---

## Communications Plan

### Internal
- [ ] Slack announcement in [#channel] at [time]
- [ ] Demo in [meeting name] on [date]
- [ ] Update internal wiki / knowledge base

### External
- [ ] In-app announcement / banner
- [ ] Release notes published
- [ ] Blog post (if P0/P1)
- [ ] Email to [segment] (if P0/P1)
- [ ] Social media (if P0)

## Cross-Functional DRIs

| Area | Owner | Status |
|------|-------|--------|
| Engineering | [Name] | Ready / Not Ready |
| Design | [Name] | |
| Product | [Name] | |
| Marketing | [Name] | |
| Support | [Name] | |
| Legal | [Name] | |
| Data / Analytics | [Name] | |

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| | High / Med / Low | High / Med / Low | |
| | | | |

---

*After launch: Schedule a retro within one week. Update this doc with actual results vs. targets.*
