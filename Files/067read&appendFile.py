# write and append in file

# write does not make append
# myFile = open(r"C:\xampp\htdocs\pythonCourse\Files\ahmed.txt", "w")
# myFile.write("Hello From Python File With Love\n")
# myFile.write("Second Line")

myList = ['osama\n', 'ahmed\n', 'mohamed\n']

myFile1 = open(r"C:\xampp\htdocs\pythonCourse\Files\fun.txt", "w")
# myFile1.write("Elxero Web School \n" * 1000)

myFile1.writelines(myList)


# append
myFile1 = open(r"C:\xampp\htdocs\pythonCourse\Files\fun.txt", "a")
myFile1.write("Hello ")
