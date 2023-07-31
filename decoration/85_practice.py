# when i do not know count of arguments

from time import time
# def myDecorator(func) :
#     def nestedFunc(*numbers):
#         for number in numbers :
#             if number < 0 :
#                 print("Number is less than zero")

#         func(*numbers)
#     return nestedFunc

# @myDecorator
# def calcNumbers(n1,n2,n3):
#     print(n1+n2,n3)

# calcNumbers(10,-2,-100)


# Speed Test
def speedTest(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Function Running Time is : {end - start}")

    return wrapper

@speedTest
def bigLoop():
    for number in range(1,20000):
        print(number)


bigLoop()
