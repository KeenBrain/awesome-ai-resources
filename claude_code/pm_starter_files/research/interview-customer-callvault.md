# Customer Interview: CallVault (Enterprise - Churned)
**Date:** November 15, 2025
**Interviewer:** Kai (Product Research)
**Duration:** 56 minutes
**Company:** CallVault (Customer support outsourcing, 500 agents, enterprise)
**Interviewee:** Derek Okafor, VP of Operations
**Wavelength Customer Since:** June 2025
**Products Used:** Voice Agents
**Note:** Recently churned - exit interview

---

*[Recording starts, video call, Derek in a corporate office with call center floor visible behind glass]*

**Kai:** Derek, thank you for taking this call. I know you've moved to another solution and you don't owe us this conversation.

**Derek:** I'll be direct — I'm doing this because I want you to get better. We WANTED Wavelength to work. The technology is genuinely impressive. But wanting isn't enough when you're running 500 agents handling 15,000 calls a day.

**Kai:** That's really helpful context. Can you walk me through what happened?

**Derek:** Sure. So we first heard about Wavelength Voice Agents through your sales rep, Marcus. He was enthusiastic. Showed us a demo that was honestly mind-blowing. The voice quality was leagues ahead of Amazon Connect or Google CCAI. We were sold on the vision: AI agents that sound so natural, callers wouldn't know the difference.

**Kai:** What happened after you signed?

**Derek:** We started a pilot with 50 agents — simple call routing and FAQ responses. The voice quality? Incredible. Our QA team couldn't reliably distinguish AI from human in blind tests. We were thrilled.

**Kai:** So where did it break down?

**Derek:** *[sighs]* Latency. From the first production deployment, we noticed it. There's this pause — about 800 milliseconds — between when the caller finishes speaking and when the agent responds. In a demo, you don't notice it. On a real phone call, with a real customer who's already frustrated? They notice. They start saying "hello? are you there?" It makes the interaction feel broken.

**Kai:** We're working on latency—

**Derek:** I've heard that. Marcus told us "we're optimizing, target is sub-200ms by Q1." But Q1 is three months away and I had customers complaining NOW. I can't tell my clients "the vendor says it'll be fixed next quarter." They'll fire us.

**Kai:** Fair point.

**Derek:** But latency wasn't even the breaking point. The breaking point was the refund incident.

**Kai:** Can you walk me through that?

**Derek:** So one of our clients — a retail company — uses our agents for order support. A customer called about a $400 order that arrived damaged. The AI agent was supposed to offer a replacement or store credit. Instead, it told the customer they were eligible for a full refund AND a replacement AND a $200 credit. The customer recorded the call. Shared it on Reddit.

*[Derek leans forward]*

**Derek:** The AI hallucinated a refund policy that doesn't exist. And because we're the outsourcer, WE were liable. That one call cost us $12,000 in the refund plus the replacement plus the credit that was promised. Our client nearly terminated our contract. I had to fly to their office personally to save the relationship.

**Kai:** That's... really bad.

**Derek:** It is. And when I escalated to your support team, the response was "the model occasionally generates responses outside the configured parameters." OCCASIONALLY. We handle 15,000 calls a day. "Occasionally" at that volume means multiple incidents per week.

**Kai:** What would have prevented this?

**Derek:** Guardrails. Real ones. I need to be able to set hard limits: "never offer refunds above $X," "always transfer to human for complaint calls," "never improvise on policy." Your product doesn't have those controls. The AI just... talks. And sometimes it says things it shouldn't.

*[pause]*

**Kai:** What about the interruption handling?

**Derek:** Oh, that's another thing. Real callers interrupt. They talk over the agent. They get angry and start shouting. Your voice agent just... stops. Goes silent. Then starts over from the beginning of its response. A human agent handles an angry caller — they lower their voice, they acknowledge, they de-escalate. Your agent acts like it glitched.

**Kai:** We've heard this from other customers too.

**Derek:** It's a fundamental problem. If you're building for customer support, you need to handle the hardest calls, not just the easy ones. Anyone can build an AI that answers "what are your hours?" It's the "I want to speak to a manager" calls that matter.

*[sounds of call center activity in background]*

**Kai:** When you decided to switch, what did you evaluate?

**Derek:** We looked at ElevenLabs, Amazon Connect, Resemble AI, and Google CCAI. We went with Amazon Connect. The voice quality isn't as good as Wavelength. But they have sub-200ms latency. They have guardrails and policy controls. They have SOC 2. They have SLAs with financial penalties if they miss uptime targets. They have a compliance team that responds in hours, not days.

**Kai:** So it came down to enterprise readiness, not voice quality?

**Derek:** Exactly. I said this to Marcus: "Your voice is a 10 out of 10. Your enterprise readiness is a 3 out of 10. I need at least a 7 in both." He understood. He's a good salesperson, honestly. He just doesn't have a product he can sell to enterprise customers.

**Kai:** What would bring you back?

**Derek:** If you solve latency — I'm talking sub-200ms, not sub-500ms. If you give me real guardrails for agent responses. If you get SOC 2. If you give me SLAs with teeth. If you build interruption handling that actually works. And if you can show me this is battle-tested at scale — not just working in a demo, but working at 15,000 calls a day.

**Kai:** That's a lot.

**Derek:** It is. But that's the bar for enterprise voice AI. You're competing against Amazon and Google. They set the bar. You need to meet it.

*[pause]*

**Derek:** Look, I'm rooting for you. The voice quality is genuinely special. If you can wrap enterprise-grade infrastructure around that voice technology, you'll win. But right now, you have a Ferrari engine in a go-kart frame.

**Kai:** That's a great analogy.

**Derek:** One more thing. When I asked your team for SOC 2 documentation, the response was "we're working on it." That's not an answer. "We're working on it" means "we don't have it." In enterprise procurement, that's a disqualifier. I need dates, I need auditor names, I need a timeline. "Working on it" is a startup answer. I need an enterprise answer.

**Kai:** Thank you, Derek. This is incredibly valuable feedback.

**Derek:** Happy to help. Fix these things and call me. I'll genuinely consider coming back.

*[recording ends]*

---

## Key Themes (Churn Reasons)
1. **Primary:** Latency (800ms p99 unacceptable for production calls)
2. AI hallucinated refund policy — $12K cost, nearly lost their client
3. No response guardrails or policy controls
4. Interruption handling completely broken
5. No SOC 2 — disqualifier for enterprise procurement
6. No SLAs with financial penalties
7. "Ferrari engine in a go-kart frame" — great tech, no enterprise wrapper
8. Switched to Amazon Connect despite worse voice quality

## Churn Risk Signals (Retrospective)
- Multiple support escalations about latency in first 30 days
- Requested SOC 2 docs early in pilot
- Reduced call volume in final month before churning
- VP-level escalation after refund incident
