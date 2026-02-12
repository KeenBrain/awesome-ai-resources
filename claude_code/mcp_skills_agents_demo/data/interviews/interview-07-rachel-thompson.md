---
participant_id: P007
name: "Rachel Thompson"
role: "UX Designer"
company: "PixelForge"
segment: "pro"
date: "2025-02-05"
interviewer: "Research Team"
duration: "38 minutes"
---

# User Interview: Rachel Thompson

## Background

Rachel Thompson is a Senior UX Designer at PixelForge, a design tools company. She uses the analytics dashboard to track user behavior, validate design decisions, and identify usability issues. She has been on the platform for 4 months and is on the Pro plan. She brings a designer's perspective to data tooling and is particularly attentive to interaction patterns and information architecture.

## Interview Transcript

**Interviewer**: Rachel, welcome. Tell me how the dashboard fits into your design work.

**Rachel**: Thanks for having me. So as a UX designer, I use data to validate my design hypotheses. Did our redesign improve the conversion rate? Are users engaging with the new navigation? Where are they dropping off in a flow? The dashboard is where I go to answer these questions -- or try to, anyway.

**Interviewer**: What works well for you?

**Rachel**: The visual design of the dashboard itself is clean. The typography is good, the color palette is thoughtful. I can tell designers worked on it. The real-time data is great -- I love being able to see how a feature performs right after launch. And the basic time series charts are easy to read at a glance.

**Interviewer**: And what doesn't work?

**Rachel**: Filters. Specifically the date range picker. This is my number one frustration. **The date range picker is fundamentally broken from a UX perspective.** It's a dropdown with preset options -- "Last 7 days," "Last 30 days," "Last quarter" -- and a custom range option. The problem is that the custom range picker is nearly unusable.

**Interviewer**: Tell me more about what's wrong with the date range picker.

**Rachel**: Okay, so when you click "Custom range," you get a calendar popup. First issue: **the calendar popup opens behind other dashboard elements about 50% of the time, so you can't even see it.** You have to scroll or resize your window to find it. Second issue: when you select a start date, the calendar sometimes jumps to a completely different month for the end date selection, and you lose context of what you picked for the start date.

**Interviewer**: That sounds like a z-index issue plus some state management problems.

**Rachel**: Exactly. As a designer, I can diagnose these issues, which makes them even more frustrating because I know exactly what's wrong and how to fix them. **The date range picker needs to be a self-contained component with proper layering, clear visual feedback for the selected range, and persistent state.** Right now it feels like it was built as an afterthought.

**Interviewer**: How does the broken date picker affect your actual work?

**Rachel**: I do a lot of before/after analysis. We ship a design change, and I need to compare the two weeks before with the two weeks after. That requires a precise custom date range. **Every time I need to set a custom date range, I budget an extra 5 minutes for fighting with the date picker.** I click, it doesn't register. I select a range, the chart doesn't update. I refresh, the range resets. It's a three-step process that takes ten steps.

**Interviewer**: Beyond the date range picker, are there other filter issues?

**Rachel**: Yes. The filter bar in general has an interaction design problem. **There's no clear visual indication of which filters are currently active.** If I've applied a date filter and a segment filter, I have to click into each filter dropdown to see what's selected. There should be filter chips or tags visible at all times showing the active filters. It's a basic UX pattern that's missing.

**Interviewer**: That's a good observation. What else would you change about the interaction design?

**Rachel**: Chart type flexibility. I'm a visual thinker, and different chart types reveal different patterns. **The dashboard only offers line charts and bar charts, which limits the visual analysis I can do.** I can't create a heat map to see engagement by time of day. I can't do a scatter plot to explore correlation between two metrics. As a designer, I need visual variety to spot patterns.

**Interviewer**: Can you give me a concrete example?

**Rachel**: Sure. We recently redesigned our checkout flow and I wanted to see how conversion varies by day of week and time of day. A heat map would be perfect for this -- days on one axis, hours on the other, color intensity showing conversion rate. Instead, I got a line chart that shows conversion over time, which is useful but doesn't reveal the day/time patterns at all. **I ended up exporting data through the API -- which was a whole adventure -- and building a heat map in Figma using a plugin. A designer should not have to build analytical charts in a design tool because the analytics tool doesn't support them.**

**Interviewer**: You mentioned "exporting data through the API." So there's no simpler export option?

**Rachel**: Oh, that reminds me. **There is absolutely no export functionality in the UI.** I had to ask our developer to help me set up API scripts just to pull data out. For someone non-technical -- and most designers are not writing API scripts -- the data is completely locked inside the dashboard. I know other designers on my team who've simply given up on using the dashboard because they can't get data out to do anything useful with it.

**Interviewer**: Let's go back to the filter and date range issues. How critical are these for your workflow?

**Rachel**: Critical. Here's the thing about UX research and design validation: timing matters enormously. I need to compare precise time windows around design changes. **If the date range picker is unreliable, my before/after analysis is unreliable, which means my design decisions are based on unreliable data.** That's a chain reaction from a UI bug all the way to a product strategy error.

**Interviewer**: You bring a unique perspective as a designer evaluating a design tool. What's your overall assessment?

**Rachel**: The information architecture is decent -- the dashboard is organized logically. The visual design is good. But the interaction design has significant gaps. The filter UX is buggy and lacks affordances. The chart types are too limited for exploratory analysis. And the absence of export is baffling. **From a UX maturity standpoint, the dashboard looks polished but behaves like a prototype. The surface is great; the interactions underneath are unfinished.**

**Interviewer**: Have you provided this kind of design-focused feedback before?

**Rachel**: I submitted a detailed bug report about the date range picker two months ago with screenshots and a proposed fix. I got an auto-reply and nothing else. I also wrote up a short UX audit and sent it to support, highlighting the filter visibility issue and the chart type limitations. No response. **I'm a designer offering free UX consulting to your product team, and it's going into a black hole.** That's demoralizing.

**Interviewer**: Is there anything else about the onboarding or initial experience that stood out to you?

**Rachel**: Actually, yes. When I first signed up, **there was no guided onboarding at all. I was dropped into a fully loaded dashboard with no explanation of what anything meant or how to use the filters.** As a designer, I figured it out, but I've watched less technical teammates struggle for 20-30 minutes before they could do anything useful. A simple guided tour or contextual tooltips would make a huge difference for first-time users.

**Interviewer**: Interesting. Multiple participants have mentioned that. How would you design the onboarding?

**Rachel**: I'd do a three-step approach. First, a short welcome modal that explains the dashboard layout -- "Your metrics are here, filters are here, time range is here." Second, contextual tooltips that appear the first time you hover over a chart or filter, explaining what it does. Third, a sample view with annotated data so new users can see what a properly configured dashboard looks like. **Good onboarding isn't about lengthy tutorials. It's about reducing the cognitive load of the first interaction.** Show people what's possible and get out of the way.

**Interviewer**: If you had to pick your top three priorities for improvement, what would they be?

**Rachel**: Fix the date range picker and filter UX -- it's broken and it undermines trust in the data. Add more chart types -- at minimum scatter plot and heat map. And add basic export functionality. **Filters, charts, and export. Those three improvements would make this a tool I'd actually recommend to my design community.** Right now I wouldn't recommend it because I'd be setting people up for the same frustrations I experience.

**Interviewer**: Thank you, Rachel. This has been incredibly insightful, especially from a design perspective.

**Rachel**: Happy to help. And seriously, if your product team wants that UX audit I wrote, I'll send it again. I genuinely want to see these improvements happen.

## Key Quotes

- "The date range picker is fundamentally broken from a UX perspective."
- "The calendar popup opens behind other dashboard elements about 50% of the time."
- "Every time I need to set a custom date range, I budget an extra 5 minutes for fighting with the date picker."
- "There's no clear visual indication of which filters are currently active."
- "The dashboard only offers line charts and bar charts, which limits the visual analysis I can do."
- "There is absolutely no export functionality in the UI."
- "From a UX maturity standpoint, the dashboard looks polished but behaves like a prototype."
- "There was no guided onboarding at all. I was dropped into a fully loaded dashboard with no explanation."
- "Good onboarding isn't about lengthy tutorials. It's about reducing the cognitive load of the first interaction."

## Themes Identified

- Filter UX / Date range picker (critical)
- Chart type flexibility (high)
- Export capability (high)
- Better onboarding (medium)
