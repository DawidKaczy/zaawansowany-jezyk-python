

class Config:
    def __init__(self, settings):
        self.settings = settings

    @property
    def settings(self):
        return self.__settings.copy()

    @settings.setter
    def settings(self, settings):
        if not isinstance(settings, dict):
            raise TypeError("settings must be a dict")
        for key, value in settings.items():
            if not isinstance(key, str):
                raise TypeError("key must be str")
            if not isinstance(value, str):
                raise TypeError("value must be str")
        self.__settings = settings.copy()

v1 = Config({"1": "Dawid", "ok": "Kamil",})



