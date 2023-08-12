# Polymorphism (overwriting , overloading)


class A:
    def do_something(self):
        print('From Class A')
        # this is like abstract class in other language 
        raise  NotImplementedError("Derived class not implemented yet")

class B(A):
     def do_something(self):
        print('From Class B')


class C(A):
    def do_something(self):
        print('From Class C')



obj = C()
obj.do_something()
