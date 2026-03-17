import numpy as np

arr=np.array([1,2,np.nan,3,4,np.nan])

print(np.isnan(arr))
# Output: [False False  True False False  True]


# Count missing values
print(np.sum(np.isnan(arr)))
# Output: 2

# ------------------ Replace Missing Values ------------------

# Replace with 0
arr[np.isnan(arr)] = 0
print(arr)
# Output: [1. 2. 0. 3. 4. 0.]

# Or Replace with 99
arr[np.isnan(arr)] = 50
print(arr)
# Output: [1. 2. 99. 3. 4. 99.]


# ------------------ Useful Functions for Missing Values ------------------
# Function	               Purpose
# np.isnan()	          Detect NaN
# np.nanmean()	          Mean ignoring NaN
# np.nansum()	          Sum ignoring NaN
# np.nanmax()	          Max ignoring NaN
# np.nanmin()	          Min ignoring NaN

