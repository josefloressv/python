import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_product(self):
        name = "Test Product"
        price = 100.00
        discount = 0.10
        product = Product(name, price, discount)
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, 101, "The price should be 101")

if __name__ == "__main__":
    unittest.main()