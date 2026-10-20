from product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Метод для добавления одного товара в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return products_str

    @classmethod
    def new_product(cls, product_korzina):
        return Product(
            product_korzina['name'],
            product_korzina['description'],
            product_korzina['price'],
            product_korzina['quantity']
        )
