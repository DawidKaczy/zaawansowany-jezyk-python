

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, celsius):
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

v1 = Temperature(12)
print(v1.fahrenheit)
v1.celsius = 15
print(v1.fahrenheit)

v2 = Temperature(13)
print(v2.fahrenheit)