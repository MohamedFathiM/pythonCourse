import numpy as np


my_list = [1,2,'A','B' , True]
my_array = np.array([1,2,'A','B' , True])


# address of elements in list is different , every element is storing in specific location
print(id(my_list[0]))
print(id(my_list[1]))

# address of elements in array is same ,all elements are storing in specific location
print(id(my_array[1]))
print(id(my_array[1]))
print("*" * 50)


# type of data

# data in list is not similar
print(my_list)
print(type(my_list[0]))

# convert all data to string
print(my_array)
print(type(my_array[0]))

print("*" * 50)

my_array2 = np.array([1,2])
print(type(my_array2[0]))

my_array3 = np.array([1,2,10.5])
print(type(my_array3[0]))
