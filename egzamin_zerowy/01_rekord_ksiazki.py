
def make_record(title, / , author, * ,year):
    return f"{title} - {author} ({year})"

print(make_record("Pająk", "Adam", year = 2001))