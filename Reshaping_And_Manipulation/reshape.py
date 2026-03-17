# In NumPy, reshaping means changing the dimensions (shape) of an array without changing its data.
# Reshape does not create a copy of the array it creates a view of the array

# Syntax: array.reshape(new_shape)

import numpy as np

arr=np.array([1,2,3,4,5,6])

new_arr=arr.reshape(2,3)

print(arr) # [1 2 3 4 5 6]

print(new_arr) # [[1 2 3]
               # [4 5 6]]

# “reshape() usually does NOT create a new separate array in memory — it just gives a different view of the same data.”
# Changing value in new array will also change the value in original array

new_arr[0][0] = 99

print(arr) # [99  2  3  4  5  6]
print(new_arr) # [[99  2  3]
               # [ 4  5  6]]

