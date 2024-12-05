def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + F(n - 1)
    else:
        return 2 * F(n - 2)

result = F(26)
print(result)
