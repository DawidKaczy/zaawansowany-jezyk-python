
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def describe(self):
        return f"Brand: {self.brand}, {self.max_speed} km/h"

class ElectricVehicle(Vehicle):
    def __init__(self, brand, max_speed, battery_capacity):
        super().__init__(brand, max_speed)
        self.battery_capacity = battery_capacity

    def describe(self):
        return f"{super().describe()}, {self.battery_capacity} km/h"

v1 = Vehicle("Ford", 110)
v2 = ElectricVehicle("Bob", 100, 100)


print(v1.describe())
print(v2.describe())