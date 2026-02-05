# Support Ticket Analysis Summary
**Period:** October - November 2025
**Total Tickets:** 683
**Analyzed by:** Customer Success Team

---

## Overview

This document summarizes themes from support tickets over the past two months across all Wavelength product lines. Categories are sorted by volume.

---

## Category 1: Latency / Performance (22% of tickets)

**Voice Agents Latency** (94 tickets)
- Enterprise customers reporting 600-900ms response delays
- Callers hanging up thinking the call dropped
- Latency spikes during peak hours (10am-2pm PT)
- Some customers experiencing intermittent 2-3 second delays

Sample tickets:
> "Our customers are noticing a delay after they finish speaking. They keep saying 'hello?' It's making the AI agent seem broken."

> "Latency was 400ms during the POC. Now that we're in production with 200 concurrent calls, it's 800ms+. Did something change?"

**Voice Studio Generation Speed** (32 tickets)
- Long-form voice generation taking 2-3x longer than 3 months ago
- API timeouts on clips longer than 5 minutes
- Batch generation jobs failing silently

**Soundscape Generation** (24 tickets)
- Music generation paused — customers asking when it returns
- Sound effect generation slower since model update

**Recommendation:** Voice Agents latency is a critical enterprise retention risk. Three enterprise accounts have explicitly threatened to leave over latency.

---

## Category 2: Billing / Pricing Confusion (18% of tickets)

**"What am I paying for?"** (62 tickets)
- Customers on multiple products can't understand combined billing
- Per-character vs per-minute vs per-sound pricing confusion
- Overage charges unexpected and poorly explained

Sample tickets:
> "I'm being charged $47 for Voice Studio and $23 for Soundscape and $89 for Voice Agents and I have no idea how those numbers are calculated."

> "What's a 'character'? Is it a letter? A word? A sentence? Your pricing says per-character but that could mean anything."

**Enterprise Pricing Negotiations** (28 tickets)
- Enterprise buyers requesting annual contracts (we offer month-to-month)
- Custom pricing requests with no clear process
- Volume discounts not published or standardized

**Unexpected Charges** (33 tickets)
- API usage spikes causing bill shock
- No usage alerts or caps
- Test/development usage being billed at production rates

**Recommendation:** Pricing confusion is generating more tickets than actual product bugs. Simplification would reduce CS load significantly.

---

## Category 3: Voice Quality Issues (15% of tickets)

**Voice Clone Degradation** (48 tickets)
- Creators reporting voice clones sound different after September model update
- Specific complaints: changed cadence, added breathiness, slight accent shifts
- Multiple creators asking "did you change something?"

Sample tickets:
> "My voice clone has been perfect for a year. Last month something changed. It sounds like a slightly different person now. My listeners are noticing."

> "I've been using my clone for an audiobook series. 8 chapters sounded perfect. Chapter 9 sounds different. I can't publish this with an inconsistent voice."

**Voice Agent Quality** (31 tickets)
- Voice agents sounding "robotic" in certain phrases
- Mispronunciation of company names and industry terms
- Inconsistent tone across different call types

**Uncanny Valley Feedback** (23 tickets)
- "Almost human but not quite" complaints
- Requests for more natural breathing, pauses, filler words
- Game developers requesting stylized (non-realistic) voice options

**Recommendation:** The September model update caused real damage to creator trust. Need a rollback option or model version pinning for Voice Studio customers.

---

## Category 4: API Errors / Technical Issues (14% of tickets)

**Voice Agents API** (42 tickets)
- WebSocket disconnects during calls
- Inconsistent response formatting
- Rate limiting errors without clear documentation

**Voice Studio API** (28 tickets)
- Timeouts on long-form generation
- Webhook delivery failures
- Authentication token expiration issues

**Soundscape API** (26 tickets)
- Music generation endpoints returning errors (due to pause)
- Sound effect generation returning incorrect formats
- Batch processing failures

**Recommendation:** API reliability is critical for developer/enterprise trust. Need better error messages, status page, and incident communication.

---

## Category 5: Ethical Concerns / Abuse Reports (12% of tickets)

**Unauthorized Voice Cloning Reports** (31 tickets)
- Individuals reporting their voice was cloned without consent
- Businesses reporting competitor using their spokesperson's cloned voice
- Takedown requests with no clear process

Sample tickets:
> "Someone cloned my wife's voice using a podcast episode and is using it for a scam. How do I get it removed? There's no report button."

> "A competitor is using our CEO's cloned voice in sales calls. This is fraud. We need this removed immediately and we need to know how it happened."

**Deepfake Concerns** (29 tickets)
- Customers asking about safeguards after TechCrunch article
- Enterprise asking for "guarantee our voices won't be misused"
- Creators worried about their own voices being cloned by others

**Content Policy Questions** (22 tickets)
- "Can I use generated audio for political content?"
- "Is Soundscape-generated music safe to use commercially?"
- "What happens to my voice data if I cancel?"

**Recommendation:** Urgent need for: (1) abuse reporting mechanism, (2) voice takedown process, (3) clear content policy documentation, (4) consent framework.

---

## Category 6: "How Do I..." / Onboarding (10% of tickets)

**Voice Studio Onboarding** (32 tickets)
- "How do I get the best voice clone?"
- "What audio quality do I need?"
- "How do I use the API?"

**Voice Agents Setup** (21 tickets)
- Enterprise onboarding is complex — no self-serve option
- "How do I configure the agent's personality?"
- "How do I set up call routing?"

**Soundscape** (15 tickets)
- "When will music generation come back?"
- "Can I use generated sound effects commercially?"

**Recommendation:** Onboarding documentation gaps are driving support volume. Interactive tutorials and better docs would reduce tickets significantly.

---

## Category 7: Soundscape Legal Questions (9% of tickets)

**Music Legal** (38 tickets)
- "Is the music I already generated safe to use?"
- "Will I get a DMCA takedown for content I've published?"
- "When is music generation coming back?"
- "Is sound effect generation also affected?"

**Commercial Use Concerns** (24 tickets)
- Game developers, video creators, podcasters asking about commercial rights
- No clear terms of service for generated content ownership
- Requests for indemnification clauses

**Recommendation:** The silence on the legal situation is generating tickets and eroding trust. A public FAQ would resolve 80% of these tickets.

---

## Trends & Alerts

### Getting Worse
- Voice Agents latency complaints (up 45% from previous period)
- Ethical concerns / abuse reports (up 60%)
- Billing confusion (up 25%)
- Voice quality complaints (up 200% — driven by model update)

### Getting Better
- Onboarding questions (down 15% — new docs helping)
- Voice Studio API errors (down 10% — stability improvements working)

### Red Flags
- 3 enterprise Voice Agents accounts explicitly threatened to leave over latency
- 2 takedown requests involved potential legal action
- 1 churned enterprise account cited "AI hallucination causing financial harm"
- Music legal questions are increasing, not decreasing — silence is not working

---

## Top 5 Most Urgent Issues (from this period)

1. Voice Agents latency (94 mentions) — enterprise retention risk
2. Billing confusion (62 mentions) — reducing sales velocity
3. Voice clone quality degradation (48 mentions) — creator trust erosion
4. API reliability (42 mentions) — developer/enterprise churn risk
5. Unauthorized cloning / abuse (31 mentions) — existential risk

---

*Report compiled by: Customer Success Team*
*Next update: End of December 2025*
