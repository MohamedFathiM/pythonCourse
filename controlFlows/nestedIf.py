name = "Mohamed"
isStudent = True
country = "KSA"
course = "Python Course"
price = 100

if country == "Egypt" or country == "KSA":
    if isStudent:
        print(f"Hello {name} because you are from {country} And Student")
        print(f"Hello {name} the course {course} price is ${price - 90}")
    else:
        print(f"Hello {name} because you are from {country}")
        print(f"Hello {name} the course {course} price is ${price - 80}")

else:
    print(f"Hello {name} because you are from {country}")
    print(f"Hello {name} the course {course} price is ${price - 30}")
