# [1] Dict items are enclosed in curly braces
# [2] Dict ITems contains key : value
# [3] Dict key need to be immutable => (number,string ,tuple) list not allowed
# [4] dict value can have any data types
# [5] dict key should be unique
# [6] dict not ordered

# Dictionary
user = {
    "name": "Mohamed",
    "age": 28,
    "country": "Egypt",
    "skills": ['html', 'css'],
    "rating": 10.5
}

print(user)
print(user["country"])
print(user.get("country"))
print(user.keys())
print(user.values())
print("=" * 40)

# Two-dimentional Dictionary
languages = {
    "one": {
        "name": "Html ",
        "progress": 88
    },
    "two": {
        "name": "Css",
        "progress": 90
    },
    "three": {
        "name": "Js",
        "progress": 90
    }
}

print(languages)
print(languages["one"])
print(languages["one"]["name"])

# Dictionary Length
print(len(languages))
print(len(languages["one"]))

# Create Dict From Variables
framework01 = {
    "name": "ReactJs",
    "progress": 88
}

framework02 = {
    "name": "Vuejs",
    "progress": 88
}

framework03 = {
    "name": "Angular",
    "progress": 88
}

allFramework = {
    "one" : framework01,
    "two" : framework02,
    "three" : framework03,
}

print(allFramework)
