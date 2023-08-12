# Multi Inheritance

class Eat:
    def __init__(self) -> None:
        print('base one')

    def isEat():
        print('is Eat')


class Drink:
    def __init__(self) -> None:
        print('base two')

    def is_drink(self):
        print('is Drink')


class Person(Eat,Drink):
    pass


mohamed = Person()
print(mohamed)
print(Person.mro())
