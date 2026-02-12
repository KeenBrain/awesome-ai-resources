# Mini PM-to-Production Pipeline Demo

A demo project showcasing a mini PM-to-Production pipeline built with Claude Code skills, agents, and MCP servers. It simulates a real-world workflow where product managers analyze user interviews, mine analytics data, prioritize features using RICE scoring, and create Linear tickets -- all orchestrated by a single `/lfg` command.

## Pipeline Flow

```
/lfg
 ├── 1. Extract Interview Insights   → output/interview-insights.md
 ├── 2. Extract Analytics Insights    → output/analytics-insights.md
 ├── 3. Prioritize Features (RICE)    → output/prioritized-features.md
 └── 4. Create Linear Tickets         → Linear workspace
```

## Project Structure

```
.claude/
  skills/       # 5 skill files (the pipeline steps)
  agents/         # 4 specialized sub-agents
data/
  interviews/     # 7 mock user interview transcripts (.md)
  analytics/      # SQLite DB + seed script for product analytics
output/           # Pipeline artifacts generated at runtime
```

## Skills (`.claude/skills/`)

| Command | Description |
|---|---|
| `/lfg` | Master orchestrator -- runs the full pipeline end-to-end |
| `/extract-interview-insights` | Analyze user interview transcripts for themes and pain points |
| `/extract-analytics-insights` | Query the SQLite analytics database for usage patterns |
| `/prioritize-features` | RICE scoring and feature ranking |
| `/manage-linear-tickets` | Create or update Linear tickets from prioritized features |

## Agents (`.claude/agents/`)

| Agent | Role |
|---|---|
| `interview-analyst` | Qualitative UX researcher for theme extraction and affinity mapping |
| `data-analyst` | Quantitative analyst with SQL expertise for analytics queries |
| `product-strategist` | Senior PM for RICE prioritization and feature scoring |
| `project-manager` | Technical PM for Linear ticket management |

## MCP Servers (`.mcp.json`)

- **Filesystem** -- Read/write access to `data/interviews/` and `output/`
- **SQLite** -- Query access to `data/analytics/product_analytics.db`

## Setup

1. Copy the environment file and fill in your keys:
   ```bash
   cp .env.example .env
   ```

2. (Optional) Regenerate the analytics database:
   ```bash
   npx tsx data/analytics/seed-database.ts
   ```

3. Run the full pipeline in Claude Code:
   ```
   /lfg
   ```

## Environment Variables

| Variable | Description |
|---|---|
| `LINEAR_API_KEY` | Linear API key (if not using global MCP config) |
| `DISCORD_WEBHOOK_URL` | Discord webhook for pipeline notifications |
