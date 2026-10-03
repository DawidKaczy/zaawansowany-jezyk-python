class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        return 0.10 * self.salary


class Manager(Employee):
    def get_bonus(self):
        return 0.20 * self.salary


# Lista z różnymi obiektami
employees = [
    Employee("Jan", 5000),
    Manager("Anna", 8000),
    Employee("Piotr", 4500),
    Manager("Kasia", 9000)
]

# Iteracja i polimorfizm
for emp in employees:
    print(f"{emp.name} | Pensja: {emp.salary} | Bonus: {emp.get_bonus()}")