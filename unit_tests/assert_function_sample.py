"""
In this example the callable function should manage the validation of the number
"""
def sum_two_positive_numbers(a: int, b: int) -> int:

    assert a >= 0 and b >= 0, "Both numbers must be positive"
    # if a < 0 or b < 0:
    #     raise ValueError("Both numbers must be positive")
    return a + b

if __name__ == "__main__":
    resultado = sum_two_positive_numbers(-1, 2)
    print(resultado)