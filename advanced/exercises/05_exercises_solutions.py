"""
Solutions for 05_exercises.md – Custom Exceptions
"""

# Q1. Basic Custom Exception
class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot take square root of a negative number")
    return n ** 0.5

try:
    print("Square root of 25:", square_root(25))
    print("Square root of -5:", square_root(-5))
except NegativeNumberError as e:
    print("Error:", e)


# Q2. Divide by Zero Handling
class ZeroDivisionCustomError(Exception):
    pass

def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionCustomError("Cannot divide by zero!")
    return a / b

try:
    print("10 / 2 =", safe_divide(10, 2))
    print("5 / 0 =", safe_divide(5, 0))
except ZeroDivisionCustomError as e:
    print("Error:", e)


# Q3. Age Validation
class AgeTooLowError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeTooLowError("Age is below 18, access denied")
    print("Access granted")

try:
    check_age(20)
    check_age(15)
except AgeTooLowError as e:
    print("Error:", e)


# Stretch Task 1 – Password Validator
class ShortPasswordError(Exception): pass
class NoNumberError(Exception): pass

def validate_password(password):
    if len(password) < 6:
        raise ShortPasswordError("Password must be at least 6 characters")
    if not any(ch.isdigit() for ch in password):
        raise NoNumberError("Password must contain at least one number")
    print("Password is valid")

try:
    validate_password("hello1")
    validate_password("short")
except (ShortPasswordError, NoNumberError) as e:
    print("Error:", e)


# Stretch Task 2 – Banking Exception
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds!")
    return balance - amount

try:
    balance = 1000
    balance = withdraw(balance, 200)
    print("Balance after withdrawal:", balance)
    balance = withdraw(balance, 900)
except InsufficientFundsError as e:
    print("Error:", e)

