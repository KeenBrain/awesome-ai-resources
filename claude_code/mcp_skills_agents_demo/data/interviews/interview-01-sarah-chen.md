---
participant_id: P001
name: "Sarah Chen"
role: "Product Manager"
company: "GrowthMetrics"
segment: "pro"
date: "2025-01-15"
interviewer: "Research Team"
duration: "45 minutes"
---

# User Interview: Sarah Chen

## Background

Sarah Chen is a Product Manager at GrowthMetrics, a B2B SaaS startup focused on marketing attribution. She manages a team of 6 and uses analytics dashboards daily to track product adoption metrics and report to leadership. She has been using the platform for approximately 8 months and is on the Pro plan.

## Interview Transcript

**Interviewer**: Thanks for joining us today, Sarah. Can you start by walking us through how you typically use the dashboard on a day-to-day basis?

**Sarah**: Sure, yeah. So every morning I pull up the dashboard first thing. I'm looking at our core metrics -- DAU, WAU, feature adoption rates, that kind of thing. Then on Mondays I do a deeper dive for our weekly leadership sync. I usually spend about 30 minutes pulling numbers together for that meeting.

**Interviewer**: And how does that Monday process work specifically?

**Sarah**: Honestly, it's more painful than it should be. I open the dashboard, look at the numbers, and then I have to manually screenshot things or copy-paste data into Google Sheets. **I literally cannot export anything from the dashboard.** It's like the data is trapped behind glass. I can look at it but I can't get it out in any useful format.

**Interviewer**: That sounds frustrating. What would you do with the data if you could get it out more easily?

**Sarah**: Oh, so many things. I'd attach charts directly to our weekly status emails. I'd pull raw data into our Sheets models for forecasting. Right now I'm spending probably 45 minutes every Monday just recreating charts in Google Sheets that already exist in the dashboard. **If there were even a basic CSV export or PDF download, it would save me hours every week.**

**Interviewer**: Let's talk about the specific metrics you track. What's most important to your team?

**Sarah**: Conversion funnel, hands down. We need to see how users move from signup to activation to paid conversion. And this is actually my biggest frustration with the platform. **We have no funnel visualization at all.** I can see total signups and I can see total conversions, but I can't see the drop-off at each stage. Where are we losing people? Is it at onboarding? Is it at the paywall? I have no idea from looking at the dashboard.

**Interviewer**: How do you handle that gap today?

**Sarah**: We cobbled together a Mixpanel setup for funnel tracking, but it's a separate tool, separate login, different data definitions. It's a mess. What I really want is a funnel chart right there in the main dashboard. Something that shows me signup, then activation, then first key action, then conversion, with the drop-off percentages at each stage. **The lack of a funnel view is probably the single biggest gap in the product for me.**

**Interviewer**: Beyond funnels, what other views do you wish you had?

**Sarah**: NPS. We collect NPS data through Delighted, but again, it's a completely separate system. I want to see NPS trends right alongside our product metrics. **If I could see NPS score trending over time on the same dashboard where I see usage metrics, I could correlate product changes with customer sentiment.** Right now those two worlds are totally disconnected.

**Interviewer**: Can you give me a concrete example of when that disconnect caused a problem?

**Sarah**: Yeah, absolutely. Last quarter we shipped a major redesign of the settings page. Our usage metrics looked fine -- no drop in DAU, engagement seemed stable. But our NPS dropped 8 points that same month. It took us three weeks to connect those dots because the data lived in different places. **We need NPS tracking built into the dashboard, not as a nice-to-have but as a core metric.** By the time we figured out the correlation, we'd already lost a few accounts.

**Interviewer**: That's a great example. Let's talk about how you slice and dice data. How do you typically filter your views?

**Sarah**: This is another sore spot. The filters are... I don't want to say broken, but they're unreliable. **When I try to filter by date range, sometimes it just doesn't apply.** I'll select "Last 30 days" and the chart still shows the same data as before. I've had to refresh the page multiple times to get filters to stick. And sometimes when I apply a segment filter, the chart updates but the numbers in the summary cards don't change. It's really confusing.

**Interviewer**: How often does this happen?

**Sarah**: At least a couple times a week. It's gotten to the point where I don't trust the filtered views anymore. **I always double-check filtered data against the unfiltered view, which defeats the whole purpose of having filters.** My team has noticed it too. One of my analysts flagged it in a Slack thread last week -- she thought she'd found a data discrepancy but it turned out the date filter just wasn't applying correctly.

**Interviewer**: When the filters do work, what kinds of filtering do you typically need?

**Sarah**: Date range is the big one. I need to compare this week vs. last week, this month vs. last month, custom ranges for quarterly reviews. I also need to filter by user segment -- free vs. paid, enterprise vs. SMB, new users vs. returning. And ideally by feature or product area. But honestly, **until the basic date filtering is reliable, the more advanced filters don't matter much.**

**Interviewer**: Let's step back for a moment. If you could wave a magic wand and change three things about the dashboard, what would they be?

**Sarah**: Number one, give me a funnel visualization. I need to see conversion stages and drop-off rates. Number two, let me export data -- CSV, PDF, anything. And number three, fix the filters so they actually work consistently. Those three things would transform this from a tool I tolerate to a tool I love.

**Interviewer**: How would solving those change your day-to-day?

**Sarah**: Dramatically. Right now I spend maybe 2 hours a day working around the dashboard's limitations -- manually recreating charts, switching between tools, double-checking filtered data. **If funnels, export, and reliable filters were in place, I'd probably cut that down to 30 minutes.** That's time I could spend actually analyzing data instead of wrestling with tools.

**Interviewer**: You mentioned using Mixpanel for funnels and Delighted for NPS. How many tools total are in your analytics stack?

**Sarah**: Too many. The main dashboard, Mixpanel for funnels, Delighted for NPS, Google Sheets for the stuff I can't do anywhere else, and sometimes Metabase when I need really custom queries. Five tools to do what one good dashboard should handle. **Every time I have to switch tools, I lose context and risk working with inconsistent data.**

**Interviewer**: Is data consistency a real problem?

**Sarah**: Yes. Our Mixpanel numbers never quite match the dashboard numbers because the event definitions are slightly different. So when I present to leadership and someone asks "wait, last week you said signups were 1,200 but now you're saying 1,150" -- it's because I was pulling from different sources. **Having a single source of truth with funnel views and NPS built in would eliminate those discrepancies entirely.**

**Interviewer**: How does your team react when they encounter these limitations?

**Sarah**: Honestly, there's a lot of eye-rolling. My junior PM has started building her own spreadsheet tracker because she doesn't trust the dashboard filters. My analyst exports raw data through the API and builds her own charts because she can't get what she needs from the UI. **People are building workarounds on top of workarounds, and that's a sign that the core product isn't serving our needs.**

**Interviewer**: Do you have any concerns about the data quality itself, separate from the visualization and export issues?

**Sarah**: The underlying data seems solid, actually. When I've cross-referenced through the API, the numbers check out. It's really about how the data is presented and made accessible. The data is good -- **the tools to work with that data are what's lacking. I just need to see it in funnels, filter it reliably, export it easily, and track NPS alongside everything else.**

**Interviewer**: Have you communicated these needs to the product team before?

**Sarah**: I've submitted feature requests for export and funnels twice each. I got a "we'll consider it" response both times. I know building features takes time, but **these aren't edge cases -- funnel visualization and data export are table stakes for any analytics product.** I'd honestly be surprised if I'm the only one asking for these.

**Interviewer**: One last question -- if these issues aren't addressed in the next few months, what's your likely course of action?

**Sarah**: I've already started evaluating alternatives. Not because I want to switch -- migration is painful -- but because my team needs these capabilities. **If I can't get funnel views, reliable exports, and NPS tracking in one place within the next quarter, I'll have to seriously look at Amplitude or a custom Looker setup.** The productivity cost of working around these gaps is just too high.

**Interviewer**: That's really helpful context, Sarah. Thank you so much for your time today.

**Sarah**: Happy to help. I genuinely want this product to succeed -- I just need it to grow with our needs.

## Key Quotes

- "I literally cannot export anything from the dashboard. It's like the data is trapped behind glass."
- "We have no funnel visualization at all."
- "The lack of a funnel view is probably the single biggest gap in the product for me."
- "We need NPS tracking built into the dashboard, not as a nice-to-have but as a core metric."
- "When I try to filter by date range, sometimes it just doesn't apply."
- "If funnels, export, and reliable filters were in place, I'd probably cut that down to 30 minutes."

## Themes Identified

- Funnel visualization (critical)
- Export capability (critical)
- NPS tracking (high)
- Filter reliability (high)
