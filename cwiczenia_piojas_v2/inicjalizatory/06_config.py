from dill import settings


class Config:
    def __init__(self, app_name):
        self.app_name = app_name
        self.settings = {}

    def __str__(self):
        return f"{self.app_name} {self.settings}"


v1 = Config("Klocki")

v1.settings = {"ok": 3}

print(v1)


