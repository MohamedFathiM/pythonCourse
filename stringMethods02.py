# split - rsplit

a = "My Name is Mohamed"
print(a.split())

b = "My-Name-is-Mohamed"
print(b.split('-'))

print(b.split('-', 2))

print(b.rsplit('-', 2))


# center
print("Mohamed".center(9))
print("Mohamed".center(9, '@'))
print("Mohamed".center(8, '@'))

# count
print('Hello World From PHP and Hello World From Python'.count('Hello', 0, 25))


# startswith , endswith
n = "I Love Python"
print(n.startswith('I'))
print(n.endswith('n'))
print(n.endswith('e', 2, 6))
