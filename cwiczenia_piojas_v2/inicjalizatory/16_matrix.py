
class Matrix:
    def __init__(self, data):
        self.rows = len(data)
        self.cols = len(data[0])

        if data:
            for rows in data:
                if len(rows) != len(data[0]):
                    raise ValueError("Data must be the same lenght")
        self.data = data



try:
    valid_data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = Matrix(valid_data)
    print("--- SUKCES ---")
    print(f"Obiekt: {matrix}")
    print(f"Liczba wierszy (rows): {matrix.rows}")
    print(f"Liczba kolumn (cols):  {matrix.cols}")
    print(f"Dane: {matrix.data}\n")
except ValueError as e:
    print(f"Błąd: {e}")

# ==========================================
# SCENARIUSZ 2: Błędna macierz (różne długości)
# ==========================================
try:
    invalid_data = [
        [1, 2, 3],
        [4, 5],      # Brakuje jednego elementu!
        [7, 8, 9]
    ]
    bad_matrix = Matrix(invalid_data)
except ValueError as e:
    print("--- BŁĄD WALIDACJI ---")
    print(e)