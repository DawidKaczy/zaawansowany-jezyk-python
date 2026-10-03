
class PasswordPolicy:
    def __init__(self, slowo, min_length = 6, require_uppercase = True, require_digit= True, require_special_char = True):

        if isinstance(min_length, int):
            self.min_length = min_length
        else:
            raise TypeError("must be int")

        if min_length >= 6 and min_length <= 128:
            self.min_length = min_length
        else:
            raise TypeError("min_length must be between 6 and 128")