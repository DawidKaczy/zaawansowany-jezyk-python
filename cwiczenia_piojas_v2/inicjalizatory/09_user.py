class User:
    def __init__(self, username , email):
        self.username = username
        if "@" not in email:
            raise ValueError("Brak @")
        self.email = email



v1 = User("Miki", "kaczorek2002@wp.pl")
v2 = User("Dawid", "kaczorek@2002")
