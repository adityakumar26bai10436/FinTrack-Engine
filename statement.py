# Problem Statement & System Requirements: FinTrack

## Problem Statement
Keeping track of daily expenses manually is messy and easy to forget. Many students end up exceeding their monthly budget without realizing where the money went, leaving little to no money for savings by the end of the month. On top of that, calculating long-term savings growth using compound interest isn't straightforward without custom tools. 

FinTrack is designed as a lightweight, clean command-line Python application that helps users track expenditures, monitor budget threshold limits to avoid overspending, and project savings growth using basic math algorithms.

## Scope of the Project
FinTrack focuses on modular programming using core Python concepts (Modules 1 to 4):
- **Expense Summaries:** Calculates total spending, average expense per item, and finds highest/lowest expense entries.
- **Budget Threshold Alerts:** Evaluates total spent against monthly income and warns when spending exceeds 80% or 100% capacity.
- **Compound Interest Forecaster:** Projects savings accumulation over time using iterative multiplication loops.
- **Input Error Handling:** Uses basic validation to make sure invalid input dose not crash the program.

## Non-Functional & Non-Technical Requirements

1. **Usability & Interface:**
   - Text output must be formatted with clear currency indicators (₹) and formatted to two decimal places.
   - Terminal prompts must clearly specify expected data types to ensure ease of use for non-technical users.

2. **Reliability & Crash Prevention:**
   - Program execution must handle non-numeric inputs gracefully using `try-except` blocks.
   - Mathematical functions must include explicit boundary checks (`if total_income <= 0:` and `if not expenses:`) to avoid zero-division and empty list index errors.

3. **Maintainability & Architecture:**
   - Separation of concerns: Display logic in `main.py` is decoupled from computation routines in `modules/`.
   - All functions must include docstrings documenting parameters and return behavior.

4. **Portability & Environment:**
   - Must run on any standard Python 3.x environment without requiring third-party library dependencies (`pip install`).

## Target Audience
- University students managing monthly allowances and hostel expenses.
- Anyone looking for a lightweight CLI spending tracker built purely in Python without external library dependencies.

## Key Modules Built
1. `modules/budget.py`: Handles income comparison, remaining allowance, and health alerts.
2. `modules/analytics.py`: Calculates sum, mean, maximum, and minimum values for expense lists.
3. `modules/interest.py`: Calculates compound interest over a given time horizon.
4. `main.py`: Drives the main terminal menu loop.
5. `tests/test_finance.py`: Automated unit verification tests.
