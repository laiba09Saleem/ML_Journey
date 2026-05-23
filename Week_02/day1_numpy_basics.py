'''What is NumPy & Why it Matters
Normal Python List     →   Slow, no math operations
NumPy Array            →   Super fast, built for math & ML
Every ML model internally works with NumPy arrays. Pandas, Scikit-learn, TensorFlow — all built on NumPy.'''

# --------------- Part A — Creating Arrays ---------------- #

import numpy as np

# 1. From Python List

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# 2D Array (like table or matrix)
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(matrix)
print(matrix.shape)

# Useful array creators

zeros = np.zeros((3,3))
ones = np.ones((2,4))
rng = np.arange(0,20,2)
rand = np.random.rand(3,3)

print(zeros)
print(ones)
print(rng)
print(rand)

# --------------- Part B — Array Properties ---------------- #

data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(data.shape)
print(data.ndim)
print(data.size)
print(data.dtype)

reshaped = data.reshape(3, 2)
print(reshaped)

flat = data.flatten()
print(flat)

# --------------- Part C — Indexing & Slicing ---------------- #

arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[0])
print(arr[-1])

# Slicing
print(arr[1:4])
print(arr[:3])

# 2D Indexing

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(matrix[0,0])
print(matrix[1,2])
print(matrix[0, :])
print(matrix[:, :1])

# Boolean Filtering

data = np.array([15, 42, 8, 73, 29, 61])
filtered = data[data > 30]
print(filtered)

# --------------- Part D — Math Operations ---------------- #

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

# Element wise operation
print( a + b)
print(a * b)
print(a / b)
print (a ** 2)

# Aggregate operation

print(np.sum(b))
print(np.mean(b))
print(np.max(b))
print(np.min(b))
print(np.std(b))
