# setters and getters

class Member:
    __name = ''

    def __init__(self) -> None:
        pass

    def getName(self):
        return self.__name

    def setName(self,name):
         self.__name = name


obj = Member()
obj.setName("Mohamed")
print(obj.getName())
