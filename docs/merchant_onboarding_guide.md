# Merchant Onboarding Guide — Sberbank Internet Acquiring

**Document type:** Internal Operations Guide  
**Version:** 1.0  
**Maintained by:** Registry Owner / Process Owner  

---

## 1. Purpose

This guide defines the end-to-end process for onboarding sub-merchants with Sberbank under the DukPay PSP structure for internet acquiring in Russia. It serves as the authoritative internal reference for all team members involved in merchant registration, batch preparation, registry maintenance, and bank communication.

The guide supersedes all informal, email-based instructions previously in circulation.

---

## 2. Scope

This guide applies to:
- All new merchant registrations submitted to Sberbank via DukPay.
- All updates to existing registered merchants (channel additions, data changes).
- All internal communications related to Sberbank merchant onboarding.

It does not cover technical integration, payment testing, or dispute handling.

---

## 3. Definitions

| Term | Definition |
|------|-----------|
| **Merchant** | A sub-merchant entity onboarded by DukPay and registered with Sberbank for internet acquiring. |
| **Merchant ID (MID)** | The unique identifier assigned by Sberbank to a registered merchant. |
| **Login** | The Sberbank system login assigned to a merchant entity. One login per merchant. |
| **Channel** | The digital channel through which a merchant accepts payments: Website, Mobile App, or Both. |
| **Batch** | A scheduled, structured submission of multiple merchant registrations or updates sent to Sberbank twice per week. |
| **Registry** | The central internal merchant registry CSV maintained by the Registry Owner. |
| **Action Type** | The classification of a submission row: NEW (first-time registration) or UPDATE (change to an existing merchant). |
| **Registry Owner** | The designated team member responsible for maintaining the merchant registry and enforcing data integrity. |

---

## 4. Business Rules

The following rules are mandatory and must be applied without exception:

1. **One merchant = one entity.** A single business entity may only be registered once with Sberbank through DukPay.
2. **One Merchant ID, one login per merchant.** Duplicate Merchant IDs or duplicate logins for the same entity are not permitted.
3. **Website and mobile app belong to the same merchant.** If a merchant operates both a website and a mobile application, both channels must be registered under the same merchant entity. A separate registration must not be created for the mobile app if the website is already registered.
4. **New channels for an existing merchant are handled as updates.** Adding a website or app to an existing merchant record is an UPDATE action, not a NEW registration.
5. **All submissions are sent in batch format, twice per week.** Ad-hoc individual submissions to Sberbank are not permitted except in exceptional circumstances approved by the Operations Manager.
6. **Onboarding communications and issue communications are kept in separate email threads.** Batch submissions and issue/clarification exchanges must not be mixed.
7. **The merchant registry is the single source of truth.** All merchant data, statuses, and histories are recorded in the central registry. No other record takes precedence.
8. **Duplicate checks are mandatory before every batch submission.** No merchant may be submitted without a confirmed duplicate check in the registry.
9. **Every registry record must have a status and a named owner.**
10. **The process must be auditable.** All changes to merchant records, submissions, and decisions must be traceable.

---

## 5. Onboarding Principles

- **Centralisation first.** All merchant data flows through the registry before any external submission.
- **Separation of concerns.** The onboarding queue and the issue/clarification queue are operationally distinct.
- **Batch discipline.** Predictable submission windows reduce confusion and allow Sberbank to process registrations efficiently.
- **Minimum data completeness.** A merchant record is not submitted until all mandatory fields are present and verified.
- **Registry-driven decisions.** The registry determines readiness for submission, not individual judgment or email threads.

---

## 6. Batch Submission Model

Merchants are submitted to Sberbank **twice per week**, on **Tuesday** and **Friday**.

**Submission window process:**

1. Before each batch day, the Registry Owner reviews the registry for all records where `Ready_for_Batch = YES` and `Internal_Status = Pending Submission`.
2. The Onboarding Team prepares the batch CSV by extracting these records into the `sber_batch_template.csv`.
3. The pre-batch checklist (`merchant_onboarding_checklist.md`) is completed and signed off.
4. The batch is sent to Sberbank using the standard batch submission email template.
5. After sending, all submitted records are updated in the registry: `Internal_Status → Submitted`, `First_Sent_Date` populated (if new), `Last_Update_Date` updated.

**Suggested internal SLA targets** *(internal practice, subject to team agreement)*:
- Merchant data collection to registry entry: same business day
- Registry entry to batch readiness confirmation: within 1 business day
- Batch prepared and dispatched: by 12:00 on Tuesday / Friday
- Registry updated post-submission: same day as batch sent

**Suggested bank-side SLA expectations** *(based on operational experience; confirm with Sberbank)*:
- Initial acknowledgement from Sberbank: within 2 business days
- Registration approval or rejection: within 5–7 business days
- Clarification response from DukPay to Sberbank: within 2 business days

---

## 7. Central Registry Model

The merchant registry (`merchant_registry_template.csv`) is the master record of all merchant onboarding activity.

**Key principles:**
- Maintained exclusively by the Registry Owner.
- Updated immediately after any status change: submission sent, bank response received, data corrected.
- Never modified based on information from email alone without a cross-check.
- Shared with relevant team members on a read-only basis as needed.

**Core registry fields** (see template for full column list):
- `Merchant_Name`, `Internal_ID`, `Sber_Merchant_ID`, `Login` — core identification
- `Channel`, `Website_URL`, `App_URL` — channel information
- `Action_Type` — NEW or UPDATE
- `Internal_Status`, `Bank_Status` — dual-layer status tracking
- `First_Sent_Date`, `Last_Update_Date` — submission timeline
- `Owner`, `Duplicate_Check`, `Ready_for_Batch` — operational controls

---

## 8. Handling Website and Mobile App Under One Merchant

Sberbank has clarified that a merchant operating both a website and a mobile app should be registered **once**, with both channels captured under the same Merchant ID.

**Operational procedure:**

| Scenario | Action |
|----------|--------|
| New merchant — website only | Register as NEW, `Channel = Web`, populate `Website_URL` |
| New merchant — app only | Register as NEW, `Channel = App`, populate `App_URL` |
| New merchant — website + app | Register as NEW, `Channel = Both`, populate both URL fields |
| Existing merchant — add app to existing web registration | Submit as UPDATE, `Channel = Both`, add `App_URL`, do not create new entry |
| Existing merchant — add web to existing app registration | Submit as UPDATE, `Channel = Both`, add `Website_URL`, do not create new entry |

Before registering any new merchant, the Registry Owner must verify that no existing record exists for the same entity under a different channel. If a match is found, the action type must be changed to UPDATE.

---

## 9. Duplicate Prevention

Before any merchant is added to a batch:

1. Search the registry by `Merchant_Name` for any existing record.
2. Search by `Website_URL` and `App_URL` for any URL match.
3. If a match is found, determine whether the incoming record is a duplicate or a legitimate update to an existing entry.
4. Mark `Duplicate_Check = YES` only after both checks are complete and confirmed clean or resolved.
5. If a potential duplicate is found and cannot be resolved with certainty, escalate to the Operations Manager before proceeding.

No record may be submitted to Sberbank without `Duplicate_Check = YES`.

---

## 10. Status Management

Each merchant record carries two status fields:

**`Internal_Status`** — reflects DukPay's internal view of the record:

| Status | Meaning |
|--------|---------|
| Draft | Data collected, not yet validated |
| Pending Submission | Validated, approved for next batch |
| Submitted | Sent to Sberbank, awaiting response |
| Pending Clarification | Awaiting bank clarification or additional data from merchant |
| Approved | Confirmed registered by Sberbank |
| Rejected | Rejected by Sberbank; requires review |
| On Hold | Paused for internal or merchant-side reasons |

**`Bank_Status`** — reflects the response received from Sberbank:

| Status | Meaning |
|--------|---------|
| Not Submitted | Not yet sent |
| Under Review | Submitted, no response yet |
| Approved | Bank has confirmed registration |
| Rejected | Bank has rejected; see `Bank_Comment` |
| Clarification Requested | Bank requires additional information |

Both fields must be updated simultaneously upon any change.

---

## 11. Escalation and Issue Handling

All clarifications, rejections, and issues raised by Sberbank are handled in a **separate email thread** from the batch submission thread.

**Escalation path:**

1. Sberbank raises an issue → Operations/Relationship Manager receives and logs it.
2. Manager updates the relevant registry record: `Bank_Status = Clarification Requested`, `Internal_Status = Pending Clarification`, adds `Bank_Comment`.
3. Manager coordinates with the Onboarding Team or merchant to gather the required information.
4. Response is sent to Sberbank using the clarification email template.
5. Registry is updated upon resolution.

If a merchant is rejected by Sberbank, the Operations Manager reviews the rejection reason, updates the registry, and determines whether resubmission is appropriate. Resubmission follows the standard batch process.

---

## 12. SLA Summary Table

| Activity | Responsible | Internal Target |
|----------|-------------|----------------|
| Merchant data entry to registry | Onboarding Team | Same business day |
| Duplicate check and readiness sign-off | Registry Owner | Within 1 business day |
| Batch preparation and dispatch | Onboarding Team | By 12:00 on batch day |
| Registry update after submission | Registry Owner | Same day as batch sent |
| Response to Sberbank clarification | Operations Manager | Within 2 business days |
| Registry update after bank response | Registry Owner | Same day as response received |

*SLA targets are suggested internal practices and should be confirmed and formalised by team leadership.*
