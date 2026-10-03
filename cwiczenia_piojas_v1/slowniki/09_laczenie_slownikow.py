def merge_dicts(dict_a, dict_b):
    result = dict_a.copy()  # kopiujemy pierwszy słownik

    for key, value in dict_b.items():
        if key in result:
            result[key] += value  # sumujemy wartości
        else:
            result[key] = value  # dodajemy nowy klucz

    return result

# Przykład użycia
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

print(merge_dicts(a, b))
#{'x': 1, 'y': 5, 'z': 4}