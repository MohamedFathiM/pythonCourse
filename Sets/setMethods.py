# clear()
a = {1, 2, 5, 3, 5}
a.clear()

print(a)


# union()
b = {"1", "2", "3"}
c = {"A", "b"}
x = {"N", "D"}
print(b | c)
print(b.union(c, x))


# add()

d = {1, 2, 3, 5}
d.add(9)
d.add(10)
print(d)

# copy()
d = {1, 2, 3, 5}
f = d.copy()
d.add("Ahmed")

print(f, d)

# remove()
g = {1, 2, 6, 5, 3}
g.remove(1)
# g.remove(7) # throw Exception
print(g)


# discard()
h = {1, 2, 6, 5, 3}
h.discard(1)
h.discard(7)
print(h)


# pop()
i = {"A", True, 1, 2, 5, 3, 5, 6}
print(i.pop())  # return random element from set and delete it
print(i)

# update()
i = {1, 2, 3, 6, 5, 3}
k = {2, "A", "B"}
myList = ["Html", "css"]

i.update(k)
i.update(myList)
print(i)
