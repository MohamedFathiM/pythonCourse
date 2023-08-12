the_file = None
tries = 5

while tries > 0:
    try:
        print('Enter File path')
        print("*" * 10)
        print(f"You Have {tries} tries left")
        print("*" * 10)
        print("Ex : D:\Python\Files\yourFile.py")
        print("*" * 10)
        file_name_and_path = input("File Name  =>  ").strip()
        print("*" * 10)
        the_file = open(file_name_and_path,'r')
        print(the_file.read())
        break

    except FileNotFoundError:
        print("File Not Found")
        tries -= 1
    finally:
        if the_file is not None:
            the_file.close()
            print('File Closed')
else:
    print("All Tries is Done")
