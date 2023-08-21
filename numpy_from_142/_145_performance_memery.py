import numpy as np
import time
import sys

elements = 150000
my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

list_start = time.time()

list_result = [(n1 + n2) for n1,n2 in zip(my_list1,my_list2)]
print(f"List Time : {time.time() - list_start}")

array_start = time.time()
array_result = my_array1 + my_array2
print(f"array Time : {time.time() - array_start}")



## memory storage test
my_array = np.arange(100)
my_list = np.arange(100)

print(f"All Bytes Of Array : {my_array.itemsize * my_array.size}")
print(f"All Bytes Of List : {sys.getsizeof(1) * my_list.size}")
