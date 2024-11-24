import unittest
from entities.product import Product

class TestProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.iphone = Product("Iphone 12", 1000.00)
        cls.xiaomi = Product("Xiaomi GT", 300.00)

    def setUp(self):
        print(f"\nRunning {self._testMethodName}")

    def test_product_name(self):
        self.assertEqual(self.iphone.name, "Iphone 12", "The product name should be Iphone 12")

    def test_product_price(self):
        self.assertEqual(self.iphone.price, 1000.00, "The product price should be 1000.00")

    def test_product_discount(self):
        self.assertEqual(self.iphone.discount, 0.00, "The product discount should be 0.00")
