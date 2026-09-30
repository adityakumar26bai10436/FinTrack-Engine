from modules.budget import calculate_remaining_budget, budget_status
from modules.analytics import calculate_total_expenses, calculate_average_expense, find_highest_expense, find_lowest_expense
from modules.interest import compute_compound_interest, compute_interest_earned

def run_fintrack():
    print("   FinTrack: Personal Finance Engine")
    try:
        income = float(input("Enter your Total Monthly Income (₹): "))
        num_expenses = int(input("Enter total number of expense items to record: "))
        expenses = []
        for i in range(1, num_expenses + 1):
            amount = float(input(f"  Enter amount for Expense #{i} (₹): "))
            expenses.append(amount)
        total_exp = calculate_total_expenses(expenses)
        remaining = calculate_remaining_budget(income, total_exp)
        status = budget_status(income, total_exp)
        avg_exp = calculate_average_expense(expenses)
        highest_exp = find_highest_expense(expenses)
        lowest_exp = find_lowest_expense(expenses)
        print("          FINANCIAL SUMMARY")
        print(f"Total Income        : ₹{income:.2f}")
        print(f"Total Expenditure   : ₹{total_exp:.2f}")
        print(f"Remaining Allowance : ₹{remaining:.2f}")
        print(f"Average Expense     : ₹{avg_exp:.2f}")
        print(f"Highest Expense     : ₹{highest_exp:.2f}")
        print(f"Lowest Expense      : ₹{lowest_exp:.2f}")
        print(f"Budget Status       : {status}")
        print("\n--- Savings & Compound Interest Forecaster ---")
        savings = float(input("Enter amount to allocate for savings (₹): "))
        rate = float(input("Enter expected annual interest rate (%): "))
        years = int(input("Enter duration in years: "))
        final_val = compute_compound_interest(savings, rate, years)
        earned = compute_interest_earned(savings, final_val)
        print(f"\nAfter {years} years at {rate}% per annum:")
        print(f"Total Projected Savings: ₹{final_val:.2f}")
        print(f"Net Interest Earned    : ₹{earned:.2f}")
    except ValueError:
        print("\n[ERROR] Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    run_fintrack()
