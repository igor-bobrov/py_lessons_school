import matplotlib.pyplot as plt
def stair(s, e, n, it):
    for i in range(int(((e-s)*len(it))//3), int(((e-s)*2*len(it))//3)):
        it[i] = 1/2**n
    if (e-s)*len(it) >= 1:
        return stair(s, (e-s)//3, n+1, it)  
    else:
        return it
t = 10000
it = [1/2 for _ in range(t)]

fig, axs = plt.subplots(1, 1, figsize=(10,10))

axs.plot([i for i in range(t)], stair(0, 1, 1, it), color="b")

fig.suptitle('Лесница', fontsize=16)
plt.show()