import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

class DatasetSplitter:
    def __init__(self, df: pd.DataFrame, target_col: str):
        self.df = df.copy()

        self.target_col = target_col
        self.train_set = None
        self.val_set = None
        self.test_set = None

    def split_train_test(self, test_size=0.2, random_state=None):
        self.train_set, self.test_set = train_test_split(self.df, test_size=test_size, random_state=random_state)
        self.val_set = None

    def split_train_val_test(self, val_size=0.2, test_size=0.2, random_state=None):
        temp_train, self.test_set = train_test_split(self.df, test_size=test_size, random_state=random_state)
        relative_val_size = val_size / (1.0 - test_size)
        self.train_set, self.val_set = train_test_split(temp_train, test_size=relative_val_size, random_state=random_state)

    def get_statistics(self):
        stats = {}
        datasets = {
            'Treningowy': self.train_set,
            'Walidacyjny': self.val_set,
            'Testowy': self.test_set
        }

        for name, dataset in datasets.items():
            if dataset is not None:
                stats[name] = {
                    'Liczba wierszy': len(dataset),
                    'Liczba klas': dataset[self.target_col].nunique(),
                    'Rozkład wartości': dataset[self.target_col].value_counts().to_dict()
                }
        return stats

    def print_statistics(self):
        stats = self.get_statistics()
        print(f"--- Statystyki podziału (Kolumna docelowa: '{self.target_col}') ---")
        for set_name, set_stats in stats.items():
            print(f"\nZbiór {set_name}:")
            print(f"  - Liczba wierszy: {set_stats['Liczba wierszy']}")
            print(f"  - Liczba unikalnych klas: {set_stats['Liczba klas']}")
            print(f"  - Rozkład klas: {set_stats['Rozkład wartości']}")


iris = load_iris()
df_iris = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_iris['target'] = iris.target

print("Rozmiar całego:", len(df_iris))

splitter = DatasetSplitter(df_iris, target_col='target')

print("\nPODZIAŁ TRAIN / TEST")
splitter.split_train_test(test_size=0.2, random_state=42)
splitter.print_statistics()

print("\nPODZIAŁ TRAIN / VAL / TEST")
splitter.split_train_val_test(val_size=0.2, test_size=0.2, random_state=42)
splitter.print_statistics()