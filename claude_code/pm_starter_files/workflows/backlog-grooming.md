# Backlog Grooming & Prioritization Workflow
**Product: Voice Agents | Owner: [PM Name] | Last updated: Jan 2026**

This is the working process for how we take the firehose of inputs and turn them into a prioritized sprint backlog. It's not perfect — still iterating on it. But it's what we've got.

---

## Step 1: Gather Inputs

Pull from all signal sources. Don't filter yet — that's step 2's job.

### Sources to check every grooming cycle (biweekly):

**Customer Feedback**
- [ ] Zendesk tickets tagged `feature-request` or `voice-agents` (export last 2 weeks)
- [ ] G2 and TrustPilot reviews mentioning Voice Agents (check the app-reviews tracker)
- [ ] Gong call recordings flagged by sales as "product feedback" (usually 3-5 per week)
- [ ] Enterprise pilot customer Slack channels — read every message, even the ones that look like small talk. The real feedback hides in casual comments.
- [ ] Churned customer exit interviews (monthly, from CS team)

**Internal Signals**
- [ ] Support ticket volume by category — look for spikes and new categories
- [ ] Sales competitive loss reasons (CRM dashboard, `lost_deal_reason` field)
- [ ] Engineering tech debt tracker (the spreadsheet Amir maintains, not Jira — Jira is always stale)
- [ ] On-call incident reports from last 2 weeks
- [ ] Latency and reliability dashboards — any regressions?

**Strategic Inputs**
- [ ] Company OKRs (current quarter)
  - **O1**: Establish Voice Agents as the enterprise leader in AI voice → KR: 15 enterprise pilots, 5 conversions to paid
  - **O2**: Reduce latency to sub-300ms average → KR: p50 <250ms, p99 <800ms by end of Q1
  - **O3**: Achieve SOC 2 Type II certification → KR: audit complete by March 2026
  - **O4**: Grow developer ecosystem → KR: 10K monthly active developers across all products
- [ ] Board deck priorities (quarterly — check with Chief of Staff)
- [ ] Competitive intel updates (see /research/competitor-intel.md)
- [ ] Regulatory developments (EU AI Act timeline, US Voice PROTECT Act)

**External Signals**
- [ ] Social media mentions (see /research/social-media-feedback.md)
- [ ] Reddit threads mentioning Wavelength or competitors
- [ ] Developer community feedback (Discord #feature-requests channel, GitHub issues on Open Voice)
- [ ] Analyst reports if any (Gartner hasn't covered us yet but Forrester had a brief mention in their Nov voice AI landscape report)

### Output of Step 1
A raw unsorted list of candidate items. Usually 40-70 items per grooming cycle. Dump everything into the `backlog-candidates` Notion database. Don't worry about duplicates yet.

---

## Step 2: Score Using RICE Framework

For each candidate item, score on the four RICE dimensions. Be honest — overscoring Impact is the most common failure mode. We all think our pet feature is a 3x.

### Reach (How many customers/users will this impact in the next quarter?)

| Score | Definition | Voice Agents Context |
|-------|-----------|---------------------|
| 10 | All enterprise pilots + all trial users | Changes to core call flow, latency improvements |
| 5 | All enterprise pilots OR all trial users | Enterprise-only features (SSO, SLA), trial-only features |
| 3 | Multiple enterprise pilots | Features requested by 2+ pilot customers |
| 1 | Single customer request | One-off integration, custom feature |
| 0.5 | Internal/speculative | Tech debt, future-looking architecture |

### Impact (How much will this move the needle for reached users?)

| Score | Definition | Voice Agents Context |
|-------|-----------|---------------------|
| 3 | Massive — directly unblocks conversion or prevents churn | SOC 2, latency <300ms, critical bug fixes |
| 2 | High — meaningful improvement to core experience | New integrations (Salesforce), analytics dashboard, multilingual expansion |
| 1 | Medium — nice to have, improves satisfaction | UI polish, minor feature additions, documentation |
| 0.5 | Low — marginal improvement | Edge case handling, cosmetic changes |

### Confidence (How sure are we about reach and impact estimates?)

| Score | Definition |
|-------|-----------|
| 100% | Have data from multiple sources confirming demand |
| 80% | Strong signal from 2+ customers or clear competitive gap |
| 50% | Some signal but unvalidated — gut feeling or single customer request |
| 20% | Speculative — no direct signal, strategic bet |

### Effort (Person-weeks of engineering effort)

Estimate with engineering lead during grooming. Use t-shirt sizes first, then convert:
- **XS**: <1 week (0.5 person-weeks)
- **S**: 1-2 weeks (1.5 person-weeks)
- **M**: 2-4 weeks (3 person-weeks)
- **L**: 4-8 weeks (6 person-weeks)
- **XL**: 8+ weeks (10 person-weeks) — consider breaking down

### RICE Score Calculation

```
RICE Score = (Reach × Impact × Confidence) / Effort
```

**Important caveats:**
- RICE is a tool, not a god. It's a starting point for discussion, not the final answer.
- Strategic items (SOC 2, latency) may override RICE scores. If the CEO says "SOC 2 or we die," SOC 2 goes to the top regardless of score.
- Don't RICE-score bug fixes. Bugs get triaged by severity separately (P0 = immediate, P1 = next sprint, P2 = backlog).

### Example Scoring (real items from our backlog)

| Item | Reach | Impact | Confidence | Effort | RICE Score |
|------|-------|--------|------------|--------|------------|
| Latency optimization (streaming engine) | 10 | 3 | 100% | 6 | 5.0 |
| SOC 2 compliance implementation | 10 | 3 | 100% | 10 | 3.0 |
| Salesforce native integration | 5 | 2 | 80% | 3 | 2.7 |
| Custom analytics dashboard | 5 | 2 | 80% | 4 | 2.0 |
| HIPAA BAA documentation + controls | 3 | 3 | 80% | 3 | 2.4 |
| Webhook reliability improvements | 10 | 1 | 100% | 1.5 | 6.7 |
| Multi-language voice agent support | 3 | 2 | 50% | 6 | 0.5 |
| Custom wake word support | 1 | 1 | 50% | 3 | 0.2 |
| Improved escalation handoff flow | 5 | 2 | 80% | 1.5 | 5.3 |

Note: webhook reliability scores highest on RICE but latency and SOC 2 get strategic override. This is exactly the kind of tension the framework should surface, not resolve.

---

## Step 3: Cross-Reference with Strategic Priorities

After RICE scoring, overlay the strategic lens. This is where PM judgment matters most.

### Current Strategic Priorities (Q1 2026)

1. **Enterprise readiness** — anything that unblocks the 5 pilot-to-paid conversions in OKR O1
2. **Latency** — the single most-cited competitive loss reason and OKR O2
3. **Reliability** — can't sell enterprise if we have outages during peak hours
4. **Compliance** — SOC 2 is table stakes, HIPAA opens healthcare vertical (OKR O3)

### Strategic Filter Questions
For each RICE-ranked item, ask:
- Does this directly support a current OKR? → Priority boost
- Does this address a competitive loss reason? → Priority boost
- Does this reduce churn risk for existing pilots? → Priority boost
- Is this a "nice to have" that doesn't map to any of the above? → Move to icebox unless RICE score is very high
- Is this a forward-looking bet (new market, new capability)? → Evaluate separately in quarterly planning, not sprint grooming

### Resource Reality Check
We have **12 engineers** on Voice Agents (3 ML, 5 backend, 2 frontend, 2 infra). That's roughly **24 person-weeks** per sprint (2-week sprints).

Realistically, after accounting for:
- On-call rotation (2 engineers, ~40% of their time)
- Bug fixes and operational work (~20% of team capacity)
- Meetings, reviews, overhead (~10%)

We have about **12-14 person-weeks of feature capacity per sprint**. That's maybe 2-3 medium features or 1 large + 1 small.

This means EVERY grooming session needs to be ruthless about saying no. We can't do everything. The backlog will always be 10x what we can ship.

---

## Step 4: Identify Dependencies and Blockers

Before finalizing sprint candidates, map dependencies. This has bitten us multiple times.

### Dependency Types to Check

**Technical Dependencies**
- Does this require ML model changes? → Need to coordinate with ML team's training pipeline schedule (they retrain biweekly, need 2-week notice for architecture changes)
- Does this require infrastructure changes? → Coordinate with infra team. They're shared across all Wavelength products — Voice Studio gets priority because it's highest revenue.
- Does this require API changes? → Breaking changes need 4-week deprecation notice to API consumers

**Cross-Product Dependencies**
- Does this touch shared services (auth, billing, voice engine)? → Needs sign-off from platform team
- Does this affect Open Voice compatibility? → Community impact assessment needed
- Does Soundscape legal situation affect this? → Legal team review if anything touches training data or music generation

**External Dependencies**
- Does this require third-party vendor work? (Twilio for telephony, AWS for infra, auditors for SOC 2)
- Does this need customer involvement? (pilot testing, feedback cycles)
- Are there regulatory timelines driving urgency?

### Blocker Resolution
If a high-priority item is blocked:
1. Can we unblock it this sprint? → Add the unblocking work as a sprint item
2. Can we do a partial version that's not blocked? → Scope it down
3. Is the blocker outside our control? → Escalate to leadership, move item to "blocked" column, schedule a check-in

### Current Known Blockers (as of Jan 2026)
- **SOC 2 audit**: blocked on infra team completing logging changes (estimated 2 more weeks)
- **Salesforce integration**: blocked on getting a Salesforce developer sandbox environment (procurement is slow)
- **Latency optimization**: streaming engine work is underway but competing for GPU resources with Voice Studio's model training pipeline. Need executive alignment on GPU allocation.

---

## Step 5: Create Prioritized Sprint Candidates

### Sprint Planning Template

**Sprint [N] — [Date Range]**
**Capacity: ~13 person-weeks (adjusted for on-call and overhead)**

| Priority | Item | RICE | Strategic Alignment | Effort | Owner | Notes |
|----------|------|------|---------------------|--------|-------|-------|
| P0 | [Item] | [Score] | [Which OKR/priority] | [Weeks] | [Eng] | [Any context] |
| P1 | [Item] | [Score] | [Which OKR/priority] | [Weeks] | [Eng] | |
| P2 | [Item] | [Score] | [Which OKR/priority] | [Weeks] | [Eng] | |
| Stretch | [Item] | [Score] | | [Weeks] | | Only if P0-P2 finish early |

### Rules of Thumb
- Never plan more than 80% of capacity — things always take longer and surprises happen
- Every sprint should have at least one reliability/tech-debt item — don't let operational health decay
- Customer-facing items should have a pilot customer lined up to validate before we build
- If an item has been in the backlog for 3+ sprints without getting picked up, either re-prioritize it up or kill it. Zombie backlog items are a morale killer.

### Handling Escalations Mid-Sprint
They happen. When an executive or customer escalates something mid-sprint:
1. Assess severity honestly — is this a real emergency or someone being loud?
2. If real: pull the lowest-priority sprint item to make room. Communicate the trade-off.
3. If not real: push back with data. "We can do this next sprint. Here's what we'd drop if we did it now."
4. Document the escalation either way. Patterns in escalations = planning failures we should fix.

---

## Step 6: Generate Stakeholder Summary

After each grooming session, send a summary to stakeholders. Keep it short — nobody reads long emails.

### Stakeholder Summary Template

**Subject: Voice Agents Sprint [N] Priorities — [Date]**

**What we're building this sprint:**
- [1-2 sentence summary of top 3 items and why they matter]

**What we're NOT building this sprint (and why):**
- [2-3 items that people have asked about but didn't make the cut, with brief rationale]

**Key trade-offs we made:**
- [Any decisions that stakeholders should know about — e.g., "We deprioritized Salesforce integration to focus on latency because latency is the #1 competitive loss reason"]

**What we need from you:**
- [Any asks — engineering resources from other teams, executive decisions, customer intros for validation]

**Risks:**
- [Anything that could derail the sprint — dependencies, known unknowns, team availability]

### Distribution List
- Engineering team (full detail)
- Design (relevant items)
- Sales + CS (what's coming that they can set customer expectations about)
- Leadership (summary only — they skim, make it scannable)
- Marketing (anything that's externally relevant — launches, positioning changes)

---

## Appendix: Grooming Cadence

| Activity | Frequency | Duration | Attendees |
|----------|-----------|----------|-----------|
| Input gathering | Ongoing (PM + PM intern) | N/A | PM |
| RICE scoring | Biweekly (before grooming) | 1 hour | PM + Eng Lead |
| Backlog grooming | Biweekly | 90 min | PM, Eng Lead, Design Lead, 2 senior engineers |
| Sprint planning | Biweekly (day after grooming) | 60 min | Full engineering team |
| Stakeholder summary | Biweekly (same day as planning) | 30 min to write | PM |
| Quarterly roadmap review | Quarterly | 2 hours | PM, Eng Lead, Design Lead, Head of Product, leadership |

---

## Appendix: Things I Keep Screwing Up (Notes to Self)

- Stop saying yes to "quick wins" that aren't on the roadmap. They're never quick.
- Latency improvements are hard to estimate. Always add 50% buffer to ML team estimates. They're optimistic by nature.
- Sales team will always say their deal is the most important. Ask for the ACV and close probability before reprioritizing.
- Customer feedback volume ≠ importance. One enterprise pilot customer's feedback is worth more than 50 free-tier users' feature requests. Weigh accordingly.
- Amir and the infra team are a shared resource. Book their time 2 sprints in advance or you'll get bumped by Voice Studio.
- The SOC 2 audit has been "2 weeks away" for 6 weeks. Track it daily or it'll slip again.
- Don't forget to account for holiday capacity. We lost a full sprint to December holidays and I didn't plan for it.
