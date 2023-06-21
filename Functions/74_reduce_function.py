# Hire Order Function
# reduce

from functools import reduce


def sumAll(num1, num2):
    return num1 + num2


numbers = [1, 8, 2, 9, 100]

result = reduce(sumAll, numbers)

print(result)


print('#' * 50)

result = reduce(lambda num1, num2: num1 + num2, numbers)

print(result)
