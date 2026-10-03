
class Survey:
    def __init__(self, title, *questions , anonymous = True):
        self.title = title
        self.questions = list(questions)
        self.anonymous = anonymous

    def __repr__(self):
        return (f"Survey(title='{self.title}', "
                f"questions_count={len(self.questions)}, "
                f"anonymous={self.anonymous})")


employee_survey = Survey(
    "Ankieta satysfakcji pracownika",
    "1. Jak oceniasz atmosferę w zespole?",
    "2. Czy narzędzia, na których pracujesz, są wystarczające?",
    "3. Jak oceniasz komunikację z bezpośrednim przełożonym?",
    "4. Czy czujesz, że masz możliwości rozwoju w firmie?",
    "5. Czy polecił(a)byś pracę tutaj swojemu znajomemu?",
)

print(employee_survey)