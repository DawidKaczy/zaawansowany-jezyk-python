class Scoreboard:
    def __init__(self, game_name: str, scores=None):
        self.game_name = game_name
        # jeśli scores nie podano, tworzymy pusty słownik
        if scores is None:
            self.scores = {}
        else:
            # tworzymy kopię, żeby nie modyfikować oryginalnego słownika
            self.scores = scores.copy()

    def add_score(self, player: str, score: int):
        self.scores[player] = score

    def __str__(self):
        return f"{self.game_name} Scoreboard: {self.scores}"


original_scores = {"Alice": 10, "Bob": 15}

board = Scoreboard("Tennis", original_scores)
print(board)

original_scores["Charlie"] = 20

print(board)
print(original_scores)