# It is used for the checking the data types of the array

import numpy as np

arr1=np.array([1,2,3,4,5])

arr2=np.array([1,2,3,4,5.0])

print(arr1.dtype)
print(arr2.dtype)

# output -> int64
# output -> float64