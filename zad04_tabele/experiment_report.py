class ExperimentReport:
    def __init__(self, tp, fp, tn, fn, name):
        self.tp = tp
        self.fp = fp
        self.tn = tn
        self.fn = fn
        self.__name = name

    @property
    def tp(self):
        return self._tp

    @tp.setter
    def tp(self, value):
        if value >= 0:
            self._tp = value
        else:
            raise ValueError('Value must be non-negative.')

    @property
    def fp(self):
        return self._fp

    @fp.setter
    def fp(self, value):
        if value >= 0:
            self._fp = value
        else:
            raise ValueError('Value must be non-negative.')

    @property
    def tn(self):
        return self._tn

    @tn.setter
    def tn(self, value):
        if value >= 0:
            self._tn = value
        else:
            raise ValueError('Value must be non-negative.')

    @property
    def fn(self):
        return self._fn

    @fn.setter
    def fn(self, value):
        if value >= 0:
            self._fn = value
        else:
            raise ValueError('Value must be non-negative.')

    @property
    def name(self):
        return self.__name

    @name.deleter
    def __del__(self):
        print(f"Usuwanie atrybutu nazwa dla: {self.__name}")
        self.__name = ""
        #del self.__name

    @property
    def accuracy(self):
        return (self.tp + self.tn) / (self.tp + self.tn + self.fp + self.fn)

    @property
    def precision(self):
        return self.tp / (self.tp + self.tp + self.fp)

    @property
    def recall(self):
        return self.tp / (self.tp + self.fn)

    @property
    def f1(self):
        return 2 * self.tp / (2 * self.tp + self.fp + self.fn)


if __name__ == '__main__':
    d1 = ExperimentReport(50, 50, 50, 50, "Krowa")

    print(f"Eksperyment: {d1.name}")
    print(f"Accuracy: {d1.accuracy:.2f}")
    print(f"Precision: {d1.precision:.2f}")
    print(f"Recall: {d1.recall:.2f}")
    print(f"F1-Score: {d1.f1:.2f}")

    del d1.name
    print(f"Eksperyment: {d1.name}")