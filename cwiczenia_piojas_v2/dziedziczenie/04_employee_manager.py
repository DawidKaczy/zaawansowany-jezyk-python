

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        return self.salary * 0.10

class Manager(Employee):

    def get_bonus(self):
        return self.salary * 0.20

v1 = Employee("Dawid", 100)
print(v1.get_bonus())

v2 = Manager("Waldek", v1.salary)
print(v2.get_bonus())

