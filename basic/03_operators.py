"""
03_operators.py
Purpose: arithmetic, comparison, logical, assignment, membership, identity.
"""

def header(t): print("\n***", t, "***\n")

header("Arithmetic")
a, b = 9, 4
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)     # float division
print("a // b =", a // b)   # floor division
print("a % b =", a % b)     # remainder
print("a ** b =", a ** b)   # power

header("Comparison")
print(a > b, a < b, a == b, a != b)

header("Logical operators and truthiness")
print(True and False, True or False, not True)
print("Truthiness examples:", bool([]), bool([1]), bool(""), bool("hi"))

header("Assignment and augmented assignment")
c = 5
c += 2   # c = c + 2
print("c after +=2:", c)

header("Membership and identity")
lst = [1,2,3]
print("2 in lst?", 2 in lst)
x = [1,2]
y = x
z = [1,2]
print("x is y?", x is y)    # same object
print("x is z?", x is z)    # equal but different object
print("x == z?", x == z)    # equality checks values

header("Operator precedence")
# parentheses first, then **, then unary +/-, then *,/,//,%, then +,-
print("Precedence example:", 2 + 3 * 4)           # -> 14
print("With parentheses:", (2 + 3) * 4)            # -> 20

header("Mini Exercises")
# 1) Compute BMI = weight_kg / (height_m ** 2) and print classification using comparisons.
# 2) Predict the output of: True + True, True * 5

