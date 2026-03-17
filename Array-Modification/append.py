# np.append() is used to add elements at the end of an array
# It return the new array and does not modify the original array

# Syntax: np.append(arr,values,axis=None)

# | Parameter | Meaning              |
# | --------- | -------------------- |
# | `array`   | Original array       |
# | `values`  | Values to append     |
# | `axis`    | Axis (for 2D arrays) |

import numpy as np


# Append in 1D array
arr=np.array([1,2,3,4,5])

new_arr=np.append(arr,6) 

print(new_arr) # [1 2 3 4 5 6]
print(arr) # [1 2 3 4 5]

# Append in 2D array along with rows
arr=np.array([[1,2,3],[4,5,6]])

new_arr=np.append(arr,[7,8,9],axis=0)

print(new_arr) # [[1 2 3]
                #  [4 5 6]
                #  [7 8 9]]

# Append in 2D array along with columns
new_arr=np.append(arr,[10,20],axis=1)
print(new_arr) # [[1 2 3 10]
                #  [4 5 6 20]]
