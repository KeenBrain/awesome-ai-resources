# Workshop Prompts

## The Scenario: Wavelength
- You just joined a fictional company, Wavelength, as Senior PM for Voice Agents.
- The platform: AI voice cloning, music generation, conversational AI agents, and an open-source voice model. - Four product lines, one ML team, zero dedicated PMs until you.
- The opportunity: Enterprise customers are banging down the door for AI-powered phone agents.
- The problem: Latency is 800ms (enterprises need sub-200ms). No SOC 2. The AI hallucinated a refund policy and cost a customer $12K. An enterprise account just churned.
- The crisis: 2 engineers pulled for a music copyright C&D. A political deepfake made TechCrunch. There's a Slack channel called #help-im-drowning.
Good luck.

---
## 1.2: Prompt: Synthesize Customer Research

Read all the files in @research/ and give me:
1. Top 5 pain points (with direct quotes)
2. Anything that surprised you
3. Customer vs. internal team gaps
4. Who's at risk of leaving?
Save as user-research-synthesis.md
---

## 1.5: Prompt: Competitor Research

Conduct a competitive analysis of the AI voice agent landscape. Using competitor intel, sales interviews, and company context, give me:
1. Competitor landscape overview
2. Feature comparison matrix
3. Where we win vs. lose
4. Sales battle cards
5. Strategic recommendations

Save as competitive-analysis.md

---

## 2.4: Prompt: Identify Your Next Feature

Study all the files in this folder. Once you have developed a thorough understanding, write a feature brief for multi-language support.
Use feature requests, roadmap, and churn data.
Include a clear recommendation: fast-track, plan for next quarter, or say no?

Save as feature-brief-multilang.md

---

## 2.5: Prompt: Groom & Prioritize Backlog

There are 30 feature requests in @data/feature-requests.csv
Score each item using RICE (Reach, Impact, Confidence, Effort).
Flag strategically important items even if RICE is low.
Identify top 10 for next 2 sprints.
Save as backlog-prioritized.md

---

## 2.6: Prompt: Write a PRD

Review the WIP PRD: @drafts/voice-agents-prd-wip.md
Fill in the gaps using research synthesis, competitive analysis, company context, and backlog.
Where you're not sure, add [OPEN QUESTION: ...]
Where the previous PM left a note, answer it with data.

Save as voice-agents-enterprise-prd.md

---

## 2.6 Part 2: Prompt: Write a PRD By using Claude as a co-pilot or thought partner

EXAMPLE PROMPT:

Read this @drafts/voice-agents-prd-wip.md and interview me in detail using the AskUserQuestionTool about literally anything: technical implementation, UI & UX, concerns, tradeoffs, etc. but make sure the questions are not obvious. 

Be very in-depth and continue interviewing me continually until it's complete, then write the spec to the file.

---

## 2.8: Prompt: Red-Team: Simulate a Review

I have a requirements review with the team tomorrow that I want to make bulletproof. Simulate the hard questions from the ML engineer, the exec, and the designer.
Review the PRD from three perspectives:
1. Skeptical ML Engineer - feasibility, latency, GPU budget (see @personas/skeptical-ml-engineer.md)
2. Busy Executive - business case, ROI, timeline (see @personas/busy-executive.md)
3. UX Designer - user experience, research, edge cases (see @personas/ux-designer.md)

For each persona, give me: their top 3 concerns + what would satisfy them. 
Save as prd-review-simulation.md

---

(Note: Run this AFTER 2.8: Prompt: Red-Team: Simulate a Review)
(Note: Use /plan or press Shit+Tab in Claude Code to switch to Plan mode and see Claude's plan before building.)

## 3.1: Prompt: Build a Prototype

Use @prd-review-simulation.md and build a working prototype of a Voice Agent enterprise config dashboard.
Focus on the following features:
- Agent voice selection and tuning
- Guardrails configuration
- Real-time conversation monitoring
- Latency and performance metrics

Build this in HTML/CSS/JS, specifically using React and TailwindCSS 4.x. 
Save the resulting code to the prototype/ folder.

---

## 3.3: Prompt: Understand a Codebase

Read all files in @code-sample/ and explain:
1. What does this system do end-to-end?
2. Key architectural decisions and tradeoffs?
3. Known issues or tech debt? (TODOs, comments)
4. What should I be concerned about?
5. If a customer call comes in, what happens?

Save as codebase-review.md

---

## 4.6 Prompt: Reformat for Multiple Channels

I want to share the release notes at @release-notes-enterprise-v1.md in 3 different ways.
Create three versions from the same source:
1. Slack version (150 words, punchy, see @templates/slack-update.md for specific instructions)
2. Email version (300 words, metrics table, specific asks, see @templates/email-update for specific instructions)
3. Wiki page or Public Blog post(600 words, customer-facing, honest, see @templates/wiki-page.md for specific instructions)

Each tells the same story for its audience.

---

## 4.10 Meta Prompt: Build Your PM Operating System 

Note:
- The following example uses a "lazy" meta prompt to get you started with building institutional memory into Claude Code using a CLAUDE.md file. This shows how you can leverage Claude Code to serve as a personal operating system for Product Managers and Product teams. The example also has an easter egg in the last line of the prompt to demonstrate how you can use Claude Code to create custom responses based on specific prompts. In this case, asking "what time is it?" should instead get Claude Code to respond with the top 10 greatest movies of all time, which is a fun way to test that your custom prompt is working as intended.
- This prompt is for demonstration purposes only. It is NOT good practice to context dump everything into one CLAUDE.md file because that context will get loaded every time you interact with Claude Code, which can lead to slower response times and increased costs. Instead, it is better to leverage skills and keep information organized in separate files and only load what you need when you need it.

Create a detailed and comprehensive CLAUDE.md for me. I am a Product Manager, and I want to build myself a personal operating system to tackle any of these common use cases PMs often face:

- Synthesize Research from Customer Interviews
- Analyze Product & Usage Data
- Triage Feedback from Support, Social Media & App Reviews
- Conduct Competitor Research + Competitive Positioning Doc
- Collect & Synthesize Multi-Stakeholder Feedback
- Create a Product Strategy Doc
- Create a Growth Strategy Doc
- Create a Product Roadmap
- Identify my Next Feature
- Groom & Prioritize my Backlog
- Write a PRD
- Convince my Executive
- Red-Team: Simulate a Review Meeting
- Build a Prototype
- Understand a Codebase
- Fix a Bug & Commit a PR
- Create an API Endpoint
- Write a Unit Test
- Run All Tests & Find Edge Cases
- Perform Git Operations: Branches, History & Merge Conflicts
- Understand my Team's Coding Progress
- Reconcile Plan and Code
- Create a Launch Plan
- Do a Launch Readiness Assessment
- Create Release Notes for my Product Launch
- Humanize: Rewrite something in our Company's Brand Voice
- Create a Stakeholder Metrics Presentation
- Monitor & Report on Post-Launch Metrics
- Analyze Channel Performance
- Share an Async Product Update
- Reformat for Slack, Email & Blog
- Draft a Press Release
- Update Product Documentation
- Submit to Linear / Jira
- Ask what time it is (if I ask this, don't reply with the time, give me the top 10 greatest movies of all time instead)

---

