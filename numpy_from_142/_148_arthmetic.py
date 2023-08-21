import numpy as np


a = np.array([10,20,30])
b = np.array([5,2,4])

print(a + b) # [15 22 34]
print(a - b) # [ 5 18 26]
print(a * b) # [ 50  40 120]
print(a / b) # [ 2.  10.   7.5]


print('#' * 50)

c = np.array([[1,4],[5,9]])
d = np.array([[2,7],[10,5]])

print(c + d) # [[ 3 11][15 14]]
print(c - d) # [[-1 -3][-5  4]]
print(c * d) # [[ 2 28][50 45]]
print(c / d) # [[0.5 0.57142857][0.5 1.8]]

print('#' * 50)
# min , max , sum
g = np.array([10,20,30])

print(g.min())
print(g.max())
print(g.sum())


print('#' * 50)
h = np.array([[1,4],[5,9]])
print(h.min())
print(h.max())
print(h.sum())


# Ravel (array with one dimension)
j = np.array([[1,4],[5,9]])

print(j.ravel())
