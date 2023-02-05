# Function Packing , Unpacking Arguments **KWArgs

# def show_skills(*skills):
#     for skill in skills:
#         print(f"{skill}")


# show_skills("html", "css", "javascript")

# (** dict)
def show_skills(**skills):
    print(type(skills))
    for skill, value in skills.items():
        print(f"{skill} => {value}")


show_skills(html="90%", css="50%", javascript="10%")

myDict = {
    "name": "Ahmed",
    "age": 26,
    "progress": "100%"
}

show_skills(**myDict)
