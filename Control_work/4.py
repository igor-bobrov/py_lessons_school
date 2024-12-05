cube_dict = {i: i ** 3 for i in range(15, 361)}
p = {k: v for k, v in cube_dict.items() if str(v).endswith('4')}
count_pairs = len(p)

print("Пары (число, куб):")
for k, v in p.items():
    print(f"{k}: {v}")

print("Количество таких пар:", count_pairs)
