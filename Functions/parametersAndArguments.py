# def => function keyword [Define]
# say_hello() => function name


a, b, c = "Mohamed", "Ahmed", "Sayed"


def say_hello(name):
    print(f"Hello {name}")


say_hello(a)
say_hello(b)
say_hello(c)


def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Only Integers Allowed")
    else:
        print(int(n1) + int(n2))


addition(1, 2)
addition("Hello", 2)
addition(-1, 2)


def full_name(first, middle, last):
    print(
        f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")


full_name("Ahmed", "Mohamed", "Fathi")
