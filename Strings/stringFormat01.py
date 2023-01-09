name = "Mohamed"
age = 28
rank = 10

print("My Name is " + name)

# print("My Name is : " + name + " and My Age is: " + age) #type Error

print("My Name is: %s" % "Mohamed")
print("My Name is : %s and Age is: %d and my rank is : %f" % (name, age, rank))

# %s => string
# %d => Number
# %f => Float

n = "Mohamed"
l = "Python "
y = 2

print("My name is %s Iam %s Developer with %d experience" % (n, l, y))


# Control Floating Point Number
myNumber = 10

print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)


# Truncate String
myLongString = "Hello People of Elzero Web School , I Love You All"

print("Message is %.5s" % myLongString)
print("Message is %s" % myLongString)
