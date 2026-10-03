
class Student:
    def __init__(self, name, grade = "A"):
        self.name = name
        self.grade = grade


v1 = Student("Dawid")
v2 = Student("Kacper", "B")

print(v1.grade)
print(v2.grade)