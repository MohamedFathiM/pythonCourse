# Encapsulation

## Attributes :

# public
# protected define using _ before name (_name)
# private define using __ before name (__name)

class Member:
    def __init__(self,name,age,job) -> None:
        self.name = name # public
        self._age = age # protected
        self.__job = job # private

member = Member('Ahmed',25,'Developer')
print(member.name)
print(member._age)
print(member._Member__job) # How to access private attribute 
print(member.__job) # it will raise error because private attributes are not access from out of class
