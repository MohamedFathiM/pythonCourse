# inheritance in oop

class Food:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price

        print(f"{self.name} is created from base class and its price is {self.price}")

    def eat(self):
        print("we are using this eat method from super class")


class Apple(Food):
    def __init__(self, name, price,amount) -> None:
        super().__init__(name, price)
        self.amount = amount

        print(f"This printed from derived class , it is overwriting the super class with name {self.name} , price {self.price} and amount {self.amount}")


food = Apple("Pizza",150,200)
print(food)
food.eat()
