# "a" append
# "r" read
# "e" write
# "x" create
import os

print(os.getcwd()) # Main Current Working Directory
print(os.path.dirname(os.path.abspath(__file__))) # Directory For The Opened File
print(os.path.abspath(__file__))


# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

# file = open("C:\\xampp\\htdocs\\pythonCourse\\Files\\mohamed.txt", 'r')
file = open(r"C:\xampp\htdocs\pythonCourse\Files\mohamed.txt", 'r')
