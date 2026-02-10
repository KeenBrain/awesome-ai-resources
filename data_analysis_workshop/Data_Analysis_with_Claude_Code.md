# Data Analysis with Claude Code

*A Step-by-Step Workshop Guide*

---

## Overview

This guide walks you through a complete data analysis workflow using Claude Code, the command-line AI coding tool from Anthropic. You'll set up a Python project from scratch, then use a series of natural language prompts to explore, analyze, and visualize a real dataset — all from your terminal.

The guide is divided into two parts:

- **Part A: Project Setup** — creating a reproducible Python project with modern tooling
- **Part B: Analysis Prompts** — a methodical series of prompts that guide Claude Code through a complete analysis

### The Dataset

We'll be working with a synthetic SaaS product usage dataset:

| | |
|---|---|
| **Dataset** | saas_product_usage.csv |
| **Records** | ~25,000 rows of SaaS product usage data |
| **Time Period** | February 1 – March 1, 2024 (30 days) |
| **Columns** | date, user_id, plan_type, feature_used, session_duration_min, actions_taken, country, device |

---

## Part A: Project Setup

Before we start analyzing data, we need to set up a clean Python project. This section uses uv, a modern Python package manager, to create a reproducible environment. If you're following along in a live demo, the presenter may skip ahead to Part B with a pre-built project.

### Step 1: Create the Project Directory

```
mkdir data_analysis_workshop
cd data_analysis_workshop
```

This creates a new empty folder for your project and moves your terminal into it. All subsequent commands will run inside this directory.

### Step 2: Initialize the Project with uv

```
uv init
```

> **What is uv?** uv is a fast Python package and project manager made by Astral (the team behind the ruff linter). It replaces pip, virtualenv, and manual pyproject.toml setup with a single, fast tool.

This command creates the following files:

- **pyproject.toml** — the project's configuration file. It defines the project name, Python version, and tracks dependencies. Think of it as the recipe card for your project.
- **.python-version** — pins which Python version the project uses, so anyone working on it gets the same one.
- **main.py** — a starter Python file (usually just a hello world).
- **.gitignore** — tells Git which files to skip when tracking changes (virtual environments, cache files, etc.).
- **.git/** — initializes a Git repository so your project is version-controlled from the start.

### Step 3: Add Data Analysis Libraries

```
uv add pandas numpy matplotlib statsmodels
```

> **What does uv add do?** It installs Python packages and records them in your pyproject.toml. It also automatically creates a virtual environment (an isolated space for your project's packages so they don't conflict with other projects) and a uv.lock file (which pins exact versions for reproducibility).

Here's what each library does:

- **pandas** — the workhorse for loading, cleaning, and analyzing tabular data. Think spreadsheets in Python.
- **numpy** — numerical computing with fast array operations and math functions. Pandas is built on top of it.
- **matplotlib** — the standard plotting library for creating charts and visualizations.
- **statsmodels** — statistical modeling and testing: regression analysis, hypothesis tests, time series tools.

### Step 4: Create a Data Directory

```
mkdir data
```

This creates a data/ folder to store your datasets. Keeping code and data separated is a common convention that makes projects easier to navigate and share.

### Step 5: Add Your Dataset

Copy the CSV file into the data directory:

```
cp /path/to/saas_product_usage.csv data/
```

Your project should now look like this:

```
data_analysis_workshop/
├── data/
│   └── saas_product_usage.csv
├── pyproject.toml
├── main.py
└── .python-version
```

### Step 6: Start Claude Code

From your project directory, launch Claude Code:

```
claude
```

Claude Code starts an interactive session in your terminal. It can see your project files, run Python scripts, install packages, and respond to natural language prompts. You're now ready to analyze data.

---

## Part B: Analysis Prompts

The prompts below follow a structured methodology that mirrors how an experienced data analyst works: start broad, verify quality, segment the data, hunt for anomalies, then verify the findings. Each prompt builds on the previous one.

> **How Claude Code differs from Claude.ai:** In Claude Code, you don't upload files — Claude already has access to your project directory. It writes and executes real Python scripts, which you can inspect, modify, and rerun. The code and outputs are saved in your project, making your analysis fully reproducible.

### Before You Begin

Type this instruction at the start of your Claude Code session, before running any analysis prompts. It constrains Claude's output to keep responses fast and focused:

```
For all analysis in this session: write concise scripts, print only key numbers and tables (no full dataframes), and keep your explanations to 2-3 sentences per finding.
```

### Prompt 1: Understand the Shape of the Data

```
Load the CSV file in data/saas_product_usage.csv and give me an overview. How many rows and columns? What are the data types? Show me the first few rows.
```

**Why this first?** Before any analysis, you need to understand what you're looking at. This prompt gets Claude to load the data, show its dimensions, and display sample rows so you can orient yourself.

**What to look for:** Column names, data types (numeric vs. categorical), the date range, and how the data is structured (one row per session, per user, per day?).

### Prompt 2: Check Data Quality

```
Are there any missing values, duplicates, or data quality issues? Check for anything that could affect our analysis.
```

**Why this matters:** Dirty data leads to wrong conclusions. This prompt catches problems early — missing values, impossible numbers, duplicate records — before they silently distort your results.

**What to look for:** Null counts per column, duplicate rows, values that seem out of range (e.g., negative session durations or impossibly high action counts).

### Prompt 3: Get Summary Statistics

```
Give me summary statistics for the numerical columns, broken down by plan type (Free, Pro, Enterprise). What stands out?
```

**Why segment by plan?** Averages across the whole dataset can hide important differences. Breaking down by plan type reveals whether Free users behave fundamentally differently from Enterprise users.

**What to look for:** Differences in session duration, actions per session, and how the spread (standard deviation) compares across plan types.

### Prompt 4: Detect Anomalies

```
Are there any users with suspiciously high activity that might be bots? Are there any other anomalies or outliers in the data?
```

**Why look for anomalies?** Outliers can be the most interesting part of a dataset — or they can be data errors that skew your analysis. Either way, you need to find them.

**What to look for:** Users with extremely high action counts but short sessions (possible bots), unusual spikes in specific features, or geographic anomalies.

### Prompt 5: Verify a Claim

```
Pick the most important numerical claim from your analysis and show me the exact calculation. Walk me through the code step by step.
```

> **Why verification matters:** AI can make mistakes — subtle calculation errors, misinterpreted columns, or aggregation bugs. Building a habit of spot-checking key claims is essential for trustworthy analysis. In Claude Code, you can inspect the generated Python script directly to verify the logic.

**What to look for:** Does the code match the claim? Are the filters correct? Is the aggregation (mean vs. median, count vs. distinct count) appropriate?

---

## Tips for Working with Claude Code

1. **Be specific about file paths.** Claude Code works from your project directory. Reference files as `data/saas_product_usage.csv`, not by uploading them.
2. **Iterate and follow up.** Don't just accept the first answer. Say "dig deeper," "why is that?," or "can you break that down by plan type?" The conversation is the analysis.
3. **Inspect the code.** Claude Code generates real Python scripts. Read them. Modify them. Rerun them. This is how you learn and how you catch mistakes.
4. **Ask for visualizations explicitly.** Claude Code can create and save charts as image files in your project. Ask for them when a visual would communicate better than numbers.
5. **Always verify key claims.** Use Prompt 5 as a habit, not just a bonus step. Trust but verify.

---

## Discussion Questions

1. What insights would you present to stakeholders based on this analysis?
2. Which findings would you want to verify before acting on them?
3. Did Claude miss anything obvious? Did it find anything surprising?
4. How would you adapt this workflow for your own datasets and projects?
