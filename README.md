# sber-merchant-onboarding-pack

## Overview

This repository contains the internal operating pack for merchant onboarding with **Sberbank** (Russia) via the DukPay PSP structure. It provides standardised documentation, process guidance, templates, and automation scripts to ensure a consistent, auditable, and scalable onboarding workflow.

This pack was created in response to Sberbank's request to systematise our merchant submission process and eliminate fragmented, email-based operations.

---

## Goal

To establish a single source of truth for all Sberbank merchant registrations — eliminating duplicate submissions, ensuring each merchant has exactly one Merchant ID and one login, and enabling clear tracking of onboarding status from initiation through to bank approval.

---

## Onboarding Model Summary

- DukPay acts as the PSP and is responsible for submitting sub-merchant information to Sberbank for registration.
- Each merchant entity is registered **once**, under a single Merchant ID and a single login.
- If a merchant operates both a website and a mobile application, both channels are registered under the same merchant entity — not as two separate registrations.
- Merchants are submitted to Sberbank in **batches**, twice per week (Tuesday and Friday).
- All onboarding activity is tracked in the **central merchant registry**, which is the single authoritative record of all registrations.

---

## Repository Contents

```
sber-merchant-onboarding-pack/
├── README.md                          # This file
├── docs/
│   ├── merchant_onboarding_guide.md   # Full internal process guide
│   ├── merchant_onboarding_checklist.md # Pre-batch operational checklist
│   ├── process_flow.md                # Step-by-step process with Mermaid flowchart
│   ├── email_templates.md             # Standard email templates for all scenarios
│   ├── decision_log.md                # Record of key operational decisions
│   └── change_log.md                  # Version history of this repository
├── templates/
│   ├── merchant_registry_template.csv # Master registry template (internal)
│   └── sber_batch_template.csv        # Batch submission template (sent to Sberbank)
└── scripts/
    └── generate_templates.py          # Script to regenerate CSV templates
```

---

## How Templates Are Used

### `merchant_registry_template.csv`
The internal merchant registry is the master record of all merchant onboarding activity. It should be maintained continuously by the Registry Owner and updated after every batch submission and every bank response. It is never sent externally.

### `sber_batch_template.csv`
This template is used to prepare each Tuesday and Friday batch submission. It is populated by extracting relevant rows from the merchant registry where `Ready_for_Batch = YES` and `Action_Type = NEW` or `UPDATE`. The completed file is attached to the batch submission email sent to Sberbank.

---

## Maintenance Ownership

| Role | Responsibility |
|------|----------------|
| Registry Owner | Maintains the merchant registry; performs duplicate checks; updates statuses |
| Onboarding Team | Collects merchant data; prepares batches; sends submissions |
| Operations / Relationship Manager | Handles escalations; manages bank communications on issues |
| Team Lead / Process Owner | Maintains this repository; approves changes; logs decisions |

---

## Optional Future Improvements

1. **Registry Migration to a Shared Database or Tool** — Replace the CSV registry with a shared Notion database, Airtable, or internal admin panel to enable real-time status tracking, filtering, and collaborative editing without version conflicts.

2. **Automated Batch Report Generation** — Extend `generate_templates.py` or add a new script that reads the live registry, filters merchants ready for batch, and auto-generates the `sber_batch_template.csv` output, reducing manual effort and copy-paste errors.

3. **Status Notification Workflow** — Implement a lightweight email or Slack notification system that alerts the relevant owner when a merchant's bank status changes (e.g., approved, rejected, pending clarification), reducing the need for manual status chasing.
