# clear()

a = [1, 2, 6, 5, 3]
a.clear()

print(a)

# copy() => Shallow Copy
a = [1, 2, 5, 5, 3, 6]
b = a.copy()
print(a, b)

a.append(5)

print(a, b)


# count()
a = [1, 2, 5, 5, 3, 6]

print(a.count(5))

# index()
a = [1, 2, 5, 5, 3, 6]
print(a.index(5))


# insert()
a = [1, 2, 5, 5, 3, 6]
a.insert(0, 5)
a.insert(-1, "Ali")
print(a)


# pop(index)
a = [1, 2, 5, 5, 3, 6]
a.pop(0)
a.pop(-1)

print(a)
