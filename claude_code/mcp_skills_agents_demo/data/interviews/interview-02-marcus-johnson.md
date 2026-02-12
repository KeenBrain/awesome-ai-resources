---
participant_id: P002
name: "Marcus Johnson"
role: "Growth Lead"
company: "ScaleUp.io"
segment: "enterprise"
date: "2025-01-18"
interviewer: "Research Team"
duration: "40 minutes"
---

# User Interview: Marcus Johnson

## Background

Marcus Johnson leads the growth team at ScaleUp.io, a mid-stage enterprise SaaS company with 50,000+ users. He focuses on acquisition funnels, A/B testing, and growth loops. He has been a power user of the dashboard for over a year and is on the Enterprise plan. His team of 12 relies heavily on data to drive growth experiments.

## Interview Transcript

**Interviewer**: Marcus, thanks for carving out time for this. Can you describe your relationship with the analytics dashboard?

**Marcus**: Yeah, it's complicated. [laughs] Look, I live in this thing. I probably have it open eight hours a day. My entire growth strategy depends on understanding our numbers in real time. So when the dashboard works, it's great. When it doesn't, it directly impacts our ability to run experiments and make decisions.

**Interviewer**: What works well for you right now?

**Marcus**: The real-time user counts are solid. The basic engagement metrics are good. I like the cohort view -- that was a great addition. And honestly, the data freshness is pretty good compared to some competitors. So the foundation is strong. It's the layer on top where things fall apart.

**Interviewer**: Tell me about where things fall apart.

**Marcus**: Where do I start? Okay, the biggest one -- **I cannot believe there's no funnel visualization in 2025.** I run a growth team. Funnels are literally what we do. I need to see signup to activation to aha-moment to conversion to expansion, and I need to see where users are dropping off at each stage. Right now I get a bunch of individual metrics but no connected funnel view.

**Interviewer**: How are you solving that today?

**Marcus**: We built a custom Amplitude integration. Took two engineers three weeks. And it still doesn't match the dashboard data perfectly because we're pulling from different event streams. **A native funnel chart would replace a custom integration that costs us engineering time and creates data discrepancies.** It's not just a feature request -- it's an operational efficiency issue.

**Interviewer**: What would an ideal funnel visualization look like for you?

**Marcus**: I want to define custom funnel stages -- pick the events, set the order, set a conversion window. Then I want to see a horizontal bar chart or a classic funnel shape showing the volume and conversion rate at each step. I want to be able to break it down by cohort or segment. And I want to see how funnel performance changes over time. **If I could compare this week's funnel against last week's funnel side by side, that alone would be worth upgrading our plan.**

**Interviewer**: Let's talk about other pain points. What else is holding your team back?

**Marcus**: Exporting. Man, the export situation is dire. I run a weekly growth review with 15 people. I need to prepare a deck. Right now, I'm literally taking screenshots of charts and pasting them into Google Slides. **There is no export button anywhere in the entire product. Not CSV, not PNG, not PDF. Nothing.** For a data product, that's kind of unbelievable.

**Interviewer**: What formats would be most useful?

**Marcus**: CSV for raw data -- my analysts need to pull numbers into their models. PNG or SVG for charts -- I need those for presentations. And PDF for the whole dashboard view -- I send that to our investors monthly. **If I had a one-click export to CSV and PDF, it would save my team collectively probably 5 hours a week in manual data wrangling.**

**Interviewer**: You mentioned presentations. How else does data flow out of the dashboard into your workflows?

**Marcus**: That's the thing -- it doesn't flow. It gets manually carried. Screenshots, re-typed numbers, manually recreated charts. I've actually had situations where someone mistyped a number in a slide and we made a wrong decision about an experiment because of it. **The lack of export isn't just inconvenient -- it introduces human error into our data pipeline.**

**Interviewer**: Let's talk about chart types. How do you feel about the visualization options available?

**Marcus**: Limited. Everything is a line chart or a bar chart. That's it. **I need more chart type flexibility. Scatter plots for correlation analysis, area charts for cumulative metrics, and especially the ability to switch between chart types on the same dataset.** Like, sometimes a line chart is the right view, but sometimes I need to see the same data as a stacked bar to understand composition. I shouldn't have to rebuild a view just to change the visualization type.

**Interviewer**: Can you give me a specific example where the chart limitation hurt you?

**Marcus**: Last month we were analyzing our trial-to-paid conversion across different company sizes. A bar chart showed us the conversion rates, but what I really needed was a scatter plot of company size vs. conversion rate to see the correlation pattern. Couldn't do it. Had to export -- well, screenshot and manually enter -- the data into a Sheets chart. Took 20 minutes for something that should be a dropdown menu change. **The current chart options feel like they were designed for a simple KPI dashboard, not for serious analytical work.**

**Interviewer**: You mentioned real-time data earlier. Are there any performance issues?

**Marcus**: Now that you bring it up, yes. **The dashboard takes forever to load when you first open it.** I'm talking 8 to 10 seconds on a good day, sometimes 15+ seconds. For something I open multiple times a day, that adds up. I've timed it -- my team collectively waits probably 30 minutes a day just for the dashboard to load.

**Interviewer**: Is it consistently slow, or does it vary?

**Marcus**: It's worst in the morning when everyone's logging in, and it's worse when you have a lot of data selected. Like if I'm looking at 90 days of data across all segments, it can take 20 seconds to render. **The initial page load is the killer though. It feels like it's loading every widget and every piece of data on the page before showing me anything.** A smarter loading strategy -- like loading the top widgets first -- would make a huge difference in perceived performance.

**Interviewer**: How does the slow load time affect your team's usage?

**Marcus**: Some people have just stopped using it for quick lookups. They'll Slack me or my analyst instead of opening the dashboard themselves because it's faster to ask a human than to wait for the page to load. That's not great for data culture. **When the tool is slow, people find workarounds, and those workarounds usually mean fewer people are looking at data directly.**

**Interviewer**: If you had to rank your top frustrations, what order would they be in?

**Marcus**: Number one is the missing funnel visualization. It's core to what my team does and we're using a janky workaround. Number two is export -- we're wasting hours every week on manual data transfer. Number three is chart type flexibility -- we need more than line and bar charts for real analysis. And number four is the load time, which is a constant low-grade annoyance.

**Interviewer**: How do these issues compare to what competitors offer?

**Marcus**: I've looked at Amplitude, Mixpanel, and Heap. They all have funnel views, they all have export, they all have multiple chart types, and they're all reasonably fast. **The only reason we haven't switched is that our core data pipeline is deeply integrated with this platform. But that integration advantage erodes every time I have to spend 20 minutes recreating a chart that Amplitude would show me in two clicks.**

**Interviewer**: What would make you a vocal advocate for this product?

**Marcus**: Fix the funnels and the export. Seriously, those two things. Give me a native funnel builder with segmentation, and give me one-click export to CSV and PDF. **If this dashboard had funnel visualization and data export, I'd move our entire analytics stack onto it and cancel three other tools.** That's how close it is to being great.

**Interviewer**: Any other feedback before we wrap up?

**Marcus**: One more thing on the chart flexibility -- **I'd love to be able to toggle between chart types without losing my configuration.** Like, I set up a view with specific date range, segments, and metrics. Then I want to see it as a line chart, then switch to bar chart, then maybe area chart. Right now there's no way to do that. Each chart type is basically a separate widget with separate configuration.

**Interviewer**: That's super helpful. Thanks, Marcus.

**Marcus**: Anytime. I'm rooting for you guys. The bones of this product are good. It just needs some muscle on top.

## Key Quotes

- "I cannot believe there's no funnel visualization in 2025."
- "A native funnel chart would replace a custom integration that costs us engineering time and creates data discrepancies."
- "There is no export button anywhere in the entire product. Not CSV, not PNG, not PDF. Nothing."
- "The lack of export isn't just inconvenient -- it introduces human error into our data pipeline."
- "I need more chart type flexibility. Scatter plots for correlation analysis, area charts for cumulative metrics."
- "The dashboard takes forever to load when you first open it."
- "If this dashboard had funnel visualization and data export, I'd move our entire analytics stack onto it."

## Themes Identified

- Funnel visualization (critical)
- Export capability (critical)
- Chart type flexibility (high)
- Slow load times (medium)
