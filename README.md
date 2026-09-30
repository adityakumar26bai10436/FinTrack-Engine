# FinTrack-Engine
# FinTrack - Personal Finance & Expense Analytics Engine

FinTrack is a basic Python CLI(Command Line Interface) app built to track daily expenditures, monitor monthly budget limits, and calculate compound savings growth. It runs purly on Python 3 without requiring external third-party packages.

## Features
- **Budget Monitoring:** Shows remaining allowance and issues a Orange Flag / `WARNING` (at 80%) or Red Flag / `CRITICAL` (at 100%) status alerts.
- **Expense Analytics:** Computes total spend, daily avg. spend, highest spend, and lowest spend.
- **Savings Projection:** Calculates compound interest earnings year-by-yearas perthe given data.
- **Modular Code:** Logic is clearly splitted across specified sub-modules.

## Non-Functional & System Specifications
- **Error Resilience:** Input loop wrapped in (try and except) block to intercept invalid numeric types.
- **Boundary Safety:** Explicit guards against division by zero and null expense lists.
- **Zero Dependencies:** Uses standard Python 3 syntax exclusively.
- **Clean Output:** Money values formatted with f-string precision.

## File Structure
```text
FinTrack-Engine/
├── main.py                # Main script and interactive CLI (Command Line Interface) menu
├── statement.md           # Problem statement and system requirements
├── README.md              # Project setup and overview
├── modules/
│   ├── __init__.py        # Package initialization
│   ├── budget.py          # Budget checking & status warnings
│   ├── analytics.py       # Sum, average, max, and min math functions
│   └── interest.py        # Compound interest power calculations
└── tests/
    └── test_finance.py    # Basic unit test cases
