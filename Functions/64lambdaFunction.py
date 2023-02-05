# it has no name
# call it inline
# use it return data from another function
# using for simple function
# single expression
# lambda function is Function
#################################


def say_hello(name): return f"Hello {name}"


# Syntax for lambda function
def hello(name, age): return f"Hello {name} your age is : {age}"
hello = lambda name,age : f"Hello {name} your age is : {age}"


print(say_hello("Mohamed"))
print(hello("Mohamed",29))


print(say_hello.__name__)
print(hello.__name__)
