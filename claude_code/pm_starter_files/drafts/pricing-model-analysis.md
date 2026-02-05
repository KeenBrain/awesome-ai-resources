# Wavelength Pricing Model Analysis

> **Status:** Working draft -- not ready for leadership review
> **Author:** Jordan Machado
> **Last updated:** 2025-11-10
> **Context:** Marcus has been escalating pricing confusion as the #1 sales blocker for 3 months. Raj finally agreed we need a proposal. This is my attempt to untangle the mess.

---

## The Problem

We have four products with four completely different pricing models. Nobody -- not customers, not sales, not even product -- can explain why. The answer is "they were each built by different teams at different times and nobody ever unified them," but that's not a good answer when a CFO asks you on a sales call.

> **Marcus Webb, Senior AE (Slack, #sales-feedback, Oct 22):**
> "I literally drew our pricing on a whiteboard during the TeleCorp call. Four columns, different units, different tiers. The CFO stared at it for thirty seconds and said 'this looks like four different companies.' I tried to explain the logic and I confused MYSELF halfway through. I had to say 'let me get back to you with a simplified proposal' and by the time I did, they'd signed with ElevenLabs. $400K deal. Gone. Because of a whiteboard."

---

## Current Pricing Structure

### Voice Studio (Text-to-Speech)

| Tier | Price | Included | Overage |
|------|-------|----------|---------|
| Free | $0 | 10,000 characters/month | N/A (hard cap) |
| Creator | $22/month | 100,000 characters/month | $0.000018/char |
| Pro | $99/month | 500,000 characters/month | $0.000015/char |
| Enterprise | Custom | Custom volume | Negotiated |

**Unit:** Characters of input text
**Billing logic:** Character count of text sent to TTS API. Includes spaces and punctuation. SSML tags are NOT counted (this was a contentious decision -- some competitors count them).

### Soundscape (Audio/Music Generation)

| Tier | Price | Included | Overage |
|------|-------|----------|---------|
| Free | $0 | 5 minutes of audio/month, 10 sound effects | N/A |
| Creator | $29/month | 60 minutes of audio, 100 sound effects | $0.08/min + $0.25/sound |
| Pro | $79/month | 300 minutes, 500 sound effects | $0.06/min + $0.20/sound |
| Enterprise | Custom | Custom | Negotiated |

**Unit:** Minutes of generated audio output + individual sound effect count
**Billing logic:** Duration of output audio (rounded up to nearest second, then aggregated monthly to minutes) PLUS count of individual sound effects generated. Music generation and ambient audio counted separately from sound effects.

NOTES TO SELF: The sound effect pricing is the weirdest one. What even counts as a "sound effect" vs. "audio"? A 3-second whoosh is a sound effect at $0.25, but a 3-second ambient rain clip is audio at $0.004 (3 sec = 0.05 min * $0.08). This makes no sense.

**UPDATE (Nov 8):** Music generation via Soundscape is currently PAUSED for new uploads due to the Universal Music legal situation. Existing customers can still generate non-music audio. This affects pricing projections.

### Voice Agents (Conversational AI)

| Tier | Price | Included | Overage |
|------|-------|----------|---------|
| Starter | $0.15/min | Pay-as-you-go | N/A |
| Growth | $500/month | 5,000 minutes/month | $0.12/min |
| Business | $2,000/month | 25,000 minutes/month | $0.10/min |
| Enterprise | Custom | Custom volume + SLA | Negotiated |

**Unit:** Minutes of conversation (both caller and agent speech, including silence/hold)
**Billing logic:** Wall-clock time from call connect to call end. Includes hold time, silence, transfers. This is a KNOWN pain point -- customers feel they're paying for silence.

TODO: Should we switch to "active speech minutes" only? What's the revenue impact?

### Open Voice (Voice Cloning API)

| Tier | Price | Included | Overage |
|------|-------|----------|---------|
| Free | $0 | 10,000 characters/month, 3 voice clones | N/A |
| Developer | $5/month | 100,000 characters/month, 10 clones | $0.00002/char |
| Pro | $49/month | 1,000,000 characters/month, 50 clones | $0.000015/char |
| Enterprise | Custom | Unlimited clones, custom volume | Negotiated |

**Unit:** Characters (like Voice Studio) + number of voice clones
**Billing logic:** Same character counting as Voice Studio, plus a cap on number of unique voice clones. Clones are persistent and count against your limit whether active or archived.

---

## The Confusion Matrix

Here's why customers (and Marcus) lose their minds:

| What the Customer Wants | Products Involved | Pricing Units | Customer Reaction |
|------------------------|-------------------|---------------|-------------------|
| "AI voice agent for support" | Voice Agents + Open Voice (for custom voice) | Minutes + Characters + Clone count | "Why am I paying in three different units?" |
| "Generate a branded voice for our app" | Voice Studio + Open Voice | Characters + Characters (but different rates!) + Clones | "Why are characters different prices in two products?" |
| "AI podcast with sound effects" | Voice Studio + Soundscape | Characters + Minutes + Sound effects | "This is three billing dimensions for one podcast" |
| "Enterprise voice platform" | All four | Characters + Minutes + Sound effects + Clones + Conversation minutes | "Are you serious?" |

### Character Pricing Inconsistency

This is the most indefensible problem:

| Product | Character Price (Pro tier) |
|---------|--------------------------|
| Voice Studio | $0.000015/char |
| Open Voice | $0.000015/char |

OK, these are the same. Good. But:

- Voice Studio counts characters of input text
- Open Voice counts characters of input text
- They use the SAME underlying TTS model
- They appear on SEPARATE line items on invoices
- You CANNOT use your Voice Studio character allocation for Open Voice or vice versa
- If a customer wants Voice Studio quality with an Open Voice clone, they pay both

{{QUESTION: Why don't we just merge Voice Studio and Open Voice billing? Is there a technical reason or is this just historical accident? I think it's the latter but need to confirm with eng.}}

### Minutes Pricing Inconsistency

| Product | "Minute" Means |
|---------|---------------|
| Soundscape | Minutes of generated audio output |
| Voice Agents | Minutes of wall-clock conversation time |

A customer asked: "If my agent talks for 3 minutes in a 10-minute call, am I billed for 3 minutes or 10?" Answer: 10. They were not happy.

---

## Customer Complaints (Verbatim)

**Enterprise Prospect, TeleCorp (via Marcus, Oct 2025):**
"We want to use Wavelength for our entire voice stack. Contact center agents, IVR prompts, hold music, customer notifications. Your sales rep quoted us four separate products with four separate billing models. Our procurement team rejected it -- they said they've never seen a vendor this fragmented."

**Existing Customer, PodFlow (Support Ticket #4891, Sep 2025):**
"We're using Voice Studio and Soundscape together for podcast production. Our invoice has characters, minutes, AND sound effects as separate line items. My finance team asked me to explain it and I couldn't. Can you just give us one number?"

**Churned Customer, CallVault (Exit Survey, Sep 2025):**
"Pricing wasn't the main reason we left (latency was), but it didn't help. We were paying per-minute for Voice Agents and per-character for the custom voice we used with it. Two invoices for what felt like one product."

**Internal, Marcus Webb (Sales All-Hands, Oct 2025):**
"I spend more time on pricing calls than product demos. That's backwards. Every enterprise deal requires a custom quote because our standard pricing is too confusing to put in a proposal. I've started just making up bundles on the fly and hoping finance doesn't yell at me."

---

## Competitive Pricing Comparison

| Vendor | Model | Simplicity Score (1-5) |
|--------|-------|----------------------|
| **ElevenLabs** | 3 tiers (Free/Starter/Pro/Scale/Enterprise), character-based across all products | 4/5 |
| **Play.ht** | 2 tiers (Pro/Enterprise), word-based pricing | 4/5 |
| **Amazon Polly** | Pure pay-as-you-go, per character, separate rate for neural vs standard | 3/5 |
| **Bland AI** | Per-minute for phone agents, simple and transparent | 5/5 (one product though) |
| **Retell AI** | Per-minute for calls + platform fee | 4/5 |
| **Wavelength (us)** | 4 products x 4 tiers x 3+ billing dimensions | 1/5 |

### ElevenLabs Detail

| Tier | Price | Included |
|------|-------|----------|
| Free | $0 | 10,000 chars/month |
| Starter | $5/month | 30,000 chars/month |
| Creator | $22/month | 100,000 chars/month |
| Pro | $99/month | 500,000 chars/month |
| Scale | $330/month | 2,000,000 chars/month |
| Enterprise | Custom | Custom |

Everything is characters. TTS, voice cloning, dubbing, agents -- all one pool. Customers understand it instantly.

NEED DATA: What are ElevenLabs' actual enterprise contract sizes? I've heard $200K-$500K ARR for large accounts. If true, their simplified pricing isn't hurting their ACV.

### Bland AI Detail

| Model | Price |
|-------|-------|
| Per minute | $0.07/min (inbound) or $0.09/min (outbound) |
| Enterprise | Custom |

That's it. Two numbers. Their pitch is literally "7 cents a minute." Our Voice Agents pitch requires a spreadsheet.

---

## Proposal: Unified Tier Structure

### Option A: Product-Specific Tiers (Minimal Change)

Keep separate products but align the tier names and simplify units within each product.

**Effort:** Low
**Impact:** Low -- doesn't solve the cross-product confusion
**My take:** Band-aid. Don't bother.

### Option B: Unified Platform Tiers (Recommended)

Collapse all products into three platform tiers with usage pools.

| Tier | Monthly Price | Voice Studio | Soundscape | Voice Agents | Open Voice |
|------|--------------|-------------|------------|--------------|------------|
| **Creator** | $49/month | 200K chars | 30 min audio | 100 min conversations | 5 clones |
| **Pro** | $199/month | 1M chars | 120 min audio | 500 min conversations | 25 clones |
| **Enterprise** | Custom (annual) | Custom | Custom | Custom + SLA | Unlimited clones |

**Single overage rate:** Normalize everything to a "credit" system.
- 1 credit = 1,000 characters = 1 minute of audio = 1 minute of conversation = 1 voice clone
- Overage: $0.02/credit (Creator), $0.015/credit (Pro)

TODO: The credit conversion ratios above are MADE UP. I need cost data from eng to set real ratios based on actual compute cost per unit.

NEED DATA: What is our actual cost per:
- 1,000 characters of TTS inference?
- 1 minute of Soundscape audio generation?
- 1 minute of Voice Agents conversation?
- 1 voice clone creation + storage?

Without this, the credit system is a guess.

### Option C: Usage-Based Only (No Tiers)

Pure pay-as-you-go with volume discounts. Like AWS.

**Effort:** Medium
**Impact:** Medium -- simple but unpredictable revenue; enterprises hate unpredictable bills
**My take:** Works for developer/SMB. Bad for enterprise. Enterprise wants predictable annual commitments.

---

## Revenue Impact Analysis

### Current Revenue Breakdown (Q3 2025, approximate)

| Product | ARR (approx) | % of Total | Avg Deal Size |
|---------|-------------|-----------|---------------|
| Voice Studio | $4.2M | 42% | $1,800/year (long tail of small customers) |
| Soundscape | $1.8M | 18% | $2,400/year |
| Voice Agents | $2.5M | 25% | $18,000/year (fewer, larger customers) |
| Open Voice | $1.5M | 15% | $3,600/year |
| **Total** | **$10.0M** | **100%** | |

NEED DATA: These numbers are from memory and the Q3 board deck. Need exact figures from Finance. Also need:
- Revenue by tier within each product
- Customer count by tier
- Average overage revenue per customer (this is important -- if overage is a significant revenue source, the credit system needs careful calibration)
- Churn rate by product and tier

### Projected Impact of Option B

**Optimistic scenario:**
- 15% of customers upgrade to higher tiers due to cross-product bundling
- 10% reduction in churn due to pricing simplicity
- 20% improvement in enterprise win rate (Marcus's estimate, probably generous)
- Net ARR impact: +$1.5-2M over 12 months

**Pessimistic scenario:**
- Some customers on cheap single-product tiers see price increases and churn
- Credit conversion ratios accidentally undercharge high-cost products (Soundscape, Voice Agents)
- Migration confusion causes temporary support surge
- Net ARR impact: -$500K to flat over 12 months, recovering in year 2

TODO: Build a proper financial model. I started a spreadsheet but it needs real data.
TODO: Identify customers who would see a price increase under Option B -- we need a migration strategy for them
TODO: Talk to Marcus about which enterprise prospects would close faster with simplified pricing
TODO: What does our billing system (Stripe + internal tooling) actually support? Can we do credits?

NEED DATA: Current billing infrastructure capabilities. I heard from eng that our Stripe integration is "held together with duct tape." If we can't technically implement credits, this whole proposal is moot.

---

## Voice Agents Enterprise Pricing (Specific)

Separate from the platform-wide pricing simplification, we need an enterprise pricing model for Voice Agents specifically. This is more urgent because we're losing deals NOW.

### Proposal: Voice Agents Enterprise Tier

| Component | Pricing |
|-----------|---------|
| Platform fee | $2,500/month (includes dedicated infrastructure, SLA, support) |
| Usage | $0.08/min of active speech (NOT wall-clock) |
| Voice clones | Included (unlimited) |
| Minimum commit | $50,000/year |
| Contract | Annual |

TODO: Validate this with Marcus. Is $50K/year minimum too high? Too low?
TODO: What SLA can we actually promise? 99.9%? 99.95%? Need Priya's input on infrastructure reliability.
TODO: "Active speech" billing requires new instrumentation. Can eng build this?

{{QUESTION: Should enterprise customers get access to ALL Wavelength products under their enterprise contract? This simplifies the story but potentially cannibalizes Voice Studio and Soundscape revenue. Or is that fine because enterprise contracts would be higher ACV anyway?}}

---

## Risks of Doing Nothing

1. **Continued deal losses** -- Marcus estimates $1.2M in pipeline lost to pricing confusion in last 2 quarters
2. **Increasing CAC** -- every deal requires custom quoting, extending sales cycles by 2-3 weeks
3. **Churn** -- customers who use multiple products are our stickiest... unless the billing drives them away
4. **Competitive disadvantage** -- every competitor has simpler pricing. This is now a differentiator (for them).
5. **Internal confusion** -- even our own finance team struggles to forecast revenue across 4 models

---

## Next Steps

1. [ ] Get accurate revenue data from Finance (Owner: Jordan -- requested Nov 5, no response yet)
2. [ ] Validate compute costs per unit with Eng (Owner: Jordan/Priya -- she's busy with Soundscape legal)
3. [ ] Build financial model for Option B (Owner: Jordan -- TODO)
4. [ ] Review with Marcus and 2-3 AEs for sales feedback (Owner: Jordan -- TODO)
5. [ ] Legal review of contract implications for existing customers (Owner: Legal -- LOL they are swamped)
6. [ ] Billing infrastructure assessment (Owner: Eng -- TODO: who owns billing?)
7. [ ] Present to Raj and leadership (Owner: Jordan -- TARGET: Dec 2025, probably slipping)

---

## Appendix: Raw Notes

**From sales all-hands (Oct 15):**
- Marcus presented "top 5 reasons we lose deals" -- pricing was #2 (after latency)
- AE team unanimously said pricing needs simplification
- Raj said "interesting, let's look at it in Q1" -- Marcus pushed back and said Q1 is too late
- Compromise: Jordan (me) to have a proposal by end of November
- It's November 10 and this document is the proposal. It's not ready. I know.

**From customer advisory board (Oct 8):**
- 4 of 6 CAB members mentioned pricing complexity unprompted
- One CAB member (enterprise) said "just give me one number and I'll pay it"
- Another said "I'd pay 20% more for a single, simple bill"

**From Stripe dashboard (quick analysis):**
- 23% of enterprise invoices require manual adjustment
- Average time to resolve billing disputes: 11 days
- 3 customers currently in billing disputes totaling $47K

---

*This document is incomplete. I know. I'm one PM across four product lines and this is the third-most-urgent thing on my plate (after Voice Agents latency and the Soundscape legal crisis). If leadership wants this done faster, I need help. Or fewer product lines. Preferably both.*

*-- Jordan, Nov 10, 2:14 AM*
