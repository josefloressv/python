from entities.product import Product

class ShoppingCart:
    def __init__(self) -> None:
        self.__products : list[Product] = []

    def products(self) -> list[Product]:
        return self.__products

    def total(self) -> float:
        return sum([product.price for product in self.__products])

    def add_product(self, product:Product) -> bool:
        self.__products.append(product)
        return True

    def remove_product(self, product:Product) -> bool:
        self.__products.remove(product)
        return True

    def is_empty_cart(self) -> bool:
        return self.num_products() == 0

    def num_products(self) -> int:
        return len(self.__products)

    def has_products(self) -> bool:
        return not self.is_empty_cart()

    def print_products(self) -> None:
        print()
        # print("name - price - discount")
        for product in self.__products:
            print(product)