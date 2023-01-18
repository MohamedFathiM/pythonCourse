# Range

myRange = range(1, 100)

# for number in myRange:
#     print(number)


mySkills = {
    "HTML": "90%",
    "Css": "80%",
    "PHP": "70%"
}

print(mySkills)


for skill in mySkills:
    print(f"My Progress in Lang {skill} is : {mySkills.get(skill)}")
