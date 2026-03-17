# concatenate() is used to join multiple arrays together (along a specific axis)
# It return the new array and does not modify the original array

# Syntax: np.concatenate((arr1,arr2,...),axis=0)
# axis=0 -> vertical stacking
# axis=1 -> horizontal stacking

import numpy as np

# Concatenate in 1D array
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

new_arr=np.concatenate((arr1,arr2),axis=0)

print(new_arr) # [1 2 3 4 5 6]


# Concatenate in 2D array along with rows
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])

new_arr=np.concatenate((arr1,arr2),axis=0)

print(new_arr) # [[1 2 3]
                #  [4 5 6]
                #  [7 8 9]
                #  [10 11 12]]

# Concatenate in 2D array along with columns
new_arr=np.concatenate((arr1,arr2),axis=1)
print(new_arr) # [[1 2 3 7 8 9]
                #  [4 5 6 10 11 12]]

