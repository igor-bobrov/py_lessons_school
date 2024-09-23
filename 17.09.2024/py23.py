def is_perfect(n):
    if n < 2:
        return False
    dsum = sum(i for i in range(1, n) if n % i == 0)
    return dsum == n
def FindPerNum(M):
    per = []
    for num in range(2, M):
        if is_perfect(num):
            per.append(num)
    return per
perNum = FindPerNum(int(input()))
print(perNum)