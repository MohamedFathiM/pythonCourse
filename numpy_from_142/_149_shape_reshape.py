import numpy as np


a = np.array([10,20,30])

print(a.ndim)
print(a.shape)

print('#' * 50)

c = np.array([[1,4],[5,9]])
print(c.ndim)
print(c.shape)

print('#' * 50)

b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(b.ndim)
print(b.shape)

reshaped = b.reshape(2,6)
print(b.ndim)
print(reshaped)


d = np.array([[2,7],[10,5]])
d_reshaped = d.reshape(-1) # = ravel
print(d_reshaped)
