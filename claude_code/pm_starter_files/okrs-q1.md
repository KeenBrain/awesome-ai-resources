# Q1 2026 OKRs - Company

## Company-Wide Theme: "Focus the Signal"

After the Series B, we're in a classic "too many bets, not enough wins" situation. Four product lines, one model team, and a music legal crisis eating resources. This quarter is about focus: double down on Voice Agents (our biggest revenue opportunity), resolve the Soundscape legal situation, simplify our pricing, and get costs under control.

Aria's words at the all-hands: "We've been saying yes to everything. This quarter, we say yes to four things and no to everything else."

(Whether she actually follows through on that is TBD. We've heard this before.)

---

## Objective 1: Make Voice Agents Enterprise-Ready

**Why this matters:** Voice Agents is growing 40% MoM but enterprise churn is 8% monthly. We're acquiring fast and losing fast. The growth is masking a retention problem. Enterprise customers want SLAs, SOC 2, low latency, and reliability - we have none of these. If we don't fix this, we'll burn through every enterprise prospect in our TAM within a year.

**Owner:** You (Senior PM, Voice Agents)

### Key Results:

**KR1:** Reduce Voice Agents p99 latency from 800ms to 300ms
- Current: 800ms p99 (enterprise customers need sub-200ms, 300ms is table stakes)
- Target: 300ms by end of Q1
- Owner: ML Team + Voice Agents Eng Squad
- Note: Priya says 300ms is achievable with model optimization. Sub-200ms requires architectural changes (Q2).

**KR2:** Complete SOC 2 Type II audit readiness
- Current: No formal compliance program
- Target: Auditor engaged, policies documented, controls implemented
- Owner: Engineering + Legal
- Note: We've been "working on it" for 6 months. This time we mean it. (Allegedly.)

**KR3:** Improve Voice Agents monthly retention from 92% to 96%
- Current: 8% monthly churn (enterprise accounts)
- Target: 4% monthly churn
- Owner: Product + Customer Success

**KR4:** Ship 3 enterprise table-stakes features
- Voice isolation per customer (data separation)
- Real-time conversation monitoring dashboard
- SLA reporting and uptime guarantees
- Owner: Voice Agents Eng Squad

### Initiatives:
- [ ] Enterprise security audit and gap analysis
- [ ] Voice agent interruption handling (the "angry caller" problem)
- [ ] Latency optimization sprint with ML team
- [ ] Enterprise onboarding playbook with CS
- [ ] Customer voice consent framework (work with T&S)

---

## Objective 2: Resolve Soundscape Legal Situation

**Why this matters:** Universal Music's C&D is a existential risk. If this escalates to litigation, it could affect ALL product lines (voice cloning has similar IP questions). Also: 2 engineers are pulled from Voice Agents to work on compliance tooling. We need those engineers back.

**Owner:** Legal + CEO

### Key Results:

**KR1:** Reach settlement or licensing agreement with Universal Music
- Current: Negotiating, Soundscape music generation paused
- Target: Signed agreement by end of Q1
- Owner: Legal + Aria

**KR2:** Implement content provenance system for all generated audio
- Current: No watermarking or provenance tracking
- Target: All generated audio includes metadata provenance
- Owner: ML Team + Platform Eng

**KR3:** Return borrowed engineers to Voice Agents team
- Current: 2 engineers on compliance tooling
- Target: Back on Voice Agents by Week 6
- Owner: CTO

### Initiatives:
- [ ] Content ID / watermarking for generated music
- [ ] Artist style detection and blocking
- [ ] Legal review of voice cloning IP implications
- [ ] Public statement on responsible AI audio generation
- [ ] Licensing framework for training data

---

## Objective 3: Simplify Pricing

**Why this matters:** Marcus (Sales) literally cannot explain our pricing to customers. 4 products x different pricing models x 3 tiers = confusion. We're losing deals because buyers can't figure out what they're paying for. One enterprise buyer asked "so are you a podcasting tool or an enterprise tool?" and Marcus didn't have a good answer.

**Owner:** Product + Finance + Sales

### Key Results:

**KR1:** Launch unified pricing page with 3 clear tiers
- Current: 4 separate pricing models, each with 3 tiers
- Target: Creator / Pro / Enterprise - simple, clear, done
- Owner: Product + Marketing

**KR2:** Reduce sales cycle length from 68 days to 45 days
- Current: 68 day average for enterprise deals
- Target: 45 days
- Owner: Sales + Product

**KR3:** Increase pricing page → trial conversion from 4% to 8%
- Current: 4% of pricing page visitors start a trial
- Target: 8%
- Owner: Growth + Marketing

### Initiatives:
- [ ] Pricing simplification proposal (analysis in drafts/)
- [ ] Customer research on willingness to pay
- [ ] Competitive pricing analysis
- [ ] Sales enablement materials for new pricing
- [ ] Migration plan for existing customers

---

## Objective 4: Reduce Model Inference Costs by 40%

**Why this matters:** We're spending $180K/month on GPU inference and it's growing 15% monthly. At this rate, we'll be spending $300K/month by Q3. The board is asking hard questions about unit economics. We need to serve more requests with less compute.

**Owner:** CTO + ML Team

### Key Results:

**KR1:** Reduce per-request inference cost by 40%
- Current: ~$0.004 per voice generation request
- Target: ~$0.0024 per request
- Owner: ML Team

**KR2:** Implement request-level cost tracking
- Current: We know total GPU spend but not cost per product line
- Target: Cost attribution by product line, customer, and request type
- Owner: Platform Eng

**KR3:** Reduce model size by 30% without quality degradation
- Current: 13B parameter model serving all products
- Target: Specialized models or distillation to reduce size
- Owner: ML Research

### Initiatives:
- [ ] Model distillation research (smaller models for specific use cases)
- [ ] Caching layer for repeated voice generations
- [ ] Spot instance optimization
- [ ] Product-specific model variants (quality vs speed tradeoff)
- [ ] Usage-based cost controls for Open Voice community

---

## Dependencies & Risks

### Dependencies:
- **ML team capacity:** EVERYTHING depends on the ML team. They're a bottleneck for Obj 1, 2, and 4. We cannot overcommit them.
- **Legal resolution:** Obj 2 affects Obj 1 (engineer allocation) and Obj 3 (positioning)
- **SOC 2 auditor:** Need to engage an auditor by Week 2 or we slip
- **Design capacity:** Enterprise features need UX work, design team is at 120% utilization

### Risks:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Music legal escalates to litigation | Medium | Critical | Prioritize settlement, prepare PR response |
| Another deepfake incident | High | Critical | Accelerate T&S investment, consent framework |
| ML team attrition (Priya leaves) | Medium | Critical | Retention package, reduce firefighting load |
| Latency target not achievable | Medium | High | Phased approach: 500ms first, then 300ms |
| Enterprise deals stall without SOC 2 | High | High | Interim security documentation, auditor letter of intent |

---

## What We're NOT Doing in Q1

Saying no is harder than saying yes. But:

- **New product lines** - We have four. That's enough. (Aria, please.)
- **Open Voice major investment** - Maintenance mode. Community contributions only.
- **Mobile app** - We don't have one and we're not building one
- **New integrations** - Focus on making existing ones reliable
- **International expansion** - English-first for now
- **Voice Studio major features** - Creator features are important but Voice Agents is the priority

---

## Tracking & Cadence

- **Weekly:** OKR check-ins in Monday all-hands
- **Bi-weekly:** Voice Agents sprint reviews (open to all)
- **Monthly:** Full product review with leadership + board metrics
- **Quarterly:** Retrospective and Q2 planning

---

*Approved by: Aria Santos (CEO), Dev Kapoor (CTO), Ravi Mehta (VP Product)*
*Last updated: January 2026*
