

class HotelRoom:
    def __init__(self, room_name, base_night_price, seasonal_discount = 0):
        self.room_name = room_name
        self.base_night_price = base_night_price
        self.seasonal_discount = seasonal_discount

    @property
    def room_name(self):
        return self.__room_name

    @room_name.setter
    def room_name(self, room_name):
        if not isinstance(room_name, str):
            raise TypeError("Nazwa pokoju musi być ciągiem znaków (str).")
        if not room_name.strip():
            raise ValueError("Nazwa pokoju nie może być pusta.")
        self.__room_name = room_name

    @property
    def base_night_price(self):
        return self.__base_night_price

    @base_night_price.setter
    def base_night_price(self, base_night_price):
        if base_night_price <= 0:
            raise ValueError("Invalid base night price")
        self.__base_night_price = base_night_price

    @property
    def seasonal_discount(self):
        return self.__seasonal_discount

    @seasonal_discount.setter
    def seasonal_discount(self, seasonal_discount):
        if not (0 <= seasonal_discount <= 100):
            raise ValueError("Invalid base night price")
        self.__seasonal_discount = seasonal_discount

    @property
    def final_night_price(self):
        discounted_price = self.base_night_price * (1 - (self.seasonal_discount / 100))
        return round(discounted_price, 2)

    def __str__(self):
        return f"Pokój {self.room_name} - Cena końcowa: {self.final_night_price:.2f} PLN/dobę"


# 1. Pokój bez zniżki (zadziała domyślne 0)
pokoj_standard = HotelRoom("Standard 101", 150)
print(pokoj_standard)

# 2. Pokój ze zniżką 20%
pokoj_premium = HotelRoom("Premium 202", 300, 20)
print(pokoj_premium)








