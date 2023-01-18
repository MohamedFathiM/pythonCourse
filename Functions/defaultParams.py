# when using unknown parameters should make it at the last

def say_hello(name, age="Unknown", country="Unknown"):
    print(f"Hello {name} Your Age is {age} and Your Country is {country}")


say_hello("Mohamed", 28, "Egypt")
say_hello("Sameh", 28, "KSA")
say_hello("Khaled")
