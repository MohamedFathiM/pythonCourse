"""
 How To raise exception
"""

# EX 1
# x = -100

# if x < 0 :
#     raise Exception(f"{x} should be greater than zero")
# else:
#     print(f"{x} is good number")


# EX 2
# y = 10
y = "Mo"

if type(y) != int:
    raise ValueError(f"{y} Should be number")

print(f"Your program is run correct ")
