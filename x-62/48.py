import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,1,250)
y_1=[x[i]**2 for i in range(250)]
y_2=[x[i]**3 for i in range(250)]
y_3=[np.cbrt(x[i]) for i in range(250)]
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)
plt.legend(("x^2","x^3","x^1/3"))
plt.xlabel("x", fontsize=16)
plt.ylabel("y", fontsize=16)
plt.grid(1)
plt.show()
