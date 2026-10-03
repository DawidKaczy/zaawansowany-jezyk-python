
class Person:
    def __init__(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name must be of type str")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Name must be of type str")

v1 = Person("Krowa")
print(v1.name)
v1.name = "ludek"
print(v1.name)