class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []
    def add_product(self, product: str):
        self.products.append(product)
    def get_by_letter(self, letter: str):
        words = [product for product in self.products if product.startswith(letter)]
        return words
    def __repr__(self):
        sorted_products = sorted(self.products)
        result = f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted_products)

        return result
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

