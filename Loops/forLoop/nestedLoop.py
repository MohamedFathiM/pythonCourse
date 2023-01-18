# people = ["Ahmed", "Mohamed", "Sayed", "Ali"]

# skills = ["Html", " Css", "js"]

# for name in people:
#     print(f"{name} skills is : ")
#     for skill in skills:
#         print(f" - {skill}")


people = {
    "Mohamed": {
        "Html": "70%",
        "css": "30%",
        "Js": "90%",
    },
    "Ahmed": {
        "Html": "80%",
        "css": "10%",
        "Js": "90%",
    }
}


# print(people["Ahmed"]["Html"])

for name in people:
    print(f"Skills and progress for {name} is ")
    for skill in people[name]:
        print(f"{skill.upper()} => {people[name][skill]}")
