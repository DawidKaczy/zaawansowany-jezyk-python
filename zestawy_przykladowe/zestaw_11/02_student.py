from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    @property
    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __eq__(self, other):
        return self.average == other.average

    def __lt__(self, other):
        return self.average < other.average

    def __repr__(self):
        return f"Student {self.name}, {self.average}"

v1 = Student("", [1,2,3])
print(v1)
print(v1 == v1)
print(v1 < v1)
print(v1 <= v1)
print(v1 > v1)

student = [Student("Da", [2,1,2,3]),
           Student("Ka", [2,2,3,2]),
           Student("Pa", [2,6,6,2]),
           Student("Ta", [2,5,5,2]),
           Student("Ra", [2,2,7,2]),
           Student("Bz", [2,6,2,2])]

sort = sorted(student, reverse=True)
print(sort)