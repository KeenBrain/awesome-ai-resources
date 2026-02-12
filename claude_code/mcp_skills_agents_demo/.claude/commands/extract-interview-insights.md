# Extract Interview Insights

Analyze all user interview transcripts and extract actionable product insights.

## Instructions

1. **Read all interview files** in `data/interviews/` using the filesystem MCP or by reading each `.md` file directly.

2. **For each interview**, extract:
   - Participant metadata (from YAML frontmatter)
   - Key pain points and frustrations
   - Feature requests (explicit and implied)
   - Direct quotes that support each finding
   - Severity assessment (critical / high / medium / low)

3. **Cross-reference across all interviews** to identify:
   - Recurring themes (mentioned by 2+ participants)
   - Theme frequency (how many participants mentioned it)
   - Strongest supporting quotes for each theme
   - Segment patterns (do certain roles/segments share frustrations?)

4. **Write the output** to `output/interview-insights.md` with this structure:

```markdown
# Interview Insights Report
Generated: [timestamp]
Interviews analyzed: [count]

## Executive Summary
[2-3 sentence overview of top findings]

## Recurring Themes (ranked by frequency)

### 1. [Theme Name] — Mentioned by [N] participants
**Severity**: [Critical/High/Medium/Low]
**Participants**: [names]
**Summary**: [1-2 sentences]
**Key Quotes**:
- "[quote]" — [Name], [Role]
- "[quote]" — [Name], [Role]
**Mapped Component**: [file name if applicable]

[Repeat for each theme...]

## Individual Interview Summaries
### [Participant Name] — [Role]
- **Top concerns**: [list]
- **Notable quotes**: [list]

## Segment Analysis
[Any patterns by role/segment]
```

5. **Verify** the output file was written successfully.
