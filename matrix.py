import random
from CSVManager import CSVManager
class Matrix(CSVManager):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.matrix = []

    def create_matrix(self, rows, cols, min_value, max_value):
        self.matrix = [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]
        self.save_to_file()

    def transpose(self):
        if not self.matrix:
            self.load_from_file()


        self.matrix = [list(row) for row in zip(*self.matrix)]
        self.save_to_file()

    def get_matrix(self):
        if not self.matrix:
            self.load_from_file()
        return self.matrix

    def save_to_file(self):
        self.overwrite_file(self.matrix)

    def load_from_file(self):
        data = self.read_data()
        if data:
            self.matrix = [[int(num) for num in row] for row in data]
