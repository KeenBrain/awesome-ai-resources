# PM-to-Production Pipeline Demo

## Project Overview
This project demonstrates a PM-to-Production pipeline using Claude skills. It simulates a real-world workflow where product managers can analyze user interviews, mine analytics data, prioritize features using RICE scoring, and create Linear tickets.

The `/lfg` skill orchestrates: user interview analysis → analytics data mining → RICE prioritization → Linear ticket creation.

## Project Structure
- `data/interviews/` — 7 mock user interview transcripts (.md with YAML frontmatter)
- `data/analytics/` — SQLite DB with product analytics (seed-database.ts to regenerate)
- `output/` — Pipeline artifacts generated at runtime
- `.claude/skills/` — 5 skill files that form the pipeline

## Key Commands
- `npx tsx data/analytics/seed-database.ts` — Regenerate analytics DB

## Pipeline Skills (in .claude/skills/)
- `/lfg` — Master orchestrator, runs full pipeline
- `/extract-interview-insights` — Analyze user interviews
- `/extract-analytics-insights` — Query analytics database
- `/prioritize-features` — RICE scoring and ranking
- `/manage-linear-tickets` — Create/update Linear tickets

## Environment Variables (.env)
- `LINEAR_API_KEY` — Linear API key (if not using global MCP)
