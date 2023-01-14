fName = input("What is your first name ? ")
mName = input("What is your middle name ? ")
lName = input("What is your last name ? ")

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName}")
