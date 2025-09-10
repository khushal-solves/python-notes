"""
04_input_output.py
Purpose: input(), converting types, formatted output (f-strings), reading/writing simple console I/O patterns.
"""

def header(t): print("\n--", t, "--\n")

header("Simple input and type conversion")
# NOTE: Uncomment to interactively test
# name = input("Enter your name: ")
# age_s = input("Enter your age: ")
# age = int(age_s)
# print(f"Hello {name}, in 5 years you'll be {age+5} years old.")

header("Safe input conversion pattern")
def safe_int(prompt):
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid integer.")

# To try, uncomment:
# n = safe_int("Enter an integer: ")
# print("You entered:", n)

header("Printing formats")
x, y = 3.14159, 2
print("Old style: %0.2f and %d" % (x, y))
print("str.format: {:.2f} and {}".format(x, y))
print(f"f-string: {x:.2f} and {y}")

header("Common pitfalls")
# input() always returns string.
# watch out for trailing whitespace; use .strip() when necessary.

header("Mini Exercises")
# 1) Write a small interactive prompt that asks for three numbers and prints their average.
# 2) Use safe_int to ask for a positive integer and print factorial (iterative).

