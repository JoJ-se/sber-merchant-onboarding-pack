# Pre-Batch Merchant Onboarding Checklist

**Use before every Tuesday and Friday batch submission.**  
Complete all sections. Do not submit the batch until all items are marked.

---

**Batch Date:** _______________  
**Prepared by:** _______________  
**Registry Owner sign-off:** _______________  
**Number of merchants in batch:** _______________  

---

## Section 1 — Duplicate Check

For each merchant record flagged `Ready_for_Batch = YES`:

- [ ] Merchant name has been searched in the registry — no duplicate name found, or existing record confirmed as separate entity.
- [ ] Website URL has been searched in the registry — no existing record with the same URL.
- [ ] App URL has been searched in the registry — no existing record with the same app URL.
- [ ] All records in this batch have `Duplicate_Check = YES` in the registry.
- [ ] Any potential duplicates identified have been reviewed and resolved before this batch was finalised.

---

## Section 2 — Login Check

- [ ] Each merchant in the batch has a login assigned or login creation has been coordinated with Sberbank.
- [ ] No two merchants in this batch share the same login.
- [ ] No merchant in this batch duplicates a login already recorded in the registry for a different entity.
- [ ] Login field is populated for all merchants where `Action_Type = UPDATE` and a login was previously assigned.

---

## Section 3 — Merchant ID Check

- [ ] For NEW merchants: `Sber_Merchant_ID` field is left blank (to be assigned by Sberbank).
- [ ] For UPDATE merchants: `Sber_Merchant_ID` is populated with the existing Sberbank-assigned ID.
- [ ] No Merchant ID appears more than once in the batch for different merchant entities.
- [ ] No Merchant ID in this batch conflicts with an existing registry record for a different merchant.

---

## Section 4 — Channel Check

- [ ] Each merchant record specifies `Channel` as one of: `Web`, `App`, or `Both`.
- [ ] All merchants with both a website and mobile app are recorded as `Channel = Both` — not as two separate records.
- [ ] `Website_URL` is populated for all records where `Channel = Web` or `Channel = Both`.
- [ ] `App_URL` is populated for all records where `Channel = App` or `Channel = Both`.
- [ ] No merchant in this batch is registering a mobile app separately when their website is already registered (must be an UPDATE instead).

---

## Section 5 — Mandatory Data Fields Check

For each merchant in the batch, confirm the following fields are complete and correctly formatted:

- [ ] `Merchant_Name` — populated, matches merchant's legal or trading name.
- [ ] `Internal_ID` — populated with DukPay internal reference.
- [ ] `Channel` — populated (`Web`, `App`, or `Both`).
- [ ] `Website_URL` — populated where applicable; valid URL format.
- [ ] `App_URL` — populated where applicable; valid URL format.
- [ ] `Payment_Methods` — populated with accepted payment method(s).
- [ ] `Action_Type` — populated as `NEW` or `UPDATE`.
- [ ] `Owner` — named owner assigned to each record.
- [ ] No mandatory fields are blank in the batch CSV.

---

## Section 6 — Action Type Check

- [ ] Each record is correctly classified as `NEW` or `UPDATE`.
- [ ] No merchant is classified as `NEW` if they already appear in the registry with an existing `Sber_Merchant_ID`.
- [ ] Channel additions or data changes to existing merchants are classified as `UPDATE`, not `NEW`.
- [ ] All UPDATE records include the existing `Sber_Merchant_ID` and `Login`.
- [ ] Comment field in the batch CSV describes the nature of the update for all `UPDATE` records.

---

## Section 7 — Email Thread Check

- [ ] The batch submission email will be sent in the designated **onboarding submission thread** — not in an issue or clarification thread.
- [ ] Any merchants with outstanding clarifications or rejections are excluded from this batch until resolved.
- [ ] Previous batch submission emails have been filed or referenced correctly for audit purposes.
- [ ] No onboarding or merchant data has been communicated to Sberbank via informal or ad-hoc emails outside the standard templates.

---

## Section 8 — Owner Check

- [ ] Every merchant record in this batch has a named `Owner` assigned.
- [ ] The assigned owner has been informed that their merchant(s) are included in this batch.
- [ ] There are no records in the batch with `Owner` field blank or set to a placeholder.

---

## Section 9 — Status Update Check

After the batch has been dispatched, confirm the following registry updates are completed on the same day:

- [ ] `Internal_Status` updated to `Submitted` for all dispatched records.
- [ ] `First_Sent_Date` populated for all NEW records in this batch (if not already set).
- [ ] `Last_Update_Date` updated for all records in this batch.
- [ ] `Bank_Status` updated to `Under Review` for all dispatched records.
- [ ] Batch email sent confirmation logged (date, time, recipient) in `Internal_Comment` or equivalent.

---

**Checklist completed by:** _______________  
**Date and time:** _______________  
**Batch dispatched:** [ ] Yes  &nbsp;&nbsp; [ ] No — Reason: _______________
