from simple_table_v2 import SimpleTableV2

class Preprocessing(SimpleTableV2):
    slots = []

    def init(self, data):
        super().__init__(data)

    @property
    def table_data(self):
        return self.data

    def clear(self):
        kolukny = len(self.data[0])
        wiersze = len(self.data)
        for i in range(wiersze):
            for j in range(kolukny):
                self.data[i][j] = 0

    def str(self):
        return super().__str__()

    def add_row(self, new_row):
        return super().add_row(new_row)

    def add_column(self, new_column):
        return super().add_column(new_column)

    def normalize(self, axis):
        if axis not in ('row', 'col'):
            raise ValueError("Axis musi być 'row' lub 'col'")

        if axis == 'col':
            for j in range(len(self.data[0])):
                col_values = [self.data[i][j] for i in range(len(self.data))]
                min_val, max_val = min(col_values), max(col_values)
                if max_val - min_val == 0:
                    continue
                for i in range(len(self.data)):
                    self.data[i][j] = (self.data[i][j] - min_val) / (max_val - min_val)
        else:
            for i in range(len(self.data)):
                row_values = self.data[i]
                min_val, max_val = min(row_values), max(row_values)
                if max_val - min_val == 0:
                    continue
                self.data[i] = [(x - min_val) / (max_val - min_val) for x in row_values]

    def min_max_scaling(self, axis, feature_range=(0, 1)):
        if axis not in ('row', 'col'):
            raise ValueError("Axis musi być 'row' lub 'col'")
        min_range, max_range = feature_range

        if axis == 'col':
            for j in range(len(self.data[0])):
                col_values = [self.data[i][j] for i in range(len(self.data))]
                min_val, max_val = min(col_values), max(col_values)
                if max_val - min_val == 0:
                    continue
                for i in range(len(self.data)):
                    self.data[i][j] = min_range + (self.data[i][j] - min_val) * (max_range - min_range) / (
                                max_val - min_val)
        else:
            for i in range(len(self.data)):
                row_values = self.data[i]
                min_val, max_val = min(row_values), max(row_values)
                if max_val - min_val == 0:
                    continue
                self.data[i] = [min_range + (x - min_val) * (max_range - min_range) / (max_val - min_val) for x in
                                  row_values]

    def standardize(self, axis):
        if axis not in ('row', 'col'):
            raise ValueError("Axis musi być 'row' lub 'col'")

        if axis == 'col':
            for j in range(len(self.data[0])):
                col_values = [self.data[i][j] for i in range(len(self.data))]
                mean = sum(col_values) / len(col_values)
                std = (sum((x - mean) ** 2 for x in col_values) / len(col_values)) ** 0.5
                if std == 0:
                    continue
                for i in range(len(self.data)):
                    self.data[i][j] = (self.data[i][j] - mean) / std
        else:
            for i in range(len(self.data)):
                row_values = self.data[i]
                mean = sum(row_values) / len(row_values)
                std = (sum((x - mean) ** 2 for x in row_values) / len(row_values)) ** 0.5
                if std == 0:
                    continue
                self.data[i] = [(x - mean) / std for x in row_values]



if __name__ == '__main__':

    d1 = Preprocessing([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

    d2 = Preprocessing([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

    print(str(d1))
    d1.clear()
    print(str(d1))

    d1.add_row([1, 2, 3])
    print(str(d1))

    d1.add_column([4, 5, 6, 7])
    print(str(d1))

    d1.clear()
    print(str(d1))

    d2.normalize(axis='row')
    print(str(d2))

    d2.min_max_scaling(axis='row')
    print(str(d2))

    d2.standardize(axis='col')
    print(str(d2))




