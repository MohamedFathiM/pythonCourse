myNumbers = [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:
    if number % 2 == 0:  # even
        print(f"{number} is Even. ")
    else:
        print(f"The Number {number} is Odd. ")

else:
    print("the Loop is finished")


myName = "Mohamed"

for letter in myName:
    print(f"[ {letter.upper()} ]")
