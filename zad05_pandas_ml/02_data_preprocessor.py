import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import numpy as np

class DataPreprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.history = []

    def save_state(self):
        self.history.append(self.df.copy())

    def undo(self):
        if self.history:
            self.df = self.history.pop()
            print("Pomyślnie cofnięto ostatnią operację.")
        else:
            print("Brak wcześniejszych operacji do cofnięcia.")

    def get_numeric_columns(self):
        return self.df.select_dtypes(include='number').columns.tolist()

    def get_categorical_columns(self):
        return self.df.select_dtypes(include=['object', 'category', 'str']).columns.tolist()

    def drop_missing(self):
        self.save_state()
        self.df = self.df.dropna(how='any')

    def fill_missing(self, strategy='mean'):
        self.save_state()
        num_cols = self.get_numeric_columns()

        if strategy == 'mean':
            self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mean())
        elif strategy == 'median':
            self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].median())
        elif strategy == 'mode':
            for col in self.df.columns:
                if not self.df[col].mode().empty:
                    self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
        else:
            raise ValueError("Dozwolone strategie to: 'mean', 'median', 'mode'")


    def scale_min_max(self):
        self.save_state()
        num_cols = self.get_numeric_columns()
        if num_cols:
            scaler = MinMaxScaler()
            self.df[num_cols] = scaler.fit_transform(self.df[num_cols])

    def scale_standard(self):
        self.save_state()
        num_cols = self.get_numeric_columns()
        if num_cols:
            scaler = StandardScaler()
            self.df[num_cols] = scaler.fit_transform(self.df[num_cols])

    def encode_label(self):
        self.save_state()
        cat_cols = self.get_categorical_columns()
        le = LabelEncoder()
        for col in cat_cols:
            self.df[col] = le.fit_transform(self.df[col].astype(str))

    def encode_one_hot(self):
        self.save_state()
        cat_cols = self.get_categorical_columns()
        if cat_cols:
            self.df = pd.get_dummies(self.df, columns=cat_cols)



data = {
    'Wiek': [25, 30, np.nan, 22, 35],
    'Zarobki': [5000, np.nan, 5500, 4500, 7000],
    'Miasto': ['Warszawa', 'Kraków', 'Warszawa', 'Poznań', 'Kraków'],
    'Dział': ['IT', 'HR', 'IT', 'Sprzedaż', 'HR']
}
df_test = pd.DataFrame(data)

print(df_test)
print("\n")


preprocessor = DataPreprocessor(df_test)
print("Numeryczne:", preprocessor.get_numeric_columns())
print("Kategoryczne:", preprocessor.get_categorical_columns())
print("\n")

preprocessor.fill_missing('mean')
print("3PO UZUPEŁNIENIU BRAKÓW ŚREDNIĄ")
print(preprocessor.df)
print("\n")

preprocessor.scale_min_max()
print("4.PO  MIN-MAX")
print(preprocessor.df)
print("\n")

preprocessor.encode_one_hot()
print("5.PO  ONE-HOT")
print(preprocessor.df)
print("\n")

print("6.TESTOWANIE")
preprocessor.undo()
print(preprocessor.df)

preprocessor.undo()
print(preprocessor.df)