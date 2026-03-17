# Fancy indexing allows you to access multiple elements from an array at once by providing a list or array

import numpy as np

arr = np.arange(10, 101, 10)
# arr is [ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100]

new_arr = arr[[0, 2, 4, 2]] # Indices can be repeated

print(new_arr)
# Output: [10 30 50 30]



# 2D array

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result = arr[[0, 2]]   # select rows

print(result)
# Output: [[1 2 3]
#          [7 8 9]]


# Selecting specific elements (row & column)
result = arr[[0, 1], [1, 2]]
print(result)
# Output: [2 6]