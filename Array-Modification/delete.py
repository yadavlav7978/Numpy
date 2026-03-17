# np.delete() is used to delete elements from an array in specified position(index)
# Syntax: np.delete(arr,index,axis=None)

import numpy as np

# Delete in 1D array
arr=np.array([1,2,3,4,5])

new_arr=np.delete(arr,0)

print(new_arr) # [2 3 4 5]
print(arr) # [1 2 3 4 5]

# Delete in 2D array along with rows
arr=np.array([[1,2,3],[4,5,6]])

new_arr=np.delete(arr,0,axis=0)

print(new_arr) # [[4 5 6]]

# Delete in 2D array along with columns
new_arr=np.delete(arr,0,axis=1)
print(new_arr) # [[2 3]
                #  [5 6]]