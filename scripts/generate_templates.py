"""
generate_templates.py
---------------------
Generates the CSV template files used in the Sberbank merchant onboarding process.

This script creates (or overwrites) the two CSV template files:
  - merchant_registry_template.csv  : internal master merchant registry (headers only)
  - sber_batch_template.csv         : batch submission file sent to Sberbank (headers only)

Safe to run multiple times. Running it will reset the templates to headers-only,
removing any data rows. Do not run against a live registry file.

Usage:
    python scripts/generate_templates.py

Output:
    templates/merchant_registry_template.csv
    templates/sber_batch_template.csv
"""

import csv
import os

# ---------------------------------------------------------------------------
# Output paths (relative to repository root)
# ---------------------------------------------------------------------------

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")

REGISTRY_OUTPUT_PATH = os.path.join(TEMPLATES_DIR, "merchant_registry_template.csv")
BATCH_OUTPUT_PATH = os.path.join(TEMPLATES_DIR, "sber_batch_template.csv")

# ---------------------------------------------------------------------------
# Column definitions
# ---------------------------------------------------------------------------

# Internal master merchant registry.
# This file is maintained by the Registry Owner and is never sent externally.
REGISTRY_HEADERS = [
    "Merchant_Name",        # Legal or trading name of the merchant
    "Internal_ID",          # DukPay internal reference ID
    "Sber_Merchant_ID",     # Merchant ID assigned by Sberbank (blank for NEW until assigned)
    "Login",                # Sberbank login assigned to this merchant (one per entity)
    "Channel",              # Web | App | Both
    "Website_URL",          # Merchant website URL (required if Channel = Web or Both)
    "App_URL",              # Merchant app URL or app store link (required if Channel = App or Both)
    "Payment_Methods",      # Payment methods accepted (e.g. Card, SBP, etc.)
    "Action_Type",          # NEW | UPDATE
    "Internal_Status",      # Draft | Pending Submission | Submitted | Pending Clarification | Approved | Rejected | On Hold
    "Bank_Status",          # Not Submitted | Under Review | Approved | Rejected | Clarification Requested
    "First_Sent_Date",      # Date first submitted to Sberbank (YYYY-MM-DD)
    "Last_Update_Date",     # Date of most recent update to this record (YYYY-MM-DD)
    "Bank_Comment",         # Feedback or notes received from Sberbank
    "Internal_Comment",     # Internal notes (e.g. issues, context, follow-up actions)
    "Owner",                # DukPay team member responsible for this record
    "Duplicate_Check",      # YES | NO — must be YES before batch submission
    "Ready_for_Batch",      # YES | NO — confirmed ready to include in next batch
]

# Batch submission template.
# This is the file sent to Sberbank on Tuesday and Friday.
# Populated by extracting relevant rows from the registry where Ready_for_Batch = YES.
BATCH_HEADERS = [
    "Merchant_Name",        # Legal or trading name of the merchant
    "Sber_Merchant_ID",     # Leave blank for NEW; include for UPDATE
    "Login",                # Sberbank login; leave blank for NEW if not yet assigned
    "Channel",              # Web | App | Both
    "Website_URL",          # Required if Channel = Web or Both
    "App_URL",              # Required if Channel = App or Both
    "Payment_Methods",      # Payment methods to be enabled
    "Action_Type",          # NEW | UPDATE
    "Comment",              # Additional context for Sberbank (e.g. nature of update)
]

# ---------------------------------------------------------------------------
# Template generation
# ---------------------------------------------------------------------------

def write_template(filepath: str, headers: list[str], label: str) -> None:
    """
    Write a headers-only CSV file to the specified path.

    Args:
        filepath: Full path to the output file.
        headers:  List of column header strings.
        label:    Human-readable name used in console output.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

    print(f"[OK] {label}")
    print(f"     Path    : {os.path.abspath(filepath)}")
    print(f"     Columns : {len(headers)}")
    print()


def main() -> None:
    print("=" * 60)
    print("  Sberbank Merchant Onboarding — Template Generator")
    print("=" * 60)
    print()

    write_template(
        filepath=REGISTRY_OUTPUT_PATH,
        headers=REGISTRY_HEADERS,
        label="merchant_registry_template.csv",
    )

    write_template(
        filepath=BATCH_OUTPUT_PATH,
        headers=BATCH_HEADERS,
        label="sber_batch_template.csv",
    )

    print("All templates generated successfully.")
    print("Note: These files contain headers only. Do not run this script")
    print("against a live registry that contains merchant data.")


if __name__ == "__main__":
    main()
