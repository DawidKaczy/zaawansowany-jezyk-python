class Scoreboard:
    def __init__(self, game_name, scores: dict = None):
        self.game_name = game_name

        if scores is None:
            self.scores = {}
        else:
            self.scores = scores.copy()


# 1. Tworzymy początkowy słownik z wynikami
initial_scores = {"Alicja": 100, "Bob": 80}

# 2. Tworzymy obiekt Scoreboard i przekazujemy nasz słownik
board = Scoreboard("Turniej Szachowy", initial_scores)

print("--- PRZED MODYFIKACJĄ ---")
print(f"Oryginalny słownik:  {initial_scores}")
print(f"Słownik w obiekcie:  {board.scores}\n")

# 3. Modyfikujemy oryginalny słownik (symulacja zmian w innej części programu)
initial_scores["Alicja"] = 9999
initial_scores["Charlie"] = 50

print("--- PO MODYFIKACJI ---")
print(f"Oryginalny słownik:  {initial_scores}")
print(f"Słownik w obiekcie:  {board.scores}")