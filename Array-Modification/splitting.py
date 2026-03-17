# Splitting = breaking one array into multiple smaller arrays
# np.split() → split into equal parts
# np.hsplit() → column split
# np.vsplit() → row split

import numpy as np

# Split in 1D array
arr=np.array([1,2,3,4,5,6])

new_arr=np.split(arr,3)
print(new_arr) # [array([1, 2]), array([3, 4]), array([5, 6])]

# Split in 2D array along with rows
arr=np.array([[1,2,3],[4,5,6]])

new_arr=np.split(arr,2,axis=0)
print(new_arr) # [array([[1, 2, 3]]), array([[4, 5, 6]])]

# Split in 2D array along with columns
new_arr=np.split(arr,3,axis=1)
print(new_arr) # [array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]


# vsplit -> vertical split
arr=np.array([[1,2,3],[4,5,6]])
new_arr=np.vsplit(arr,2)
print(new_arr) # [array([[1, 2, 3]]), array([[4, 5, 6]])]

# hsplit -> horizontal split
new_arr=np.hsplit(arr,3)
print(new_arr) # [array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]