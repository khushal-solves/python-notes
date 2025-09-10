"""
05_conditionals.py
Purpose: if / elif / else, nested conditions, truthy/falsy, short-hand if, and common mistakes.
"""

def header(t): print("\n>>>", t, "<<<\n")

header("Basic if / elif / else")
n = 0
if n > 0:
    print("positive")
elif n == 0:
    print("zero")
else:
    print("negative")

header("Nested conditions")
x = 12
if x % 2 == 0:
    if x % 3 == 0:
        print("multiple of 2 and 3")
    else:
        print("multiple of 2 only")
else:
    print("odd")

header("Truthy / Falsy values")
tests = [0, 1, "", "hi", [], [1], {}, {"k":1}, None]
for t in tests:
    print(repr(t), "->", bool(t))

header("Short-hand if / ternary")
a, b = 5, 10
smaller = a if a < b else b
print("Smaller:", smaller)

header("Common mistakes")
# - using = instead of == in comparisons (SyntaxError)
# - relying on float equality (use tolerance)
# - forgetting indentation (IndentationError)

header("Mini Exercises")
# 1) Implement grade assignment: given score 0-100, print A/B/C/D/F with >=90 A etc.
# 2) Given a year, print whether it's a leap year (rules: divisible by 4, but not by 100 unless by 400).

