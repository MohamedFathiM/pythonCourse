# File Handling => Read File

myFile = open(r"C:\xampp\htdocs\pythonCourse\Files\mohamed.txt", "r")

# print(myFile) # File Data Object

# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# اول واحده بتقرأ الي بعدها بتكمل
# print(myFile.read())
# print(myFile.read(5))

# print(myFile.readline()) # read line only

# print(myFile.readlines()) # return list
# print(type(myFile.readlines())) # return list


for line in myFile:
    print(line)

    if line.startswith("07"):
        break



# Close The File
myFile.close()
