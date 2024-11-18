import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0,2*np.pi,1000)


def x(t, c):
    a = [3, 3, 5, 3, 3, 5]
    d = [2, 2, 2, 4, 6, 8]
    return 5*np.sin(a[c]*t +np.pi/d[c]) 

def y(t, c):
    b = [3, 2, 6, 3, 2, 6]
    return 5*np.sin(b[c]*t) 

fig, axs = plt.subplots(3, 2, figsize=(40,20))

axs[0,0].plot(x(t, 0), y(t, 0), color="r")
axs[0,0].set_ylabel('b/a=1 d =p/2')

axs[1,0].plot(x(t, 1), y(t, 1), color="g")
axs[1,0].set_ylabel('b/a=2/3 d =p/2')

axs[2,0].plot(x(t, 2), y(t, 2), color="b")
axs[2,0].set_ylabel('b/a=6/5 d =p/2')

axs[0,1].plot(x(t, 3), y(t, 3), color="r")
axs[0,1].set_ylabel('b/a=1 d =p/4')

axs[1,1].plot(x(t, 4), y(t, 4), color="g")
axs[1,1].set_ylabel('b/a=2/3 d =p/6')

axs[2,1].plot(x(t, 5), y(t, 5), color="b")
axs[2,1].set_ylabel('b/a=6/5 d =p/8')

fig.suptitle('Фигуры Лиссажу', fontsize=16)
plt.show()
