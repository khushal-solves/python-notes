"""
solutions_basics.py
===================

This script demonstrates all the fundamental Python concepts in one file.
Run it section by section, read the comments, and experiment with the code.
"""

print("\n=== 1. PRINTING & COMMENTS ===")
# Single-line comment
print("Hello, World!")       # Basic print
print("Hello", "Python")     # Multiple arguments
print("Line1\nLine2")        # Escape character
print("A", "B", sep="-")     # Custom separator
print("End without newline", end=" ")
print(" <- continues on same line")

"""
This is a multi-line comment
(or docstring, if used inside functions/classes).
"""


print("\n=== 2. VARIABLES & DATA TYPES ===")
x = 10                 # int
y = 3.14               # float
name = "Khushal"       # str
is_learning = True     # bool
z = None               # NoneType
print(x, type(x))
print(y, type(y))
print(name, type(name))
print(is_learning, type(is_learning))
print(z, type(z))

# Type casting
a = "123"
print(int(a) + 1)      # Convert str → int


print("\n=== 3. OPERATORS ===")
a, b = 7, 2
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Power:", a ** b)

print("Comparison (a > b):", a > b)
print("Equality (a == b):", a == b)
print("Logical AND:", True and False)
print("Logical OR:", True or False)

print("Membership:", "a" in "cat")
print("Identity:", a is b)


print("\n=== 4. INPUT / OUTPUT ===")
# Uncomment to test input
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")


print("\n=== 5. CONDITIONALS ===")
num = 5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Truthy/falsy example
if "":
    print("Empty string is truthy")
else:
    print("Empty string is falsy")


print("\n=== 6. LOOPS ===")
print("For loop with range:")
for i in range(1, 6):
    print(i, end=" ")

print("\nLooping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("While loop:")
count = 0
while count < 3:
    print("Count =", count)
    count += 1

print("Using break and continue:")
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)


print("\n=== 7. FUNCTIONS ===")
def greet(person):
    """Return a greeting message"""
    return f"Hello, {person}!"

print(greet("Khushal"))

# Default argument
def power(base, exp=2):
    return base ** exp

print("Square of 3:", power(3))
print("Cube of 3:", power(3, 3))

# Lambda function
double = lambda n: n * 2
print("Double of 5:", double(5))


print("\n=== 8. COLLECTIONS ===")
# List
numbers = [1, 2, 3]
numbers.append(4)
print("List:", numbers)

# Tuple
coordinates = (10, 20)
print("Tuple:", coordinates)

# Set
unique = {1, 2, 2, 3}
print("Set:", unique)

# Dictionary
student = {"name": "Khushal", "age": 25}
print("Dictionary keys:", student.keys())
print("Dictionary values:", student.values())


print("\n=== 9. STRINGS IN DEPTH ===")
text = " Python Basics "
print("Original:", repr(text))
print("Lower:", text.lower())
print("Upper:", text.upper())
print("Strip:", text.strip())
print("Substring [1:6]:", text[1:6])
print("Replace:", text.replace("Python", "Coding"))
print("Split:", text.split())
print("Join:", "-".join(["a", "b", "c"]))


print("\n=== 10. FILE HANDLING ===")
with open("example.txt", "w") as f:
    f.write("This is a sample file.\nHello Python!")

with open("example.txt", "r") as f:
    print("File contents:\n" + f.read())


print("\n=== 11. EXCEPTIONS ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero not allowed.")
finally:
    print("This block always runs.")


print("\n=== 12. CLASSES & OBJECTS ===")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old."

p1 = Person("Khushal", 25)
print(p1.introduce())

# Inheritance
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    
    def introduce(self):
        return super().introduce() + f" I study {self.course}."

s1 = Student("Amit", 20, "Python")
print(s1.introduce())


print("\n=== END OF BASICS ===")
print("You have completed the Python basics tour!")

