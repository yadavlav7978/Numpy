# np.insert() is used to insert values into an array at a specified position.
# It return the new array and does not modify the original array.

# Syntax: np.insert(arr,index,values,axis=None)
# arr: array to insert values into
# index: index at which to insert values
# values: values to insert
# axis: axis along which to insert values , axis=0 for rows, axis=1 for columns

import numpy as np

# Insert in 1D array
arr=np.array([1,2,3,4,5])

new_arr=np.insert(arr,0,10)

print(new_arr) # [10  1  2  3  4  5]
print(arr) # [1 2 3 4 5]

# Insert in 2D array along with rows

arr=np.array([[1,2,3],[4,5,6]])

new_arr=np.insert(arr,0,[10,20,30],axis=0)

print(new_arr) # [[10 20 30]
                #  [ 1  2  3]
                #  [ 4  5  6]]


# Insert in 2D array along with columns
new_arr=np.insert(arr,0,[10,20],axis=1)
print(new_arr) # [[10  1  2  3]
                #  [20  4  5  6]]

# ValueError: could not broadcast input array from shape (1,2) into shape (1,3)
new_arr=np.insert(arr,0,[10,20],axis=0)
print(new_arr)


