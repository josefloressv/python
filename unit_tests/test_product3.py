import unittest
from product import Product

class TestProduct(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # We can use this method to setup the test, initialize variables, etc.
        # This method is called before the first test method in the test class
        # and can share resources for all test methods
        print("Setting up the test class")
        cls.name = "Iphone 12"
        cls.price = 1000.00
        cls.smartphone = Product(cls.name, cls.price)
    @classmethod
    def tearDownClass(cls):
        # We can use this method to clean up the test, close connections, etc.
        # This method is called after the last test method in the test class
        print("Tearing down the test class")
    def setUp(self):
        # Whe can use this method to setup the test, initialize variables, etc.
        print("Setting up the test")
    def tearDown(self):
        # We can use this method to clean up the test, close connections, etc.
        print("Tearing down the test")
        # pass

    def test_product(self):
        self.assertEqual(self.smartphone.name, self.name, "The name should be Iphone")
        self.assertEqual(self.smartphone.price, self.price, "The price should be 1000")

    def test_product_with_discount(self):
        self.smartphone.discount = 100
        self.assertEqual(self.smartphone.discount, 100, "The discout should be 100")
if __name__ == "__main__":
    unittest.main()