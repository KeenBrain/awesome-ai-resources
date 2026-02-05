# Workflow: Competitive Analysis

This workflow produces a structured competitive analysis for voice AI products.

## What It Does

1. **Gather** - Collect information about competitors
2. **Structure** - Organize into standard framework
3. **Analyze** - Identify patterns, strengths, weaknesses
4. **Position** - Determine our differentiation
5. **Recommend** - Actionable insights for product/marketing

---

## When to Use

- Quarterly competitive review
- Preparing for sales enablement
- Evaluating new market entrants
- Informing product strategy for Voice Agents enterprise positioning

---

## Key Competitors

| Competitor | Focus | Threat Level |
|-----------|-------|-------------|
| **ElevenLabs** | Voice cloning, TTS, enterprise voice agents | Primary |
| **Play.ht** | Voice cloning, podcast tools | Secondary |
| **Resemble AI** | Enterprise voice, compliance-focused | Secondary |
| **Amazon Polly / Connect** | Enterprise TTS, contact center AI | Incumbent |
| **Google Cloud TTS / CCAI** | Enterprise TTS, contact center AI | Incumbent |
| **Cartesia** | Ultra-low latency voice generation | Emerging |

---

## Step 1: Gather Competitor Information

For each competitor, collect:
- Product features and pricing
- Target customers and use cases
- Recent announcements or changes
- Customer reviews and feedback
- Marketing messaging and positioning
- Enterprise readiness (SOC 2, SLAs, compliance)
- Latency benchmarks
- Voice quality comparisons

Sources to check:
- Competitor websites and docs
- G2/Capterra reviews
- Product Hunt
- Twitter/LinkedIn
- Industry publications (TechCrunch, VentureBeat)
- Sales team win/loss notes (ask Marcus)
- Hacker News threads
- AI voice comparison blogs/videos

Save raw information in `competitive-raw/[competitor-name].md`.

## Step 2: Structure the Analysis

For each competitor, create a profile using this template:

```markdown
## [Competitor Name]

### Overview
- Founded: [Year]
- Funding: [Amount/Stage]
- Company size: [Employees]
- Target market: [Description]

### Product
- Core features: [List]
- Key differentiators: [List]
- Weaknesses: [List]
- Recent changes: [List]

### Voice Quality
- Naturalness rating: [1-10]
- Latency: [ms]
- Language support: [Count]
- Emotion/tone controls: [Yes/No]

### Enterprise Readiness
- SOC 2: [Yes/No/In Progress]
- SLAs: [Yes/No]
- Data residency: [Options]
- Compliance: [List]

### Pricing
- Model: [Per-seat, per-minute, per-character, etc.]
- Price points: [Tiers]
- Comparison to us: [Higher/lower/similar]

### Positioning
- Tagline: [Quote]
- Main message: [Summary]
- Target persona: [Description]

### Customer Sentiment
- Strengths (from reviews): [List]
- Complaints (from reviews): [List]
- NPS or rating: [If available]
```

Save as `competitive-profiles/[competitor-name].md`.

## Step 3: Create Comparison Matrix

Build a feature comparison table focused on Voice Agents competition:

| Feature | Wavelength | ElevenLabs | Resemble | Amazon Connect | Google CCAI | Cartesia |
|---------|-----------|-----------|----------|---------------|------------|---------|
| Voice Quality | | | | | | |
| Latency (p99) | | | | | | |
| SOC 2 | | | | | | |
| SLAs | | | | | | |
| Interruption Handling | | | | | | |
| Guardrails | | | | | | |
| Pricing Clarity | | | | | | |
| Enterprise Support | | | | | | |

Use: Strong / Adequate / Weak / None

Save as `competitive-comparison-matrix.md`.

## Step 4: Identify Patterns

Analyze across competitors:
- Where are we ahead? Behind?
- What features are table stakes vs. differentiators?
- What are competitors investing in? (signals from recent launches)
- Where is the voice AI market going?
- What gaps exist that no one addresses?

Save as `competitive-patterns.md`.

## Step 5: Define Our Positioning

Based on analysis, articulate:
- Our primary differentiation (voice quality is our moat)
- Our secondary differentiators
- Where we compete head-to-head
- Where we don't compete (and shouldn't)
- How we should position against each competitor
- The "Wavelength vs. X" story for each major competitor

Save as `competitive-positioning.md`.

## Step 6: Generate Deliverables

Create audience-specific outputs:

**For Sales:** Battle cards with talk tracks
- How to position against each competitor
- Key objection handlers
- When we win and when we lose
- Enterprise-specific positioning

**For Product:** Strategic recommendations
- Features to build/improve for competitive advantage
- Enterprise readiness gaps to close
- Areas to double down on

**For Marketing:** Messaging guidance
- Differentiation claims we can make
- Proof points to highlight
- Messaging to avoid

Save as:
- `deliverables/sales-battlecards.md`
- `deliverables/product-recommendations.md`
- `deliverables/marketing-messaging.md`

---

## Example Usage

```
Using the workflow in @workflows/competitive-analysis.md:
- Analyze our top 3 competitors: ElevenLabs, Amazon Connect, Resemble AI
- Focus on Voice Agents enterprise positioning
- Create sales battlecards and product recommendations
```

---

## Tips

- Refresh quarterly at minimum - voice AI competitive landscape changes fast
- Include qualitative (reviews, sentiment) not just features
- Talk to Marcus - he hears competitive intel in every sales call
- Be honest about where we're behind (especially enterprise readiness)
- Voice quality is our moat — make sure the analysis reflects that

---

*Workflow version 1.1 - Updated December 2025*
