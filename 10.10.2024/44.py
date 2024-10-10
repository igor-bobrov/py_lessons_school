import numpy as np
lower_matrix = np.zeros((5, 5), dtype=int)
lower_matrix[1, 0] = 1
lower_matrix[2, 1] = 2
lower_matrix[3, 2] = 3
lower_matrix[4, 3] = 4
print(lower_matrix)
