# Workflow: Stakeholder Update

This workflow transforms status information into polished stakeholder communications.

## What It Does

1. **Gather** - Collect status from various sources
2. **Synthesize** - Combine into coherent narrative
3. **Format** - Structure for the audience
4. **Humanize** - Apply writing guidelines
5. **Distribute** - Create versions for different channels

---

## When to Use

- Weekly/bi-weekly status updates
- Milestone communications
- Project kickoffs or completions
- Any stakeholder-facing update

---

## Step 1: Gather Status Information

Collect from:
- OKR tracking (`@okrs-q1.md`)
- Project status docs
- Recent shipped features or milestones
- Usage metrics (`@data/usage-metrics.csv`)
- Risks and blockers
- Team updates
- Customer feedback highlights

Create a bullet-point dump of everything relevant.

Save as `status-raw.md`.

## Step 2: Synthesize Key Points

From the raw status, identify:
- Top 3-5 things stakeholders need to know
- Overall status (green/yellow/red)
- Key metrics and progress (latency, churn, enterprise pipeline)
- Important decisions made or needed
- Risks worth flagging (legal, T&S, ML team retention)

Save as `status-synthesis.md`.

## Step 3: Determine Audience

Different audiences need different depth:

**Executive Leadership (Aria, Dev, Ravi):**
- Status, metrics, decisions needed
- 30 seconds to read
- Focus on business impact and revenue

**Cross-Functional Partners (ML team, Sales, T&S):**
- What's coming that affects them
- 2-3 minutes to read
- Focus on dependencies and collaboration

**Your Team (Voice Agents squad):**
- Detailed status and priorities
- 5 minutes to read
- Focus on what to do next

Identify primary audience and adjust accordingly.

## Step 4: Format for Audience

Use appropriate template:
- Executives: `@templates/exec-summary.md`
- Broader team: `@templates/email-update.md`
- Quick update: `@templates/slack-update.md`

Fill in template with content from `status-synthesis.md`.

Save as `status-draft.md`.

## Step 5: Humanize

Review against `@brand-voice.md`:
- Use audio-inspired language naturally ("amplify" not "leverage," "tune" not "optimize")
- Be specific with numbers (latency targets, churn rates, revenue impact)
- Active voice
- Clear action items
- Appropriate length
- Honest about risks — don't bury bad news

Update `status-draft.md` in place.

## Step 6: Create Distribution Versions

From the main update, create channel-specific versions:

**Slack Update** (short)
- 3-5 bullet points
- Link to full update
- Emoji for status

**Email Update** (medium)
- Executive summary
- Key highlights
- Next steps
- Link to details

**Document Update** (full)
- Complete status
- All metrics
- Full risk assessment
- Appendix/links

Save as:
- `updates/slack-update.md`
- `updates/email-update.md`
- `updates/full-status.md`

---

## Example Usage

```
Using the workflow in @workflows/stakeholder-update.md:
- Create a mid-quarter update on Voice Agents enterprise readiness
- Primary audience is executive leadership
- Create Slack and email versions
```

---

## Tips

- Write for the executive audience first, then expand for others
- Lead with status and headlines - details after
- Be honest about risks - the music legal situation, the deepfake incident, ML team retention
- Include clear next steps and owners
- Don't bury the lede - important stuff first
- If latency numbers haven't improved, say so. Don't spin.

---

## Customization

- **Different cadence:** Weekly, bi-weekly, monthly
- **Different scope:** Voice Agents only, or cross-product
- **Different audience:** Tailor depth and focus
- **Different channels:** Add Teams, wiki, etc.

---

*Workflow version 1.2 - Updated December 2025*
