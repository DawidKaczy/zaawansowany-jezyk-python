class Survey:
    def __init__(self, title, *questions, anonymous = True):
        self.title = title
        self.questions = list(questions)
        self.anonymous = anonymous

    def __str__(self):
        return f"{self.title} {self.questions}, {self.anonymous}"

    def __delitem__(self, key):
        self.questions.remove(key)

my_survey = Survey(
    "Opinie o produkcie",
    "Jak oceniasz jakość produktu?",
    "Czy polecił(a)byś nasz produkt znajomym?",
    "Co Ci się najbardziej podoba w produkcie?",
    "Co można poprawić w produkcie?",
    "Jak często korzystasz z naszego produktu?"
)
print(my_survey )

my_survey.__delitem__("Jak często korzystasz z naszego produktu?")

print(my_survey )