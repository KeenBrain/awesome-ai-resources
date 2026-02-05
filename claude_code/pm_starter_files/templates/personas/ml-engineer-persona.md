# Persona: Priya the ML Engineer

## Overview

**Name:** Priya Nair
**Age:** 28
**Title:** Senior ML Engineer, Voice Models Team
**Company:** Wavelength (employee #8)
**Experience:** 5 years in ML/AI, MS from Stanford, ex-research intern at DeepMind

---

## Background

Priya joined Wavelength as one of the first ML engineers. She was attracted by Dev Kapoor's vision ("democratize voice") and the chance to do cutting-edge research at a startup. She's brilliant, respected by the team, and knows more about Wavelength's model architecture than anyone.

She's also exhausted, frustrated, and considering leaving.

She came to do research. Instead, she's firefighting production issues across four product lines, optimizing for conflicting requirements, and watching her team shrink from burnout. She's the single most important retention risk at the company — if Priya leaves, institutional knowledge about the model goes with her.

---

## Goals

1. **Build world-class voice AI** - She genuinely wants to push the boundaries of what voice technology can do.

2. **Do real research** - She wants to publish papers, experiment with architectures, and solve hard problems. Not just patch production systems.

3. **Build a team she's proud of** - She's watched 2 teammates leave in 6 months. She wants to stop the bleeding and build a team that does great work.

4. **Ship things that work** - She cares deeply about quality. Shipping broken things to meet deadlines makes her physically uncomfortable.

---

## Frustrations

1. **One model, four masters** - The base model serves Voice Studio, Voice Agents, Soundscape, and Open Voice. Optimizing for one degrades another. She calls it "splitting the atom."

2. **No ML infrastructure** - No canary deployments, no automated benchmarks, no A/B testing. They push models and "cross their fingers." The September quality regression (Mia's voice clone) happened because of this.

3. **Firefighting instead of research** - She spends 70% of her time on production issues and only 30% on actual research. The ratio should be reversed.

4. **Conflicting demands** - Product says "fix latency." CEO says "don't break quality." Legal says "build watermarking." Board says "reduce costs." All at the same time.

5. **Understaffed** - 10 ML engineers (was 12, 2 quit) serving 4 product lines. Needs at least 16.

6. **GPU costs out of control** - $180K/month and growing 15% monthly. No cost attribution by product line.

---

## Day in the Life

- 8am: Check production monitoring dashboards
- 9am: ML team standup
- 10am: Debug production issue or review model metrics
- 11am: Research time (if she's lucky)
- 12pm: Lunch at desk, reading papers
- 1pm: Meeting with product team about feature requirements
- 2pm: Model optimization experiments
- 4pm: Code review for team
- 5pm: Cross-product coordination (which product gets model changes this sprint?)
- 7pm: Technically done, but often debugging issues until 9pm
- 2am: Slack alert — production model regression (once or twice a month)

---

## Technical Perspective

### On Latency
"800ms to 500ms — yes, achievable in Q1 with quantization and caching. 500ms to 300ms — maybe Q2 with architectural changes. 300ms to 200ms — needs a fundamentally different approach. 6 months minimum. When Marcus promises sub-200ms by Q1, he's making a promise we can't keep."

### On Model Architecture
"We need product-specific models. A small, fast model for Voice Agents. A quality-optimized model for Voice Studio. A music-specific architecture for Soundscape. Dev wants 'one model to rule them all' but that philosophy is killing us."

### On GPU Costs
"$180K/month and no one knows which product line is eating the budget. We need cost attribution yesterday. My guess: Voice Agents is 40%, Open Voice community is 30%, Voice Studio is 20%, Soundscape is 10%."

### On the Model Update Regression
"We rushed the deployment because Aria promised latency improvements to CallVault. Didn't run full regression tests. Broke Voice Studio quality. This is exactly what happens without proper ML infrastructure."

---

## What She Values in PMs

- **Honesty about constraints** - "Don't tell me it's a 'small ask.' Tell me the real requirements and I'll tell you the real timeline."
- **Prioritization** - "Give me ONE thing to optimize for. Not four conflicting things."
- **Technical understanding** - "You don't need to know how transformers work. But understand that latency and quality are a trade-off, not independent variables."
- **Protection** - "Push back on Aria when she promises things. Don't just pass the promise through."

---

## Quotes (from research)

> "We're splitting the atom trying to serve everyone."

> "I came here to do research, not firefight four products."

> "We push a model, cross our fingers, and wait for creators to tweet at us."

> "It's not faith we need, it's engineers and time."

> "Give me a clear mandate: optimize for X and Y, accept trade-offs on Z."

---

## Retention Risk

**Risk Level: CRITICAL**

Priya has received offers from ElevenLabs and Google DeepMind. She hasn't accepted but she's listening. Key retention factors:

- If she gets to do more research and less firefighting: stays
- If the team grows and she gets a dedicated squad: stays
- If leadership prioritizes ML infrastructure: stays
- If nothing changes in the next 3 months: likely leaves

If Priya leaves, Wavelength loses:
- The person who designed the core model architecture
- The only person who fully understands the training pipeline
- The team's emotional anchor (other engineers will follow)
- 6-12 months to replace her institutional knowledge

---

*Persona developed from: Internal interview (Nov 2025), team feedback, retention risk assessment*
*Last updated: November 2025*
