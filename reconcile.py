import os
import sys
import pandas as pd

def reconcile_datasets(system_log_path, db_record_path):
    """
    Simulates ERP inventory/sales data reconciliation between system logs and database records.
    """
    if not os.path.exists(system_log_path) or not os.path.exists(db_record_path):
        print("Error: Input files not found. Creating mock data for demonstration...")
        create_mock_data()
        system_log_path = "system_logs.csv"
        db_record_path = "db_records.csv"

    print("Loading datasets for ERP reconciliation...")
    df_sys = pd.read_csv(system_log_path)
    df_db = pd.read_csv(db_record_path)

    # Merge datasets on transaction ID to find discrepancies
    merged = pd.merge(df_sys, df_db, on="TransactionID", suffixes=('_system', '_db'), how='outer', indicator=True)

    # Flag mismatches or missing records
    discrepancies = merged[merged['_merge'] != 'both']
    matched = merged[merged['_merge'] == 'both']

    # Check for value differences in matched records
    if 'Amount_system' in matched.columns and 'Amount_db' in matched.columns:
        value_mismatches = matched[matched['Amount_system'] != matched['Amount_db']]
    else:
        value_mismatches = pd.DataFrame()

    print("\n=== ERP Reconciliation Report ===")
    print(f"Total Matched Records: {len(matched)}")
    print(f"Missing / Unmatched Records: {len(discrepancies)}")
    print(f"Value Discrepancies Found: {len(value_mismatches)}")

    # Export reconciliation audit log
    output_file = "reconciliation_audit_report.csv"
    merged.to_csv(output_file, index=False)
    print(f"\nSuccess! Audit report saved to '{output_file}'.")

def create_mock_data():
    """Helper to create dummy CSV files if none are provided."""
    sys_data = {"TransactionID": [101, 102, 103, 104], "Amount": [500, 1200, 300, 750]}
    db_data = {"TransactionID": [101, 102, 103, 105], "Amount": [500, 1150, 300, 900]}
    
    pd.DataFrame(sys_data).to_csv("system_logs.csv", index=False)
    pd.DataFrame(db_data).to_csv("db_records.csv", index=False)

if __name__ == "__main__":
    sys_log = sys.argv[1] if len(sys.argv) > 1 else "system_logs.csv"
    db_rec = sys.argv[2] if len(sys.argv) > 2 else "db_records.csv"
    reconcile_datasets(sys_log, db_rec)