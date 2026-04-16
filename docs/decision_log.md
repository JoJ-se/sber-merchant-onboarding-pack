# Decision Log — Sberbank Merchant Onboarding

This log records key operational and process decisions made during the design and implementation of the DukPay–Sberbank merchant onboarding operating model. It is maintained by the Process Owner and updated whenever a significant decision is made.

---

| # | Date | Decision | Reason | Owner |
|---|------|----------|--------|-------|
| 001 | 2025-01-01 | One merchant entity = one Merchant ID and one login. Duplicate registrations are prohibited. | Sberbank requirement and internal operational clarity. Duplicate registrations cause confusion in payment routing, settlement, and support. | Process Owner |
| 002 | 2025-01-01 | Website and mobile app belonging to the same merchant must be registered under the same merchant entity, not as separate records. | Confirmed by Sberbank: if a merchant's website is already registered, the mobile app should not trigger a new merchant registration. One entity, one MID. | Process Owner |
| 003 | 2025-01-01 | Merchant submissions to Sberbank are sent in batch format, twice per week — on Tuesday and Friday. | Sberbank requested a structured, predictable submission schedule. Ad-hoc individual submissions are operationally inefficient and difficult to track. | Operations Manager |
| 004 | 2025-01-01 | Batch onboarding communications and issue/clarification communications are handled in separate email threads. | Mixing onboarding and issue content in the same thread creates confusion, makes audit difficult, and risks critical information being overlooked. | Process Owner |
| 005 | 2025-01-01 | A central merchant registry (CSV) is established as the single source of truth for all Sberbank merchant registrations. | The previous process relied on fragmented emails with no unified view of merchant status, ownership, or history. A registry provides full auditability and reduces duplicates. | Registry Owner / Process Owner |
| 006 | 2025-01-01 | Adding a new channel (website or app) to an existing merchant is classified as an UPDATE action, not a NEW registration. | Consistent with the one-entity rule. Creating a new record for a channel addition would result in duplicate Merchant IDs and confusion over login assignment. | Process Owner |
| 007 | 2025-01-01 | The pre-batch checklist must be completed and signed off before every Tuesday/Friday submission. Batches without a completed checklist must not be sent. | Mandatory gate to prevent duplicate submissions, incomplete data, and unreviewed records from being sent to Sberbank. | Registry Owner |

---

*New entries should be added in chronological order. Include the date the decision was made (not the date it was recorded).*
