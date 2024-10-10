import numpy as np
boundary_array = np.zeros((10, 10), dtype=int)
boundary_array[0, :] = 1
boundary_array[-1, :] = 1
boundary_array[:, 0] = 1
boundary_array[:, -1] = 1
print(boundary_array)
