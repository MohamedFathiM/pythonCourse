# magic classes __class__
# __str__ # human readable message when print instance as string
# __len__ # called when use len function on object


class Skill:
     def __init__(self):
        self.skills = ['html','css']

     def __str__(self):
         return "Hello From Skill Class"

     def __len__(self):
         return len(self.skills)

profile = Skill()
print(profile.__class__)
print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("Javascript")
print(len(profile))
