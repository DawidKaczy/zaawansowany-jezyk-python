class DefaultDict:
    def __init__(self, default_value, initial_data=None):
        # Przechowujemy wartość, którą będziemy zwracać dla brakujących kluczy
        self.default_value = default_value

        # Inicjalizujemy słownik danymi od użytkownika lub pustym słownikiem
        self.data = initial_data if initial_data is not None else {}

    # ==========================================
    # ODCZYT (__getitem__) - Tu dzieje się magia
    # ==========================================
    def __getitem__(self, key):
        # Sprawdzamy, czy klucz fizycznie istnieje w naszym słowniku
        if key in self.data:
            return self.data[key]

        # Jeśli klucza nie ma, ZAMIAST błędu KeyError, zwracamy wartość domyślną
        return self.default_value

    # ==========================================
    # ZAPIS (__setitem__)
    # ==========================================
    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return f"DefaultDict(default={repr(self.default_value)}, data={self.data})"

