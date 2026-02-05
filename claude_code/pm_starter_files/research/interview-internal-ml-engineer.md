# Internal Interview: ML Engineer
**Date:** November 5, 2025
**Interviewer:** Kai (Product Research)
**Duration:** 62 minutes
**Name:** Priya Nair
**Role:** Senior ML Engineer, Voice Models Team
**Tenure:** 2 years (employee #8)

---

*[Recording starts, in-office meeting room, Priya has a laptop open with monitoring dashboards]*

**Kai:** Priya, thanks for making time. I know you're slammed.

**Priya:** *[dry laugh]* That's one word for it. I'm glad someone is finally asking the ML team what's actually happening. Product asks us "can you make it faster?" and we say "it's complicated" and they hear "yes but later." So. Let me explain what's actually happening.

**Kai:** Please. Start from wherever you want.

**Priya:** Okay. The fundamental problem. We have ONE base model. One. It serves Voice Studio, Voice Agents, Soundscape, and Open Voice. Four product lines with completely different requirements, running on the same model.

**Kai:** Walk me through the differences.

**Priya:** Voice Studio needs maximum quality. Podcasters, creators — they need voices that are indistinguishable from human. They don't care if generation takes 3 seconds because they're pre-generating audio, not doing it in real-time. So: optimize for quality, latency doesn't matter.

Voice Agents needs the opposite. Enterprise phone calls need responses in under 200 milliseconds. The voice can be slightly lower quality — nobody expects a customer service call to sound like a podcast. So: optimize for speed, quality can trade off.

Soundscape needs MUSIC generation, which is architecturally completely different from speech. We hacked music generation onto a speech model and it works but it's... not great. It's like using a hammer to drive screws. It works but you know it's wrong.

Open Voice needs to be general-purpose because the community uses it for everything. We can't optimize for any specific use case without hurting others.

**Kai:** So what happens when you optimize for one?

**Priya:** Three months ago, we did a model update to improve Voice Agents latency. We shaved 100ms off response time. Great. But the optimization changed the voice quality characteristics for Voice Studio. Mia Chen — that podcaster with 50K subscribers — her cloned voice changed. Subtle but noticeable. She tweeted about it. Other creators noticed too. We degraded one product to improve another.

**Kai:** Can't you run separate models?

**Priya:** That's what I've been advocating for. Product-specific models. A speed-optimized model for Voice Agents. A quality-optimized model for Voice Studio. A music-specific architecture for Soundscape. But that means training and maintaining multiple models, which means more compute, more engineers, more GPU cost.

**Kai:** How much more?

**Priya:** Rough estimate: 60-80% increase in GPU costs. We're already at $180K/month. Dev nearly fell out of his chair when I presented that number to him.

*[Priya pulls up a graph on her laptop]*

**Priya:** Look at this. GPU costs over the last 6 months. Up 300%. And it's not because we're doing more — it's because every product line keeps adding load. Voice Agents is growing 40% month-over-month. Every new enterprise customer is more inference load. Open Voice community usage is up 200% because we got featured in a Hacker News thread.

**Kai:** Is cost the main reason you can't split models?

**Priya:** Cost and people. I have 12 people on the ML team. Two quit last quarter. Raj went to ElevenLabs — they offered him 40% more and a pure research role. Chen went to a PhD program because she said "I came here to do research, not be on-call for production systems." We're down to 10 and we're stretched across four products.

**Kai:** What's morale like?

**Priya:** *[long pause]* Honestly? Bad. My team is exhausted. We're splitting the atom trying to serve everyone. Every sprint, we get pulled in four directions. Product says "fix latency." Aria says "don't break voice quality." Legal says "build content watermarking for Soundscape." The board says "reduce GPU costs." These are all real priorities and they all conflict.

*[Priya closes the laptop]*

**Priya:** Last month, an engineer on my team was debugging a production issue at 2am. She posted in #help-im-drowning asking if anyone knew why the model was generating garbled audio for some voice clones. Nobody answered because everyone was asleep. She fixed it herself at 3am. The next morning in standup, nobody mentioned it. That's the culture right now. Heroics are expected. Burnout is normalized.

**Kai:** Are you worried about more attrition?

**Priya:** I'm worried about MY attrition. I'll be honest with you because this is a research interview and you need to hear it. I came here because Dev's vision was inspiring — "democratize voice with world-class ML." But I'm not doing research anymore. I'm firefighting. I'm patching production systems. I'm optimizing latency for enterprise deals that Sales promised without asking us. I'm being asked to do the work of 20 people with 10.

**Kai:** That's tough. What would change things for you?

**Priya:** Focus. Pick TWO product lines and do them well. Not four. Give me a clear mandate: "optimize the model for X and Y, we accept trade-offs on Z." Right now everything is priority one and nothing gets done well.

Second: hire. I need at least 4 more ML engineers. Not junior ones — senior people who can own subsystems. The kinds of people who cost $400K/year. Leadership balks at the salary but they're losing $400K deals because we can't hit enterprise latency targets.

Third: let me build proper infrastructure. We need a model serving platform, not the duct tape we have now. We need canary deployments so we don't break voice clones when we update models. We need cost attribution so we know which product line is eating GPU budget. None of this is sexy but without it, we can't scale.

**Kai:** Let me ask about the latency target specifically. 800ms to 200ms. Is that achievable?

**Priya:** *[thinks carefully]* 800ms to 500ms? Yes, in Q1. We can do model quantization, KV caching improvements, and speculative decoding. That gets us there.

500ms to 300ms? Maybe in Q2 with a dedicated latency squad and some architectural changes.

300ms to 200ms? That requires a fundamentally different approach. Streaming token generation, edge deployment, maybe a specialized small model just for Voice Agents. That's a 6-month project minimum.

When Marcus tells customers "sub-200ms by Q1," he's making a promise we literally cannot keep with the laws of physics and our current architecture.

**Kai:** Does Marcus know this?

**Priya:** I've told him. I've told Ravi. I've told Aria. They hear "it's hard" and translate it to "it's hard but Priya will figure it out." They have infinite faith in the ML team. I appreciate the confidence but it's not faith we need, it's engineers and time.

*[pause]*

**Kai:** What's your honest take on the model update that affected Voice Studio quality?

**Priya:** It was a mistake. We should have run a more extensive evaluation before deploying. But we were under pressure to show latency improvements because Aria promised Derek at CallVault that we'd hit 500ms by October. We rushed the deployment, didn't run full regression tests on Voice Studio outputs, and broke things.

This is exactly the kind of thing that happens when you don't have proper ML infrastructure. Canary deployments, A/B testing, automated quality benchmarks — we don't have any of this. We push a model, cross our fingers, and wait for creators to tweet at us.

**Kai:** If you could change one thing, what would it be?

**Priya:** Give Voice Agents its own model. Let me build a small, fast, specialized model for conversational voice. It doesn't need to be the same quality as Voice Studio. It needs to be FAST and RELIABLE and have guardrails. That's a 3-month project. It would solve the latency problem, stop us from breaking Voice Studio when we optimize for speed, and reduce GPU costs because a smaller model is cheaper to run.

**Kai:** Why hasn't that happened?

**Priya:** Because Dev wants one unified model. It's his research philosophy — one model to rule them all. He thinks splitting models is "giving up on the vision." But the vision is killing us.

**Kai:** Thank you, Priya. This is incredibly important.

**Priya:** I hope someone listens this time. And buy me a coffee — oat milk latte.

*[recording ends]*

---

## Key Themes
1. ONE model serves FOUR products with conflicting requirements
2. Optimizing for one product degrades another (zero-sum)
3. GPU costs up 300% in 6 months ($180K/month)
4. ML team lost 2/12 people — burned out, underpaid vs. competition
5. Latency roadmap: 500ms achievable Q1, 300ms maybe Q2, 200ms is 6+ months
6. No proper ML infrastructure (canary deploys, A/B tests, automated benchmarks)
7. CTO's "one model" philosophy is causing architectural problems
8. Priya is considering leaving — biggest retention risk
9. Need product-specific models but cost would increase 60-80%
10. Team morale is critically low — burnout is normalized
