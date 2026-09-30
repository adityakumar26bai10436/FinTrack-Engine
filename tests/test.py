from modules.budget import calculate_remaining_budget, budget_status
from modules.analytics import calculate_total_expenses, calculate_average_expense
from modules.interest import compute_compound_interest

def test_budget_calculations():
    assert calculate_remaining_budget(10000, 3000) == 7000
    assert "HEALTHY:D" in budget_status(10000, 5000)
    assert "WARNING:O" in budget_status(10000, 8500)
    assert "CRITICAL:<" in budget_status(10000, 11000)

def test_analytics_calculations():
    sample_expenses = [100.0, 200.0, 300.0]
    assert calculate_total_expenses(sample_expenses) == 600.0
    assert calculate_average_expense(sample_expenses) == 200.0

def test_interest_calculations():
    # Principal: 1000, Rate: 10%, Years: 2 -> 1000 * 1.1 * 1.1 = 1210
    assert round(compute_compound_interest(1000, 10, 2), 2) == 1210.0

if __name__ == "__main__":
    test_budget_calculations()
    test_analytics_calculations()
    test_interest_calculations()
    print("All unit tests passed successfully!")
