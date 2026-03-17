# it is used for the changing the data types of the array
# Syntax: np.astype(array, dtype)

import numpy as np

arr_float=np.array([1,2.5,3,4,5.6,7.8])

print(arr_float.dtype)   # float64
print(arr_float)         # [1.  2.5 3.  4.  5.6 7.8]

arr_int=np.astype(arr_float,int)
print(arr_int.dtype)     # int64
print(arr_int)           # [1 2 3 4 5 7]

