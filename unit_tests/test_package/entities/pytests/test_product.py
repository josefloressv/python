import pytest
from entities.product import Product

class TestProduct:
    @classmethod
    def setup_class(cls):
        cls.iphone = Product("Iphone 12", 1000.00)
        cls.xiaomi = Product("Xiaomi GT", 300.00)

    @pytest.fixture(autouse=True)
    def setup_method(self, request):
        print(f"\nRunning {request.node.name}")

    def test_product_name(self):
        assert self.iphone.name == "Iphone 12", "The product name should be Iphone 12"

    def test_product_price(self):
        assert self.iphone.price == 1000.00, "The product price should be 1000.00"

    def test_product_discount(self):
        assert self.iphone.discount == 0.00, "The product discount should be 0.00"