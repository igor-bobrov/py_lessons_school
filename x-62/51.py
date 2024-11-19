import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0,2*np.pi,1000)


def x(t, c):
    a = [5, 5, 13, 8]
    b = [13, 8, 5, 8]
    return(a[c]*np.cos(t)**2 + b[c]*np.cos(t))

def y(t, c):
    a = [5, 5, 13, 8]
    b = [13, 8, 5, 8]
    return(a[c]*np.cos(t)*np.sin(t) + b[c]*np.sin(t))

fig, axs = plt.subplots(2, 2, figsize=(10,10))
axs[0,0].plot(x(t, 0), y(t, 0), color="r")
axs[0,0].set_title('b>2a')

axs[0,1].plot(x(t, 1), y(t, 1), color="r")
axs[0,1].set_title('a<b<2a')

axs[1,0].plot(x(t, 2), y(t, 2), color="g")
axs[1,0].set_ylabel('a>b')
  
axs[1,1].plot(x(t, 3), y(t, 3), color="b")
axs[1,1].set_ylabel('a=b')

fig.suptitle('Улитки Паскаля', fontsize=16)
plt.show()
