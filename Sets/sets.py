# ---------------------------
# -- set --
# [1] Set items are enclosed in curly braces
# [2] Set Items are not ordered and not indexed
# [3] Set Indexing and slicing can not be Done
# [4] Set Has Only Immutable Data Types (Numbers , Strings,Tuples) List and Dict Are not
# [5] Set Items must be unique
#
# ---------------------------


# not ordered and not indexed
mySet = {"Mohamed", "Ahmed", 100}
print(mySet)
print(type(mySet))
# print(mySet[0]) => throw an exception


# Has Only Immutable Data Types
# mySet = {"Mohamed", 10, 100.2, True, [1, 2, 3]}  # unhashable type: 'list'
print(mySet)

mySet = {"Mohamed", 10, 100.2, True, (1, 2, 3)}  # unhashable type: 'list'
print(mySet)


# Items is unique
mySet = {2, 2, 3, 5, 1, "Mohamed", "Ahmed", "Mohamed"}
print(mySet)
