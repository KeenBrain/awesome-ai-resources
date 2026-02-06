# Marketecture Template

A marketecture is a marketing-oriented view of your system architecture. Unlike engineering architecture diagrams, marketectures are designed for customers, sales teams, and executives. They emphasize capabilities and value, not implementation details.

---

## [Product Name] — Architecture Overview

### One-Line Description

*What does this product do, in a sentence a VP of Ops would understand?*



---

### High-Level Diagram

*Create a clean visual showing the major capability layers. Use ASCII art or Mermaid diagram syntax.*

```
┌─────────────────────────────────────────────────────┐
│                 [Customer Touchpoint]                │
├─────────────────────────────────────────────────────┤
│                                                     │
│    ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│    │Capability │   │Capability │   │Capability │     │
│    │    1      │   │    2      │   │    3      │     │
│    └──────────┘   └──────────┘   └──────────┘     │
│                                                     │
├─────────────────────────────────────────────────────┤
│              [Intelligence / AI Layer]               │
├─────────────────────────────────────────────────────┤
│              [Security & Compliance]                 │
├─────────────────────────────────────────────────────┤
│              [Integrations & APIs]                   │
└─────────────────────────────────────────────────────┘
```

---

### Capability Layer Descriptions

*For each capability block, describe in customer language.*

| Capability | What It Does | Key Differentiator |
|------------|-------------|-------------------|
| | | |
| | | |
| | | |

---

### Integration Points

*What does this connect to? Show the ecosystem.*

| Integration | Type | Customer Value |
|------------|------|----------------|
| CRM (Salesforce, HubSpot) | API | |
| Analytics (Datadog, Mixpanel) | Webhook | |
| Phone Systems (Twilio, NICE) | SIP/API | |
| Identity (Okta, Azure AD) | SSO/SAML | |

---

### Security & Compliance Layer

*What makes enterprise buyers feel safe?*

- [ ] SOC 2 Type II
- [ ] Data encryption (at rest and in transit)
- [ ] Tenant isolation
- [ ] Audit logging
- [ ] Role-based access control
- [ ] Data residency options

---

### Narrative Description

*Write 2-3 paragraphs that a sales rep could drop into a proposal deck. Focus on outcomes, not technology. Avoid jargon.*



---

### Competitive Differentiators

*What makes your architecture better than alternatives? 2-3 things a customer would notice.*

1.
2.
3.

---

*Template version 1.0*
