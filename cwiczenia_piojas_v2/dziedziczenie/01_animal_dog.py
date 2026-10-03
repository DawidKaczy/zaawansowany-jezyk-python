

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"To jest {self.name}"

class Dog(Animal):
    def speak(self):
        return f"{self.name} szczeka: Hau hau!"

# 1. Tworzymy ogólne zwierzę
generic_animal = Animal("Tajemnicze stworzenie")
print(generic_animal.speak())

# 2. Tworzymy psa
my_dog = Dog("Burek")
print(my_dog.speak())