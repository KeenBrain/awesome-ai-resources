---
participant_id: P003
name: "Priya Patel"
role: "Data Analyst"
company: "RetailStack"
segment: "pro"
date: "2025-01-22"
interviewer: "Research Team"
duration: "50 minutes"
---

# User Interview: Priya Patel

## Background

Priya Patel is a Senior Data Analyst at RetailStack, an e-commerce analytics company. She works with data all day and is highly technical. She has been using the platform for 6 months and is the primary dashboard user on her team. She evaluates tools with a critical eye and has experience with Tableau, Looker, and Power BI.

## Interview Transcript

**Interviewer**: Priya, thanks for meeting with us. Tell me about your role and how analytics dashboards fit into your work.

**Priya**: I'm the data person on our product team. Everything runs through me -- weekly reports, ad hoc analysis, experiment results, board deck numbers. I've used basically every BI tool out there, so I have strong opinions about what works and what doesn't. I switched to this platform because the data integration was cleaner than what we had with Looker, but the visualization and interaction layer needs serious work.

**Interviewer**: Let's start with what you'd improve first.

**Priya**: Export. Without question. **I cannot do my job effectively without being able to export data from the dashboard.** I'm an analyst. My workflow is: look at a trend in the dashboard, identify something interesting, pull the underlying data, run deeper analysis in Python or R, then share findings with stakeholders. Step two -- pulling the data -- is completely broken because there's no export functionality.

**Interviewer**: How do you work around that today?

**Priya**: I use the API. I've written a collection of Python scripts that pull data from the API endpoints and dump it into DataFrames. But it took me two weeks to set that up, and it's fragile -- every time the API changes, my scripts break. **A simple "Download CSV" button on any chart would eliminate an entire layer of custom tooling that I have to maintain.** It's absurd that I need to write code to get data out of a data product.

**Interviewer**: What about non-technical stakeholders? How do they get data out?

**Priya**: They don't. They ask me. I've become the human export button. My product manager needs numbers for a deck? She pings me. Our VP wants a monthly report? I have to manually compile it. **The lack of export turns analysts into data couriers instead of data analysts.** I spend probably 30% of my time just extracting and reformatting data that people should be able to pull themselves.

**Interviewer**: That's a significant time drain. What other capabilities are missing?

**Priya**: NPS integration. We track NPS religiously at RetailStack -- it's one of our top three KPIs. But NPS lives in a completely separate tool. **I need to see NPS trends directly in the dashboard so I can correlate customer satisfaction with product usage patterns.** Right now I'm doing that correlation manually in a spreadsheet, and it takes hours.

**Interviewer**: Can you walk me through that manual process?

**Priya**: Sure. Every month I pull NPS data from our survey tool into a spreadsheet. Then I pull usage data from the dashboard -- through my API scripts, of course, since there's no export. Then I join them on user ID and run correlation analysis. The whole thing takes about 4 hours. **If NPS were a native widget in the dashboard, I could do that same analysis in maybe 15 minutes by just looking at the trends side by side.** Four hours down to fifteen minutes. That's the kind of efficiency we're talking about.

**Interviewer**: You mentioned correlating NPS with usage patterns. What patterns have you found?

**Priya**: Lots of interesting stuff. Users who hit three core features in their first week have NPS scores 20 points higher than those who don't. Users who experience slow load times -- which is a different issue -- rate us lower. But here's the thing: **every time I want to update that analysis, it's another 4-hour manual effort because the tools don't talk to each other.** With NPS built into the dashboard, I could set up a view once and just check it whenever I need to.

**Interviewer**: Let's talk about the filtering experience. How do you use filters?

**Priya**: Extensively, or at least I try to. Filters are where I do my real analysis -- segmenting users, narrowing time ranges, isolating cohorts. But **the filters are genuinely buggy. I've documented at least five distinct filtering issues.** The worst one is the date range filter. I select a custom date range, and about one in three times, the data doesn't update. The filter UI shows my selection, but the chart still displays the old date range.

**Interviewer**: One in three times? That's quite frequent.

**Priya**: It's reproducible, too. I've noticed it happens more often when you change filters quickly -- like if I select a date range and then immediately try to add a segment filter, the date range filter gets silently dropped. **The filter state management is clearly broken. Filters should be atomic -- when I apply a set of filters, all of them should apply or none of them.** Right now I get partial filter application, which is worse than no filters because it gives me wrong data that looks right.

**Interviewer**: Have you encountered other filter issues?

**Priya**: Yes. When I apply a segment filter -- say, "enterprise users only" -- the main chart updates but the summary metrics at the top of the page don't. So the chart shows enterprise data but the cards above it show all-user data. **You end up with a dashboard where different widgets are showing different slices of data, and unless you're really paying attention, you'd never notice.** I've caught my PM about to present with incorrect filtered data twice.

**Interviewer**: As a data analyst, how does that filter inconsistency affect your trust in the tool?

**Priya**: It's devastating for trust. The whole point of a dashboard is to be a reliable source of truth. **If I can't trust that the filters are applied correctly, I have to verify every single number independently, which means the dashboard provides negative value -- it's slower than just querying the database directly.** I'm at the point where for anything that matters, I bypass the dashboard and go straight to SQL.

**Interviewer**: Let's switch to chart types. You mentioned having experience with other BI tools -- how do the chart options here compare?

**Priya**: Poorly. I came from Tableau, where I had every chart type imaginable. Here I get line charts and bar charts. That's it. **I need at minimum: scatter plots, area charts, stacked bar charts, and heat maps. Those aren't exotic -- they're standard analytical visualizations.** A scatter plot is the most basic tool for showing correlation between two variables, and I can't make one.

**Interviewer**: Which chart type do you miss most?

**Priya**: Scatter plot, because I do a lot of correlation analysis. But honestly, **what I really want is the ability to change chart types dynamically. Show me the data, then let me toggle between line, bar, area, and scatter to find the best representation.** In Tableau I do that constantly -- the same dataset looks completely different depending on the chart type, and switching between them is how I discover insights.

**Interviewer**: Can you give me a specific example?

**Priya**: Last week I was analyzing feature adoption across customer segments. In a bar chart, it looked like all segments were roughly similar. But if I could have switched to a scatter plot with company size on one axis and adoption on the other, I would have immediately seen that there's a cluster of mid-market companies with unusually low adoption. Instead, I had to export the data -- through my API scripts -- and rebuild the chart in Python. **The dashboard should be a tool for exploration, not just a static display of pre-configured views.**

**Interviewer**: How does all of this impact your overall productivity?

**Priya**: I've actually tracked it. In a typical week, I spend about 6 hours on workarounds: 3 hours on manual data extraction because there's no export, 1.5 hours on NPS correlation analysis that should be built-in, 1 hour on filter troubleshooting, and 30 minutes rebuilding charts in Python because the chart options are too limited. **That's six hours a week -- almost a full day -- lost to tool limitations.**

**Interviewer**: If you were prioritizing fixes, what order would they go in?

**Priya**: Export first -- it's foundational. I need data to flow freely. Then fix the filters -- I need to trust the data I'm seeing. Then NPS integration -- it's a critical metric that's isolated from everything else. Then chart type flexibility. **Export and filters are blocking issues. NPS and chart types are capability gaps.** There's a difference, but they all need addressing.

**Interviewer**: What would the ideal export experience look like for you?

**Priya**: Every chart should have a small download icon. Click it, get a dropdown: CSV for raw data, PNG for the chart image, PDF for a formatted view. For the whole dashboard, there should be a "Export All" button that gives me a zip file with CSVs for every widget. **And critically, the export should respect the current filter state.** If I've filtered to enterprise users in Q4, the CSV should contain exactly that data slice.

**Interviewer**: Any other feedback?

**Priya**: One thing I want to emphasize: the underlying data quality is good. The ingestion pipeline is reliable, the metrics calculations are correct. **The product's weakness is in the interface layer -- export, filters, NPS, chart types. Fix those four things and this becomes a genuinely competitive analytics platform.** Right now it's a great data engine with a mediocre interface.

**Interviewer**: That's very clear and actionable feedback. Thanks, Priya.

**Priya**: Sure. I hope something changes. I'd rather fix this tool than migrate to another one, but my patience has a limit.

## Key Quotes

- "I cannot do my job effectively without being able to export data from the dashboard."
- "A simple Download CSV button on any chart would eliminate an entire layer of custom tooling."
- "The lack of export turns analysts into data couriers instead of data analysts."
- "I need to see NPS trends directly in the dashboard so I can correlate customer satisfaction with product usage patterns."
- "The filter state management is clearly broken. Filters should be atomic."
- "I need at minimum: scatter plots, area charts, stacked bar charts, and heat maps."
- "That's six hours a week -- almost a full day -- lost to tool limitations."

## Themes Identified

- Export capability (critical)
- NPS tracking (critical)
- Filter reliability (critical)
- Chart type flexibility (high)
