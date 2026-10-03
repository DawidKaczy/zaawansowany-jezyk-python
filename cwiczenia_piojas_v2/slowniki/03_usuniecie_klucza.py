config = {"host": "localhost", "port": 8080, "debug": True}

# Usunięcie klucza "debug" i przypisanie jego wartości do zmiennej
removed_value = config.pop("debug")

# Wypisanie wyników
print(f"Usunięta wartość: {removed_value}")
print(f"Pozostały słownik: {config}")