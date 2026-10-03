from datetime import datetime

class DateRange:
    def __init__(self, start_date, end_date):
        if start_date < end_date:
            self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            self.end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        else:
            raise ValueError('start_date must be less than end_date')\

    def __str__(self):
        return f'{self.start_date} - {self.end_date}'


v1 = DateRange("2002-02-22", "2002-02-23")
print(v1)