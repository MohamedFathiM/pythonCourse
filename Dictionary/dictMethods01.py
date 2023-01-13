# clear()
user = {
    "name": "Mohamed",
    "age": 28,
    "country": "Egypt",
    "skills": ['html', 'css'],
    "rating": 10.5
}

print(user.clear())
print("=" * 40)

# update()
user = {
    "name": "Mohamed",
    "age": 28,
    "country": "Egypt",
    "skills": ['html', 'css'],
    "rating": 10.5
}

user['job'] = "Developer"
print(user)

user.update({"state": "Farskour"})
print(user)
print("=" * 40)

# copy()
main = {
    "name": "Osama"
}
b = main.copy()
print(b)
main.update({"skills": "fighting"})
print(main, b)
print("=" * 40)

# keys() , values
