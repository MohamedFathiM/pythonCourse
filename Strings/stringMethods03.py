# index() , find()

a = "Hello World"
print(a.index('l'))  # if not found throw exception
print(a.find('l'))  # if not found return -1


# ljust , rjust  --> justify text
o = "Osama"
print(o.rjust(9, "/"))
print(o.ljust(7, "/"))


# splitlines
f = """Hello
Everyone
I am Mohamed
"""

print(f.splitlines())

# expandtabs
g = "Hello\tWorld"

print(g.expandtabs(5))

# istitle() , isspace() , islower() , isidentifier() , isalpha() , isalnum()
