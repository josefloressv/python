import pytest
from entities.product import Product
from entities.product import ProductDiscountError
from entities.shopping_cart import ShoppingCart
import re

def is_not_connected():
    return True

class TestShoppingCart():
    @classmethod
    def setup_class(cls):
        # test products
        cls.iphone = Product("Iphone 12", 1000.00)
        cls.xiaomi = Product("Xiaomi GT", 300.00)

    @pytest.fixture(autouse=True)
    def setup_method(self, request):
        # Create a new cart for each test
        self.cart = ShoppingCart()
        print(f"\nRunning {request.node.name}")

    def test_add_product_iphone(self):
        self.cart.add_product(self.iphone)
        assert self.cart.num_products() == 1, "The product should be added to the cart"
        self.cart.print_products()

    def test_add_product_xiaomi(self):
        assert self.cart.add_product(self.xiaomi), "The product should be added to the cart"
        self.cart.print_products()

    def test_remove_product_iphone(self):
        self.cart.add_product(self.iphone)
        assert self.cart.remove_product(self.iphone), "The product should be removed from the cart"
        self.cart.print_products()

    def test_has_products(self):
        self.cart.add_product(self.iphone)
        self.cart.add_product(self.xiaomi)
        print(f"\nItems in cart: {self.cart.num_products()}")
        assert self.cart.has_products(), "The cart should have products"
        assert not self.cart.is_empty_cart(), "The cart should not be empty"

    def test_is_empty_cart(self):
        print(f"\nItems in cart: {self.cart.num_products()}")
        assert self.cart.is_empty_cart(), "The cart should be empty"

    def test_is_iphone_in_cart(self):
        self.cart.add_product(self.iphone)
        assert self.iphone in self.cart.products(), "The cart should have the Iphone"

    def test_cart_has_not_xiaomi(self):
        self.cart.add_product(self.iphone)
        # self.cart.add_product(self.xiaomi)
        assert not self.xiaomi in self.cart.products(), "The cart should not have the Xiaomi"

    def test_raise_discount_error(self):
        with pytest.raises(ProductDiscountError):
            Product("Iphone 12", 1000.00, 1200.00)
    
    def test_total_cart(self):
        self.cart.add_product(self.iphone)
        self.cart.add_product(self.xiaomi)
        assert self.cart.total() == 1300.00, "The total should be 1300.00"
    
    def test_total_more_than_or_equal_1000(self):
        self.cart.add_product(self.iphone)
        assert self.cart.total() >= 1000.00, "The total should be greater than or equal to 1000.00"

    # Skip tests
    @pytest.mark.skip(reason="I don't want to run this test")
    def test_skip(self):
        pass

    @pytest.mark.skipif(is_not_connected(), reason="Skip this test because it is not connected")
    def test_skip_condition(self):
        pass

    # Regex
    def test_regex(self):
        assert re.match("abc", "abc"), "The strings should match"
