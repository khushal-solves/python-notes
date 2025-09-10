"""
11_exceptions.py
Purpose: try/except/else/finally, raising exceptions, custom exceptions, best practices.
"""

def h(t): print("\n***", t, "***\n")

h("Try / Except basics")
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("Caught ZeroDivisionError:", e)
except Exception as e:
    print("Generic exception:", e)
else:
    print("No exception occurred")
finally:
    print("This always runs")

h("Raising exceptions")
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True

try:
    check_age(-5)
except ValueError as e:
    print("Raised ValueError:", e)

h("Custom exceptions")
class MyAppError(Exception):
    pass

def do_something(flag):
    if not flag:
        raise MyAppError("Flag was False")

try:
    do_something(False)
except MyAppError as e:
    print("Handled custom exception:", e)

h("Best practices")
# - Catch specific exceptions, not bare except.
# - Use finally for cleanup (closing files or releasing resources).
# - Add helpful messages when raising exceptions.

h("Mini Exercises")
# 1) Implement a safe division function safe_div(a,b) that returns None on error but logs the type of error.
# 2) Create a custom exception InvalidInput and use it when parsing numbers from a string fails.

