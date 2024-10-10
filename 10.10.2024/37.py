import numpy as np
A = np.ones((5, 5), dtype = np.int64)
B = np.zeros((5, 5), dtype=int)
np.fill_diagonal(B, 3)
C = A + B
D = 3*C
print('#1', A, '#2', B, '#3' , C, '#4', D, '#5', 'max(D) = ' + str(np.max(D)), 'sum(D) = ' + str(np.sum(D)), np.diag(D), sep = '\n')

