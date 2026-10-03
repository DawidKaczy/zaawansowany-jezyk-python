
class Student:
    def __init__(self, name, grade = "A"):
        self.name = name
        self.grade = grade


v1 = Student("a")
v2 = Student("Alek", "B")

print(v1.name, v1.grade)
print(v2.name, v2.grade)