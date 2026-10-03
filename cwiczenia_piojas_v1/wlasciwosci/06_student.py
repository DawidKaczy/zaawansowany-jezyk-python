from time import sleep


class Student:
    def __init__(self, grades):
        self.grades = list(grades)

    @property
    def grades(self):
        grades_copy = self.__grades.copy()
        return grades_copy

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, list):
            raise TypeError("Grades must be a list")
        for grade in grades:
            if not isinstance(grade, int) or not (1 <= grade <= 6):
                raise ValueError("All grades must be integers between 1 and 6")
        self.__grades = grades.copy()  # zapisujemy kopię listy

    def __repr__(self):
        return f"{self.__grades}"


    def dodaj(self, lista):
        for i in lista:
            if not (1 <= i <= 6):
                raise ValueError("All grades must be integers between 1 and 6")
            self.__grades.append(i)

v1 = Student([1,2,3,4,5])
print(v1)
v1.grades = [1,4,5]
print(v1)

v1.dodaj([1,2,3,4])
print(v1)

