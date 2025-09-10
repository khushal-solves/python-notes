
---

### `02_exercises.md`

````markdown
# Exercises – Modules & Packages

## 1. Concept Questions
1. What is the difference between a **module** and a **package** in Python?  
2. Explain the purpose of using an **alias** when importing a module.  
3. Why is it sometimes better to use `import math` instead of `from math import *`?  
4. How can you create and use your **own module** in Python?  

---

## 2. Coding Exercises

### Q1. Import and Use Math
Import the `math` module and print:
- The square root of 64  
- The value of π  

---

### Q2. Random Numbers
Use the `random` module to:
- Generate a random integer between 1 and 100  
- Select a random element from the list `["apple", "banana", "cherry"]`  

---

### Q3. Aliases
Import the `datetime` module as `dt` and print today’s date.

---

### Q4. Create a Custom Module
1. Create a file named `greetings.py` with a function:
```python
def say_hello(name):
    return f"Hello, {name}!"
````

2. Import `greetings` into your main script and call `say_hello("Khushal")`.

---

## 3. Stretch Tasks

### Task 1 – Multiplication Module

Create a module named `mathutils.py` with a function `multiply(a, b)` that returns the product. Import and test it in a main script.

---

### Task 2 – Package Simulation

Simulate a package structure:

```
mypackage/
    __init__.py
    helper.py
```

In `helper.py`, write a function `greet()` that prints `"Hello from helper!"`.
Import and call it from your main script.

````

