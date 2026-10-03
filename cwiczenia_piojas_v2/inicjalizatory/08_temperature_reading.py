

class TemperatureReading:
    def __init__(self, value , unit = "Celsius"):
        self.value = value
        if unit not in ("Celsius", "Fahrenheit", "Kelvin"):
            raise ValueError("Dozwolone są Celsius", "Fahrenheit", "Kelvin")
        self.unit = unit



v1 = TemperatureReading(12, "Celsius")

