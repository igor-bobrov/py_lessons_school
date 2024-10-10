import numpy as np
random_array = np.random.rand(10, 10)
print(random_array, "Суммы элементов в каждой строке:", np.sum(random_array, axis=1).reshape(-1, 1), sep = '\n')
