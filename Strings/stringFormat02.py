name = "Mohamed"
age = 28
rank = 10

print("My Name is " + name)

# print("My Name is : " + name + " and My Age is: " + age) #type Error

print("My Name is: {}".format("Mohamed"))
print("My Name is : {} and Age is: {:d} and my rank is : {:f}".format(name, age, rank))

# {} => string
# {:d} => Number
# {:f} => Float

n = "Mohamed"
l = "Python "
y = 2

print("My name is {} Iam {} Developer with {:d} experience".format(n, l, y))


# Control Floating Point Number
myNumber = 10

print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))


# Truncate String
myLongString = "Hello People of Elzero Web School , I Love You All"

print("Message is {:.5s}".format(myLongString))
print("Message is {}".format(myLongString))


# Format Money
myMoney = 26464646446
print("My Money is {:_d}".format(myMoney))
print("My Money is {:,.2f}".format(myMoney))


# Rearrange Items
x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1} {2} {0}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {1:.2f} {2:.2f} {0:.2f}".format(x, y, z))


# Format in Version 3.6+
myName = "Mohamed"
myAge = 36

print("My Name is : {myName} and My Age is :{myAge}")
print(f"My Name is : {myName} and My Age is :{myAge}")
