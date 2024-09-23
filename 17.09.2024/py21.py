def fibonacci(n):
    fib = []
    a, b = 1, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib
print(fibonacci(int(input())))
