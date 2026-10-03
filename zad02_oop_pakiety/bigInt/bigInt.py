class BigInt:
    def __init__(self, value: str):
        self.value = value

    def __add__(self, other: "BigInt") -> "BigInt":
        return BigInt(str(int(self.value) + int(other.value)))

    def __sub__(self, other: "BigInt") -> "BigInt":
        return BigInt(str(int(self.value) - int(other.value)))

    def __mul__(self, other: "BigInt") -> "BigInt":
        return BigInt(str(int(self.value) * int(other.value)))

    def __iadd__(self, other: "BigInt") -> "BigInt":
        self.value = str(int(self.value) + int(other.value))
        return self

    def __isub__(self, other: "BigInt") -> "BigInt":
        self.value = str(int(self.value) - int(other.value))
        return self

    def __imul__(self, other: "BigInt") -> "BigInt":
        self.value = str(int(self.value) * int(other.value))
        return self

    def __eq__(self, other: "BigInt") -> bool:
        return int(self.value) == int(other.value)

    def __ne__(self, other: "BigInt") -> bool:
        return int(self.value) != int(other.value)

    def __lt__(self, other: "BigInt") -> bool:
        return int(self.value) < int(other.value)

    def __le__(self, other: "BigInt") -> bool:
        return int(self.value) <= int(other.value)

    def __gt__(self, other: "BigInt") -> bool:
        return int(self.value) > int(other.value)

    def __ge__(self, other: "BigInt") -> bool:
        return int(self.value) >= int(other.value)

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value