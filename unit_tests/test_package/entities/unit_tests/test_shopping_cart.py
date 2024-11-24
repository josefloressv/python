"""
In the unittest framework, the order in which tests are executed is not guaranteed.
By default, unittest runs tests in the order they are defined in the class,
but this behavior should not be relied upon. Tests should be independent of each other to ensure reliability and maintainability.
"""
import unittest
from entities.product import Product
from entities.product import ProductDiscountError
from entities.shopping_cart import ShoppingCart


def is_not_connected():
    return True

class TestShoppingCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # test products
        cls.iphone = Product("Iphone 12", 1000.00)
        cls.xiaomi = Product("Xiaomi GT", 300.00)

    def setUp(self):
        # Create a new cart for each test
        self.cart = ShoppingCart()
        print(f"\nRunning {self._testMethodName}")

    def test_add_product_iphone(self):
        self.cart.add_product(self.iphone)
        self.assertEqual(self.cart.num_products(), 1, "The product should be added to the cart")
        self.cart.print_products()

    def test_add_product_xiaomi(self):
        self.assertTrue(self.cart.add_product(self.xiaomi), "The product should be added to the cart")
        self.cart.print_products()

    def test_remove_product_iphone(self):
        self.cart.add_product(self.iphone)
        self.assertTrue(self.cart.remove_product(self.iphone), "The product should be removed from the cart")
        self.cart.print_products()

    def test_has_products(self):
        self.cart.add_product(self.iphone)
        self.cart.add_product(self.xiaomi)
        print(f"\nItems in cart: {self.cart.num_products()}")
        self.assertTrue(self.cart.has_products(), "The cart should have products")

    def test_is_empty_cart(self):
        print(f"\nItems in cart: {self.cart.num_products()}")
        self.assertTrue(self.cart.is_empty_cart(), "The cart should be empty")

    def test_is_iphone_in_cart(self):
        self.cart.add_product(self.iphone)
        self.assertIn(self.iphone, self.cart.products(), "The cart should have the Iphone")

    def test_cart_has_not_xiaomi(self):
        self.cart.add_product(self.iphone)
        # self.cart.add_product(self.xiaomi)
        self.assertNotIn(self.xiaomi, self.cart.products(), "The cart should not have the Xiaomi")

    def test_raise_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product("Iphone 12", 1000.00, 1200.00)
    
    def test_total_cart(self):
        self.cart.add_product(self.iphone)
        self.cart.add_product(self.xiaomi)
        self.assertEqual(self.cart.total(), 1300.00, "The total should be 1300.00")
    
    def test_total_more_than_or_equal_1000(self):
        self.cart.add_product(self.iphone)
        self.assertGreaterEqual(self.cart.total(), 1000.00, "The total should be greater than 1000.00")

    # Skip tests
    @unittest.skip("Skip this test")
    def test_skip(self):
        pass

    @unittest.skipIf(is_not_connected(), "Skip this test because is not connected")
    def test_skip_condition(self):
        pass

    # Regex
    def test_regex(self):
        self.assertRegex("abc", "abc", "The strings should match")

if __name__ == "__main__":
    unittest.main()