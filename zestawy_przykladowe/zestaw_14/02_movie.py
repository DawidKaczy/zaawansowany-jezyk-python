from functools import total_ordering
@total_ordering
class Movie:
    def __init__(self, title, ratings):
        self.title = title
        self.ratings = ratings

    @property
    def average_rating(self):
        wynik = sum(self.ratings) / len(self.ratings)
        return wynik

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.ratings == other.ratings

    def __lt__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.average_rating < other.average_rating

    def __repr__(self):
        return f"Movie({self.title}, {self.average_rating})"

v1 = Movie("Elo", [20, 30, 40])
print(v1)
print(v1 == v1)
print(v1 <= v1)
print(v1 < v1)
print(v1 > v1)

moviess = [Movie("Ta", [10, 30, 40]),
          Movie("Ra", [20, 15, 40]),
          Movie("Bn", [20, 30, 3]),
          Movie("Fr", [2, 30, 40]),
          Movie("Nm", [20, 45, 40])]

sorted_movies = sorted(moviess, reverse=True)

for i in sorted_movies:
    print(i)

