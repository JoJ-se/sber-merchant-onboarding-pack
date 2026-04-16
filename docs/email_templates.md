# Email Templates — Sberbank Merchant Onboarding

**Usage instructions:**
- Replace all bracketed placeholders `[like this]` with the relevant values before sending.
- Use the correct template for the correct communication type.
- Do not mix batch submission content with issue/clarification content in the same thread.
- All emails to Sberbank should be sent from the designated DukPay operations inbox.

---

## Template A — Batch Onboarding Submission

**Use for:** Tuesday and Friday batch submissions of new merchant registrations and updates.

**Thread:** Dedicated onboarding submission thread. Do not use for issue follow-up.

---

**Subject:** DukPay — Merchant Onboarding Batch — [Batch Date]

Dear [Sberbank Contact Name],

Please find attached the merchant onboarding batch for [Batch Date].

**Batch summary:**

| Item | Count |
|------|-------|
| New registrations | [Number] |
| Updates to existing merchants | [Number] |
| Total records | [Total] |

All records in this batch have been validated internally for completeness and duplicate status prior to submission.

Please confirm receipt at your earliest convenience, and advise if any records require clarification or additional information.

The attached file: `sber_batch_[Batch Date].csv`

Best regards,  
[Sender Full Name]  
[Title] | DukPay  
[Email] | [Phone]

---

## Template B — Follow-Up on Pending Batch

**Use for:** Following up on a batch that has not received an acknowledgement or status update within the expected timeframe.

**Thread:** Reply to the original batch submission thread.

---

**Subject:** RE: DukPay — Merchant Onboarding Batch — [Original Batch Date]

Dear [Sberbank Contact Name],

I am writing to follow up on our merchant onboarding batch submitted on [Original Batch Date].

As of today, [Follow-Up Date], we have not yet received confirmation of the status for the following merchants:

- [Merchant Name 1]
- [Merchant Name 2]
- [Merchant Name 3] *(add or remove as needed)*

Could you please provide an update on the review status? We would appreciate any feedback by [Expected Response Date].

We are happy to provide any additional information required.

Best regards,  
[Sender Full Name]  
[Title] | DukPay  
[Email] | [Phone]

---

## Template C — Clarification / Issue Resolution

**Use for:** Responding to Sberbank clarification requests, rejections, or issue notifications. Always in a separate thread from the batch submission.

**Thread:** New thread titled as shown below. Do not reply to the batch submission thread.

---

**Subject:** DukPay — Merchant Clarification — [Merchant Name] — [Date]

Dear [Sberbank Contact Name],

Thank you for your message regarding [Merchant Name].

We have reviewed the clarification request / feedback received on [Date of Bank Communication] and can confirm the following:

**Merchant reference:**
- Merchant Name: [Merchant Name]
- Sberbank Merchant ID: [Merchant ID] *(if already assigned)*
- Login: [Login] *(if already assigned)*

**Response to clarification:**

[Provide a clear, factual response to the specific question or issue raised by Sberbank. State what information is being corrected, updated, or added. If documents are attached, list them here.]

**Updated information** *(if applicable)*:
- [Field updated]: [New value]

Please let us know if any further information is required.

Best regards,  
[Sender Full Name]  
[Title] | DukPay  
[Email] | [Phone]

---

## Template D — Update to Existing Merchant

**Use for:** Notifying Sberbank of a change to an already-registered merchant (e.g., adding a mobile app, updating a URL, modifying payment methods). This is sent as part of the standard Tuesday/Friday batch — it does not require a separate ad-hoc email. The template below is for the comment field or a standalone communication if the update is raised outside of a batch context.

*Note: In most cases, updates are handled via the batch CSV with `Action_Type = UPDATE`. This template applies when a standalone update notification is required outside the batch cycle.*

---

**Subject:** DukPay — Merchant Update Notification — [Merchant Name] — [Date]

Dear [Sberbank Contact Name],

We are writing to notify you of an update to the following registered merchant:

**Merchant reference:**
- Merchant Name: [Merchant Name]
- Sberbank Merchant ID: [Merchant ID]
- Login: [Login]

**Nature of update:**

| Field | Previous Value | Updated Value |
|-------|---------------|---------------|
| [Field name] | [Old value] | [New value] |
| [Field name] | [Old value] | [New value] |

**Reason for update:** [Brief explanation — e.g., merchant has launched a mobile application in addition to their existing website.]

Please confirm receipt and advise whether any additional documentation is required to process this update.

Best regards,  
[Sender Full Name]  
[Title] | DukPay  
[Email] | [Phone]
