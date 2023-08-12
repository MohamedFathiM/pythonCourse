class Member:
    not_allowed_names = ['shit','hell']
    usersCount = 0

    def __init__(self,fname,mname,lname,gender):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.gender = gender
        Member.usersCount += 1

    def getFullName(self):
        if self.fname in Member.not_allowed_names :
            print(self.deleteUser())
            print("*" * 50)

            raise ValueError("This name is not allowed")

        return self.fname + " "  + self.mname + " " + self.lname

    def sayHello(self):
        if self.gender == 'M' :
            return f"Hello Mr. {self.fname}"
        elif self.gender == 'F':
            return f"Hello Miss. {self.fname}"
        else:
            return f"Hello {self.fname}"

    def get_all_info(self):
        return f"{self.sayHello()}, You FullName is {self.getFullName()}"

    def deleteUser(self):
        Member.usersCount -= 1

        return f"{self.fname} Deleted From Count , and Users Count become {Member.usersCount}"

member = Member("Mohamed","Fathi","Metwally","M")
member2 = Member("Amany","Fathi","Metwally","F")

member3 = Member("hell","Fathi","Metwally","F")

print(member.getFullName())
print("*" * 10)
print(member.sayHello())
print("*" * 10)
print(member2.sayHello())
print("*" * 10)
print(member2.get_all_info())
print("*" * 10)
print(Member.usersCount)
print("*" * 10)
print(member3.getFullName())
