"""
05_custom_exceptions.py
=======================
Creating and using custom exceptions.
"""

print("\n=== CUSTOM EXCEPTION CLASS ===")
class NegativeNumberError(Exception):
    """Raised when a number is negative."""
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot take square root of a negative number")
    return n ** 0.5

try:
    print(square_root(25))
    print(square_root(-5))
except NegativeNumberError as e:
    print("Error:", e)

