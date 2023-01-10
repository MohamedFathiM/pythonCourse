myFriend = ["ahmed", "Mohamed"]
myOldFriends = ["Ali", "Hosny"]


# Append
myFriend.append(myOldFriends)

print(myFriend)
print(myFriend[2][0])


# extend
a = [1, 2, 3, 5]
b = ["A", "B", "C"]
c = ["One", "Two"]


a.extend(b)
a.extend(c)
print(a)


# remove()  => delete the first occurrence of list
listOfDevelopers = ["Ali", "Ali", "hosny", "Ahmed", "Mario"]
listOfDevelopers.remove("Ali")

print(listOfDevelopers)


# sort()
y = [1, 2, 5, 6, -1, 5, 0, 10]
y.sort()

print(y)

y.sort(reverse=True)
print(y)

# testList = ["a", "b", "c", 1, 5, 63, 78]
# print(testList.sort())  # Error Cannot Sort


# reverse() # reverse only list

testList = ["a", "b", "c", 1, 5, 63, 78]
testList.reverse()
print(testList)
