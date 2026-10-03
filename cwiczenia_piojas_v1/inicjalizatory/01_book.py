class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

v1 = Book("Oskar i mały pies", "Wowak")
v2 = Book("mały pies i oskar ", "Norka")

print(v1.title, v1.author)
print(v2.title, v2.author)