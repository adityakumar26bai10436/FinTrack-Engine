# modules/interest.py

def compute_compound_interest(p: float, r: float, t: int) -> float:
    amt = p
    mult = 1.0 + (r / 100.0)

    for _ in range(t):
        amt *= mult

    return amt

def compute_interest_earned(p: float, final_amt: float) -> float:
    return final_amt - p
