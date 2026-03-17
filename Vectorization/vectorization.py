# Vectorization = applying operations to entire arrays at once without writing explicit Python loops.

import numpy as np

# Example 1: Simple Addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vectorized operation
result = a + b
print(result)  # [5 7 9]

# Without vectorization (using loops)
result_loop = []
for i in range(len(a)):
    result_loop.append(a[i] + b[i])
print(result_loop)  # [5 7 9]

# Example 2: Squaring elements
arr = np.array([1, 2, 3, 4])

# Vectorized operation
squared = arr ** 2
print(squared)  # [1 4 9 16]


# Example 3: Conditional operations
arr = np.array([1, -2, 3, -4, 5])

# Vectorized operation
result = np.where(arr > 0, arr * 2, arr)
print(result)  # [ 2 -4  6 -8 10]

# Without vectorization
result_loop = []
for x in arr:
    if x > 0:
        result_loop.append(x * 2)
    else:
        result_loop.append(x)
print(result_loop)  # [ 2 -4  6 -8 10]



# Example 5: Matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Vectorized operation
result = np.dot(a, b)
print(result)  # [[19 22]
               #  [43 50]]


# Example 6: Broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])

# Vectorized operation with broadcasting
result = a + b
print(result)  # [[11 22 33]
               #  [14 25 36]]


# Example 7: Aggregations
arr = np.array([1, 2, 3, 4, 5])

# Vectorized operations
print(np.sum(arr))      # 15
print(np.mean(arr))     # 3.0
print(np.max(arr))      # 5
print(np.min(arr))      # 1
print(np.std(arr))      # 1.4142135623730951
print(np.var(arr))      # 2.0
print(np.cumsum(arr))   # [ 1  3  6 10 15]
print(np.cumprod(arr))  # [  1   2   6  24 120]

#
# Example 9: Comparison operations
a = np.array([1, 2, 3])
b = np.array([1, 3, 3])

# Vectorized operations
print(a == b)  # [ True False  True]
print(a != b)  # [False  True False]
print(a < b)   # [False  True False]
print(a > b)   # [False False False]
print(a <= b)  # [ True  True  True]
print(a >= b)  # [ True False  True]

