# class method
# static method

# class method
class Member :
    members_count = 0

    @classmethod
    def getMembersCount(cls):
        print(f"Members count is {cls.members_count}")

    def addMember(self):
        Member.members_count += 1


    # static method
    @staticmethod
    def printHelloWorld():
        print(f"Hello World")

member = Member()
Member.addMember(member)
Member.addMember(member)
Member.addMember(member)
Member.getMembersCount()

print('*' * 50 )
Member.printHelloWorld()
