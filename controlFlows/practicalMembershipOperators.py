admins = ["Ahmed", "Mohamed", "Fathi", "Ali"]

name = input("Enter Your Name ").strip().capitalize()

if name in admins:
    print(f"Welcome Back {name}")
    option = input("Delete Your name or Update ? ").strip().capitalize()

    if option == 'Delete':
        admins.pop(admins.index(name))
        print(admins)
    elif option == 'Update':
        newName = input("Enter New Name ? ").strip().capitalize()
        admins[admins.index(name)] = newName
        print(admins)
    else:
        print("Your Choose is wrong")
else:
    status = input("Not Admin , Add you Y, N ? ").strip().capitalize()
    if status in ["Y", "Yes"]:
        admins.append(name)
        print(admins)
    else:
        print("Thanks For Using Our Program")
