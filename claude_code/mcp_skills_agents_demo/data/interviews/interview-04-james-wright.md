---
participant_id: P004
name: "James Wright"
role: "VP of Engineering"
company: "CloudNine Technologies"
segment: "enterprise"
date: "2025-01-25"
interviewer: "Research Team"
duration: "35 minutes"
---

# User Interview: James Wright

## Background

James Wright is VP of Engineering at CloudNine Technologies, a cloud infrastructure company with 200+ employees. He oversees engineering teams and uses the analytics dashboard primarily for tracking engineering productivity metrics, release velocity, and platform health. He has been on the platform for 14 months and is on the Enterprise plan. He accesses the dashboard from both desktop and mobile.

## Interview Transcript

**Interviewer**: James, thanks for fitting this in. I know your schedule is packed. Can you describe how the analytics dashboard fits into your engineering leadership workflow?

**James**: Sure. I use it in two modes. Mode one is the daily check-in -- I glance at it every morning to see platform health, error rates, deployment frequency. Mode two is the weekly and monthly reporting -- I pull metrics for my engineering review and for the exec team. The daily mode works okay. The reporting mode is where I run into walls.

**Interviewer**: Let's talk about those walls. What's the biggest one?

**James**: Funnel visibility across our platform. We're a developer tools company, so our "funnel" is: developer signs up, creates a project, deploys their first app, invites team members, and then converts to paid. I need to see that progression and where we lose developers. **We have zero funnel visualization capability. I can see how many developers signed up and how many converted, but the middle of the journey is a complete black box.**

**Interviewer**: How does that affect your engineering decisions?

**James**: Directly. If I knew that 60% of developers drop off at the "first deployment" stage, I'd prioritize simplifying that flow. If the drop-off is at team invitation, I'd focus on collaboration features. But without a funnel view, I'm guessing. **My engineering roadmap should be driven by funnel data, but instead it's driven by intuition because we can't visualize the funnel.**

**Interviewer**: Have you tried to build this internally?

**James**: We spent a sprint building a custom funnel dashboard using Redash. It works, but it's another tool to maintain, and the data doesn't perfectly match what we see in the main dashboard. I don't want my engineers spending time building internal tools when there's a product that should provide this. **Every sprint we spend maintaining our custom funnel dashboard is a sprint we're not spending on our actual product.**

**Interviewer**: You mentioned accessing the dashboard on mobile. How's that experience?

**James**: Terrible. Just terrible. I'm often in back-to-back meetings, and I'll pull up the dashboard on my phone to quickly check a metric before walking into a room. **The mobile experience is essentially unusable. Charts overlap, text gets cut off, and half the interactive elements don't work on touch.** I've given up trying to use filters on mobile entirely -- the dropdowns are too small to tap accurately.

**Interviewer**: Can you give me a specific situation where the mobile experience failed you?

**James**: Last Tuesday. I was about to walk into a board meeting and wanted to check our latest deployment metrics. Pulled up the dashboard on my iPad. The charts were rendering at desktop width inside a mobile viewport, so everything was tiny and I had to pinch-zoom constantly. **The charts aren't responsive at all -- they're just shrunk-down desktop views crammed onto a mobile screen.** I couldn't read the axis labels. I ended up asking my EA to pull the numbers on her laptop and text them to me. That's not a workflow. That's a workaround.

**Interviewer**: How often do you try to use the dashboard on mobile?

**James**: I've mostly stopped, which is the problem. I'd use it on mobile probably 3-4 times a day if it worked. Quick checks between meetings, glancing at it during lunch, checking weekend metrics from the couch on Sunday night. **The mobile use case isn't "nice to have" for an exec -- it's how I stay connected to the data when I'm not at my desk, which is most of the day.** I'm in meetings 6 hours a day. My phone is the only screen I have access to half the time.

**Interviewer**: Beyond mobile, what other issues affect your workflow?

**James**: Performance. **The dashboard loads incredibly slowly. I've clocked it at 12-15 seconds for the initial page load.** For my daily morning check-in, that means I'm staring at a loading spinner for 15 seconds before I can see anything. It doesn't sound like much, but when you're trying to quickly check numbers before a meeting starts in 2 minutes, 15 seconds of loading feels like an eternity.

**Interviewer**: Is the slowness consistent?

**James**: It's worst during business hours, which is exactly when I need it most. Early mornings and evenings it's a bit faster, maybe 6-8 seconds. But during the workday, especially around 10 AM when everyone's checking dashboards, **it regularly takes over 10 seconds to load. I've actually started keeping a browser tab permanently open just to avoid the reload time,** but then the data gets stale and I have to refresh anyway, which takes just as long.

**Interviewer**: How does the slow performance affect your team's usage?

**James**: My engineering managers have largely stopped using it for real-time monitoring. They built a simple Grafana dashboard for the stuff they need to check frequently because it loads in under a second. **We're paying for an enterprise analytics platform that our engineers bypass in favor of a free tool because the free tool is faster.** That tells you something about how critical load time is.

**Interviewer**: Going back to the funnel topic -- what would an ideal funnel view look like for your use case?

**James**: I want to define a sequence of events: signup, project creation, first deploy, team invite, paid conversion. I want to see the volume at each stage and the drop-off rate between stages. I want to break it down by time period -- did our onboarding changes last month improve the signup-to-first-deploy conversion? **Ideally, I'd see a funnel chart that I can overlay with release dates so I can directly see the impact of engineering changes on user conversion.**

**Interviewer**: That's an interesting use case -- correlating engineering releases with funnel performance.

**James**: Exactly. That's the holy grail for an engineering leader. I ship a feature or fix a bug, and I want to see if it moved the needle. Right now I have to eyeball it by comparing dates in my head. **A funnel visualization with time-based comparison would let me prove the ROI of engineering investments to the board. Right now, that story is told with hand-waving and anecdotes.**

**Interviewer**: Speaking of the board -- how do you present dashboard data to your board?

**James**: Badly. [laughs] I screenshot charts on my laptop -- can't do it on mobile because of the rendering issues -- paste them into Keynote, and add manual annotations. **Between the slow load times, the missing funnel view, and the broken mobile experience, preparing for a board meeting takes me about 2 hours of dashboard wrestling.** If the dashboard loaded fast, had funnels, and worked on mobile, I could prepare in 20 minutes.

**Interviewer**: Let's talk about your team's engineers. Do they use the dashboard?

**James**: Some do, for specific metrics. But the performance issues have really hurt adoption. My platform team lead tried to use it as a real-time monitoring tool during an incident last month. She said **the slow load time made it useless for incident response -- by the time the dashboard loaded, she'd already found the problem through the CLI.** We need sub-second load times for it to be useful in high-urgency situations.

**Interviewer**: If you prioritize your needs, what's the ranking?

**James**: Funnel visualization is number one because it directly impacts my roadmap decisions. Mobile responsiveness is number two because I'm away from my desk most of the day. Load time improvement is number three because it affects daily usability for my whole team. Everything else is secondary.

**Interviewer**: Any other thoughts?

**James**: One more thing about mobile. **I don't need the full desktop experience on mobile. I'd be happy with a simplified mobile view -- top 5 metrics, a funnel summary, and the ability to drill into one chart at a time.** Don't try to shrink the whole desktop dashboard onto a phone. Give me a purpose-built mobile experience. That's what separates good products from great ones.

**Interviewer**: Really valuable perspective, James. Thanks for your candor.

**James**: Happy to help. I want this product to succeed because switching costs are real, and I'd rather you fix these issues than force me to evaluate alternatives.

## Key Quotes

- "We have zero funnel visualization capability... the middle of the journey is a complete black box."
- "My engineering roadmap should be driven by funnel data, but instead it's driven by intuition."
- "The mobile experience is essentially unusable. Charts overlap, text gets cut off."
- "The charts aren't responsive at all -- they're just shrunk-down desktop views crammed onto a mobile screen."
- "The dashboard loads incredibly slowly. I've clocked it at 12-15 seconds for the initial page load."
- "We're paying for an enterprise analytics platform that our engineers bypass in favor of a free tool because the free tool is faster."
- "A funnel visualization with time-based comparison would let me prove the ROI of engineering investments to the board."

## Themes Identified

- Funnel visualization (critical)
- Slow load times (high)
- Mobile responsiveness (high)
