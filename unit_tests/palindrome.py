"""Docstring is used to document objects like modules, functions, classes, and methods

palindrome.py
This module contains a User class and a function to check if a string is a palindrome.

Classes:
    User: Represents a user with a name and age.
Functions:
    is_palindrome(s: str) -> bool: Check if the given string is a palindrome.

For VSCode we can use> autoDocstring: VSCode Python Docstring Generator
To check the doctrine test run python -m doctest palindrome.py -v 
How to check in interactive python:
  import palindrome
    help(palindrome)
    help(palindrome.User)
    help(palindrome.User.__init__)
    help(palindrome.is_palindrome)
"""

class User:
    """Represents a user."""
    def __init__(self, name: str, age: int) -> None:
        """Create a new User object.

        Args:
            name (str): The user's name.
            age (int): The user's age.
        """
        self.name = name
        self.age = age

def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome("Hola Mundo")
        False
        >>> is_palindrome("Anita Lava la tina")
        True
    """
    # Remove non-alphanumeric characters and convert to lowercase
    # basic
    cleaned = s.lower().replace(' ', '')
    # advanced
    # cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
