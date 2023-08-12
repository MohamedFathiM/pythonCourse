# search (return only first match )
# findall (return all  matches ) return (empty list or list of matches)

import re


# mySearch = re.search(r"[A-Z]{2}","MMohamedFathi")

# print(mySearch)
# print(mySearch.group())

# is_email = re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.[A-z]+$",'os@osama.com')

# if is_email:
#     print("This is a valid email")
# else:
#     print("This is Not a valid email")


email_input = input("Please , write your email:")

search = re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.[A-z]+$",email_input)

empty_list = []

if search != [] :
    empty_list.append(search)
    print("Email Added")
else:
    print("Invalid Email")

for email in empty_list:
    print(email)
