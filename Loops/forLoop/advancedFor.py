mySkills = {
    "HTML": "80%",
    "CSS": "90%",
    "JS": "70%",
    "PHP": "80%"
}


# for skill in mySkills:
#     print(f"{skill} => {mySkills[skill]}")


# for key, value in mySkills.items():
#     print(f"{key} => {value}")


myUltimateSkills = {
    "HTML": {
        "Main": "80%",
        "PugJs": "70%"
    },
    "CSS": {
        "Main": "80%",
        "Sass": "70%"
    }
}


for main_key, main_value in myUltimateSkills.items():
    print(f"{main_key} => ")
    for child_key, child_value in main_value.items():
        print(f"- {child_key} => {child_value}")
