import numpy as np
rm = np.random.rand(7, 7)
ms = rm - rm.mean(axis=1, keepdims=True)
print(rm, rm.mean(axis=1, keepdims=True), ms, sep = "\n\n")
