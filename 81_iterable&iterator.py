## Iterable
# Object contains data that can be iterated upon
# Examples (string,list,set,tuple,dictionary)


## Iterator
# Object Used to iterator over iterable using next() method return 1 element at a time
# You can generate iterable from iterable when using iter() method
# for loop already calls iter() method on the iterable behind the scene
# Gives "StopIteration" if theres no next element

myString = "mohamed"

# for char in myString :
#     print(char,end=" ")

myIterator = iter(myString)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
