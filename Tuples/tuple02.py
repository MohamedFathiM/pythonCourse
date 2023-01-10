# Tuples


# Detect if single item is tuple or string
myTuple1 = ("Mohamed",)
myTuple2 = "Mohamed",


print(type(myTuple1))
print(type(myTuple2))
print(len(myTuple2))

# tuple Concat
a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", True) + b
print(c)
print(d)

# Tuple , List , String Repeat (*)
myString = "Mohamed"
myList = [1, 2]
myTuple = ("Mohamed", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)


# count()
a = (1, 5, 5, 5, 6, 3, 5, 1, 6)
print(a.count(5))


# index()
b = (1, 5, 5, 5, 6, 3, 5, 1, 6)
print("The Position Of index is : {:d}".format(b.index(5)))
print(f"The Position of index is:{b.index(5)}")


# Tuple Destruct
a = ("A", "B", 5, "C")
x, y, _, z = a
print(x, y, z)
