class MyList:
    def __init__(self, initial_data=None):
        self.data = initial_data if initial_data is not None else []

    def __len__(self) :
        return len(self.data)

    def __repr__(self):
        return f"MyList({self.data})"


imiona = MyList(["Ania", "Kamil", "Dawid"])
print(len(imiona))
