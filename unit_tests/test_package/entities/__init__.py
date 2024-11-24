"""
The __init__.py file is used to mark a directory as a Python package.
It can be an empty file, but it can also execute initialization code for the package or set the __all__ variable
to control what is imported when from package import * is used.
"""

from entities.product import Product, ProductDiscountError

# print("Initializing entities package")