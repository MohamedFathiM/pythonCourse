import numpy as np

# print(dir(np))

my_list = [1,2,3,4,5,6]
my_array = np.array(my_list)


print(my_list)
print(my_array)

print(type(my_list))
print(type(my_array))

# accessing elements
print(my_array[0])
print(my_list[0])


print("*" * 50)

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

print(arr1)


# multi dimensions arrays

# zero dimensions
a = np.array(10)

# one dimensions
b = np.array([10,20])

# two dimensions
c = np.array([[10,20],[25,23]])

# three dimensions
d = np.array([[[10,20]],[[25,23]]])


print(d[0][0][-1])
print(d[0,0,-1])
print(c[0][0])


print("*" * 50)

# get number of dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# custom dimensions
my_custom_array = np.array([1,2,3],ndmin=3)

print(my_custom_array.ndim)
print(my_custom_array)
print(my_custom_array[0][0][0])
