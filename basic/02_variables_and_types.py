"""
02_variables_and_types.py
Purpose: variable rules, dynamic typing, type checking, conversions, None.
"""

def section_header(title):
    print("\n" + "-"*8 + " " + title + " " + "-"*8 + "\n")

section_header("Naming rules & assignment")
# valid names: letters, numbers, underscore; cannot start with digit; case-sensitive
my_var = 10
_myVar2 = "ok"
# avoid reserved keywords (e.g., class, def, if)

section_header("Dynamic typing demonstration")
x = 5
print("x:", x, type(x))
x = "now a string"
print("x:", x, type(x))

section_header("Common types")
a_int = 10
a_float = 3.5
a_str = "text"
a_bool = True
a_none = None
print(a_int, a_float, a_str, a_bool, a_none)

section_header("Type conversion / casting")
s = "123"
n = int(s)          # -> 123 (int)
f = float("4.5")    # -> 4.5
print("int('123'):", n, "float('4.5'):", f)
# invalid conversion raises ValueError
try:
    int("abc")
except ValueError as e:
    print("ValueError converting 'abc' to int:", e)

section_header("Type checking and isinstance")
print(isinstance(5, int))
print(isinstance(True, bool))  # bool is subclass of int, still True

section_header("Mutability notes")
# immutable: int, float, str, tuple; mutable: list, dict, set
a = [1,2,3]
b = a
b.append(4)
print("a after b.append:", a)  # shows list is shared (mutability)

section_header("Mini Exercises")
# 1) Create variables: radius (float), area (compute using pi), and print with 2 decimals.
# 2) Show what happens when you try to change a character inside a string: s[0] = 'X'

