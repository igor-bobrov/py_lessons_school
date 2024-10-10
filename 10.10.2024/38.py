import numpy as np
A = np.linspace(-2*np.pi, 2*np.pi, 20)
B = np.sin(A)**2 + np.cos(A)**2
print(A, B, np.all(B) == 1, sep = '\n')
