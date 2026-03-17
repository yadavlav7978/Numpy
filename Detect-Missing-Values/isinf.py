# np.isinf() is used to check for infinite values in an array.

# In NumPy:
# np.inf → positive infinity
# -np.inf → negative infinity

import numpy as np

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

print(np.isinf(arr))
# Output: [False False  True False  True False]

# Count infinite values
print(np.sum(np.isinf(arr)))
# Output: 2

# Replace infinite values with 0
arr[np.isinf(arr)] = 0
print(arr)
# Output: [1. 2. 0. 4. 0. 6.]

# Replace with 99
arr[np.isinf(arr)] = 99
print(arr)
# Output: [1. 2. 99. 4. 99. 6.]

# ------------------ Useful Functions for Infinity ------------------
# Function	Purpose
# np.isinf()	Detect infinity
# np.isposinf()	Detect positive infinity
# np.isneginf()	Detect negative infinity
# np.isfinite()	Detect finite numbers (not infinity)
