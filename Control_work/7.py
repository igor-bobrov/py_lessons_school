def min_sum():
    n = int(input())
    pairs = [tuple(map(int, input().strip().split(' '))) for _ in range(n)]
    total = 0
    remainders = {0: [], 1: [], 2: []}

    for a, b in pairs:
        min_num = min(a, b)
        total += min_num
        remainder = min_num % 3
        remainders[remainder].append(max(a, b))
    if total % 3 != 0:
        return total
    min_replace = float('inf')
    for rem in [1, 2]:
        if remainders[rem]:
            min_replace = min(min_replace, min(remainders[rem]))
    if min_replace == float('inf'):
        return total

    new_total = total - (total % 3) + (min_replace % 3)
    return new_total
print(min_sum())
