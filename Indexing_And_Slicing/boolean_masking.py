# Used to filter data based on conditions (True/False)

import numpy as np

arr=np.array([10,20,30,45,15,28])

print(arr[arr>20])
# Output: [30 45 28]


arr = np.arange(10, 61, 10)
# arr is [10, 20, 30, 40, 50, 60]

# Create a boolean mask: select elements greater than 30
mask = arr > 30
# mask is [False, False, False, True, True, True]

# Apply the mask to the array
filtered_elements = arr[mask]
print(filtered_elements)
# filtered_elements is [40, 50, 60]

# Combine conditions (e.g., greater than 10 AND less than 50)
combined_mask = (arr > 10) & (arr < 50)
# combined_mask is [False, True, True, True, False, False]
filtered_combined = arr[combined_mask]
print(filtered_combined)
# filtered_combined is [20, 30, 40]
