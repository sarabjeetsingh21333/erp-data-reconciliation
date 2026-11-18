# ERP Data Reconciliation & Business Audit Tool

A Python utility designed to cross-reference enterprise logs against database records, flag transactional anomalies, and automate tabular data reconciliation for ERP workflows.

## Features
- **Tabular Cross-Referencing:** Merges multi-source datasets to check for parity and missing records.
- **Discrepancy Detection:** Flags variances in transactional amounts and structural logs.
- **Audit Reporting:** Automatically compiles reconciliation findings into clean CSV audit summaries using `pandas`.

## Tech Stack
- **Python** (Core script logic)
- **Pandas & NumPy** (Data manipulation and relational merging)

## Quick Start
1. Run the reconciliation tool:
   ```bash
   python reconcile.py