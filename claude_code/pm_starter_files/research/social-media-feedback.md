# Social Media Mentions — Wavelength
Collected Nov-Dec 2025. Raw captures, not cleaned up.

---

## Twitter/X

### Thread 1 — @sarahk_ai (AI Product Consultant, 24.3K followers)
**Nov 8, 2025**

> Just spent a week evaluating every major voice AI platform for a client's contact center migration. Thread on what I found 🧵

> 1/ **Wavelength Voice Agents** — the voice quality is genuinely the best I've heard. In blind tests, 4 out of 5 listeners couldn't distinguish it from a human agent. That's insane.

> 2/ BUT. The latency. Oh god the latency. We're measuring 450-520ms average response time. In a real phone conversation that creates this uncanny pause that makes people think the line dropped. ElevenLabs is at ~220ms for comparison.

> 3/ Enterprise readiness is also a gap. No SOC 2, no HIPAA BAA, SLA is "commercially reasonable efforts" which is lawyer speak for "lol good luck." My client is in healthcare. This was a non-starter.

> 4/ That said — their trajectory is steep. They shipped 3 latency improvements in October alone. If they hit 250ms by Q1 2026 and get SOC 2 done, they could leapfrog ElevenLabs in enterprise. The voice quality moat is real.

> 5/ For now we went with Amazon Connect + custom voice overlay. Boring but compliant. Will revisit Wavelength in 6 months.

**142 retweets, 891 likes**

Replies worth noting:
- @wavelength_ai: "Thanks for the detailed feedback Sarah. Latency improvements are our #1 priority this quarter. DM us if your client wants to try the beta of our new streaming engine."
- @random_dev_42: "lmao 'commercially reasonable efforts' I'm dead. every startup does this"
- @voiceai_nerd: "ElevenLabs latency numbers are misleading. That's TTS only, not full conversation loop. Apples to oranges."

---

### Thread 2 — @marcus_sound (Music Producer, 8.7K followers)
**Nov 19, 2025**

> ok I need to talk about @wavelength_ai Soundscape because nobody is saying the quiet part loud enough

> I generated a jazz quartet piece in Soundscape yesterday. It was beautiful. Like genuinely beautiful. And then I ran it through audio fingerprinting software and it matched fragments from 3 different Blue Note recordings from the 60s.

> This isn't "inspired by." This is memorization. The model is regurgitating copyrighted material with enough variation to pass a casual listen but not enough to survive legal scrutiny.

> I WANT to use this tool. The interface is incredible, the iteration speed is unmatched. But I can't risk my career on music that might be stolen. @wavelength_ai needs to address this directly. Not with PR speak. With actual data about their training set.

**287 retweets, 1,204 likes**

Replies:
- @music_copyright_law: "This is exactly the kind of evidence that will matter in the pending litigation. DM me."
- @wavelength_ai: [no reply as of capture date]
- @indie_producer_j: "Same experience. Generated a 'lo-fi hip hop' track and my roommate immediately said 'that's a Nujabes beat'"

---

### Thread 3 — @priya_builds (Startup CTO, 15.1K followers)
**Dec 3, 2025**

> Shipped our customer support AI using @wavelength_ai Voice Agents last week. Sharing real numbers from our first 7 days:

> - 2,847 calls handled autonomously
> - 73% resolution without human escalation
> - Average handle time: 3.2 min (down from 8.7 min with human agents)
> - CSAT: 3.4/5 (our human agents average 3.8)
> - Cost per call: $0.42 (down from $4.80)

> The cost reduction alone pays for itself 10x. Voice quality is magic. Customers genuinely don't know they're talking to AI until we disclose at the end (which we always do, legally required in our state).

> Pain points: the escalation handoff is rough. When the AI can't handle something it just says "let me transfer you" and there's a 4-5 second dead silence before a human picks up. We've lost calls in that gap. Also the analytics are bare bones — had to build our own dashboard.

> Overall: 8/10 for a Series A startup. Would NOT recommend yet for regulated industries or anyone needing >99.9% uptime. But for our scale? Chef's kiss.

**198 retweets, 1,456 likes**

---

### Thread 4 — @deepfake_watch (AI Safety Researcher, 41K followers)
**Dec 14, 2025**

> We need to talk about Wavelength Voice Studio and the deepfake problem.

> Voice Studio can clone anyone's voice from a 30-second sample. THIRTY SECONDS. I just cloned a US senator's voice using a clip from a public hearing. Took me 2 minutes total.

> Yes they have consent verification. It's a checkbox. "I confirm I have the right to clone this voice." That's it. No identity verification, no watermarking on output, no detection API.

> Compare to Resemble AI which requires multi-factor voice consent, embeds inaudible watermarks, and provides a detection API. Wavelength is prioritizing ease of use over safety and it's going to blow up in their face.

> This isn't hypothetical. There are already Wavelength-cloned voices being used in scam calls. I've documented 3 cases in the past month. Thread with evidence below.

**892 retweets, 3,241 likes**

Replies:
- @wavelength_ai: "Voice safety is a top priority. We're rolling out enhanced consent verification in January and our watermarking system is in beta. We'd welcome a conversation about our safety roadmap — DM open."
- @ai_ethics_prof: "The 'consent checkbox' approach is fundamentally broken. It assumes good faith actors which is exactly who you DON'T need to worry about."
- @random_user: "tbf every voice cloning tool has this problem, not just wavelength"

---

## Reddit

### r/voiceai — "Wavelength Voice Agents vs ElevenLabs for enterprise — real comparison"
**u/contact_center_pm** — Nov 22, 2025 — 347 upvotes

> I'm a PM at a mid-market insurance company and we just finished a 4-week bake-off between Wavelength Voice Agents and ElevenLabs Conversational AI for our claims hotline. Sharing the raw data because I couldn't find a good comparison anywhere.
>
> **Voice Quality (subjective, panel of 20 listeners)**
> - Wavelength: 4.6/5 naturalness, 4.4/5 emotional range
> - ElevenLabs: 4.1/5 naturalness, 3.8/5 emotional range
> - Winner: Wavelength, clearly
>
> **Latency (avg over 10K calls)**
> - Wavelength: 467ms avg, 1.8s p99
> - ElevenLabs: 231ms avg, 890ms p99
> - Winner: ElevenLabs, not close
>
> **Hallucination Rate**
> - Wavelength: 2.8% (agent made up policy details, gave wrong claim numbers)
> - ElevenLabs: 1.9% (similar issues but less frequent)
> - Winner: ElevenLabs, though both are concerning
>
> **Enterprise Features**
> - Wavelength: No SOC 2, no HIPAA BAA, basic analytics, decent API
> - ElevenLabs: SOC 2 Type II, HIPAA BAA available, Salesforce integration, robust analytics
> - Winner: ElevenLabs by a mile
>
> **Pricing (for our volume ~50K calls/month)**
> - Wavelength: $0.08/min ($14K/month estimated)
> - ElevenLabs: $0.12/min ($21K/month estimated)
> - Winner: Wavelength
>
> **Our decision:** ElevenLabs. The voice quality difference doesn't matter if customers are hanging up because of latency pauses. And our compliance team wouldn't sign off without SOC 2.
>
> **My honest take:** Wavelength has the better core technology. If they fix latency and ship compliance certs, they win this market. But right now they're bringing a Formula 1 car to a road rally — fast in theory, can't handle the terrain.

Top comments:
- "This is the best comparison I've seen. We had almost identical results at our bank." (+89)
- "Wavelength team if you're reading this — latency latency latency. Everything else is fixable but if you lose the enterprise deals NOW those contracts are locked for 2-3 years." (+156)
- "Have you looked at Cartesia? Their new Sonic model does voice agents at like 130ms. Still early but worth watching." (+67)

---

### r/startups — "We replaced 80% of our support team with AI voice agents. Here's what happened."
**u/founder_throwaway_99** — Dec 8, 2025 — 1,203 upvotes

> Throwaway because this will piss people off.
>
> We're a 40-person B2B SaaS company. Support team was 8 people handling ~200 calls/day. We implemented Wavelength Voice Agents 6 weeks ago and are now handling 160 of those 200 calls with AI.
>
> We laid off 5 support reps. Kept 3 for escalations and QA.
>
> **Numbers:**
> - Cost per call: $4.20 → $0.55
> - Average handle time: 7.1 min → 3.8 min
> - First-call resolution: 64% → 71%
> - CSAT: 3.9 → 3.6 (slight dip)
>
> The CSAT dip is real but manageable. Most complaints are about "the voice sounds too perfect" or latency-related pauses. A few customers called us directly to complain about "talking to a robot" even though they rated the actual resolution positively.
>
> ROI paid back the integration cost in 3 weeks.
>
> I feel terrible about the layoffs. These were good people. But the math was impossible to argue with. Our board would have replaced ME if I hadn't made this call.
>
> AMA I guess.

Top comments:
- "The fact that you feel terrible about it doesn't make it better for the 5 people who lost their jobs. But I appreciate the honesty." (+445)
- "Which voice AI did you evaluate besides Wavelength?" — "ElevenLabs and Amazon Connect. ElevenLabs was close but more expensive. Connect was too robotic." (+89)
- "What's your plan when Wavelength has an outage during peak hours? 3 people can't handle 200 calls." — OP: "That happened week 2 actually. 22-minute outage. It was chaos. We now have an overflow contract with a BPO. Insurance policy basically." (+201)
- "I'm one of the people companies like yours are replacing. Just want to say this sucks." (+1,847)

---

### r/voiceai — "Open Voice fine-tuning results — beating commercial APIs on our domain"
**u/ml_engineer_voice** — Dec 21, 2025 — 512 upvotes

> Spent the last 3 weeks fine-tuning Wavelength's Open Voice model on our medical terminology dataset (~40 hours of doctor-patient conversations, fully consented and anonymized).
>
> Results compared to commercial APIs for medical voice agent use case:
> - Open Voice (fine-tuned): 4.7/5 naturalness, 96% medical term accuracy
> - Wavelength Voice Agents API: 4.8/5 naturalness, 89% medical term accuracy
> - ElevenLabs: 4.2/5 naturalness, 84% medical term accuracy
>
> The fine-tuned open model BEATS the commercial APIs on domain-specific accuracy. And we're running it on our own HIPAA-compliant infrastructure so no BAA needed from Wavelength.
>
> Inference latency on 2x A100s: 95ms average. That's faster than any commercial API because we're not going through their network.
>
> Open Voice is the real deal. Wavelength is playing 4D chess — they'll make their money on Voice Studio and Voice Agents while the open model builds a moat of community adoption.

---

## LinkedIn

### Post 1 — Jennifer Walsh, VP of Customer Experience at MedLine Health Systems
**Nov 28, 2025**

> Excited to share results from our Wavelength Voice Agents pilot for patient appointment scheduling!
>
> After 30 days:
> ✅ 12,400 appointments scheduled autonomously
> ✅ Patient satisfaction up 18% vs our old IVR system
> ✅ Average call time down from 6.2 minutes to 2.8 minutes
> ✅ After-hours coverage that we simply couldn't staff before
>
> The voice quality is what sets Wavelength apart. Patients have told us the AI agent is "the friendliest receptionist we've ever had." One patient sent a thank-you card. TO THE AI.
>
> Huge thanks to the Wavelength team, especially @David_Chen_wavelength for the white-glove onboarding. Looking forward to expanding this across our 14 clinic locations in Q1.
>
> #VoiceAI #HealthcareInnovation #PatientExperience

482 likes, 67 comments

Notable comment from @Rajesh_Patel_CTO: "Jennifer, what was your experience with latency? We evaluated them for our urgent care line but the response delay was a dealbreaker." Jennifer's reply: "Latency was our biggest concern too. We worked with their team to optimize for our specific flows and got it to ~380ms which is acceptable for scheduling (not for urgent clinical calls though — I'd agree it's not there yet)."

---

### Post 2 — Tom Bradley, Director of Operations at RetailMax
**Dec 18, 2025**

> I don't usually post negative reviews on LinkedIn but I think other enterprise buyers need to hear this.
>
> We signed a $48K annual contract with Wavelength for Voice Agents to power our customer returns hotline. After 3 months, we're terminating.
>
> What went wrong:
>
> 1. **Latency promises not met.** We were told to expect "sub-300ms by November." In December we're still seeing 400ms+. Customers complained constantly about the pause.
>
> 2. **Two significant outages** in 8 weeks, including one during Black Friday weekend. No SLA credits offered.
>
> 3. **Hallucination problems.** The agent told a customer they could return an item after 90 days. Our policy is 30 days. This happened at least 4 more times after we "fixed" the guardrails.
>
> 4. **Account management disappeared.** Great during the sale, invisible after. Took 3 days to get a response to a P1 ticket during the Black Friday outage.
>
> The voice quality IS remarkable. I'll give them that. But a beautiful voice that gives wrong information and goes down during your busiest day is worse than a robotic voice that's reliable.
>
> Going back to our previous solution (Twilio + Dialogflow) until the space matures. $48K lesson learned.
>
> Happy to connect with anyone doing due diligence on voice AI platforms.
>
> #EnterpriseAI #VoiceAI #LessonsLearned

1,247 likes, 203 comments

Notable comments:
- Wavelength CEO @Sarah_Wavelength: "Tom, I'm sorry about your experience. This isn't the standard we hold ourselves to. I've asked our Head of Customer Success to reach out directly. Your feedback on latency, reliability, and support is being heard and acted on."
- @VP_at_BigCo: "We had a similar experience with the hallucination issue. Guardrails aren't robust enough for regulated use cases."
- @Random_Sales_Guy: "This is why we went with ElevenLabs. Enterprise features matter more than voice quality when you're running a real business."

---

## Hacker News

### "Show HN: Wavelength Open Voice — Apache 2.0 voice synthesis model"
**Nov 15, 2025 — 847 points, 312 comments**

**Selected comments (highest-voted first):**

---

**jsmith_ml** (428 points)
> This is genuinely impressive. I've been in speech synthesis research for 12 years and Open Voice's quality-to-size ratio is the best I've seen in an open model. The architecture paper is solid too — the modified flow-matching approach for prosody is novel and well-executed.
>
> Running inference benchmarks now. Initial results on my 3090: 110ms for a 5-second clip. That's very workable.
>
> Wavelength is making a bet that the ecosystem play is worth more than keeping this proprietary. Time will tell if that's right but as a researcher I'm thrilled.

---

**skeptical_dev** (267 points)
> Genuinely curious about the business model here. They release their core voice tech as open source while selling... voice products? This is either brilliant or suicidal.
>
> The quality gap between Open Voice and their commercial Voice Studio is real but not insurmountable. Community fine-tuning will close it within 6 months. Then what?

> > **wavelength_cto** (198 points)
> > Fair question. A few things: (1) Open Voice is our base model — Voice Studio, Voice Agents, and Soundscape all use significantly enhanced versions with proprietary improvements in voice cloning, real-time conversation, and music generation respectively. (2) We believe the managed service + enterprise features + support are worth paying for even if the base model is free. See: Red Hat, Databricks, etc. (3) Community contributions to Open Voice actually improve our commercial products too. It's a positive-sum game.

---

**privacy_hawk** (234 points)
> Am I the only one concerned about releasing a high-quality voice cloning model as open source? Yes it requires consent verification in their commercial product but the open model has no such guardrails. Anyone can clone anyone's voice with this.
>
> The deepfake implications are terrifying. We're going to see this used for election interference, fraud, and harassment within months.

> > **counter_point_ai** (189 points)
> > This argument has been made about every open-source AI release since GPT-2. The cat is already out of the bag — there are multiple open voice models available. Wavelength releasing a better one doesn't meaningfully change the risk landscape. What it DOES do is enable legitimate researchers and developers to build responsible applications.

> > > **privacy_hawk** (112 points)
> > > "The cat is already out of the bag" is a thought-terminating cliché. Each improvement in quality and accessibility raises the risk. A model that requires 30 seconds of audio vs 5 minutes meaningfully lowers the barrier.

---

**indie_hacker_23** (156 points)
> Just integrated Open Voice into my side project (AI language tutor). Replaced ElevenLabs API and my costs went from $340/month to $12/month (GPU time on RunPod). Quality is 90% as good for my use case. This is going to destroy the pricing of every voice API company.

---

**enterprise_buyer_hn** (134 points)
> We evaluated Wavelength's commercial Voice Agents product for our contact center. Voice quality was best-in-class but they lost the deal on enterprise readiness (no SOC 2, latency issues, reliability concerns).
>
> Interesting that they're investing in open source while their enterprise product has these gaps. Feels like a prioritization question — should they be polishing the product that makes money or building community goodwill?

> > **startup_pm_here** (98 points)
> > Both. Open Voice builds developer adoption and brand awareness which feeds the commercial pipeline. Enterprise features are table stakes they need to ship regardless. Different teams, different timelines. The real question is whether they can execute on both simultaneously with what I assume is a 50-100 person eng team.

---

**voice_researcher** (112 points)
> The technical report is worth reading in detail. Key innovations:
> - Modified flow-matching for prosody control (Section 3.2) — this is why the emotional range is better than other open models
> - Efficient attention mechanism that cuts inference time ~40% vs naive transformer approach
> - Training data: they claim 680K hours of "ethically sourced, consented audio" but provide no audit or verification of this claim
>
> That last point matters. Their commercial Soundscape product is currently being sued for training on copyrighted music. How confident can we be that Open Voice's training data is clean?

---

**just_a_user** (87 points)
> Not to be dramatic but this might be the most important open source release of 2025. Voice is the last frontier of human-AI interaction that felt obviously artificial. A high-quality open model changes the game for accessibility, education, and human-computer interaction broadly.
>
> Also the contributor guide is excellent. Already submitted a PR for Japanese language improvements.
