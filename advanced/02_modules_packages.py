"""
02_modules_packages.py
=======================
Importing modules and creating custom modules.
"""

print("\n=== USING BUILT-IN MODULES ===")
import math
print("Square root of 16:", math.sqrt(16))
print("Pi value:", math.pi)

import random
print("Random number [1-10]:", random.randint(1, 10))


print("\n=== IMPORTING WITH ALIASES ===")
import datetime as dt
today = dt.date.today()
print("Today's date:", today)


print("\n=== CREATING YOUR OWN MODULE ===")
# Save the following as mymodule.py in the same folder:
# def greet(name):
#     return f"Hello, {name}!"

import mymodule
print(mymodule.greet("Khushal"))

