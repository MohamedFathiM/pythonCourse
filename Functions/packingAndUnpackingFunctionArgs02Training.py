def show_skills(name, *skills, **skillsWithProgress):
    print(f"Hello {name} \nSkills without progress : ")
    for skill in skills:
        print(f"- {skill}")
    print(f"\nSkills With Progress : ")
    for key, value in skillsWithProgress.items():
        print(f"{key} => {value}")


show_skills("Mohamed",*( "Html", "css", "js"), **{"html": "80%", "Css": "50%"})
