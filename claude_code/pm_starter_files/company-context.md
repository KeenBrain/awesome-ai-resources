# Wavelength - Company Context

ok so if you're reading this, I'm sorry. I'm the PM who tried to own all four product lines for 18 months and finally broke. I'm writing this brain dump the weekend before my last day because I feel guilty leaving without SOMETHING for whoever comes after me. This is messy. I know. I'll try to organize it but honestly my brain is scattered and I've been averaging 4 hours of sleep for the last three months so... bear with me.

## The Basics

Wavelength - founded 2022, SF-based. Started by Aria Santos (CEO, ex-Spotify, music + tech background) and Dev Kapoor (CTO, ex-DeepMind, ML researcher). The origin story is that Aria was obsessed with the idea that everyone should be able to "give their voice to their ideas" - literally. She wanted to democratize voice. Dev had been working on voice synthesis at DeepMind and thought the tech was finally ready to go mainstream.

The tagline is "Give your ideas a voice." It's cheesy but honestly it works.

We're at ~70 people now. HQ is SF, remote folks in NYC, London, Bangalore. Product org is 8 people (you'll be the only dedicated PM for Voice Agents - congrats? sorry?). Engineering is ~30 people across 4 squads. ML/Research is 12 people (they're special - more on that). Sales is 8, Marketing is 5, Trust & Safety is 3 (should be 10), CS is 4.

Series B closed 6 months ago - $38M led by a]16z. Previous rounds: $5M seed, $12M Series A. Runway is ~18 months but the board is pushing for path to profitability. The problem is we keep expanding into new product lines instead of making the existing ones profitable. Classic Aria move - she sees opportunity everywhere and can't say no.

## What We Do

Wavelength is an AI voice and audio platform. We started as a voice cloning tool for podcasters and creators, and now we're... a lot of things. Probably too many things. Here are the four product lines:

### 1. Voice Studio (the OG)
Voice cloning, text-to-speech, voice design. This is what we built first. You upload a few minutes of audio, we clone your voice, you can use it for podcasts, audiobooks, video narration, whatever. Power users LOVE this. Creators have built entire businesses on it. Mia Chen (50K subscriber podcaster) literally runs two shows using her cloned voice because she records one and the AI generates the other.

Revenue: ~$2.8M ARR (mostly creator subscriptions)
Users: ~15K active monthly

The problem: we updated the model 3 months ago and quality degraded for some voices. We didn't tell anyone. People noticed. There was a whole Twitter thread. Aria promised to fix it in the next sprint. That was 6 sprints ago.

### 2. Soundscape (the lawsuit)
AI music generation and sound effects. Think: you describe a mood or scene, we generate original music and sound effects. Indie game devs love the sound effects. Music creators use it for backing tracks and loops.

Revenue: ~$1.2M ARR
Users: ~8K active monthly

The problem: An AI-generated song that was clearly mimicking a popular artist went viral on TikTok (2M views). Universal Music's lawyers sent a cease & desist within 48 hours. We paused new music uploads. There was a board emergency call. Legal is eating engineering resources - 2 engineers got pulled FROM Voice Agents (YOUR team) to build compliance tooling for Soundscape. I'm still mad about this.

### 3. Voice Agents (YOUR product line - the one exploding)
Conversational AI voices for customer support, sales, scheduling. Originally this was just a side feature - "hey what if people could make their cloned voice interactive?" Then enterprise customers started asking if they could use it for phone support. Then a few big ones started USING it for phone support. Then the revenue started growing 40% month-over-month.

Revenue: ~$3.5M ARR and climbing fast
Users: ~200 enterprise accounts (but only ~30 are "real" deployments, rest are trials/POCs)

The problem: EVERYTHING. We built this for podcasters making fun interactive demos, not for enterprises running production phone systems. Latency is 800ms p99 - customers notice. The voice can't handle interruptions or angry callers. We don't have SOC 2. The AI gave a customer incorrect refund information and it cost them $12K. An enterprise account (CallVault, 500 agents) churned because of this stuff. And Marcus from sales keeps promising features we don't have.

### 4. Open Voice (the community thing)
We open-sourced our base voice model and built a community hub around it. Researchers, hobbyists, startups use it. It's great for brand/reputation. The problem? Some of our competitors are literally using our open-source model as their foundation. Dev is philosophical about it ("rising tide lifts all boats") but Sales is furious.

Revenue: $0 direct (some conversion to paid products)
Users: ~50K community members, ~5K active contributors

## The Model Problem

This is the thing that nobody outside the ML team really understands but it's THE issue.

We have ONE base model that serves ALL FOUR product lines. One model, four masters.

- Voice Studio needs high quality (doesn't care about speed)
- Voice Agents needs low latency (sub-200ms target, currently at 800ms p99)
- Soundscape needs music generation (totally different architecture)
- Open Voice needs to be general purpose (can't be too specialized)

Priya on the ML team calls it "splitting the atom." Every time they optimize for one use case, another one degrades. The model update that improved Voice Agents latency by 100ms? It degraded Voice Studio quality. The one that improved music generation? It broke some cloned voices.

GPU costs are up 300% in 6 months. We're spending $180K/month on inference and it's growing. The board is asking questions.

## Team & Culture

Aria is incredibly charismatic and visionary. She's also a "yes to everything" person. I've seen her commit to features in customer meetings that would take 6 months to build. She promises things because she genuinely believes we can do them. The engineers call this "The Aria Effect" - when a customer ask turns into a sprint commitment within 24 hours.

Dev is the opposite - methodical, research-driven, wants to do things properly. He and Aria clash constantly but productively (usually). Dev would rather build one thing perfectly than four things adequately. He's been losing that argument.

There's a Slack channel called #help-im-drowning. It started as a joke. It's not a joke anymore. 200+ messages last month. People use it to vent about scope creep, resource conflicts, context switching. The ML team is the worst off - they're the bottleneck for everything and everyone is pulling them in different directions.

Two ML engineers quit last quarter. One went to ElevenLabs. Priya (Sr. ML Engineer, Voice Models team) is considering leaving because "I came here to do research, not firefight four products." If we lose Priya, we're in serious trouble.

## The Deepfake Incident

I need to tell you about this because it's still haunting us.

In September 2025, someone used Voice Studio to clone a political candidate's voice and made robocall recordings. It went viral. TechCrunch covered it. Then a Congressional staffer sent us a letter asking about our voice verification and consent policies.

Jordan Ellis (Trust & Safety Lead) nearly quit over this. Our safeguards were - and honestly still are - "duct tape." Voice verification is bypassable. We don't have a real consent framework. Enterprise customers ask "can you guarantee our voices won't be misused?" and the honest answer is no.

Jordan says we're "one incident away from regulation." Leadership treats T&S as a cost center, not a priority. Jordan has 3 people. They need 10.

## Competition

**ElevenLabs** - the big one. They have SOC 2. They have enterprise-grade latency. They have a simple pricing model. We lose deals to them constantly. Marcus lost a $400K deal because they had SOC 2 and we didn't.

**Play.ht** - strong on voice cloning, growing fast. Good developer experience.

**Resemble AI** - focus on enterprise, good on compliance. They're eating our lunch on voice agents for regulated industries.

**Amazon Polly / Google Cloud TTS** - the giants. Not as good quality but enterprise buyers trust them by default. "Nobody ever got fired for buying AWS."

**Cartesia** - newer player, incredibly fast inference. Their latency numbers are embarrassing us.

How we differentiate:
1. Quality - our voices are genuinely better (when they work)
2. Versatility - nobody else does voice + music + agents
3. Open source community - developer goodwill, model contributions
4. Creator ecosystem - loyal base of podcasters/creators

How we lose:
1. Enterprise readiness (no SOC 2, no SLAs, latency issues)
2. Focus (what are we? a creator tool? enterprise platform? research lab?)
3. Pricing (confusing, can't explain it, Marcus literally drew it on a whiteboard and confused himself)
4. Trust & safety (the deepfake thing follows us everywhere)

## Pricing Mess

Oh god, the pricing. Ok so:

- Voice Studio: per-character pricing (why??) with 3 tiers
- Soundscape: per-minute pricing for music, per-sound for effects
- Voice Agents: per-minute of conversation time
- Open Voice: free base, paid for higher rate limits and premium models

4 products x different pricing models x 3 tiers = nobody understands it. Marcus says he literally cannot explain this to customers. There was a meeting where someone asked him to draw it on a whiteboard and he confused HIMSELF.

We need to simplify. I started a doc on this (check drafts/pricing-model-analysis.md) but didn't finish.

## Company Values

**Amplify** - "Give every idea a voice. Amplify creativity."

**Resonate** - "Build things that resonate with real people, not just demos."

**Harmonize** - "Work in harmony across teams. One company, one mission."

**Innovate Responsibly** - "Push boundaries, but own the consequences."

(The music/audio metaphors are intentional. Aria loves them. Some people find them corny. They've grown on me.)

## Key Metrics We Track

- Total ARR: ~$7.5M (growing, but messy across product lines)
- Voice Agents MRR growth: 40% MoM (the exciting number everyone focuses on)
- Voice Agents churn: 8% monthly (the scary number nobody wants to talk about)
- Model inference cost: $180K/month (up 300% in 6 months)
- NPS: +38 overall (down from +51 six months ago)
- Voice Agents p99 latency: 800ms (target: sub-200ms)
- Trust & Safety incidents: 12 in last quarter (up from 3)
- ML team attrition: 2 out of 14 left last quarter

## The Inbox

When you start, you'll have:
- 47 unread Slack DMs (sorry)
- A half-finished PRD for Voice Agents Enterprise (drafts/voice-agents-prd-wip.md - I started it, it has TODOs everywhere)
- An escalation from CallVault about the $12K refund incident (they churned)
- A request from Marcus for "a simple story I can tell enterprise prospects"
- A request from Aria to "make Voice Agents enterprise-ready by Q2"
- A request from Dev to "stop adding features and fix the latency problem"
- A request from Jordan to "for the love of god, build a consent framework"
- A Slack thread at 2am from the ML team about a production model regression

## Questions I Never Got To

- How do we serve creators AND enterprise with the same product?
- Should Voice Agents be its own product or part of Voice Studio?
- What's the minimum viable enterprise offering?
- How do we get latency from 800ms to 200ms without a model rewrite?
- What do we do about the music legal situation?
- How do we build trust & safety without slowing down the product?
- Is Open Voice helping us or helping our competitors?

## I'm Sorry

I tried to own all of this for 18 months. It was too much. The VP (Ravi) kept saying "we'll hire more PMs" but it never happened until now. You're the first dedicated PM for Voice Agents, which means everything else is still kind of floating. There's another PM starting for Voice Studio next month, supposedly.

Voice Agents is the biggest revenue opportunity. It's also the biggest mess. Enterprise customers are banging down the door, but the product was built for podcasters making fun demos, not for phone systems handling 10,000 calls a day.

Good luck. I mean that sincerely.

Oh, and Priya is the most important person for you to talk to first. She knows where all the bodies are buried. Buy her coffee. She drinks oat milk lattes.

---

*Brain dump by: [redacted, they're gone now]*
*Last updated: January 2026*
*I'm sorry about the mess.*
