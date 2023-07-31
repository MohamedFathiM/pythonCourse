# decorators with functions has params

def myDecorator(func):
    def nestedFunction(num1,num2):
        if num1 < 0 or num2 < 0 :
            print("be ware one of the numbers is less than zero")

        func(num1,num2)
    return nestedFunction


def decoratorTwo(func):
    def nestedFunction(n1,n2):
        print('coming from decorator two')

        func(n1,n2)
    return nestedFunction

@myDecorator
@decoratorTwo
def calcTwoNumbers(num1 , num2) :
    print(num1 + num2)

calcTwoNumbers(-2,20)
