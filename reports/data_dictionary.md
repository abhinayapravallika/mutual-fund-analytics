# Data Dictionary

## nav_history

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | AMFI Scheme Code |
| date | DATE | NAV Date |
| nav | FLOAT | Net Asset Value |

---

## investor_transactions

| Column | Type | Description |
|----------|----------|----------|
| transaction_id | INTEGER | Unique transaction |
| investor_id | INTEGER | Investor ID |
| amount | FLOAT | Transaction amount |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| transaction_date | DATE | Transaction Date |
| kyc_status | TEXT | KYC verification status |

---

## scheme_performance

| Column | Type | Description |
|----------|----------|----------|
| return_1y | FLOAT | One year return |
| return_3y | FLOAT | Three year return |
| return_5y | FLOAT | Five year return |
| expense_ratio | FLOAT | Expense ratio percentage |