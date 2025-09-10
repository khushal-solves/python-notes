"""
solutions_advanced.py
=====================
Combined script covering all advanced Python topics.
"""

# 1. Comprehensions
print("\n=== LIST, DICT, SET COMPREHENSIONS ===")
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print("Squares:", squares)

lengths = {w: len(w) for w in ["apple", "banana", "cherry"]}
print("Word lengths:", lengths)

unique_letters = {ch for ch in "hello world" if ch.isalpha()}
print("Unique letters:", unique_letters)

gen = (n**2 for n in range(5))
print("Generator values:", list(gen))


# 2. Modules & Packages
print("\n=== MODULES ===")
import math, random, datetime, os, sys
print("Math sqrt:", math.sqrt(16))
print("Random int:", random.randint(1, 10))
print("Today:", datetime.date.today())
print("CWD:", os.getcwd())
print("Python version:", sys.version)


# 3. Advanced OOP
print("\n=== OOP ADVANCED ===")
class Dog:
    species = "Canis"   # class variable
    def __init__(self, name):
        self.name = name

dog1 = Dog("Tommy")
print(dog1.name, dog1.species)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount): self.__balance += amount
    def get_balance(self): return self.__balance

acc = Account("Khushal", 1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

class Animal: 
    def sound(self): return "Some sound"
class Dog(Animal): 
    def sound(self): return "Woof"
class Cat(Animal): 
    def sound(self): return "Meow"

for a in [Dog(), Cat(), Animal()]:
    print(a.sound())


# 4. Custom Exceptions
print("\n=== CUSTOM EXCEPTIONS ===")
class NegativeNumberError(Exception): pass
def square_root(n):
    if n < 0: raise NegativeNumberError("Negative number!")
    return n ** 0.5
try:
    print(square_root(9))
    print(square_root(-1))
except NegativeNumberError as e:
    print("Error:", e)


# 5. Virtualenv & Pip (instructions only)
print("\n=== VIRTUALENV & PIP ===")
print("python -m venv myenv")
print("source myenv/bin/activate (Linux/Mac)")
print("myenv\\Scripts\\activate   (Windows)")
print("pip install requests")

