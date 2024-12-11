from CSVManager import CSVManager

class Products(CSVManager):
  def __init__(self, path):
    super().__init__(path)
    self.products = self._load_products()
    if self.products is None:
      self.products = []

  def _load_products(self):
    data = self.read_data()
    if not data:
      return []
    headers = data[0]
    return [dict(zip(headers, row)) for row in data[1:]]

  def _save_products(self):
    if not self.products:
      headers = self.products[0].keys()
      rows = [headers] + [[product[header] for header in headers] for product in self.products]
      self.overwrite_file(rows)

  def search_product(self, name):
    return [product for product in self.products if product['Название'] == name]

  def add_product(self, name, quantity, price):
    quantity = int(quantity)
    price = float(price)
    if not self.products:
      self.overwrite_file([['Название', 'Количество', 'Цена']])
    new_product = {'Название': name, 'Количество': quantity, 'Цена': price}
    self.products.append(new_product)
    self.add_row(new_product.values())

  def print_products(self, th=None):
      low_stock_products = [product for product in self.products if int(product['Количество']) < th] if th else self.products
      for product in low_stock_products:
        print(f"Название: {product['Название']}, Количество: {product['Количество']}, Цена: {product['Цена']}")
