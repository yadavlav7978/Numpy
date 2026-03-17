# NumPy replaces loops using vectorized operations and broadcasting, making computations faster and cleaner.

import numpy as np

prices=np.array([10,20,30])
dicount=10

final_prices=prices-(prices*dicount/100)

print(final_prices)