from datetime import datetime

class DateRange:
    def __init__(self, start, end):
        self.__start = None
        self.__end = None
        self.start = start
        self.end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        if not isinstance(start, datetime):
            raise TypeError("start must be datetime")
        if self.__end is not None and start > self.__end:
            raise ValueError("start must be less than end")
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        if not isinstance(end, datetime):
            raise TypeError("start must be datetime")
        if self.__start is not None and end < self.__start:
            raise ValueError("end must be bigger than start")
        self.__end = end


