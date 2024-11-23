"""
In python we could use conditional statements to check if a condition is met, but we can also use the assert statement.
is preffered to use the assert statement to check for conditions that should never happen.
"""
if __name__ == "__main__":
    try:
        assert  10 == 9, "Error, should be equal"
        # if not 10 == 9:
        #     raise AssertionError("Error, should be equal")

        print("Everything passed")
    except AssertionError as e:
        print(e)