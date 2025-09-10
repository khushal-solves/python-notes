"""
03_standard_libraries.py
========================
Quick intro to some useful standard libraries.
"""

print("\n=== MATH MODULE ===")
import math
print("Factorial of 5:", math.factorial(5))
print("Ceil of 2.3:", math.ceil(2.3))


print("\n=== RANDOM MODULE ===")
import random
print("Random choice:", random.choice(["red", "green", "blue"]))


print("\n=== DATETIME MODULE ===")
import datetime
now = datetime.datetime.now()
print("Now:", now)
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))


print("\n=== OS MODULE ===")
import os
print("Current directory:", os.getcwd())


print("\n=== SYS MODULE ===")
import sys
print("Python version:", sys.version)

