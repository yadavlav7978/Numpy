# Broadcasting = It allows arithmetic operations on arrays of different shapes without manually reshaping or creating explicit loops


import numpy as np


# ----------------- 1. Simple Example (1D + Scalar)
arr = np.array([1, 2, 3])

result = arr + 10

print(result) # [11 12 13]

# Here:
# 10 is broadcast across the array
# NumPy treats 10 like [10, 10, 10]

#-------------------- 2. 1D + 1D Broadcasting

a = np.array([1, 2, 3])
b = np.array([10])

print(a + b) # [11 12 13]

# Here:
# b is broadcast across a
# NumPy treats b like [10, 10, 10]

#-------------------- 3. 2D + 1D Broadcasting

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

print(a + b) # [[11 22 33]
             #  [14 25 36]]

# Here:
# b is broadcast across a
# NumPy treats b like [[10, 20, 30],
#                      [10, 20, 30]]


# 🔷------------------ 4. Broadcasting Rules (Very Important 🔥) ---------------------------

# NumPy compares shapes from right to left

# Dimensions must be:Equal OR
# One of them is 1


# Example of ValueError
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20])


# print(a + b)  # ValueError: operands could not be broadcast together with shapes (2,3) (2,)

# 🔷-------------- 5. How Broadcasting Works (Step-by-step) ------------------------------------

# Example: (2,3) + (3,)

# 👉 Step 1: Align shapes

# (2,3)
# (1,3)

# 👉 Step 2: Expand smaller array

# (2,3)
# (2,3)