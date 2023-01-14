name = "Mohamed"
country = "KSA"
course = "Python Course"
price = 100

if country == "Egypt":
    print(f"Hello {name} because you are from {country}")
    print(f"Hello {name} the course {course} price is ${price - 80}")
elif country == "KSA":
    print(f"Hello {name} because you are from {country}")
    print(f"Hello {name} the course {course} price is ${price - 50}")
else:
    print(f"Hello {name} because you are from {country}")
    print(f"Hello {name} the course {course} price is ${price - 30}")
