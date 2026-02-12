---
name: manage-linear-tickets
description: "Create or update Linear tickets for the top prioritized features with RICE scores, evidence, and acceptance criteria."
triggers:
  - "manage linear tickets"
  - "create linear tickets"
  - "update linear tickets"
---

# Manage Linear Tickets

Create or update Linear tickets for the top prioritized features.

## Instructions

1. **Read the prioritization report** from `output/prioritized-features.md`.

2. **For the top 5 features**, for each one:

   a. **Search Linear** for existing tickets that match the feature (search by title keywords in the `Keenbrain` team).

   b. **If a matching ticket exists**: Update it with the latest RICE score, evidence, and implementation notes. Add a comment with the new analysis.

   c. **If no matching ticket exists**: Create a new ticket in the `Keenbrain` team with:
      - **Title**: Clear, actionable (e.g., "Implement funnel visualization chart")
      - **Assignee**: "me" (assign to the current user)
      - **State**: "Todo"
      - **Description** (markdown):
        ```
        ## Summary
        [1-2 sentence description]

        ## RICE Score: [X.X]
        - Reach: [X] — [justification]
        - Impact: [X] — [justification]
        - Confidence: [X] — [justification]
        - Effort: [X] — [justification]

        ## Evidence
        ### User Interviews
        [Key quotes and participant references]

        ### Analytics Data
        [Key metrics and findings]

        ## Implementation
        **Files to modify**: [list]
        **Approach**: [brief description]

        ## Acceptance Criteria
        - [ ] [Specific criteria 1]
        - [ ] [Specific criteria 2]
        - [ ] [Specific criteria 3]
        ```
      - **Priority**: Based on RICE rank (1=Urgent for top, 2=High for 2-3, 3=Normal for 4-5)
      - **Labels**: Add relevant labels if they exist (e.g., "feature", "user-feedback")

   d. **After creating each ticket**, explicitly update its status to "Todo" using `update_issue` with `state: "Todo"`, since the create API defaults to Backlog.

3. **Log all actions** to `output/linear-tickets-log.md`:

```markdown
# Linear Tickets Log
Generated: [timestamp]

## Tickets Created/Updated

| # | Feature | Action | Ticket ID | Priority | Status |
|---|---------|--------|-----------|----------|--------|
| 1 | [name] | Created/Updated | [ID] | [priority] | [status] |

## Ticket Details

### [Feature Name]
- **Action**: Created new / Updated existing
- **Ticket**: [identifier with URL]
- **Priority**: [level]
- **Key evidence included**: [brief]
```

4. **Verify** all tickets were created/updated successfully.
