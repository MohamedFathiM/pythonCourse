import datetime

# print(dir(datetime.datetime))

# Current Date and Time
print(datetime.datetime.now())


# print the current month
print(datetime.datetime.now().month)

# print the current day
print(datetime.datetime.now().day)

#print start and end of day
print('#' * 40)
print(datetime.datetime.min)
print(datetime.datetime.max)


# print time
print('#' * 40)
print(datetime.datetime.now().time())


# print current time
print('#' * 40)
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)


# print birthday
myBirthDay = datetime.datetime(1982,10,25)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And " ,end="")
print(f"Date now is {dateNow}")

print(f"I lived for {dateNow - myBirthDay}")
print(f"I lived for {(dateNow - myBirthDay).days} days .")
