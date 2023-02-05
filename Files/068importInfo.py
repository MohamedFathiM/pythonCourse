import os

myFile = open(r"C:\xampp\htdocs\pythonCourse\Files\fun.txt", "a")

# get the part from file and delete the other
# myFile.truncate(5)


# the position of cursor
# print(myFile.tell())


# position to move cursor to it
myFile = open(r"C:\xampp\htdocs\pythonCourse\Files\fun.txt", "r")
myFile.seek(6)
print(myFile.read())

myFile.close()

# To Remove file
# os.remove({"C:\xampp\htdocs\pythonCourse\Files\fun.txt"})
