# split(pattern,string,maxSplit)
# sub(pattern,replace,string,replaceCount)
import re

string_one = "I Love Python Programming Language"

splittedString = re.split('\s',string_one)
print(splittedString)
print("*" * 50)


# EX 2
string_two = "Python-is_a-very_good-language"

splittedStringTwo = re.split('-|_',string_two)
print(splittedStringTwo)
print("*" * 50)

# get words from url
for counter , word in enumerate(splittedStringTwo,1):
    if len(word) > 1:
        print(f"Word Number {counter} => {word.lower()}")


# sub
print('*' * 50)

print(re.sub('\s','-',"I Love My Son",2))
