class ProductDiscountError(Exception):
    pass

class Product:
    def __init__(self, name:str, price:float, discount:float = 0.00) -> None:
        self.name = name
        self.price = price
        if discount > price:
            raise ProductDiscountError("Discount should be a value less than the price")
        self.discount = discount

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f} - ${self.discount:.2f}"