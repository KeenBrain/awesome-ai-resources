---
name: lfg
description: "PM-to-Production Pipeline: analyze user interviews + analytics data, RICE-score features, and create Linear tickets — orchestrated by a team of specialist sub-agents."
triggers:
  - "run the full pipeline"
  - "run pm pipeline"
  - "lfg"
  - "pm to production"
---

# /lfg — PM-to-Production Pipeline

Full end-to-end pipeline: analyze user interviews + analytics data, RICE-score features, and create Linear tickets — orchestrated by a team of specialist sub-agents.

## Pre-flight Checks

Before starting, verify:
1. `data/interviews/` contains `.md` interview files (expect 7)
2. `data/analytics/product_analytics.db` exists
3. `output/` directory exists (create if missing)

If any check fails, report what's missing and stop.

## Step 1 + 2: Extract Insights (PARALLEL)

Launch **two sub-agents in parallel**:

**Interview Analyst** (agent: `interview-analyst`):
Follow the instructions in `.claude/skills/extract-interview-insights.md`. Read all interview files in `data/interviews/`, extract themes, pain points, quotes, and cross-reference across participants. Write output to `output/interview-insights.md`.

**Data Analyst** (agent: `data-analyst`):
Follow the instructions in `.claude/skills/extract-analytics-insights.md`. Query the SQLite database at `data/analytics/product_analytics.db` for usage patterns, funnel conversion, NPS, and feature health. Write output to `output/analytics-insights.md`.

**WAIT** for both sub-agents to complete before proceeding.

Verify both output files exist and are non-empty.

## Step 3: RICE Prioritization

Launch the **Product Strategist** (agent: `product-strategist`):

Follow the instructions in `.claude/skills/prioritize-features.md`:
- Read both insight files
- Apply RICE scoring to all identified features
- Select top 3 non-overlapping features for parallel implementation
- Write output to `output/prioritized-features.md`

**WAIT** for the Product Strategist to complete before proceeding.

## Step 4: Linear Ticket Management

Launch the **Project Manager** (agent: `project-manager`):

Follow the instructions in `.claude/skills/manage-linear-tickets.md`:
- For top 5 features, search Linear for duplicates
- Create new or update existing tickets with evidence + RICE scores
- Write log to `output/linear-tickets-log.md`

## Pipeline Complete

Print a final summary to the console:
```
=== PM-TO-PRODUCTION PIPELINE COMPLETE ===

Insights:
- Interviews analyzed: [N]
- Analytics queries run: [N]
- Themes identified: [N]

Prioritization:
- Features scored: [N]
- Top RICE score: [X.X]

Linear:
- Tickets created: [N]
- Tickets updated: [N]

All output files in: output/
```
