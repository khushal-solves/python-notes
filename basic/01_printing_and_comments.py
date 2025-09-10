"""
01_printing_and_comments.py
Purpose: Deep dive into print(), comments, docstrings, formatting, and common pitfalls.
Run: python 01_printing_and_comments.py
"""

def section_header(title):
    print("\n" + "="*10 + " " + title + " " + "="*10 + "\n")

section_header("Basic print and types")
print("Hello, world!")           # simple string
print(123, 456, "mixing types")  # print accepts multiple args, separated by spaces by default
print("No newline...", end="")   # change end
print(" still same line")
print("a", "b", "c", sep="-")    # custom separator

section_header("Escape sequences and raw strings")
print("Line1\nLine2\tTabbed")    # \n, \t
print(r"Raw string: backslash\n not interpreted")  # raw string literal

section_header("f-strings and formatting")
name = "Khushal"
age = 25
print(f"My name is {name} and I am {age} years old.")
# advanced formatting
pi = 3.1415926535
print(f"Pi to 3 decimals: {pi:.3f}")

section_header("Docstrings and comments")
def example(a, b):
    """This function adds a and b and returns result.
    Docstrings describe purpose, parameters and return.
    """
    # single-line comment: explain non-obvious code
    return a + b

print("Docstring:", example.__doc__)

section_header("Common pitfalls")
# 1) Forgetting parentheses in Python 3: print "hello" -> SyntaxError
# 2) Mixing bytes and strings in print on some I/O setups
# 3) Long outputs: prefer writing to file or pagers

section_header("Mini Exercises (try these, edit file, re-run)")
# 1) Print a multi-line message using a single print() call.
# 2) Print a table of numbers 1 to 3 and their squares using sep and end.
# 3) Create a function with a docstring and print that docstring.

