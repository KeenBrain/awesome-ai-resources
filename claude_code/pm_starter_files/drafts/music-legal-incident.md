# Soundscape Music Copyright Incident -- Internal Working Document

> **Classification:** CONFIDENTIAL -- DO NOT SHARE EXTERNALLY
> **Author:** Jordan Machado (PM), with input from Legal, Comms, and Eng
> **Last updated:** 2025-11-12
> **Distribution:** Leadership team, Legal, Comms, Trust & Safety
>
> This is a living document. Updates are being made as the situation evolves.

---

## Incident Summary

On **October 14, 2025**, a Soundscape user generated a song using our music generation model that closely mimicked the vocal style, lyrical patterns, and production aesthetic of a major recording artist (publicly identified as **Aria Voss**, signed to Universal Music Group). The user uploaded the track to TikTok with the caption "POV: Aria Voss wrote a song about your cat" and it went viral.

**Within 72 hours, the video had 2.1 million views.** Multiple music industry news outlets picked up the story. Universal Music Group's legal team issued a cease-and-desist letter to Wavelength on **October 16, 2025** (48 hours after the TikTok post).

This document tracks the incident timeline, current status, impact on all product lines, and action items.

---

## Detailed Timeline

### Week 1: The Viral Moment (Oct 14-20)

**Monday, Oct 14 -- 3:42 PM PT**
- User @synthwave_dreams generates a 2:47 track via Soundscape music generation
- Track uses the prompt: "upbeat pop song, female vocalist, style similar to Aria Voss, about a tabby cat named Beans"
- Our model generates the track. No content filter is triggered.
- User downloads and uploads to TikTok at approximately 5:15 PM PT

**Tuesday, Oct 15 -- Morning**
- TikTok video hits 200K views overnight
- Music Twitter/X starts discussing it
- First media mention: TechCrunch newsletter "AI-generated Aria Voss song goes viral"
- **No one at Wavelength is aware yet**

**Tuesday, Oct 15 -- 11:23 AM PT**
- Amara Osei (Head of Voice AI) sees the TechCrunch mention, alerts Jordan (me) and Priya via Slack

> **Amara (Slack, #leadership, 11:23 AM):**
> "Has anyone seen this? A Soundscape user apparently generated an Aria Voss-style song and it's going viral on TikTok. 400K views and climbing. This is going to be a problem."

> **Priya (Slack, #leadership, 11:25 AM):**
> "Looking at the generation logs now. The prompt explicitly asked for 'style similar to Aria Voss.' Why didn't our content filter catch this?"

> **Jordan (Slack, #leadership, 11:31 AM):**
> "Because we don't HAVE a content filter for artist name matching in music generation. We have it for voice cloning in Open Voice but never built the equivalent for Soundscape. This is a gap I flagged in the Q2 risk review. Checking the doc now."

**Tuesday, Oct 15 -- 2:00 PM PT**
- Emergency meeting: Jordan, Priya, Amara, Diana Park (Head of Legal), Kevin Cho (Comms)
- Decision: Do NOT issue a public statement yet. Monitor the situation.
- Action: Diana to prepare response if/when label reaches out
- Action: Priya to investigate whether we can retroactively identify all "artist style" generations
- TikTok video at 600K views

**Wednesday, Oct 16 -- 9:14 AM PT**
- **Universal Music Group sends a cease-and-desist letter** via email to legal@wavelength.ai and our registered agent
- The C&D demands:
  1. Immediate removal of the content from our platform (it's not hosted on our platform -- user downloaded it)
  2. Identification of the user who generated the content
  3. Technical details of the model that generated the content
  4. Commitment to prevent future generations mimicking UMG artists
  5. Preservation of all relevant data and logs

> **Diana Park (Slack, #leadership, 9:32 AM):**
> "We have the C&D. This is real. I'm engaging outside counsel immediately. Everyone: do NOT discuss this on social media, do NOT respond to press inquiries, route everything through me."

> **Raj Mathur, CEO (Slack, #leadership, 9:45 AM):**
> "Emergency board call at 11 AM. Jordan, Priya, Diana -- I need you all on. Prepare a 5-minute summary of what happened, what we know, and what our options are."

**Wednesday, Oct 16 -- 11:00 AM PT**
- Emergency board call
- Board reactions ranged from "this was inevitable" to "how did we not have safeguards"
- Board directive: Engage top-tier IP litigation firm. Do NOT admit liability. Cooperate reasonably with UMG.
- Board asks: "Does this affect the Series B timeline?" Raj says "it shouldn't, but it might."

**Wednesday, Oct 16 -- 3:00 PM PT**
- TikTok video at 1.2M views. Second video from same user (different artist style) at 400K views.
- BuzzFeed runs: "This AI Song Sounds Exactly Like Aria Voss And The Music Industry Is Freaking Out"
- We identify the user from generation logs. Diana advises against contacting them directly at this stage.

**Thursday, Oct 17**
- TikTok video hits 1.8M views
- Wavelength receives press inquiries from: The Verge, Wired, Billboard, Music Business Worldwide
- Kevin Cho (Comms) responds to all with: "We are aware of the situation and are reviewing it. We take intellectual property rights seriously."
- Priya's team identifies **847 other music generations** in the past 90 days that reference specific artist names in prompts. 23 of these closely mimic recognizable artists based on audio similarity scoring.
- Internal debate about whether to proactively take down the 23 high-risk tracks. Diana says no -- they were downloaded by users, we don't host them. But we should preserve the generation logs.

**Friday, Oct 18**
- We engage Morrison & Foley LLP (IP litigation) as outside counsel
- First call with UMG's lawyers. Tone is "aggressive but not scorched earth." They want to establish a framework, not necessarily sue us into oblivion. (Diana's words: "they want to make an example, but they'd prefer a settlement example over a litigation example.")
- Decision: **Pause all new music generation uploads to Soundscape, effective immediately.** Existing non-music audio generation (ambient, sound effects, narration) continues.

> **Priya (Slack, #eng-all, 5:47 PM):**
> "Team -- effective immediately, we are pausing music generation in Soundscape for new submissions. This is a legal decision. If you get questions, direct them to Diana or me. I know this is frustrating. We'll share more context when we can."

**Weekend, Oct 19-20**
- TikTok video crosses 2.1M views and remains viral
- Saturday Night Live references it in Weekend Update (not by name, but "an AI company is getting sued because a robot wrote a better pop song than most humans")
- Multiple Wavelength employees post on social media expressing opinions. Diana sends an all-hands email on Sunday reminding everyone of the social media policy.

### Week 2: Containment & Legal (Oct 21-27)

**Monday, Oct 21**
- Raj holds all-hands meeting. Provides high-level update without sharing legal strategy.
- Comms fields 14 press inquiries. Continues with no-comment approach.
- Morrison & Foley sends formal response to UMG C&D: "We take the matter seriously, preserving relevant data, and wish to engage in constructive dialogue."

**Tuesday, Oct 22**
- **Critical eng decision:** Priya pulls 2 engineers from Voice Agents team (Noor Sayeed and Chris Tan) to build content moderation tooling for Soundscape. The tooling needs to:
  1. Detect artist name references in prompts (text filter)
  2. Audio fingerprinting against a database of copyrighted works
  3. Style similarity scoring to flag generations that too closely mimic known artists
- Estimated timeline for basic filters: 3-4 weeks. Audio fingerprinting: 6-8 weeks.

> **Jordan (Slack DM to Priya, Oct 22):**
> "I understand why you need Noor and Chris on this, but pulling them from Voice Agents is going to blow up our Q4 roadmap. We're already behind on the latency work. Can we hire contractors?"
>
> **Priya:** "I asked Raj. Hiring freeze until Series B closes. I'm sorry, Jordan. This is a fire we have to put out."
>
> **Jordan:** "Our whole house is on fire, Priya. We're just choosing which rooms to let burn."

**Wednesday-Friday, Oct 23-25**
- Morrison & Foley begins detailed analysis of our legal exposure
- Key legal questions identified:
  1. Does "style" constitute a protectable element under copyright law? (Answer: probably not for musical style, but voice/likeness is murkier)
  2. Are we liable as a platform or as a creator? (Section 230 implications)
  3. Does our Terms of Service adequately disclaim liability? (Diana's assessment: "it's... not great")
  4. What about the user's liability? (They explicitly prompted for "Aria Voss style")
- UMG files a DMCA takedown notice with TikTok for the specific video. TikTok removes it (but mirrors exist everywhere).

### Week 3-4: Negotiation & Impact (Oct 28 - Nov 12)

**Oct 28 -- Settlement discussions begin**
- UMG's opening position: $5M in damages + permanent injunction against artist-mimicking generation + licensing agreement for any future music generation using UMG-signed artist styles
- Morrison & Foley's assessment: "The $5M is an opener. Real exposure is probably $500K-$1.5M in a settlement. Litigation could go either way but would cost $2M+ in legal fees and take 18 months."
- Raj's position: "Settle if we can. We can't afford the distraction or the legal fees."

**Nov 1 -- Noor and Chris officially reassigned from Voice Agents**
- Voice Agents sprint velocity drops by roughly 35%
- Latency improvement work effectively paused. The streaming architecture prototype sits untouched.
- Jordan (me) has to re-plan the entire Q4/Q1 Voice Agents roadmap.

**Nov 5 -- Second round of settlement talks**
- UMG drops to $2M + content moderation requirements + public acknowledgment
- We counter at $750K + content moderation (which we're building anyway) + private acknowledgment
- Gap is narrowing but not closed

**Nov 8 -- Soundscape music generation remains paused**
- 12 Soundscape customers with active music generation workflows have filed support tickets
- 3 are threatening to churn if music generation isn't restored within 30 days
- Estimated revenue at risk: $180K ARR from music-dependent Soundscape customers
- Decision to build a "safe mode" for music generation that blocks all artist-referencing prompts and runs audio fingerprinting. Target: December 15.

**Nov 12 (today) -- Current Status**
- Settlement negotiations ongoing. Next call scheduled for Nov 18.
- Content moderation tooling in progress. Prompt-level filtering (text) is ~80% complete. Audio fingerprinting is ~20% complete.
- Music generation still paused.
- 2 Voice Agents engineers still reassigned.
- PR statement drafted but not released (see below).
- No additional legal actions from other labels (yet), but Morrison & Foley advises this is "when, not if" without content moderation in place.

---

## Impact on Voice Agents Team

This incident has directly impacted Voice Agents in the following ways:

| Impact | Details | Severity |
|--------|---------|----------|
| 2 engineers reassigned | Noor (backend) and Chris (ML) pulled to Soundscape compliance | HIGH -- 35% velocity loss |
| Latency work paused | Streaming architecture prototype untouched since Oct 22 | CRITICAL -- this is our #1 customer pain point |
| Enterprise trust concerns | 3 enterprise prospects have asked about the incident in sales calls | HIGH -- brand damage |
| Q4 roadmap blown | Guardrails engine pushed to Q1 at earliest | HIGH |
| PM bandwidth | Jordan (me) spending ~30% of time on incident response instead of Voice Agents | MEDIUM |
| Series B risk | If Series B is delayed, Voice Agents Enterprise is delayed | HIGH |

> **Marcus Webb (Slack, #sales-feedback, Nov 4):**
> "Just got off a call with a banking client. First question: 'We saw the music copyright thing. How do we know our customer voice data is safe with you?' I didn't have a good answer. This is hurting us beyond Soundscape."

---

## Risk Assessment for Other Product Lines

### Voice Studio
**Risk: LOW-MEDIUM**
- Voice Studio uses pre-built voices, not clones of real people
- However, if we fine-tune on voice data, the same "style mimicking" argument could apply
- TODO: Audit Voice Studio's training data for any celebrity/recognizable voice data

### Voice Agents
**Risk: MEDIUM**
- Voice Agents use Wavelength's default agent voices (not clones)
- Enterprise customers may want agents with specific voice characteristics ("warm, female, Southern accent") -- could this be construed as mimicking a real person?
- The bigger risk is the trust/brand damage from the Soundscape incident spilling over
- TODO: Review Voice Agents voice selection process for potential IP issues

### Open Voice (Voice Cloning)
**Risk: HIGH**
- Open Voice is literally a voice cloning product. This is the most legally exposed product line.
- We have identity verification for voice cloning (you must consent to having your voice cloned), but the Soundscape incident raises the question: what if someone clones a voice that sounds SIMILAR to a celebrity without using their actual voice data?
- The deepfake incident in September (fake CEO earnings call) is a separate but related concern
- Morrison & Foley has flagged Open Voice as "the next shoe to drop" if we don't proactively strengthen our safeguards

TODO: Comprehensive legal review of Open Voice's IP exposure
TODO: Strengthen voice cloning consent verification
TODO: Consider "voice similarity" detection -- flag clones that are too similar to known public figures

### Soundscape (Non-Music)
**Risk: LOW**
- Ambient audio, sound effects, and narration don't raise the same artist-mimicry concerns
- However, if sound effects are similar to copyrighted audio (movie sound effects, game audio), there could be exposure
- TODO: Audit sound effect generation model training data

---

## The Deepfake Connection

On **September 8, 2025**, a separate incident occurred: a user used the Wavelength API (Open Voice) to generate a fake audio recording of a CEO giving an earnings call with fabricated financial results. The audio was posted on a stock discussion forum and briefly affected the company's stock price before being identified as synthetic.

This incident was contained more quietly:
- We identified the user via API logs and terminated their account
- We cooperated with SEC inquiries (ongoing)
- We added basic "public figure" voice detection to Open Voice

But the two incidents together paint a pattern: **Wavelength's trust and safety infrastructure is not keeping up with the product's capabilities.**

Key questions this raises:
1. Do we need a dedicated Trust & Safety team? (Currently: 1 person, Lin Torres)
2. Should we implement real-time content moderation across ALL products, not just reactive filters?
3. How do we balance open/accessible AI with responsible use? This is an existential question for the company.
4. What voice cloning IP protections do we need? Voice likeness rights are an evolving legal area -- some states have specific protections, federal law is unclear.

TODO: Trust & Safety headcount proposal (Jordan to draft -- when??)
TODO: Cross-product content moderation architecture (Priya to scope -- when??)
TODO: Voice likeness rights legal memo (Diana/Morrison & Foley -- requested, pending)

---

## Draft PR Statement (NOT APPROVED -- DO NOT RELEASE)

The following statement was drafted by Kevin Cho (Comms) and reviewed by Diana Park (Legal). It has NOT been approved by Raj or the board. It is parked here for reference.

---

> **FOR IMMEDIATE RELEASE -- DRAFT v3 -- NOT APPROVED**
>
> **Wavelength's Commitment to Responsible AI Audio**
>
> Wavelength is aware of recent public discussion regarding AI-generated music content created using our Soundscape platform. We take intellectual property rights seriously and are committed to building AI tools that empower creators while respecting the rights of artists and rights holders.
>
> Upon learning of the content in question, we immediately took the following steps:
>
> - Launched an internal investigation into how the content was generated
> - Engaged constructively with the affected rights holders
> - Implemented additional content safeguards across our music generation tools
> - Temporarily paused music generation capabilities while we strengthen our moderation systems
>
> We believe AI and human creativity can coexist and complement each other. We are actively developing technology to ensure our platform cannot be used to infringe on artists' rights, including prompt-level filtering, audio fingerprinting, and style-similarity detection.
>
> We are committed to working with the music industry, rights holders, and policymakers to establish clear standards for AI-generated audio content.
>
> Media inquiries: press@wavelength.ai

---

**Diana's notes on the draft:**
- "Too apologetic. We haven't admitted fault and shouldn't."
- "Remove 'immediately' -- we didn't act immediately, there was a 24-hour gap."
- "The 'paused music generation' part -- do we want to highlight that publicly? Could be seen as admission that the feature is problematic."
- "'Working with the music industry' -- we're literally being threatened by UMG. This is aspirational at best."

**Kevin's response:**
- "We need to say SOMETHING. The silence is becoming the story."
- "Every day we don't comment, someone else frames the narrative for us."

**Raj's position (verbal, Nov 6):**
- "Nothing goes out until the settlement framework is agreed. Diana, tell me when."

---

## Legal Questions: Voice Cloning IP

The Soundscape incident has raised broader questions about voice and audio IP that affect ALL Wavelength products. Morrison & Foley is preparing a comprehensive memo, but here are the key issues as we understand them:

1. **Voice as intellectual property:** Several states (CA, NY, TN) have "right of publicity" laws that protect a person's voice. Tennessee passed the ELVIS Act in 2024 specifically targeting AI voice cloning. Are we compliant?

2. **Musical style vs. voice:** Can you copyright a "style"? Generally no -- you can't copyright a genre or a vibe. But the Aria Voss situation is murkier because the output was arguably a mimicry of a specific, identifiable artist, not just a genre.

3. **Training data liability:** What was our music generation model trained on? Do we have licenses for all training data? (Morrison & Foley's preliminary assessment: "unclear and potentially problematic." This is the scariest part.)

4. **User vs. platform liability:** If a user prompts for "Aria Voss style" and the model generates it, who is liable? Is this like YouTube (platform, DMCA safe harbor) or like a ghostwriter (direct infringement)?

5. **Voice Agents implications:** If an enterprise customer wants their AI agent to have a "warm female voice that sounds like [specific celebrity]," and our system generates something similar, is that infringement? We need guidelines ASAP.

6. **International considerations:** EU AI Act has specific provisions about AI-generated content and deepfakes. Are we compliant? NEED LEGAL REVIEW.

TODO: Get Morrison & Foley's full IP memo (expected: late November)
TODO: Audit training data licensing for ALL models (estimated effort: significant)
TODO: Develop company-wide IP and content policy

---

## Action Items

| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 | Settle with UMG | Diana Park / Morrison & Foley | Ongoing | IN PROGRESS -- next call Nov 18 |
| 2 | Build prompt-level content filtering for Soundscape | Noor Sayeed | Nov 22 | ~80% complete |
| 3 | Build audio fingerprinting system | Chris Tan | Dec 15 | ~20% complete |
| 4 | Implement style-similarity detection | Chris Tan | Jan 2026 | NOT STARTED |
| 5 | Audit music generation training data for licensing | Amara Osei / Legal | Dec 2025 | NOT STARTED -- need external audit support |
| 6 | Restore music generation in "safe mode" | Priya / Noor | Dec 15 | BLOCKED on items 2 & 3 |
| 7 | Finalize and release PR statement | Kevin Cho / Diana | TBD | BLOCKED on settlement progress |
| 8 | Develop company-wide content moderation policy | Jordan / Diana | Dec 2025 | NOT STARTED |
| 9 | Trust & Safety headcount proposal | Jordan | Nov 30 | NOT STARTED (me, writing this at midnight) |
| 10 | Legal memo on voice cloning IP | Morrison & Foley | Late Nov | IN PROGRESS |
| 11 | Audit Voice Studio training data | Amara | Jan 2026 | NOT STARTED |
| 12 | Strengthen Open Voice consent verification | Eng (TBD) | Dec 2025 | NOT STARTED |
| 13 | Return Noor and Chris to Voice Agents | Priya | ??? | NO DATE -- Priya says "when content moderation is stable." I say "when is that?" She says "I don't know." |
| 14 | Update Terms of Service re: AI-generated content | Diana / Legal | Dec 2025 | NOT STARTED |
| 15 | SEC cooperation (deepfake incident) | Diana | Ongoing | IN PROGRESS -- separate track |
| 16 | Board update on combined legal exposure | Raj / Diana | Nov 25 | SCHEDULED |

---

## Financial Impact Summary

| Category | Estimated Impact | Confidence |
|----------|-----------------|------------|
| Legal fees (Morrison & Foley) | $300-500K | Medium |
| Settlement (UMG) | $750K-2M | Low (still negotiating) |
| Lost Soundscape revenue (music pause) | $180K ARR at risk | Medium |
| Lost Voice Agents velocity (eng reassignment) | Unquantified but significant | High |
| Lost enterprise deals (trust damage) | $200-400K pipeline at risk | Low |
| Future litigation risk (other labels) | $1-5M (Morrison & Foley estimate) | Very Low |
| PR/brand repair | TBD | Unknown |
| **Total estimated exposure** | **$2.4M - $8M+** | **Very Low** |

For a company at ~$10M ARR, this is potentially existential if the worst case materializes. The board is aware.

---

## Lessons Learned (So Far)

1. **Content moderation is not optional.** We shipped music generation without artist-name filtering. This was a known risk that was deprioritized. We should have built moderation before launch, not after an incident.

2. **Trust & Safety cannot be a team of one.** Lin Torres has been incredible, but one person cannot cover four product lines. We need at least 3-4 people on this team.

3. **Legal review of new features needs to be mandatory.** Soundscape music generation launched without legal review of IP implications. This cannot happen again.

4. **Incident response needs a playbook.** We lost 24 hours because nobody realized the TikTok video was going viral until Amara happened to see a TechCrunch newsletter. We need monitoring and alerting for brand/product mentions.

5. **Product lines are interconnected.** An incident in Soundscape directly impacts Voice Agents (eng resources), Open Voice (legal exposure), and Voice Studio (brand trust). We can't manage them as independent products.

---

*This is a living document. Last updated Nov 12, 2025 by Jordan.*
*Next update expected after Nov 18 UMG settlement call.*
*If you have questions, please Slack me. But also maybe don't, because my Slack is 90% fire emojis right now.*
