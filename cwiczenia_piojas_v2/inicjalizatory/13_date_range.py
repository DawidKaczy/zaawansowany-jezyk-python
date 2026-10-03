from datetime import datetime

class DateRange:
    def __init__(self, start_date, end_date):
        if start_date < end_date:
            self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            self.end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        else:
            raise ValueError("start_date and end_date must be in the same date")

    def __repr__(self):
        return f"DateRange(start_date={self.start_date}, end_date={self.end_date})"


v1 = DateRange("2002-1-1" , "2003-1-1")

print(v1)



