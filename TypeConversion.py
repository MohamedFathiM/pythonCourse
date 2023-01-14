# str()
a = 10
print(type(a))
print(type(str(a)))
print("=" * 40)

# tuple()
c = "Mohamed"
d = [1, 2, 3,  4, 5]
e = {"A", "B", "C"}
f = {"A": 1, "b": 2}

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
print("=" * 40)

# print(tuple(500)) throw error , because it is not iterable

# list()
c = "Mohamed"
d = (1, 2, 3,  4, 5)
e = {"A", "B", "C"}
f = {"A": 1, "b": 2}

print(list(c))
print(list(d))
print(list(e))
print(list(f))
print("=" * 40)


# set()
c = "Mohamed"
d = (1, 2, 3,  4, 5)
e = ["A", "B", "C"]
f = {"A": 1, "b": 2}

print(set(c))
print(set(d))
print(set(e))
print(set(f))
print("=" * 40)


# dict()
d = (("A", 1), ("B", 2))
e = [["A", 1], ["B", 2]]
# f = {{"a", 1}, {"b", 2}} # unhashable type

print(dict(d))
print(dict(e))
# print(dict(f))
print("=" * 40)
