import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0,2*np.pi,1000)


def x(t, c):
    a = [5, 10]
    b = [15, 15]
    return (a[c] + b[c])*np.cos(t) - a[c]*np.cos((a[c] + b[c])*t/a[c]) 

def y(t, c):
    a = [5, 10]
    b = [15, 15]
    return (a[c] + b[c])*np.sin(t) - a[c]*np.sin((a[c] + b[c])*t/a[c])

fig, axs = plt.subplots(1, 2, figsize=(10,20))
axs[0].plot(x(t, 0), y(t, 0), color="r")
axs[0].set_title('b/a=3')

axs[1].plot(x(t, 1), y(t, 1), color="g")
axs[1].set_title('b/a=3/2')

fig.suptitle('Кривые Эпициклоида', fontsize=16)
plt.show()
