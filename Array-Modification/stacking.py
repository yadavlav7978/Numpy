# Stacking is used to join multiple arrays together (along a specific axis)
# There are 3 common ways:

# np.vstack() → vertical stack
# np.hstack() → horizontal stack
# np.stack() → new dimension

import numpy as np

#----------------------- Stacking in 1D array------------------

# Vertical stacking
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

new_arr=np.vstack((arr1,arr2))
print(new_arr) # [[1 2 3]
                #  [4 5 6]]

# Horizontal stacking
new_arr=np.hstack((arr1,arr2))
print(new_arr) # [1 2 3 4 5 6]

# Stacking
new_arr=np.stack((arr1,arr2),axis=0)
print(new_arr)


#----------------------- Stacking in 2D array------------------
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])

new_arr=np.vstack((arr1,arr2))
print(new_arr) # [[1 2 3]
                #  [4 5 6]
                #  [7 8 9]
                #  [10 11 12]]

new_arr=np.hstack((arr1,arr2))
print(new_arr) # [[1 2 3 7 8 9]
                #  [4 5 6 10 11 12]]

new_arr=np.stack((arr1,arr2),axis=0)
print(new_arr)
