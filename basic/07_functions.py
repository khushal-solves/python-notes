"""
07_functions.py
Purpose: defining functions, arguments, defaults, keyword args, *args, **kwargs, scope, lambda, documentation.
"""

def header(t): print("\n###", t, "###\n")

header("Defining & calling")
def add(a, b):
    """Return sum of a and b."""
    return a + b

print("add(2,3):", add(2,3))

header("Default arguments and mutables gotcha")
def append_item(lst=None):
    if lst is None:
        lst = []
    lst.append("item")
    return lst

print("append_item:", append_item())
print("append_item again:", append_item())  # safe because we used None default

header("*args and **kwargs")
def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1,2, x=3, y=4)

header("Scope: local vs global")
g = 10
def scope_demo():
    g = 5  # local
    print("local g:", g)
scope_demo()
print("global g:", g)

header("Lambda (anonymous) functions")
square = lambda x: x * x
print("square(5):", square(5))

header("Docstrings and type hints")
def greet(name: str) -> str:
    """Return greeting for name (type-hinted)."""
    return f"Hello {name}"

print(greet("Khushal"))

header("Mini Exercises")
# 1) Write a function factorial(n) iterative and recursive versions.
# 2) Write a function that accepts *args and returns their average.

