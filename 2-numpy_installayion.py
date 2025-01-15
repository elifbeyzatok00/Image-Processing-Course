import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr2 = np.zeros((3, 4))
print(arr2)

arr3 = np.ones((3, 4))
print(arr3)

arr4 = np.ones((3, 4)) * 5
print(arr4)

arr5 = np.arange(10, 100, 10) # 10 to 90
print(arr5)

arr6 = np.arange(12) # 0 to 11
print(arr6)

arr7 = np.arange(12).reshape(3, 4)
print(arr7)


""" 
ndim - number of dimensions
shape - size of each dimension
size - total number of elements
dtype - data type of elements
"""

arr2d = np.arange(12).reshape(3, 4)
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr2d.ndim) # 2
print(arr3d.ndim) # 3

print(arr2d.shape) # (3, 4)
print(arr3d.shape) # (2, 2, 2)

print(arr2d.size) # 12
print(arr3d.size) # 8

print(arr2d.dtype) # int64
print(arr3d.dtype) # int64