def myDecorator(func):
    def nestedFunc():
        print('Before')

        func()

        print('after')

    return nestedFunc

@myDecorator
def sayHello():
    print('hello from say hello function')


sayHello()
print("*" * 50)
