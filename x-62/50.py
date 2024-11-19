import matplotlib.pyplot as plt
import numpy as np
r = 50
h1 = 30
h2 = 50
h3 = 80
x, y = [],[]
t = np.linspace(0,50,1000)

for i in range(0,1000):
    x.append(r*t[i]-h1*np.sin(t[i]))
    y.append(r-h1*np.cos(t[i]))
    
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(3, 1, 1)
plt.plot(x,y, color="r")
ax1.set_ylabel('h<r')
x, y = [],[]
for i in range(0,1000):
    x.append(r*t[i]-h2*np.sin(t[i]))
    y.append(r-h2*np.cos(t[i]))

ax2 = fig.add_subplot(3, 1, 2)
plt.plot(x,y, color="g")
ax2.set_ylabel('h=r')
x, y = [],[]
for i in range(0,1000):
    x.append(r*t[i]-h3*np.sin(t[i]))
    y.append(r-h3*np.cos(t[i]))
    
ax3 = fig.add_subplot(3, 1, 3)
plt.plot(x,y, color="b")
ax3.set_ylabel('h>r')

fig.suptitle('Графики Колеса', fontsize=16)
plt.show()
