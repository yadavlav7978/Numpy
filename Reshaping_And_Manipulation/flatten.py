# Flattening in NumPy refers to the process of converting a multidimensional array into a one-dimensional (1D) array. 
# This can be achieved using several methods, primarily .flatten(), .ravel(), and .reshape(-1).

import numpy as np

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr.flatten())
print(arr.ravel())
print(arr.reshape(-1))

# Difference between flatten() and ravel()
# flatten() always returns a copy of the array
# ravel() returns a view of the array

print("\n")
# Changing value in flatten array will not change the value in original array

arr_flat=arr.flatten()
arr_flat[0]=99
print(arr)
print(arr_flat)

# Changing value in ravel array will change the value in original array

arr_ravel=arr.ravel()
arr_ravel[0]=99
print(arr)
print(arr_ravel)