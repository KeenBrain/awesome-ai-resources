# Competitive Intelligence — Raw Notes
Last updated: Jan 2026
Sources: sales team calls, win/loss interviews, public info, conference notes, customer conversations

**STATUS: INTERNAL ONLY — DO NOT SHARE EXTERNALLY**

---

## ElevenLabs

### Pricing (as of Dec 2025)
- Free tier: 10K characters/month (they keep tightening this)
- Starter: $5/month — 30K chars
- Creator: $22/month — 100K chars
- Pro: $99/month — 500K chars + API access
- Scale: $330/month — 2M chars + priority support
- Enterprise: Custom pricing, heard quotes from $2K-$15K/month depending on volume
- Conversational AI (voice agents equivalent): $0.12/min — confirmed from 3 separate prospects

Source: pricing page + customer interviews

### Recent Product Launches
- **Conversational AI v2** (launched Nov 2025) — major upgrade. Now supports multi-turn conversations, custom knowledge bases, and real-time tool calling. This is their direct competitor to our Voice Agents. Multiple prospects have mentioned this in competitive evaluations.
- **Projects** — collaborative workspace for managing large voice projects. Studios and agencies love this. We don't have anything like it.
- **Voice Library marketplace** — community can share and monetize voice designs. 12K+ voices listed. Interesting community play.
- **Dubbing Studio v3** — automated video dubbing with lip sync. Taking market from traditional localization companies. Not in our product roadmap but worth watching.

### Enterprise Features (where they're ahead of us)
- SOC 2 Type II certified (got it in Aug 2025) — this is killing us in enterprise deals
- HIPAA BAA available — we keep hearing this from healthcare prospects
- SSO/SAML support — standard enterprise table stakes
- Custom data retention policies
- Dedicated infrastructure option for enterprise
- 99.95% SLA with credits — vs our "commercially reasonable efforts" lol
- Salesforce and Zendesk native integrations

Source: their enterprise page + confirmed by 4 prospects who chose them over us

### Where They're Winning Deals Against Us
From the last 8 competitive loss interviews:
1. **Compliance** (6 out of 8 mentions) — SOC 2 is the single biggest reason we lose enterprise deals
2. **Latency** (5/8) — their 220ms avg vs our 400ms+. Not even close right now
3. **Integrations** (4/8) — Salesforce, Zendesk, HubSpot out of the box
4. **Reliability** (3/8) — they publish 99.97% actual uptime vs our ~99.5%
5. **Track record** (3/8) — "they've been around longer, more references"

### Where We Win Against Them
1. **Voice quality** (7/8) — consistently rated higher in blind tests
2. **Pricing** (5/8) — 30-35% cheaper at equivalent volume
3. **Voice cloning quality** (4/8) — our 30-sec cloning vs their 5-min requirement
4. **Support responsiveness** (3/8) — our team is faster and more technical

### Intel from Q4 deals
- **Lost: NorthStar Insurance ($180K ACV)** — compliance was dealbreaker. They specifically asked for SOC 2 report in the first meeting. When we said "in progress" they scheduled a follow-up with ElevenLabs that same week. Deal closed with EL in 3 weeks. Contact: James Rivera (VP Ops) — says he'd revisit if we get SOC 2 by Q2.
- **Lost: TechServe Solutions ($72K ACV)** — latency. They did a live side-by-side demo with ElevenLabs for their board. The pause difference was obvious. "We loved the voice quality but our CEO said the delay was a non-starter." Contact: Maria Chen (Director of CX).
- **Won: BrightPath Education ($54K ACV)** — they cared most about voice quality and multilingual support for language learning. Compliance wasn't a requirement for their use case. Happy customer, great reference potential.

### Concerns
- They raised $180M Series C in Oct 2025 at a reported $3.3B valuation. War chest is massive.
- Hiring aggressively in enterprise sales — 14 enterprise AE openings on their careers page
- Rumored to be working on real-time voice agents with sub-150ms latency. If they close the voice quality gap with more compute AND have lower latency, we're in trouble.

---

## Amazon Connect

### Enterprise Positioning
- They lean HARD on the AWS ecosystem integration. If a company is already on AWS (and most enterprises are), the "just add Connect" pitch is very effective.
- Not competing on voice quality — their TTS is clearly robotic. But enterprises don't always care. They care about reliability, compliance, and integrations.
- Positioning: "enterprise-grade contact center with AI capabilities" vs our "AI-first voice agent"

### Latency Benchmarks
- From our testing (Dec 2025): ~180ms for TTS-only, ~350ms for full conversational loop
- Note: their latency is good because they're running on AWS backbone. Low network hop advantage.
- But the voice sounds like... a robot. A fast robot, but a robot.

### Integration Ecosystem
This is their real moat:
- Native AWS integrations (Lambda, S3, DynamoDB, Lex, Bedrock)
- Salesforce integration (built-in)
- ServiceNow connector
- 50+ partner integrations via AWS Marketplace
- Contact Lens for real-time analytics and sentiment
- Built-in workforce management
- Native call recording and compliance features
- PCI DSS, SOC, HIPAA, FedRAMP — they have EVERYTHING

### Where They Win
- Regulated industries (finance, healthcare, government) — compliance is just not a conversation
- Large enterprises with existing AWS infrastructure — IT team prefers "one vendor"
- Use cases where reliability > voice quality (utility companies, logistics, etc.)
- RFPs with strict compliance requirements — we literally can't bid on these right now

### Where We Win
- Any deal where voice quality matters to the buyer's brand
- Startups and mid-market who find Connect overwhelming to implement
- Use cases requiring emotional intelligence and nuanced conversation
- Buyers who've been burned by AWS lock-in and want a neutral vendor

### Notes from field
- [Nov 12] Sales engineer at PacificBank told our AE: "We wanted to use Wavelength but our CISO vetoed it. Amazon Connect was the only option that passed our security review without exceptions."
- [Dec 3] Heard from a partner that AWS is building a "premium voice" tier for Connect using a model they acquired. Could close the quality gap in 2026. Unconfirmed but credible source.
- [Dec 19] Connect pricing is confusing — per-minute for telephony + per-minute for various AI features. At scale it can be MORE expensive than us but enterprises don't comparison-shop on price when they're already in the AWS ecosystem.

---

## Play.ht

### Positioning
- Creator-first platform. Going after podcasters, YouTubers, audiobook narrators.
- Less focused on enterprise/voice agents — mostly TTS and voice cloning.
- "The friendly alternative to ElevenLabs" — that's almost literally their pitch.

### Product
- Voice quality: good, not great. Maybe 85% of our Voice Studio quality.
- Strong in long-form content generation (audiobooks, podcasts). Good editor UI.
- Recently launched "PlayDialog" — conversational voices optimized for dialogue. Actually pretty good for podcast use cases.
- API available but developer community is small compared to ours or ElevenLabs.

### Pricing
- Cheaper than ElevenLabs across the board. Most plans are 20-30% less.
- Free tier is generous — 12.5K characters.
- Pro at $39/month for 1M characters — undercutting EL's $99 plan significantly.

### Competitive Dynamics
- Not a direct threat to Voice Agents — they don't have a voice agent product
- Threat to Voice Studio for creator use cases — some customers mention them as a lower-cost alternative
- [Dec 5] One of our Voice Studio customers (YouTube creator, $2K/month account) told support they were evaluating Play.ht because of our pricing changes. Need to watch churn signal here.
- Their developer community is small but passionate. Active Discord with ~4K members.

### Assessment
Low threat to Voice Agents. Moderate threat to Voice Studio on price-sensitive creator segment. Not worth prioritizing competitively but should monitor for moves into the voice agent space.

---

## Cartesia

**EMERGING THREAT — WATCH CLOSELY**

### Background
- Founded 2023, Stanford research spinout
- Focus: ultra-low-latency neural voice synthesis
- Their "Sonic" model claims <100ms inference for TTS

### Recent Developments
- **Series A: $27M** (announced Nov 2025, led by Index Ventures)
- Launched Sonic voice agent API in beta (Dec 2025)
- Published benchmarks showing 85ms average latency for full conversational loop
- Small team (~25 people) but all senior ML researchers

### Product Assessment
[Tested their API Dec 15, 2025 — internal only]
- Latency: WOW. Measured 92ms average. This is real.
- Voice quality: noticeably behind us. Maybe 75% of our quality. Slightly metallic, less emotional range.
- Conversational ability: basic. Their knowledge grounding is primitive compared to ours. Hallucination rate in our testing was ~5%.
- Enterprise features: nonexistent. No auth, no analytics, no compliance.
- Languages: English only for now.

### Why I'm Worried
- Latency is the #1 thing killing our enterprise deals. Cartesia SOLVES this.
- Voice quality can improve with scale and data. Latency is an architectural advantage that's harder to replicate.
- With $27M and a small focused team they can iterate fast
- Their research team published a paper on "sub-50ms voice synthesis" at NeurIPS 2025. If they get there...
- Index Ventures also invested in Figma and Notion early. Smart money.

### Why I Might Be Overreacting
- Voice quality gap is significant. Enterprise buyers who've heard our voice won't settle for Cartesia's current quality.
- No enterprise features. They're 12+ months behind us on the enterprise roadmap.
- Small team means they can't do everything. Voice agents is not their only product bet.
- English-only is a big limitation for multinational enterprises.

### Key Question
Can they close the voice quality gap before we close the latency gap? That's the race.

[Jan 3] Heard from a prospect that Cartesia is doing free pilots with any enterprise willing to test. Aggressive GTM for a company their size. They're trying to build reference customers fast.

[Jan 8] Our ML team says our new streaming architecture should get us to 250ms by end of Q1. That's still 3x Cartesia's speed. But might be "good enough" for most enterprise use cases?

---

## Resemble AI

### Positioning
- "The responsible voice AI company"
- Focus on voice security, consent management, and ethical voice cloning
- Going after regulated industries and government

### Key Differentiators
- **Voice consent verification**: multi-factor — requires live voice sample + liveness check + legal consent form. Much more robust than our checkbox.
- **Audio watermarking**: inaudible watermark embedded in all generated audio. Can be detected by their API. Published a paper on the technique.
- **Voice detection API**: can identify Resemble-generated audio with 97% accuracy. Offering this as a separate product for media companies and platforms.
- **Localize**: their dubbing product. Competitive with ElevenLabs Dubbing Studio.

### Product Quality
- Voice quality: good but a tier below us and ElevenLabs. ~80% of our quality.
- Latency: ~300ms for TTS. Haven't tested their conversational product.
- The consent and watermarking features add overhead but for their target market (regulated industries, defense) it's a selling point not a bug.

### Market Position
- Smaller than us and ElevenLabs but growing in government and defense
- Won a contract with [REDACTED - US government agency] for voice authentication
- Partnered with major news organizations for deepfake detection
- Revenue estimated $8-12M ARR (unconfirmed, from industry sources)

### Competitive Dynamics
- Not a direct competitor for Voice Agents today
- Potential threat if enterprises start requiring consent verification and watermarking for voice agents (which they will, eventually)
- Their safety positioning makes us look irresponsible by comparison — multiple press articles have contrasted Wavelength's "move fast" approach with Resemble's "safety first" approach
- The deepfake concerns thread on Twitter about Voice Studio (@deepfake_watch, Dec 14) explicitly mentioned Resemble as the responsible alternative

### Assessment
Low-medium threat. Not competing on the same axis as us (quality/features vs safety/compliance). But the regulatory environment is shifting in their favor. If voice AI regulations pass (EU AI Act provisions, proposed US Voice PROTECT Act), companies with built-in safety features will have a structural advantage. We should probably talk to their team about licensing their watermarking tech.

### Notes
- [Nov 20] Their CEO did a podcast interview where he called Voice Studio "recklessly easy to misuse." Not a direct attack but the implication was clear.
- [Dec 1] Resemble partnered with a major bank for voice authentication. This is an adjacent market but could give them a beachhead into enterprise voice agents.
- [Dec 22] One of our enterprise prospects (healthcare) specifically asked if we had "Resemble-level consent verification." We didn't have a good answer.

---

## Quick Competitive Summary Table

| Dimension | Wavelength | ElevenLabs | Amazon Connect | Cartesia | Play.ht | Resemble |
|-----------|-----------|------------|----------------|----------|---------|----------|
| Voice Quality | ★★★★★ | ★★★★ | ★★½ | ★★★ | ★★★½ | ★★★½ |
| Latency | ★★½ | ★★★★ | ★★★★ | ★★★★★ | N/A | ★★★ |
| Enterprise Ready | ★★ | ★★★★ | ★★★★★ | ★ | ★★ | ★★★ |
| Safety/Consent | ★½ | ★★★ | ★★★★ | ★ | ★★ | ★★★★★ |
| Pricing | ★★★★ | ★★★ | ★★★ | ★★★★ | ★★★★★ | ★★★ |
| Developer Ecosystem | ★★★★ | ★★★★★ | ★★★ | ★★ | ★★★ | ★★½ |
| Voice Agents | ★★★½ | ★★★★ | ★★★★ | ★★ | N/A | ★★ |

---

## Open Questions / Things to Investigate
- [ ] Is ElevenLabs really working on sub-150ms? Need to verify through second source
- [ ] What's Cartesia's actual enterprise roadmap? Can someone get a demo?
- [ ] AWS "premium voice" tier for Connect — need to confirm/deny
- [ ] Resemble's watermarking tech — should we build or license?
- [ ] What's our win rate vs ElevenLabs trending? Need Q4 data from sales ops
- [ ] Play.ht churn signal — how many Voice Studio customers have we lost to them?
- [ ] Has anyone mapped the VC funding across the voice AI landscape? We should know who's well-funded vs running out of runway
