
class PasswordPolicy:
    def __init__(self, słowo):

        if len(słowo) >= 6 and len(słowo) < 128:
            self.słowo = słowo
        else:
            raise ValueError("Długośc hasła od 6 do 128 znaków")
        if any (char.isupper() for char in słowo):
            self.słowo = słowo
        else:
            raise ValueError("Musi byc duża literaz")

        if any (char.isdigit() for char in słowo):
            self.słowo = słowo
        else:
            raise ValueError("Musi byc cyfra")

        if any (not char.isalnum() for char in słowo):
            self.słowo = słowo
        else:
            raise ValueError("Musi byc specjalny znak")



v1 = PasswordPolicy("Kra2asdasd!")