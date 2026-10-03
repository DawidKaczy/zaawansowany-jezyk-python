class Config:
    def __init__(self, settings):
        self.__settings = settings

    @property
    def settings(self):
        return self.__settings.copy()

    @settings.setter
    def settings(self, value):
        if not isinstance(value, dict):
            raise TypeError('settings must be a dict')
        for keys, values in value.items():
            if not isinstance(keys, str):
                raise TypeError
            if not isinstance(values, str):
                raise TypeError
        self.__settings = value

c = Config({"theme": "dark", "lang": "pl"})
c.settings = {"mode": "test"}      # OK
c.settings = ["a", "b"]            # błąd
c.settings = {1: "test"}

