from Product import Products
from matrix import Matrix
from Transactions import Transactions


class DataManager:
    def __init__(self, name):
        self.products_handler = Products(f'products_{name}.csv')
        self.matrix_handler = Matrix(f'matrix_{name}.csv')
        self.transactions_handler = Transactions(f'transactions_{name}.csv')