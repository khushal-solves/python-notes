# Exercises – Advanced OOP

## 1. Concept Questions
1. What is the difference between a **class variable** and an **instance variable**?  
2. How does **encapsulation** protect data inside a class?  
3. Explain **method overriding** with an example.  
4. What does **polymorphism** mean in object-oriented programming?  

---

## 2. Coding Exercises

### Q1. Class vs Instance Variables
Create a class `Car` with:
- A class variable `wheels = 4`  
- An instance variable `brand`  
Create two cars with different brands, and print their brand and wheels.

---

### Q2. Encapsulation
Create a class `BankAccount` with:
- A private variable `__balance`  
- Methods `deposit(amount)` and `get_balance()`  
Demonstrate depositing money and checking balance.

---

### Q3. Method Overriding
Create two classes `Animal` and `Dog`.  
- `Animal` has a method `sound()` returning `"Some sound"`.  
- `Dog` overrides it with `"Woof"`.  
Print results from both classes.

---

### Q4. Polymorphism
Create classes `Cat`, `Bird`, and `Dog`. Each should have a `speak()` method returning a different sound.  
Write a loop that goes through a list of these animals and calls `speak()` on each.

---

## 3. Stretch Tasks

### Task 1 – Inheritance Chain
Create a base class `Person` with `name`.  
Create a child class `Student` with `grade`.  
Create another child class `GraduateStudent` with `thesis_title`.  
Demonstrate creating a `GraduateStudent` object and printing all attributes.

---

### Task 2 – Operator Overloading
Create a class `Vector` with attributes `x` and `y`.  
Overload the `+` operator so you can add two vectors like:
```python
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2   # should give Vector(6, 8)

