# Slicing extracts a range or subset of elements
# Syntax: array[start:stop:step]

import numpy as np

# 1D Array Slicing

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[1:5])     # Output: [1 2 3 4] (indices 1 up to, but not including, 5)
print(arr[2:])      # Output: [2 3 4 5 6 7 8 9] (from index 2 to the end)
print(arr[:4])      # Output: [0 1 2 3] (from the beginning to index 4, excluded)
print(arr[::2])     # Output: [0 2 4 6 8] (every other element)
print(arr[-3:-1])   # Output: [7 8] (from the third to the second last element)
print(arr[::-1])    # Output: [9 8 7 6 5 4 3 2 1 0] (reverses the array)


# Multidimensional Array Slicing

# Apply slicing to each dimension using commas.

arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Access the entire second column (all rows, index 1 column)
print(arr_2d[:, 1]) # Output: [20 50 80]

# Access the sub-array from the second row onwards, and columns 0 to 1
# (rows 1:end, columns 0:2 (exclusive))
print(arr_2d[1:, :2])
# Output:
# [[40 50]
#  [70 80]]

