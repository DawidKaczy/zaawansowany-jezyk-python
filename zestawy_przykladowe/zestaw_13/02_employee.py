from functools import total_ordering


@total_ordering
class Employee:
    def __init__(self, name, bonuses):
        self.name = name
        self.bonuses = bonuses

    @property
    def average_bonus(self):
        if not self.bonuses:
            return 0.0
        return round(sum(self.bonuses) / len(self.bonuses), 2)

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.average_bonus == other.average_bonus

    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.average_bonus < other.average_bonus

    def __repr__(self):
        return f"Employee({self.name}, {self.average_bonus})"

v1 = Employee("Dawid", [20,30,50])
print(v1)
print(v1 == v1)
print(v1 < v1)
print(v1 <= v1)
print(v1 > v1)


employee_list = [Employee("Da", [2,1,2,3]),
           Employee("Ka", [2,2,3,2]),
           Employee("Pa", [2,6,6,2]),
           Employee("Ta", [2,5,5,2]),
           Employee("Ra", [2,2,7,2]),
           Employee("Bz", [2,6,2,2])]

sorted_employees = sorted(employee_list, reverse=True)
for i in sorted_employees:
    print(i)


