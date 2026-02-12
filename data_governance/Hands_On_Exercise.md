# Hands-On Exercise: "Should This Be an Agent?"

**Format:** Live Demo (5 min) + Interactive Decision Framework (5–10 min)
**Audience:** Product Managers
**Materials needed:** Laptop with internet, projector, and this guide

---

## Part 1: Live Demo — Watch an Agent Think (5 min)

### Setup

You'll run a pre-built Python script that simulates an agent loop using the Claude API. The audience watches the agent reason, select tools, execute, observe results, and decide what to do next — in real time.

**What the demo shows:**
- The agent receives a task: “Find the top 3 competitors for [Product X] and summarize their pricing."
- It reasons about what tools to use (web search, data extraction, summarization)
- It executes each step, observes results, and decides next actions
- It encounters an error (one competitor’s page is down) and adapts
- It delivers a final structured summary

**Why this works for PMs:** They see the agent loop from the presentation in action — Perception → Planning → Tool Selection → Execution → Observation → Evaluation → Decision.

### Demo Script (pre-built, ready to run)

```python
"""
Agent Demo — Competitive Analysis Agent
========================================
This script simulates an agent loop for demonstration purposes.
It shows the reasoning, tool selection, and adaptation process
that makes agents different from simple automations.

Requirements: pip install anthropic
Set ANTHROPIC_API_KEY environment variable before running.
"""

import anthropic
import json
import time

# ============================================================
# CONFIGURATION — Change these for your demo!
# ============================================================
PRODUCT_NAME = "Notion"
TASK = f"""You are a competitive intelligence agent for a Product Manager.

Your task: Find the top 3 competitors for {PRODUCT_NAME} and summarize
their key features and pricing tiers.

Think step by step. For each step:
1. State what you're doing and why
2. Use the available tools
3. Evaluate results before moving on
4. If something fails, adapt your approach

Deliver a final summary table."""

# ============================================================
# TOOLS — These are what the agent can use
# ============================================================
tools = [
    {
        "name": "web_search",
        "description": "Search the web for information. Returns relevant results.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "extract_pricing",
        "description": "Extract pricing information from a company's website.",
        "input_schema": {
            "type": "object",
            "properties": {
                "company": {
                    "type": "string",
                    "description": "The company name to look up pricing for"
                }
            },
            "required": ["company"]
        }
    },
    {
        "name": "create_summary",
        "description": "Create a structured summary table from collected data.",
        "input_schema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "string",
                    "description": "The raw data to summarize into a table"
                }
            },
            "required": ["data"]
        }
    }
]

# ============================================================
# SIMULATED TOOL RESPONSES (for demo reliability)
# ============================================================
SIMULATED_RESPONSES = {
    "web_search": {
        "default": json.dumps({
            "results": [
                {"title": "Top Notion Alternatives 2026", "snippet": "Leading competitors include Coda, Confluence, and Monday.com..."},
                {"title": "Notion vs Competitors", "snippet": "Feature comparison across productivity platforms..."}
            ]
        })
    },
    "extract_pricing": {
        "Coda": json.dumps({"tiers": [{"name": "Free", "price": "$0"}, {"name": "Pro", "price": "$10/mo"}, {"name": "Team", "price": "$30/mo"}], "features": ["Docs + Tables + Apps in one", "Automations", "Cross-doc packs"]}),
        "Confluence": json.dumps({"tiers": [{"name": "Free", "price": "$0 (10 users)"}, {"name": "Standard", "price": "$6.05/mo"}, {"name": "Premium", "price": "$11.55/mo"}], "features": ["Team wikis", "Jira integration", "Page analytics"]}),
        "Monday.com": json.dumps({"error": "Rate limited. Unable to access pricing page."}),
        "ClickUp": json.dumps({"tiers": [{"name": "Free", "price": "$0"}, {"name": "Unlimited", "price": "$7/mo"}, {"name": "Business", "price": "$12/mo"}], "features": ["Task management", "Docs", "Whiteboards", "AI assistant"]})
    },
    "create_summary": {
        "default": json.dumps({"status": "Summary table created successfully"})
    }
}

def simulate_tool(name, input_data):
    """Simulate tool execution with realistic delays."""
    time.sleep(1)  # Simulate network latency

    if name == "extract_pricing":
        company = input_data.get("company", "")
        return SIMULATED_RESPONSES[name].get(company, json.dumps({"error": f"No data found for {company}"}))
    return SIMULATED_RESPONSES.get(name, {}).get("default", json.dumps({"result": "OK"}))


def run_agent_demo():
    """Run the agent loop with visible reasoning."""

    print("=" * 60)
    print(f"  AGENT TASK: Competitive analysis for {PRODUCT_NAME}")
    print("=" * 60)
    print()

    # Initialize client (comment out for offline demo)
    # client = anthropic.Anthropic()

    # For the demo, we simulate the agent's reasoning steps
    steps = [
        {
            "reasoning": f"I need to find the top competitors for {PRODUCT_NAME}. Let me start with a web search to identify them.",
            "tool": "web_search",
            "input": {"query": f"top competitors for {PRODUCT_NAME} 2026"},
            "evaluation": "Found relevant results. The top competitors appear to be Coda, Confluence, and Monday.com. Let me get pricing for each."
        },
        {
            "reasoning": "Now I'll extract pricing information for Coda, the first competitor.",
            "tool": "extract_pricing",
            "input": {"company": "Coda"},
            "evaluation": "Got Coda's pricing. Three tiers: Free, Pro ($10/mo), Team ($30/mo). Moving to the next competitor."
        },
        {
            "reasoning": "Extracting pricing for Confluence, the second competitor.",
            "tool": "extract_pricing",
            "input": {"company": "Confluence"},
            "evaluation": "Got Confluence pricing. Three tiers starting at free for 10 users. Now let me get Monday.com."
        },
        {
            "reasoning": "Extracting pricing for Monday.com, the third competitor.",
            "tool": "extract_pricing",
            "input": {"company": "Monday.com"},
            "evaluation": "ERROR: Rate limited on Monday.com. I need to ADAPT. Let me try an alternative competitor — ClickUp is also a strong Notion competitor."
        },
        {
            "reasoning": "Monday.com pricing is unavailable. Adapting my approach — I'll use ClickUp as the third competitor instead.",
            "tool": "extract_pricing",
            "input": {"company": "ClickUp"},
            "evaluation": "Got ClickUp pricing. Three tiers starting at free. I now have data for 3 competitors. Let me create the summary."
        },
        {
            "reasoning": "I have pricing and feature data for all three competitors. Creating the final summary table.",
            "tool": "create_summary",
            "input": {"data": "Coda, Confluence, ClickUp pricing and features"},
            "evaluation": "Summary created. Task complete."
        }
    ]

    for i, step in enumerate(steps, 1):
        print(f"--- STEP {i} ---")
        print()

        # Show reasoning
        print(f"  THINKING: {step['reasoning']}")
        print()
        time.sleep(1.5)

        # Show tool selection
        print(f"  ACTION:   Using tool '{step['tool']}'")
        print(f"  INPUT:    {json.dumps(step['input'])}")
        print()

        # Execute tool
        result = simulate_tool(step['tool'], step['input'])
        print(f"  RESULT:   {result[:120]}...")
        print()
        time.sleep(1)

        # Show evaluation
        if "ERROR" in step['evaluation']:
            print(f"  EVALUATE: ⚠️  {step['evaluation']}")
        else:
            print(f"  EVALUATE: ✓ {step['evaluation']}")
        print()
        time.sleep(1)

    # Final output
    print("=" * 60)
    print("  FINAL OUTPUT")
    print("=" * 60)
    print()
    print("  | Competitor   | Free Tier | Mid Tier     | Top Tier      | Key Differentiator     |")
    print("  |-------------|-----------|--------------|---------------|------------------------|")
    print("  | Coda        | $0        | $10/mo (Pro) | $30/mo (Team) | Docs + Tables + Apps   |")
    print("  | Confluence  | $0 (10u)  | $6.05/mo     | $11.55/mo     | Jira integration       |")
    print("  | ClickUp     | $0        | $7/mo        | $12/mo        | All-in-one workspace   |")
    print()
    print("  NOTE: Monday.com was unavailable (rate limited).")
    print("  The agent adapted and substituted ClickUp as the third competitor.")
    print()
    print("=" * 60)
    print("  KEY OBSERVATION FOR PMs:")
    print("  The agent encountered a failure and adapted autonomously.")
    print("  An automation would have stopped or returned an error.")
    print("=" * 60)


if __name__ == "__main__":
    run_agent_demo()
```

### How to Run the Demo

```bash
# No API key needed — the demo uses simulated responses for reliability
python agent_demo.py
```

### Talking Points During the Demo

As the script runs, narrate what's happening:

- **Step 1:** "The agent is reasoning about what to do first. It chose web search — that's the Planning pattern."
- **Step 2–3:** "Now it's systematically working through competitors. This is the agent loop in action."
- **Step 4:** "Here's where it gets interesting — the tool failed. Watch what happens..."
- **Step 5:** "It adapted! Instead of stopping, it chose an alternative. An automation would have thrown an error and stopped."
- **Step 6:** "Now it's synthesizing everything into a deliverable. This is the full Perception → Action → Evaluation → Decision loop."

**Close the demo with:** "That adaptation — the ability to handle the unexpected — is what makes an agent an agent."

---

## Part 2: Interactive Exercise — "Should This Be an Agent?" (5–10 min)

### Instructions for Facilitator

1. Present each scenario to the group (on screen or verbally)
2. Give 30 seconds for individual thinking
3. Ask for show of hands: Agent? Automation? Workflow? Simple API call?
4. Reveal the recommended answer and discuss

### Scenario Cards

---

#### Scenario 1: Customer Onboarding Emails

> Your product sends a welcome email sequence when a new customer signs up. The emails are sent at Day 1, Day 3, and Day 7 with fixed content based on the customer's plan tier.

**Question:** Agent, Automation, or Workflow?

**Answer:** **Workflow / Automation** — The steps are fixed and deterministic. There's no decision-making needed. A simple workflow (Zapier, SendGrid sequence) handles this perfectly. Using an agent here is over-engineering.

---

#### Scenario 2: Competitive Intelligence Dashboard

> Your team wants a system that monitors competitor websites daily, detects pricing changes, evaluates the strategic impact of those changes, and generates a brief analysis for the product team.

**Question:** Agent, Automation, or Workflow?

**Answer:** **Agent** — This involves open-ended analysis (evaluating strategic impact), adaptation (different competitors present info differently), and reasoning (generating analysis). The monitoring part could be automated, but the analysis requires an agent.

**Discussion prompt:** "Where would you put the human-in-the-loop? Probably before the analysis is shared with the team."

---

#### Scenario 3: Invoice Processing

> Your finance team processes 500 invoices/month. Each invoice needs to be: extracted from email, matched to a PO, validated for correct amounts, and routed for approval.

**Question:** Agent, Automation, or Workflow?

**Answer:** **It depends (trick question!)** — If invoices are standardized and come from known vendors: **Workflow with OCR**. If invoices vary wildly in format, have discrepancies that need investigation, or require judgment calls on partial matches: **Agent with human approval gates**. The right answer depends on the complexity of your vendor landscape.

**Discussion prompt:** "This is exactly the 'start simple, add complexity' principle. Begin with automation, upgrade to an agent only when the edge cases justify it."

---

#### Scenario 4: Code Review Assistant

> Your engineering team wants AI to review pull requests, check for security vulnerabilities, suggest improvements, and flag potential breaking changes based on the broader codebase context.

**Question:** Agent, Automation, or Workflow?

**Answer:** **Agent** — This requires understanding context (the broader codebase), reasoning about implications (breaking changes), and adapting analysis based on what it finds. A static linter can catch syntax issues, but contextual code review needs an agent.

**Discussion prompt:** "Notice this agent would use MCP to connect to your GitHub repo, CI pipeline, and documentation."

---

#### Scenario 5: Meeting Scheduler

> An executive wants AI to coordinate meeting times across 4 people in different time zones, checking their calendars, suggesting times, handling conflicts, and sending invites.

**Question:** Agent, Automation, or Workflow?

**Answer:** **Workflow with some agentic features** — Calendar checking and time zone math is deterministic. Conflict resolution might benefit from agent reasoning. But for most cases, tools like Calendly or Google Calendar's scheduling feature handle this without an agent. Only go agentic if the scheduling involves complex priority rules and negotiation.

**Discussion prompt:** "This is a case where the simpler solution almost always wins. Don't build an agent when a $12/month SaaS tool solves it."

---

### Scoring & Discussion (2 min)

After all scenarios, discuss as a group:

**Key Takeaways from the Exercise:**

1. **The answer is often "start with automation"** — Agents are powerful but add complexity, cost, and unpredictability. Default to the simplest solution.

2. **The decision hinges on three factors:**
   - Is the task open-ended or deterministic?
   - Does it require reasoning or just execution?
   - Do edge cases justify the complexity?

3. **Hybrid approaches are common** — Use automation for the predictable parts and agents for the reasoning parts. You don't have to go all-in.

4. **Human-in-the-loop is your friend** — Almost every production agent system has approval gates. Full autonomy is rare.

---

### Decision Framework Cheat Sheet (handout or slide)

```
┌─────────────────────────────────────────┐
│     SHOULD THIS BE AN AGENT?            │
│                                         │
│  1. Are the steps predictable?          │
│     YES → Automation or Workflow        │
│     NO  → Continue ↓                    │
│                                         │
│  2. Does it require reasoning?          │
│     NO  → API call or simple logic      │
│     YES → Continue ↓                    │
│                                         │
│  3. Must it adapt to unexpected input?  │
│     NO  → Workflow with branching       │
│     YES → Continue ↓                    │
│                                         │
│  4. Is the ROI worth the complexity?    │
│     NO  → Simplify the problem first    │
│     YES → Build an Agent                │
│           (with human-in-the-loop!)     │
└─────────────────────────────────────────┘
```

---

## Facilitator Notes

**Timing:**
- Demo setup + run: 5 minutes
- Scenario discussion: 5–10 minutes (adjust based on audience engagement)
- Total: 10–15 minutes

**If running short (5 min version):**
- Skip the demo, just describe it verbally
- Do scenarios 1, 2, and 3 only
- Show the decision framework cheat sheet

**If audience is engaged (15 min version):**
- Run the full demo with narration
- Do all 5 scenarios with group discussion
- End with the decision framework and open Q&A

**Tips:**
- The trick question (Scenario 3) always generates good discussion
- Encourage PMs to think about their own products during scenarios
- The decision framework cheat sheet is a great leave-behind
