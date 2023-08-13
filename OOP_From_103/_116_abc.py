from abc import ABCMeta,abstractmethod


class Programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):
        pass



class Python(Programming):
    def has_oop(self):
        return True

class Pascal(Programming):
    def has_oop(self):
        return False


obj = Python()
print(obj.has_oop())
