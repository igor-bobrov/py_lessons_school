cube = {i: i ** 3 for i in range(15, 361)}
p = {k: v for k, v in cube.items() if v%10==4}
c = len(p)

for k, v in p.items():
    print(f"{k}: {v}")
print("Ans", c)
