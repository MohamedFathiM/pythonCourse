def checkNumber(num):
    return num == 0


myNumbers = [1, 19, 10, 100, 5, 0, 1, 0]

myResults = filter(checkNumber, myNumbers)

for number in myResults:
    print(number)

print('#' * 50)


def checkName(name):
    return name.startswith("O")


myText = ["Osama", "Omer", "Ahmed", "Amer"]

myReturnedData = filter(checkName, myText)

for name in myReturnedData:
    print(name)


print('#' * 50)

myText = ["Osama", "Omer", "Ahmed", "Amer"]

for b in filter(lambda name: name.startswith('O'), myText):
    print(b)
