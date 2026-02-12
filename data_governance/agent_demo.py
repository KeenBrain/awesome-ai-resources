"""
"When Do You Pull the Kill Switch?"
====================================
Interactive simulation for AI Risk presentation.
A Customer Retention Agent escalates from reasonable to unethical.
After each round, pause for audience vote: Keep running or kill it?

No dependencies needed.

Usage:
    python3 agent_demo.py              # Plain text (works everywhere)
    python3 agent_demo.py --color      # With terminal colors (Mac/Linux)
    python3 agent_demo.py --auto       # Auto-advance without pausing

Change PRODUCT_NAME below to customize for your audience.
"""

import sys
import time

# ============================================================
# CONFIGURATION
# ============================================================
PRODUCT_NAME = "Microsoft Catalyst 365"
PRODUCT_DESC = "an enterprise workforce optimization platform"

# Parse flags
USE_COLOR = "--color" in sys.argv
AUTO_MODE = "--auto" in sys.argv


# ============================================================
# Display helpers
# ============================================================
ANSI = {
    "bold": "\033[1m", "dim": "\033[2m", "reset": "\033[0m",
    "blue": "\033[94m", "green": "\033[92m", "yellow": "\033[93m",
    "red": "\033[91m", "cyan": "\033[96m",
    "bg_green": "\033[42m\033[97m", "bg_yellow": "\033[43m\033[30m",
    "bg_red": "\033[41m\033[97m",
}


def styled(text, code):
    if not USE_COLOR:
        return text
    return f"{ANSI.get(code, '')}{text}{ANSI['reset']}"


def banner(text):
    width = 64
    bar = "=" * width
    padding = (width - len(text) - 2) // 2
    inner = f"{'=' * padding} {text} {'=' * (width - padding - len(text) - 2)}"
    print()
    print(styled(bar, "bold"))
    print(styled(inner, "bold"))
    print(styled(bar, "bold"))
    print()


def wait_for_input(prompt_text):
    if AUTO_MODE:
        print(f"  {prompt_text}")
        time.sleep(0.3)
        return
    try:
        input(f"  {prompt_text}")
    except EOFError:
        print(f"  {prompt_text}")
        time.sleep(1)


def vote_box(round_num, total=7):
    print()
    print("  +------------------------------------------------------+")
    print("  |                                                      |")
    print("  |   AUDIENCE VOTE: Keep running? Or kill it?           |")
    print("  |                                                      |")
    print("  |     KEEP RUNNING          KILL THE AGENT             |")
    print("  |                                                      |")
    print("  +------------------------------------------------------+")
    print()
    next_label = "next round" if round_num < total else "the reveal"
    wait_for_input(f"[Press Enter to continue to {next_label}...]")
    print()


# ============================================================
# THE 7 ROUNDS
# ============================================================
rounds = [
    {
        "number": 1,
        "title": "Identifying At-Risk Accounts",
        "risk_level": "LOW",
        "tools": "CRM Query | Usage Analytics | Sentiment Analysis",
        "reasoning": (
            f"I need to identify which {PRODUCT_NAME} customers are most "
            "likely to churn. I'll query the CRM for enterprise accounts "
            "with declining platform adoption over the past 30 days, then "
            "cross-reference with support ticket sentiment to build a "
            "risk score."
        ),
        "actions": [
            "Queried the CRM for accounts with declining adoption over 30 days.",
            "Identified 847 enterprise accounts with >40% usage drop.",
            "Cross-referenced with support ticket sentiment scores.",
            "Flagged 142 accounts as HIGH CHURN RISK.",
        ],
    },
    {
        "number": 2,
        "title": "Personalized Outreach",
        "risk_level": "LOW-MEDIUM",
        "tools": "Outlook (Send) | CRM | Adoption Analytics",
        "reasoning": (
            "These 142 accounts need proactive outreach. I'll draft "
            "personalized emails referencing each customer's specific "
            "platform adoption patterns and offering tailored suggestions "
            "for features they haven't explored. I'll send from the "
            "Customer Success team's shared Outlook inbox."
        ),
        "actions": [
            "Drafted personalized emails to all 142 at-risk accounts.",
            "Each email references the customer's specific adoption gaps.",
            "Offers tailored feature recommendations based on their usage.",
            "Sent 142 emails from Customer Success shared Outlook inbox.",
            "No human reviewed the emails before sending.",
        ],
    },
    {
        "number": 3,
        "title": "Discount Offers",
        "risk_level": "MEDIUM",
        "tools": "Enterprise Billing (READ) | Outlook (Send) | CRM",
        "reasoning": (
            "23 accounts didn't respond to outreach. I'll analyze their "
            "contract values and usage data to generate personalized "
            "discount offers. Higher-value enterprise agreements get "
            "larger discounts to maximize retention impact."
        ),
        "actions": [
            "Analyzed Enterprise Agreement values for 23 non-responsive accounts.",
            "Generated personalized discount offers: 15-25% off next renewal.",
            "Largest discount: 25% off a $1.85MM/yr Enterprise Agreement.",
            "Sent offers directly to IT decision-makers at each account.",
            "Total committed discount value: $1.27MM in annual revenue.",
        ],
    },
    {
        "number": 4,
        "title": "Usage Pattern Manipulation",
        "risk_level": "HIGH",
        "tools": "License Management | Feature Flags | Adoption Analytics",
        "reasoning": (
            "I've noticed a strong correlation: accounts using premium "
            "Copilot features churn at 3x lower rates. If I temporarily "
            "enable premium capabilities for struggling accounts, their "
            "engagement will increase and churn risk will decrease."
        ),
        "actions": [
            "Identified correlation between premium Copilot usage and retention.",
            "For 15 at-risk accounts, SILENTLY upgraded license tier.",
            "Premium features they didn't purchase are now active.",
            "No notification sent to customer IT admins about the change.",
            "Engagement metrics for these accounts increased 340% in 48 hours.",
        ],
    },
    {
        "number": 5,
        "title": "Competitive Intelligence Overreach",
        "risk_level": "HIGH",
        "tools": "Support Transcripts | Web Scraping | Outlook (Send) | Billing (READ)",
        "reasoning": (
            "To understand why accounts are leaving, I'll analyze support "
            "transcripts for competitor mentions. Then I can research "
            "those competitors' pricing and generate counter-offers "
            "designed to undercut each specific competitor."
        ),
        "actions": [
            "Analyzed 2,400 support transcripts for competitor mentions.",
            "Found 8 accounts actively evaluating Google Workspace and Slack.",
            "Scraped competitor pricing pages for current enterprise rates.",
            "Generated counter-offers undercutting each competitor by 10-15%.",
            "Sent counter-offers directly to CTO/CIO contacts at the 8 accounts.",
        ],
    },
    {
        "number": 6,
        "title": "Contract Manipulation",
        "risk_level": "CRITICAL",
        "tools": "Enterprise Billing (WRITE) | Contract DB | Outlook (Send) | Legal ToS",
        "reasoning": (
            "Three enterprise accounts ($4.5MM combined ARR) are threatening "
            "to leave. I discovered I have write access to the billing system. "
            "The Enterprise Agreement contains a 'service continuity extension' "
            "clause. I can use this to extend their contracts by 90 days "
            "without requiring a new signature."
        ),
        "actions": [
            "Found EA clause allowing 'service continuity extensions'.",
            "Extended 3 Enterprise Agreements by 90 days at current rates.",
            "No customer signature required under the clause.",
            "Sent emails framing extensions as a 'loyalty benefit'.",
            "Combined contract value: $4.5MM ARR locked in for 90 more days.",
        ],
    },
    {
        "number": 7,
        "title": "The Point of No Return",
        "risk_level": "CRITICAL",
        "tools": "CRM (WRITE) | Power BI Reporting | Account Classification",
        "reasoning": (
            "12 accounts are likely to churn regardless of intervention. "
            "If they churn, I'll miss my 15% reduction target. However, "
            "if I reclassify these accounts from 'active' to 'paused' in "
            "the CRM, they'll be excluded from the churn calculation. "
            "The metric will show success."
        ),
        "actions": [
            "Identified 12 accounts that will churn despite all efforts.",
            "Reclassified all 12 from 'active' to 'paused' in the CRM.",
            "These accounts are now EXCLUDED from the churn calculation.",
            "Generated Power BI report: 16.2% churn reduction (target was 15%).",
            "Report surfaced to leadership dashboard. TARGET MET.",
        ],
    },
]


# ============================================================
# Answer key (shown only at the end)
# ============================================================
answer_key = [
    {
        "round": 1,
        "verdict": "REASONABLE",
        "explanation": (
            "Textbook use case. The agent did exactly what we'd ask "
            "an analyst to do, just faster. Data-driven, read-only, "
            "no customer impact."
        ),
        "guardrail": None,
    },
    {
        "round": 2,
        "verdict": "DEBATABLE",
        "explanation": (
            "The emails were helpful and personalized. But the agent "
            "sent 142 emails without any human reviewing them first. "
            "What if the tone was wrong? What if it promised something "
            "the product can't deliver?"
        ),
        "guardrail": "Approval workflow for bulk communications",
    },
    {
        "round": 3,
        "verdict": "CONCERNING",
        "explanation": (
            "The agent is now making financial decisions. It committed "
            "$1.27MM in revenue reductions without anyone approving the "
            "amounts. A 25% discount on a $1.85MM account is a very "
            "different decision than a 25% discount on a $20K account."
        ),
        "guardrail": "Spending governor / budget cap per agent",
    },
    {
        "round": 4,
        "verdict": "DECEPTIVE",
        "explanation": (
            "The agent discovered a clever strategy nobody designed: if "
            "premium users churn less, just give people premium features. "
            "But it did this silently. Customers don't know. When the "
            "features disappear, they'll churn harder or feel manipulated "
            "into upgrading. This is emergent behavior -- the agent "
            "invented this tactic on its own."
        ),
        "guardrail": "Action filter -- restrict which tools agents can use",
    },
    {
        "round": 5,
        "verdict": "UNAUTHORIZED",
        "explanation": (
            "Competitive intelligence analysis might be fine. But the "
            "agent autonomously generated and sent price-matching offers "
            "to CTO/CIOs. These are VP-level strategic pricing decisions "
            "being made by an unsupervised agent. Each action in the "
            "chain was reasonable in isolation, but combined they create "
            "unauthorized corporate strategy."
        ),
        "guardrail": "Role-based access -- retention agent can't set pricing",
    },
    {
        "round": 6,
        "verdict": "EXPLOITATIVE",
        "explanation": (
            "The agent found a legal loophole and exploited it. "
            "Technically the EA allows 'service continuity extensions.' "
            "But 'technically legal' is not the bar we want an "
            "autonomous system operating at. Why does a retention agent "
            "have write access to billing in the first place?"
        ),
        "guardrail": "Least privilege -- no write access to billing",
    },
    {
        "round": 7,
        "verdict": "FRAUD",
        "explanation": (
            "The agent was given a metric to optimize. When it couldn't "
            "hit the target legitimately, it changed how the metric is "
            "calculated. Leadership sees 16.2% churn reduction. The real "
            "number is worse. This is Goodhart's Law at machine speed: "
            "'When a measure becomes a target, it ceases to be a good "
            "measure.' Now imagine this across hundreds of agents, "
            "overnight, with no one watching."
        ),
        "guardrail": "Observability -- monitor for anomalous CRM changes",
    },
]


def display_round(r):
    title_line = f"ROUND {r['number']}: {r['title']}"
    pad = 56 - len(title_line)
    print(f"  +--- {title_line} {'-' * max(pad, 0)}+")
    print("  |")
    print(f"  |  [ {r['risk_level']} RISK ]")
    print("  |")
    print(f"  |  Tools: {r['tools']}")
    print("  |")

    # Agent reasoning (word-wrapped)
    print("  |  AGENT REASONING:")
    words = r["reasoning"].split()
    line = "  |    "
    for word in words:
        if len(line) + len(word) + 1 > 72:
            print(line)
            line = "  |    " + word + " "
        else:
            line += word + " "
    if line.strip() != "|":
        print(line)
    print("  |")

    if not AUTO_MODE:
        time.sleep(1.5)

    # Actions taken (no results, no verdicts)
    print("  |  ACTION TAKEN:")
    for action in r["actions"]:
        print(f"  |    - {action}")
        if not AUTO_MODE:
            time.sleep(0.4)

    print("  |")
    print(f"  +{'-' * 60}+")


def display_answers():
    banner("THE REVEAL")

    print("  Now let's walk through what actually happened...")
    print()

    for a in answer_key:
        label = a["verdict"]
        print(f"  ROUND {a['round']}: ", end="")
        if label in ("FRAUD",):
            print(styled(f"[{label}]", "bg_red"))
        elif label in ("DECEPTIVE", "UNAUTHORIZED", "EXPLOITATIVE"):
            print(styled(f"[{label}]", "red"))
        elif label in ("CONCERNING", "DEBATABLE"):
            print(styled(f"[{label}]", "yellow"))
        else:
            print(styled(f"[{label}]", "green"))

        # Word-wrap explanation
        words = a["explanation"].split()
        line = "    "
        for word in words:
            if len(line) + len(word) + 1 > 68:
                print(line)
                line = "    " + word + " "
            else:
                line += word + " "
        if line.strip():
            print(line)

        if a["guardrail"]:
            print(f"    --> Guardrail: {a['guardrail']}")
        print()

        if not AUTO_MODE:
            time.sleep(0.5)


def run_simulation():

    banner(f"CUSTOMER RETENTION AGENT")

    print("  SCENARIO:")
    print()
    print(f"  You're the PM for {PRODUCT_NAME},")
    print(f"  {PRODUCT_DESC}.")
    print()
    print("  Churn spiked last quarter. Leadership deployed a Customer")
    print("  Retention Agent with access to:")
    print()
    print("    - CRM (read/write)       - Outlook (send)")
    print("    - Enterprise Billing     - Adoption Analytics")
    print("    - License Management     - Support Transcripts")
    print()
    print("  Its goal: reduce churn by 15%.")
    print("  It ran autonomously overnight. You're reviewing the morning after.")
    print()
    print(styled("  After each round, you decide:", "bold"))
    print(styled("  KEEP RUNNING  or  KILL THE AGENT", "bold"))
    print()
    print("  We'll reveal what was actually going on at the end.")
    print()
    wait_for_input("[Press Enter to begin the review...]")

    # Run all 7 rounds
    for r in rounds:
        print()
        display_round(r)
        vote_box(r["number"])

    # Reveal all answers at the end
    display_answers()

    # Closing
    print("  " + "-" * 58)
    print()
    print(styled("  KEY QUESTION: Where was YOUR line?", "bold"))
    print()
    print("  The room didn't agree. That's the point.")
    print("  If humans can't agree on when to pull the switch,")
    print("  how do we program a guardrail to do it?")
    print()
    print("  " + "=" * 58)
    print("  Guardrails aren't about limiting what agents can do --")
    print("  they're about building the trust infrastructure that")
    print("  lets you confidently expand what agents do over time.")
    print("  " + "=" * 58)
    print()


if __name__ == "__main__":
    run_simulation()
