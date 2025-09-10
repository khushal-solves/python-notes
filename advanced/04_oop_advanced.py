"""
04_oop_advanced.py
==================
Advanced OOP features in Python.
"""

print("\n=== CLASS VS INSTANCE VARIABLES ===")
class Dog:
    species = "Canis"   # class variable

    def __init__(self, name):
        self.name = name  # instance variable

dog1 = Dog("Tommy")
dog2 = Dog("Max")
print(dog1.name, dog1.species)
print(dog2.name, dog2.species)


print("\n=== ENCAPSULATION ===")
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account("Khushal", 1000)
acc.deposit(500)
print("Balance:", acc.get_balance())


print("\n=== POLYMORPHISM & METHOD OVERRIDING ===")
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.sound())

