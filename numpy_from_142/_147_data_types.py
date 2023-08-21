import numpy as np

a = np.array([1,2,3])
b = np.array([1.5,2.5,3.20])
c = np.array(['a','v','c'])


print(a.dtype)
print(b.dtype)
print(c.dtype)

print("#" * 50)

# Create array with specific data type
d = np.array([1,2,3],dtype='f') # float , 'float' , 'f'
e = np.array([1.5,2.2,3.4],dtype='int') # int , 'int' ,'i'

print(d.dtype)
print(e.dtype)

print("#" * 50)

g = np.array([1.5,2.2,3.4])
g = g.astype('int')

print(g.dtype)


# Test Capacity
h = np.array([100,200,300,400],dtype='f')
print(h.dtype)
print(h[0].itemsize)

# float 64
h = h.astype('float')
print(h.dtype)
print(h[0].itemsize)
