class Config:
    def __init__(self, app_name):
        self.app_name = app_name
        self.settings = {}


config = Config("MojaAplikacja")

config.settings["theme"] = "dark"
config.settings["language"] = "pl"

print("Aplikacja:", config.app_name)
print("Ustawienia:", config.settings)