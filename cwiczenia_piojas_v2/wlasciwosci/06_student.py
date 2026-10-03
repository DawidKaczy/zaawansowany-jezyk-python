
class Student:
    def __init__(self, grades):
        self.grades = grades

    @property
    def grades(self):
        return self.__grades.copy()

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, list):
            raise TypeError("grades must be a list")
        for grade in grades:
            if not isinstance(grade, int):
                raise TypeError("grade must be a int")
            if not 1 <= grade <= 6:
                raise ValueError("grade must be between 1 and 6")
        self.__grades = grades.copy()


v1 = Student([1,2,3,4,5,6])

print(v1.grades)
