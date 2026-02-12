"""
Agent Demo — Competitive Analysis Agent
========================================
This script simulates an agent loop for demonstration purposes.
It shows the reasoning, tool selection, and adaptation process
that makes agents different from simple automations.

Requirements: pip install anthropic
Set ANTHROPIC_API_KEY environment variable before running.
"""

# import anthropic
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
