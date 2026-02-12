---
participant_id: P005
name: "Elena Rodriguez"
role: "Customer Success Manager"
company: "HealthBridge"
segment: "pro"
date: "2025-01-28"
interviewer: "Research Team"
duration: "42 minutes"
---

# User Interview: Elena Rodriguez

## Background

Elena Rodriguez is a Customer Success Manager at HealthBridge, a healthcare SaaS platform. She manages a portfolio of 35 enterprise accounts and uses the analytics dashboard to monitor customer health, track satisfaction, and identify at-risk accounts. She has been on the platform for 10 months and is on the Pro plan. She is non-technical but data-savvy.

## Interview Transcript

**Interviewer**: Elena, thanks for joining us. Tell me about your role and how you use the analytics dashboard.

**Elena**: Of course. So my job is to keep our customers happy and growing. I manage 35 enterprise accounts, and for each one I need to understand their usage patterns, satisfaction levels, and whether they're trending toward renewal or churn. The dashboard is supposed to be my command center for all of that, but it's more like... a command center with half the screens blacked out.

**Interviewer**: That's a vivid description. What's blacked out?

**Elena**: NPS. It's the most important metric for customer success, and **it's completely absent from the dashboard. I live and die by NPS scores, but I have to go to a separate tool to see them.** Our NPS data is in Wootric, our usage data is in this dashboard, and I'm manually cross-referencing between the two. For 35 accounts. Every week.

**Interviewer**: Walk me through what that manual process looks like.

**Elena**: Every Monday morning, I export NPS scores from Wootric -- which at least has an export feature -- and then I open the dashboard and go through each account one by one to check their usage trends. Then I open a spreadsheet where I've built a manual health score model that combines both. **What should be a single dashboard view takes me about 3 hours every Monday.** I call it my "Monday morning misery."

**Interviewer**: What would the ideal NPS integration look like for you?

**Elena**: A widget on the dashboard that shows NPS score over time, with the ability to filter by account or segment. I want to see trending -- is this account's NPS going up or down? And I want to see it alongside their usage metrics on the same page. **If NPS scores were right there next to usage data, I could identify at-risk accounts in seconds instead of hours.** An account with declining usage AND declining NPS? That's a five-alarm fire that I'm currently blind to.

**Interviewer**: Have you ever missed a churn signal because of this gap?

**Elena**: Yes. Last quarter, one of our mid-market accounts churned. When I did the post-mortem, I found that their NPS had dropped from 45 to 15 over three months AND their usage had declined 40%. Both signals were there, but because they lived in different tools, I didn't see the combined picture until it was too late. **If NPS and usage had been on the same dashboard, I would have caught that account two months before they churned.** That's a $180,000 ARR account we lost.

**Interviewer**: That's a significant loss. Let's talk about other pain points. What else frustrates you?

**Elena**: Exporting data for Quarterly Business Reviews. I do QBRs with every account, and I need to pull usage data into a presentation. **There's no way to export charts or data from the dashboard. I'm taking screenshots and cropping them in Preview.** For a professional QBR with an enterprise customer, pasting screenshots into a deck feels amateur. My customers have noticed.

**Interviewer**: They've actually commented on it?

**Elena**: One of my accounts' VP of Operations said, and I quote, "Do you not have a proper reporting tool?" when I showed him a slide with a cropped screenshot that still had the browser tab visible. I wanted to disappear. **I need to be able to export clean, professional-looking charts and data summaries for customer-facing presentations.** It's not just an internal inconvenience -- it affects how our customers perceive us.

**Interviewer**: What formats would be most useful for your QBRs?

**Elena**: PDF of the full dashboard view, filtered to that specific account, would be the dream. Short of that, PNG exports of individual charts that I can drop into a deck. And CSV for when a customer's data team wants the raw numbers. **I'd use PDF export probably 35 times a quarter -- once per QBR -- and PNG exports probably 100+ times a quarter across all my prep work.**

**Interviewer**: Let's discuss filtering. How do you filter data for individual accounts?

**Elena**: This is where I want to scream. I manage 35 accounts. I need to filter the dashboard to show one account at a time. **The account filter works maybe 70% of the time. The other 30%, I select an account and the data either doesn't change or shows a different account's data.** I've learned to always verify by checking a known metric for the account before trusting the filtered view.

**Interviewer**: How did you discover the filter wasn't working correctly?

**Elena**: The hard way. I was preparing a QBR for a large hospital system. I filtered to their account, pulled the numbers, and built my slides. During the actual QBR, their data analyst pointed out that one of the charts didn't match their internal tracking. I went back and checked, and the filter had silently failed -- I was showing data from a different account. **I had to apologize to a major enterprise customer for showing them incorrect data. That's not just embarrassing -- it erodes trust.**

**Interviewer**: That sounds incredibly stressful.

**Elena**: It was. And now I spend extra time double-checking every filtered view, which adds probably 30 minutes to every QBR prep session. **I need filters to be 100% reliable. Not 70%, not 95%. One hundred percent. When I select an account, I need absolute certainty that I'm looking at that account's data.** In customer success, presenting wrong data is worse than presenting no data.

**Interviewer**: Are there other filtering issues beyond account selection?

**Elena**: Date range filtering is also unreliable. I need to show trends over the last quarter for QBRs, and **the date range picker sometimes resets to a different range when I switch between dashboard tabs.** So I'll set "October 1 to December 31," navigate to the engagement tab, and the date range has silently changed back to "Last 30 days." It's the kind of subtle bug that you don't notice until you've already built a slide with wrong data.

**Interviewer**: How do these issues affect your overall effectiveness?

**Elena**: I'll be honest -- they make me less effective at my job. Customer success is a proactive role. I should be spending my time building relationships, identifying expansion opportunities, and preventing churn. Instead, **I spend probably 40% of my dashboard time on workarounds and verification rather than actual analysis.** That's time I'm not spending with customers.

**Interviewer**: If you could have three wishes for the dashboard, what would they be?

**Elena**: NPS integration -- native, built-in, trending over time. Reliable export -- PDF, PNG, CSV, all respecting current filters. And rock-solid filters that work every single time. **Those three things would literally transform my Monday from a 3-hour data wrestling session into a 30-minute strategic review.** I'd be more effective, my customers would get a better experience, and I'd probably prevent at least one churn per quarter.

**Interviewer**: How confident are you in that churn prevention estimate?

**Elena**: Very. The account we lost last quarter? If I'd had NPS alongside usage on one dashboard, I would have flagged it immediately. That's $180K. Over a year, preventing even two churns like that is $360K in retained revenue. **The ROI of building NPS into the dashboard isn't theoretical -- I can point to real accounts we've lost because the data was siloed.**

**Interviewer**: Is there anything else you'd like to share?

**Elena**: Just that I feel like the dashboard is so close to being what I need. The usage data is good, the account-level views are conceptually right, and the real-time updates are helpful. **But without NPS, without export, and without reliable filters, I'm only getting about 60% of the value I should be getting.** That last 40% is the difference between a tool I tolerate and a tool I depend on.

**Interviewer**: That's great feedback, Elena. Thank you so much.

**Elena**: Thank you. And please -- the NPS thing. It's not just a nice feature for customer success teams. It's existential. We can't do our jobs without it.

## Key Quotes

- "NPS is completely absent from the dashboard. I live and die by NPS scores, but I have to go to a separate tool to see them."
- "If NPS scores were right there next to usage data, I could identify at-risk accounts in seconds instead of hours."
- "If NPS and usage had been on the same dashboard, I would have caught that account two months before they churned."
- "There's no way to export charts or data from the dashboard. I'm taking screenshots and cropping them in Preview."
- "The account filter works maybe 70% of the time."
- "I had to apologize to a major enterprise customer for showing them incorrect data."
- "The date range picker sometimes resets to a different range when I switch between dashboard tabs."
- "Those three things would literally transform my Monday from a 3-hour data wrestling session into a 30-minute strategic review."

## Themes Identified

- NPS tracking (critical)
- Export capability (critical)
- Filter reliability (critical)
