"""
Solutions for 04_exercises.md – Advanced OOP
"""

# Q1. Class vs Instance Variables
class Car:
    wheels = 4  # class variable

    def __init__(self, brand):
        self.brand = brand  # instance variable

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand, "has", car1.wheels, "wheels")
print(car2.brand, "has", car2.wheels, "wheels")


# Q2. Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Khushal", 1000)
account.deposit(500)
print(account.owner, "balance:", account.get_balance())


# Q3. Method Overriding
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

a = Animal()
d = Dog()
print("Animal sound:", a.sound())
print("Dog sound:", d.sound())


# Q4. Polymorphism
class Cat:
    def speak(self): return "Meow"

class Bird:
    def speak(self): return "Tweet"

class Dog:
    def speak(self): return "Woof"

animals = [Cat(), Bird(), Dog()]
for animal in animals:
    print(animal.speak())


# Stretch Task 1 – Inheritance Chain
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

class GraduateStudent(Student):
    def __init__(self, name, grade, thesis_title):
        super().__init__(name, grade)
        self.thesis_title = thesis_title

grad = GraduateStudent("Khushal", "A", "AI in Education")
print(f"Name: {grad.name}, Grade: {grad.grade}, Thesis: {grad.thesis_title}")


# Stretch Task 2 – Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print("Vector addition:", v3)

