country = "Egypt"


if country == "Egypt":
    print(f"The Weather in {country} is 15")
elif country == 'KSA':
    print(f"The Weather in {country} is 30")
else:
    print(f"Country is not in the list")



movieRate = 18
age = 16

if age < movieRate:
    print("Movie is not good for you")
else:
    print("Movie is good for you")

# Short if
print("Movie is not good for you" if age < movieRate else "Movie is good for you")
