"""
Solutions for 02_exercises.md – Modules & Packages
"""

# Q1. Using math module
import math
print("Square root of 64:", math.sqrt(64))
print("Pi value:", math.pi)


# Q2. Using random module
import random
print("Random integer [1–100]:", random.randint(1, 100))
print("Random choice:", random.choice(["apple", "banana", "cherry"]))


# Q3. Aliases with datetime
import datetime as dt
print("Today's date:", dt.date.today())


# Q4. Custom module (requires greetings.py file)
# greetings.py:
# def say_hello(name):
#     return f"Hello, {name}!"
import greetings
print(greetings.say_hello("Khushal"))


# Stretch Task 1 – mathutils module
# mathutils.py:
# def multiply(a, b):
#     return a * b
import mathutils
print("5 * 6 =", mathutils.multiply(5, 6))


# Stretch Task 2 – Package Simulation
# mypackage/__init__.py (empty or setup)
# mypackage/helper.py:
# def greet():
#     print("Hello from helper!")

from mypackage import helper
helper.greet()
