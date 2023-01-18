print(1, 2, 3, 4)

myList = [1, 2, 5, 3, 4]

print(myList)

# unpacking
print(*myList)


def say_hello(*people):
    for name in people:
        print(f"Hello {name}")


say_hello("Mohamed", "Ahmed", "ali", "Fathi", "Alaa")


def show_details(name, *skills):
    print(f"Hello {name}, you skills is: ")
    for skill in skills:
        print(f"{skill}")


show_details("Mohamed", "HTML", "CSS", "JS", "PSD")
