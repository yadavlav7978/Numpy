## What is NumPy?

NumPy is a Python library used for fast numerical and mathematical computations, especially when working with arrays and matrices.

---

## Why is NumPy faster than Python lists?

### 1. Faster Computations
- NumPy is implemented in C (a low-level language), which makes it very fast.
- Python lists are implemented in pure Python, so they are slower.
- NumPy operations can be significantly faster (often up to 50x) than standard Python list operations.

---

### 2. Memory Efficient
- NumPy arrays are **homogeneous**, meaning they store only one data type (e.g., all integers or all floats).
- Elements are stored in a **contiguous block of memory**, allowing faster access.
- Since all elements are of the same type, NumPy stores only the raw values without extra type information.

In contrast:
- Python lists can store mixed data types (e.g., int, float, string).
- Each element requires additional memory to store its type and reference.
- This makes lists consume more memory compared to NumPy arrays.

---

### 3. Vectorization (No Loops Needed)
- NumPy performs operations on entire arrays at once.
- No need to write explicit loops.
- This leads to cleaner and faster code.

## NumPy vs Python Lists

| Feature                  | NumPy Array                          | Python List                      |
|-------------------------|--------------------------------------|----------------------------------|
| Speed                   | Very fast (C implementation)         | Slower (Python-based)            |
| Memory Usage            | Less (homogeneous, compact storage)  | More (stores type + reference)   |
| Data Type               | Single type only (homogeneous)       | Multiple types allowed           |
| Execution               | Vectorized (no loops needed)         | Requires loops                   |
| Mathematical Operations | Built-in, optimized                  | Limited, manual implementation   |
| Scalability             | Best for large datasets              | Not ideal for large data         |

Example:
```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr * 2)  # Output: [2 4 6]

