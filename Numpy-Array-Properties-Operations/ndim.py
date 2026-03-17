# Used for getting the dimension of the array
# It will return the number of dimensions of the array
# For 1d array it will return 1, For 2d array it will return 2, For 3d array it will return 3 and so on


import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# output -> 1
# output -> 2
# output -> 3
