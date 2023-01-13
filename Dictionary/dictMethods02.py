# setdefault()
user = {
    "name": "Mohamed",
}

print(user)
print(user.setdefault("age", 28))
print(user)
print("=" * 40)

# popitem()
member = {
    "name": "Mohamed",
    "skill": "PS4"
}

print(member)
member.update({"Rating": 88})
print(member.popitem())
print("=" * 40)

# items
member = {
    "name": "Mohamed",
    "skill": "PS4"
}

allItems = member.items()
print(member)
member["age"] = 28
print(allItems)
print("=" * 40)

# fromkeys()
a = ("one", "two", "three")
b = "X"

print(dict.fromkeys(a, b))
