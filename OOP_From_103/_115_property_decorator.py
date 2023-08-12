# using method as property

class Member:
    def __init__(self,age) -> None:
        self.age = age

    @property
    def age_in_days(self):
        return self.age * 365


person = Member(25)
# print(person.age_in_days()) # When using method normally
print(person.age_in_days) # as property
