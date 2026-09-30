# modules/budget.py

def calculate_remaining_budget(inc: float, exp: float) -> float:
    return inc - exp

def budget_status(inc: float, exp: float) -> str:
    if inc <= 0:
        return "Invalid Value Given"

    percentage = (exp / inc) * 100

    if percentage >= 100:
        return f"CRITICAL Budget Exceeded! ({percentage:.1f}% used)"
    elif percentage >= 80:
        return f"WARNING Approaching Budget Limit!! ({percentage:.1f}% used)"
    else:
        return f"HEALTHY within Safe Budget Limits!!! ({percentage:.1f}% used)"
