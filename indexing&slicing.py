# indexing in python
# start from zero

firstName = "Mohamed"

# positive index
print(firstName[0])

#negative index
print(firstName[-1])

## Slicing
# [start:End]
# [start:End:steps]
myString = "I Love Python"

print(myString[0:5])
print(myString[5:])
print(myString[:5])
print(myString[:])

#Steps
print(myString[0:5:1])
print(myString[::1])
print(myString[::2])
