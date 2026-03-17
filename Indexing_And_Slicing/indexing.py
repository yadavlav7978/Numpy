# Indexing is used to access individual elements. Indices in NumPy are zero-based, and negative indices count from the end of the array.

import numpy as np

# 1-Dimension Array
arr=np.array([1,2,3,4,5,6,7,8,9])

print(arr[0]) 
print(arr[-1])

# 2D Array
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr_2d[0,0])
print(arr_2d[1,1])
print(arr_2d[2,2])

# 3D Array
arr_3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr_3d[0,0,0])
print(arr_3d[1,1,1])
print(arr_3d[2,2,2])
