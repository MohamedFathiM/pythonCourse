# enumerate
mySkills = ["HTMl", 'css', 'js', 'php']

mySkillsWithCounter = enumerate(mySkills, 20)

for c, s in mySkillsWithCounter:
    print(f"{c} - {s}")

print("#" * 50)


# help
print(help(print))


# reversed(iterable)
myString = "Elzero"
print(reversed(myString))

for letter in reversed(myString) :
    print(letter)
