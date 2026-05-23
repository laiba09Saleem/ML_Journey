'''1. Create a 4x4 matrix of random numbers (use np.random.rand)
'''

import numpy as np
matrix = np.random.rand(4,4)
print(matrix)

'''2. Print its shape, size, and data type'''

print(matrix.shape)
print(matrix.size)
print(matrix.dtype)

''' 3. Extract the entire 3rd row'''

print(matrix[2])

'''4. Extract the entire 2nd column'''
print(matrix[:, 1])

'''5. Find the max, min, and mean of the entire matrix'''
print(np.max(matrix))
print(np.min(matrix))
print(np.mean(matrix))

'''6. Filter and print only values greater than 0.5'''
filtered = matrix[matrix > 0.5]
print(filtered)

'''7. Reshape it into a 2x8 matrix'''
reshaped = matrix.reshape(2, 8)
print(reshaped)
