## Pytest execute all tests in a directory
## Group unit tests in a separated contexts

```bash
# Install pytest
pip install pytest

# Run all tests in a directory
pytest
pytest -v -s # verbose and show print statements

# Run specific test
pytest test_sample.py
pytest test_sample.py::test_sample_class
pytest test_sample.py::test_sample_class::test_sample_1

# Run tests in a directory
pytest test_dir

# Run tests with specific marker
pytest test_dir -v -m "smoke"
```

## Coverage
```bash
# Install coverage
pip install coverage

# Run tests with coverage
coverage run -m pytest test_dir
coverage report -m

# Generate html report
coverage html
```
