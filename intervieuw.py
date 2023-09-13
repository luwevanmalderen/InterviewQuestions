INF = float("inf")
def maxProfit(A):
    bystart = []
    high = -INF  # maximum so far
    best = 0
    for x in reversed(A):
        best = max(best, high - x)
        bystart.append(best)
        high = max(high, x)

    low = INF  # minimum so far
    best = 0
    total = 0
    for x, best2 in zip(A, reversed(bystart)):
        best = max(best, x - low)
        total = max(total, best + best2)
        low = min(low, x)

    return total
