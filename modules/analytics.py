# modules/analytics.py

def calculate_total_expenses(exp: list) -> float:
    tot = 0.0
    for amt in exp:
        tot += amt
    return tot

def calculate_average_expense(exp: list) -> float:
    if not exp: return 0.0
    return calculate_total_expenses(exp) / len(exp)

def find_highest_expense(exp: list) -> float:
    if not exp: return 0.0
    hi = exp[0]
    for amt in exp:
        if amt > hi: hi = amt
    return hi

def find_lowest_expense(exp: list) -> float:
    if not exp: return 0.0
    lo = exp[0]
    for amt in exp:
        if amt < lo: lo = amt
    return lo
