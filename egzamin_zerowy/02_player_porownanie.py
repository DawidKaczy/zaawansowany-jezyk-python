from functools import total_ordering

@total_ordering
class Player:
    def __init__(self, name, scores: list):
        self.name = name
        self.scores = scores

    @property
    def average_score(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)


    def __eq__(self, other):
        if not isinstance(other, Player):
            raise TypeError("Must be same type")
        return self.average_score == other.average_score

    def __lt__(self, other):
        if not isinstance(other, Player):
            raise TypeError("Must be same type")
        return self.average_score < other.average_score

    def __repr__(self):
        return f"Player ({self.name, self.average_score})."



v1 = Player("Waldek", [20, 30, 40])
print(v1)
print(v1.average_score)


v2 = Player("Kamil", [20, 30, 40])
print(v2)
print(v2.average_score)

print(f"Czy Waldek == Kamil? {v1 == v2}")
print(f"Czy Waldek > Kamil? {v1 > v2}")
print(f"Czy Waldek < Kamil? {v1 < v2}")
print(f"Czy Waldek <= Kamil? {v1 <= v2}")

lista_graczy = [
    Player("Waldek", [20, 30, 40]),
    Player("Kamil", [10, 50]),
    Player("Dawid", [50, 60, 70]),
    Player("Anna", [90, 100, 80]),
    Player("Zosia", [5, 10, 15])
]

lista_graczy.sort(reverse=True)
print("\n--- PO SORTOWANIU (MALEJĄCO) ---")
for pozycja, gracz in enumerate(lista_graczy, start=1):
    print(f"{pozycja}. {gracz.name} - Średnia: {gracz.average_score:.2f}")


