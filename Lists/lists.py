# LISTS
# Lists are not array
# List Items are enclosed in square brackets
# list are ordered , to use index to access item
# list are mutable => add,delete ,edit
# list can have different data types

myList = ["One", "two", "three", 1, 500, 2, True]

print(myList)
print(myList[1])
print(myList[-5])
print(myList[1:4])


myList[1] = "Changed Value"
print(myList)


myList[1:2] = []
print(myList)
