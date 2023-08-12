# try :
#     number = int(input("Write Your Age "))
# except:
#     print("Age should be correct number")
# else:
#     print("This is correct Number")
# finally:
#     print("End of try")


# EX 2

try :
    # print(int("Hi"))
    print(100 /0)

except ValueError:
    print('Value Error')
except ZeroDivisionError:
    print('Cannot Divide Zero')
