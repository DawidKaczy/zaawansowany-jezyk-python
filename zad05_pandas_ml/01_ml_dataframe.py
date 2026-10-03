import pandas as pd
from sklearn.datasets import load_iris


class MLDataFrame:
    def __init__(self, df: pd.DataFrame, nazwa_kolumny):
        self.__name = nazwa_kolumny
        self.df = df.copy()

    @property
    def name(self):
        return self.__name

    def add_feature(self, nowa_nazwa, func):
        self.df[nowa_nazwa] = self.df[self.__name].apply(func)

    def __repr__(self):
        return f"Kolumna: {self.name}\nDataset:\n{self.df}"

    def mean(self, col):
        return self.df[col].mean()

    def variance(self, col):
        return self.df[col].var()

    def describe(self):
        return self.df.describe()

    @classmethod
    def from_iris(cls):
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['target'] = iris.target
        return cls(df, iris.feature_names[0])


if __name__ == '__main__':
    # Setup initial data
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    })

    # Initialize with 'a' as our primary column
    v1 = MLDataFrame(df, 'a')
    v1.add_feature('x^2', lambda x: x ** 2)

    print(v1)

    print(v1.mean('a'))
    print("\n")
    print(v1.variance('a'))
    print("\n")
    print(v1.describe())

    v2 = MLDataFrame.from_iris()
    print(v2.mean("sepal width (cm)"))
    print(v2.describe())


