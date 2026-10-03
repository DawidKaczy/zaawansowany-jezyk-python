from functools import total_ordering


@total_ordering
class Book:
    def __init__(self, title, ratings):
        self.title = title
        self.ratings = ratings

    @property
    def average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.average_rating == other.average_rating

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.average_rating < other.average_rating

    def __repr__(self):
        return f"Book({self.title}, {round(self.average_rating, 2)})"


v1 = Book("Komar", [-5, -2, 0, 3, 7, 10])
v2 = Book("Kloc", [3, -2, 0, 3, 7, 10])
print(v1)

print(v1 == v2)
print(v1 < v2)
print(v1 <= v1)
print(v1 > v2)

v = [Book("qw", [-5, 7, 0, 3, 7, 10]),
      Book("we", [-5, -2, 5, 3, 7, 10]),
      Book("er", [-5, -2, 0, 3, 7, 10]),
      Book("rt", [-5, -2, 0, 3, 3, 10]),
      Book("ty", [-5, -2, 0, 3, 7, 1]),]

sorted_books = sorted(v, reverse=True)
for book in sorted_books:
    print(book)

