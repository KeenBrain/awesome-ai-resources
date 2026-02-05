# Workflow: Research to PRD

This workflow takes raw research (interviews, surveys, feedback) and produces a complete PRD.

## What It Does

1. **Analyze** - Read research files, extract themes and insights
2. **Synthesize** - Create a research summary document
3. **Frame** - Define the problem statement and opportunity
4. **Prioritize** - Score against criteria, recommend approach
5. **Draft** - Create PRD using company template
6. **Humanize** - Apply writing guidelines, remove jargon
7. **Review** - Generate checklist for stakeholder review

---

## When to Use

- Starting a new feature from research
- Converting customer feedback into product requirements
- Synthesizing multiple data sources into an actionable spec

---

## Step 1: Analyze Research

Read all files in `@research/` and identify:
- Top pain points mentioned by multiple sources
- Frequency of each pain point (how many sources mention it?)
- User quotes that illustrate the problem
- Any solutions customers suggested

Save as `research-analysis.md`.

## Step 2: Synthesize Findings

Based on `@research-analysis.md`, create a synthesis that includes:
- Top 3-5 problem themes with supporting evidence
- User segments affected by each problem (creator, enterprise, game-dev, community)
- Business impact (revenue, churn, NPS implications)
- Quotes from users (verbatim, with source)

Save as `research-synthesis.md`.

## Step 3: Frame the Problem

From `@research-synthesis.md`, draft:
- A clear problem statement (1-2 sentences)
- The target user/persona
- The current state (how users deal with this today)
- The desired future state
- Why solving this matters now

Save as `problem-framing.md`.

## Step 4: Generate Solution Options

Based on `@problem-framing.md`, brainstorm:
- 3 different approaches to solving the problem
- Pros and cons of each approach
- Effort estimate (T-shirt size)
- Recommendation with rationale

Save as `solution-options.md`.

## Step 5: Draft PRD

Using `@templates/prd-template.md` as the structure and all previous documents as input, draft a complete PRD:
- Fill in all required sections
- Include research citations
- Reference the recommended solution from Step 4
- Add placeholders for sections that need more input (design, technical)

Save as `draft-prd.md`.

## Step 6: Humanize

Rewrite `@draft-prd.md` using `@brand-voice.md` guidelines:
- Remove jargon and corporate speak
- Use audio-inspired language where natural ("amplify" not "leverage," "tune" not "optimize")
- Ensure clarity and specificity
- Check for passive voice
- Verify every section adds value

Update the file in place.

## Step 7: Generate Review Checklist

Create a review document that includes:
- Summary of the PRD for reviewers
- Specific questions for each stakeholder type:
  - ML Engineer: model feasibility, latency targets, GPU cost
  - Executive: revenue impact, resource ask, timeline
  - Designer: voice agent UX, configuration interface, customer experience
- Open questions that need resolution
- Suggested reviewers and timeline

Save as `prd-review-request.md`.

---

## Example Usage

```
Using the workflow in @workflows/research-to-prd.md:
- Analyze the customer and internal interviews in @research/
- Focus on the "enterprise voice agent latency" problem theme
- Create a PRD for Voice Agents latency optimization
```

---

## Customization

- **Different research sources:** Point to any folder with research docs
- **Different template:** Swap `prd-template.md` for your format
- **Skip steps:** Run individual steps as needed
- **Different focus:** Specify which problem theme to focus on

---

## Tips

- Start with Step 1-3 to validate the problem before jumping to solutions
- Share `research-synthesis.md` with stakeholders before writing the full PRD
- The PRD draft will need human review - AI provides the skeleton, you add judgment
- Don't skip the humanize step - first drafts often sound robotic
- For Voice Agents features, make sure to get Priya's input on feasibility before finalizing

---

*Workflow version 1.2 - Updated December 2025*
