# all()
# any()
# bin()
# id()


x = [1, 2, 3, 5, '']

# كل العناصر لازم تكون true
if all(x):
    print("All Elements is true")
else:
    print("There is at least one element is false")

# في عنصر واحد ب true
if any(x):
    print("There is at least one element is false")
else:
    print("All Elements is true")

# Convert to Binary
print(bin(100))

a = 1
b = 2

# id of variable in memory
print(id(a))
print(id(b))
