"""
Solutions for 03_exercises.md – Standard Libraries
"""

# Q1. Math – Factorial & Square Root
import math
print("Factorial of 6:", math.factorial(6))
print("Square root of 49:", math.sqrt(49))


# Q2. Random – Dice Rolls
import random
dice_rolls = [random.randint(1, 6) for _ in range(5)]
print("Dice rolls:", dice_rolls)


# Q3. Datetime – Format Dates
import datetime
now = datetime.datetime.now()
print("Formatted datetime:", now.strftime("%Y-%m-%d %H:%M:%S"))


# Q4. OS Module – Directory Work
import os
print("Current working directory:", os.getcwd())
print("Contents of directory:", os.listdir("."))


# Q5. Sys Module – Python Info
import sys
print("Python version:", sys.version)


# Stretch Task 1 – Random Password Generator
import string
chars = string.ascii_letters + string.digits
password = "".join(random.choice(chars) for _ in range(8))
print("Generated password:", password)


# Stretch Task 2 – Simple Stopwatch
import time
input("Press Enter and then type your name quickly...")
start = datetime.datetime.now()
name = input("Enter your name: ")
end = datetime.datetime.now()
elapsed = (end - start).total_seconds()
print(f"Well done, {name}! You took {elapsed:.2f} seconds.")

