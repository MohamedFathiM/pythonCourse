import numpy as np


array = np.array([1,2,3,4,5,6])
multiArray = np.array([[1,25,6],[41,23,5]])


# Slicing [start,end,step]
# end not including
print(array[:1])
print(array[:])
print(array[::2])
print(array[1:3])

print("#" * 50)
print(multiArray[:1,:2])
