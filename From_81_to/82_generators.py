# Generators


def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4


myGen = myGenerator()

print(next(myGen))
print(next(myGen))
print(next(myGen))


for number in myGen:
    print(number)
