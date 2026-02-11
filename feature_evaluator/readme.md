# Build a Feature Evaluation App with Claude

A step-by-step prompt guide for product managers. No coding experience required.

---

## What You're Building

A browser-based tool that helps product teams prioritize features using a 2x2 matrix — one of the most widely used frameworks in product management. You score each feature on two dimensions:

- **Interesting** — How novel, exciting, or innovative is this feature?
- **Valuable** — How much impact does it deliver to users or the business?

Those scores place each feature into one of four quadrants:

| | Low Value | High Value |
|---|---|---|
| **High Interest** | **Science Projects** — Fun to build, hard to justify | **Strategic Bets** — Novel AND needed. Prioritize. |
| **Low Interest** | **Pass** — Skip entirely | **Workhorses** — Boring but important. Don't overlook. |

The app uses a Fibonacci scoring scale (1, 2, 3, 5, 8, 13) instead of a simple 1–10 range. The reasoning: with a linear scale, people tend to cluster everything around 6–8 and avoid the extremes. Fibonacci's non-linear gaps — especially the jumps from 3→5 and 8→13 — force you to make a real commitment every time you move the slider up. A "5" means something fundamentally different from a "3" in a way that a "6" never really felt different from a "7."

The finished app is a single HTML file. No server, no database, no installs. Double-click it to open in any browser.

---

## What You'll Need

1. **Claude** — Go to [claude.ai](https://claude.ai) and start a new conversation
2. **A web browser** — Chrome, Safari, Firefox, Edge — anything works
3. **The 2x2 grid reference image** — Either screenshot the grid from an existing template or describe it in words (the prompts below cover both approaches)

That's it. You don't need to know HTML, CSS, JavaScript, or any programming language. Claude writes all the code. You just tell it what you want.

---

## Step-by-Step Prompts

Below are the exact prompts to paste into Claude, in order. After each one, you'll find an explanation of why the prompt works, what to expect, and how to respond if Claude asks follow-up questions.

---

### Step 1: Set the Context

**Copy and paste this into Claude:**

```
We're going to create a new app to help product managers evaluate features.
The app is a simple 2x2 grid. The Y axis is "Interesting" (low to high) and
the X axis is "Valuable" (low to high). The four quadrants are:

- Top-left: "Science Projects" — Fun to build, hard to justify
- Top-right: "Strategic Bets" — Novel AND needed. Prioritize.
- Bottom-left: "Pass" — Skip entirely
- Bottom-right: "Workhorses" — Boring but important. Don't overlook.

The app should allow product managers to score each feature using a simple
set of controls. The app should be all front-end (tailwind, html, etc.)
in a single HTML file.
```

**Why this prompt works:** You're giving Claude three things it needs upfront — the visual layout (2x2 grid with labeled quadrants), the interaction model (scoring controls), and the technical constraints (single HTML file, Tailwind CSS). Being specific about the quadrant names and descriptions means the AI doesn't have to guess at your framework.

**What to expect:** Claude will likely ask you a couple of clarifying questions before it starts building. Here's how to answer them:

- **"How should PMs score features?"** — Choose **sliders**. They're the most intuitive input for a spectrum like "low to high." Each feature gets two sliders: one for Interesting, one for Valuable.
- **"Should it support multiple features?"** — Choose **yes, multiple features**. The whole point is to compare features against each other on the same grid. A single-feature version wouldn't be very useful for prioritization.

After you answer, Claude will generate the complete HTML file. Save it to your computer and open it in a browser to verify it works.

---

### Step 2: Move the Controls Below the Grid

**Copy and paste this into Claude:**

```
Let's put the slider controls underneath the output
```

**Why this prompt works:** The first version probably places the input controls on the left side with the grid on the right. That's a common default layout, but it buries the most important thing — the grid itself — in a two-column view. By moving controls underneath, you're making the grid the hero of the page. Product managers will spend most of their time looking at the grid, not the sliders, so it should dominate the screen.

**What to expect:** Claude will restructure the layout so the 2x2 grid takes full width at the top. The "Add a Feature" form and the feature list will sit side by side below it. Save the updated file and refresh your browser.

---

### Step 3: Switch to Fibonacci Scoring

**Copy and paste this into Claude:**

```
Let's change the sliders so that they are on the fibonacci sequence going
from 1, 2, 3, 5, 8, 13. This way the changes really feel like they have
some significance.
```

**Why Fibonacci matters:** This is the single most important design decision in the app. Here's the reasoning:

With a standard 1–10 scale, people fall into a trap. They score almost everything between 5 and 8. The differences feel arbitrary — is this feature a 6 or a 7? Nobody really knows, and the resulting grid becomes a crowded mess in the upper-right quadrant where nothing is meaningfully differentiated.

The Fibonacci sequence solves this by making each step feel progressively more consequential:

- **1 → 2** is a small bump. Fine.
- **2 → 3** is still incremental. No big deal.
- **3 → 5** is where it gets real. You're jumping past 4 entirely. You're saying "this isn't just somewhat interesting — it's meaningfully interesting."
- **5 → 8** is a major commitment. You're separating the good from the great.
- **8 → 13** is reserved for the truly exceptional. If you score something a 13, you're putting your reputation behind it.

This is the same principle used in agile story point estimation — and for the same reason. It forces honest prioritization by making the cost of over-scoring feel real.

**What to expect:** Claude will replace the 1–10 sliders with a 6-step Fibonacci scale. Each slider snaps to discrete values (1, 2, 3, 5, 8, 13) with tick marks underneath. The quadrant boundary will be set at the 3/5 threshold — features scored 5 or above on an axis land in the "high" zone for that dimension. Save and refresh.

---

### Step 4: Add Sharing

**Copy and paste this into Claude:**

```
Now create a share button to allow me to share this with my colleagues.
```

**Why this prompt works:** A prioritization tool is only useful if the whole team can see the results. Since the app is a static HTML file with no backend, the sharing mechanism needs to be clever. The best approach is to encode the feature data directly into the URL.

**What to expect:** Claude will ask how you want sharing to work. Choose **"Shareable URL with data."** Here's what happens behind the scenes:

- When you click the Share button in the header, the app takes all your features and scores and encodes them into the URL hash (the part after the `#`).
- That URL gets copied to your clipboard automatically.
- When a colleague opens the same HTML file and navigates to that URL, the app reads the hash and pre-populates the grid with your exact features.

No server, no database, no login. The data lives in the URL itself. The only requirement is that your colleague has the same HTML file — just send it along with the link, or host it on any internal web server.

---

## Using the Finished App

1. **Open the HTML file** in any browser by double-clicking it
2. **Type a feature name** in the input field (e.g., "Dark Mode", "SSO Integration")
3. **Set the Interesting score** using the slider — it snaps to 1, 2, 3, 5, 8, or 13
4. **Set the Valuable score** on the second slider
5. **Click "Add to Grid"** — the feature appears as a colored dot on the matrix
6. **Keep adding features** — each one gets a unique color so you can tell them apart
7. **Review the grid** — features in the top-right (Strategic Bets) quadrant deserve the most attention
8. **Remove a feature** by hovering over it in the list and clicking the ✕ button
9. **Share your grid** by clicking the Share button — the URL is copied to your clipboard
10. **Clear everything** with the Clear All button in the header to start fresh

---

## Going Further: Additional Prompts

Once you have the base app working, here are optional prompts to extend it. Use whichever ones are relevant to your workflow.

### Export to CSV
```
Add a button that exports all scored features as a CSV file with columns
for Feature Name, Interesting Score, Valuable Score, and Quadrant.
```
Useful for importing into spreadsheets, sharing with leadership, or feeding into other tools.

### Drag-and-Drop Repositioning
```
Let me drag feature dots around the grid to adjust their scores visually.
Update the slider values to match the new position.
```
Good for workshops where you want a more tactile, whiteboard-like experience.

### Category Tags
```
Add an optional category dropdown when adding a feature (e.g., UX,
Performance, Revenue, Retention) and color-code the dots by category
instead of assigning random colors.
```
Helps you spot patterns — e.g., "all our UX features are Workhorses" or "Revenue features cluster in Strategic Bets."

### Team Voting
```
Add the ability for multiple people to score the same feature. Show the
average score on the grid and display the spread of individual votes.
```
Turns the tool into a lightweight team alignment exercise. Disagreements on a score become visible and discussable.

### Custom Brand Colors
```
Change the color scheme to use our brand colors. The primary accent
should be [your hex code] and the secondary should be [your hex code].
```
Handy if you're presenting to stakeholders and want the tool to look polished and on-brand.

---

## Prompting Tips

A few principles that will help you get better results from Claude (or any AI assistant) when building tools like this:

**Be specific, not vague.** "Make it look better" is hard for an AI to act on. "Increase the quadrant label font size to 24px and add more padding inside each quadrant" is easy. Specificity is kindness.

**Iterate one change at a time.** Each prompt should do one thing. If you ask for three changes at once and something breaks, you won't know which one caused it. Small prompts, frequent saves, quick tests.

**Name things the way the app names them.** Refer to "Strategic Bets" and "Workhorses" instead of "the top-right box" and "the bottom-right box." Refer to "the Interesting slider" not "the first slider." Shared vocabulary reduces misunderstandings.

**Upload screenshots when words fall short.** If you see a bug, a layout you don't like, or a design you want to match, take a screenshot and upload it. An image is often more precise than a paragraph of description.

**Save working versions.** Before each new prompt, save a copy of the HTML file (e.g., `feature-evaluator-v2.html`). If a change goes wrong, you can always go back to the last version that worked.

---

## Summary

| Step | Prompt | What It Does |
|------|--------|--------------|
| 1 | Describe the 2x2 grid and requirements | Generates the base app with sliders and multi-feature support |
| 2 | "Put the slider controls underneath the output" | Makes the grid the visual hero of the page |
| 3 | "Change sliders to Fibonacci (1, 2, 3, 5, 8, 13)" | Forces meaningful scoring distinctions |
| 4 | "Create a share button" | Encodes feature data into a shareable URL |

Four prompts. One HTML file. A fully functional prioritization tool your team can use immediately.
