class TemperatureReading:
    def __init__(self, value, unit = "Celsius"):
        self.value = value
        if unit not in ("Celsius", "Fahrenheit", "Kelvin"):
            raise ValueError("Dozwolone jednostki to Celsius, Fahrenheit, Kelvin")
        self.unit = unit

v1 = TemperatureReading(1, "Celsius")
v2 = TemperatureReading(1, "Celsius")
print(v1.value)

