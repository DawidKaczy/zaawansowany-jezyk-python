class User:
    def __init__(self, username , email):
        self.username = username
        if "@" not in(email):
            raise ValueError("Podaj email z @")
        self.email = email

v1 = User("Tomek", "<EMAIL>")