# Unit Test Package

This directory contains unit tests for the `entities` package, demonstrating how to modularize and organize unit tests in a Python project.

## Directory Structure

```
unit_tests/
├── test_package/
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── product.py
│   │   ├── shopping_cart.py
│   │   └── unit_tests/
│   │       ├── __init__.py
│   │       ├── test_product.py
│   │       └── test_shopping_cart.py
│   ├── main.py
│   └── README.md
```

## How to execute the Tests
### With UnitTest

```bash
# Run all filtest tests from a package
python -m unittest discover -s entities/unit_tests

# Run Product tests
python -m unittest entities.unit_tests.test_product -v

# Run ShoppingCart tests
python -m unittest entities.unit_tests.test_shopping_cart -v

# Run an specific test
python -m unittest entities.unit_tests.test_shopping_cart.TestShoppingCart.test_add_product_iphone -v
```

### with Pytest
```bash
# Install pytest
pip install pytest

# Run all tests in a directory
pytest -v -s entities/pytests
```

### Generating report with Coverage
```bash
# Install coverage
pip install coverage

# Run tests with coverage and unitest
coverage run -m unittest discover -s entities/unit_tests

# Run tests with coverage and pytest
coverage run -m pytest entities/pytests

# Generate report
coverage report -m

# Generate html report
coverage html
```

## Test Organization

### `entities` Package

- `product.py`: Contains the `Product` class and `ProductDiscountError` exception.
- `shopping_cart.py`: Contains the `ShoppingCart` class.

### `unit_tests` Directory

- `test_product.py`: Contains unit tests for the `Product` class.
- `test_shopping_cart.py`: Contains unit tests for the `ShoppingCart` class.

### `__init__.py` Files

- `entities/__init__.py`: Marks the `entities` directory as a package and imports `Product` and `ProductDiscountError`.
- `unit_tests/__init__.py`: Marks the `unit_tests` directory as a package.

## Best Practices

- **Modularization**: Organize tests in a directory structure that mirrors the structure of the code being tested.
- **Test Independence**: Ensure that tests are independent of each other to maintain reliability and maintainability.
- **Setup and Teardown**: Use `setUp` and `tearDown` methods to prepare and clean up before and after each test. Use `setUpClass` and `tearDownClass` for class-level setup and teardown.
- **Assertions**: Use assertions to validate the expected outcomes of tests.
