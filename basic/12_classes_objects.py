"""
12_classes_objects.py
Purpose: classes, instances, attributes, methods, inheritance, __repr__, encapsulation basics.
"""

def h(t): print("\n---", t, "---\n")

h("Basic class and instance")
class Person:
    """Simple person class."""
    species = "Homo sapiens"   # class attribute

    def __init__(self, name, age):
        self.name = name       # instance attribute
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, age {self.age}"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

p = Person("Khushal", 25)
print(p.introduce())
print("repr:", repr(p))
print("species:", Person.species)

h("Encapsulation and 'private' attributes")
class Counter:
    def __init__(self):
        self._value = 0   # single underscore: internal by convention
    def inc(self):
        self._value += 1
    def value(self):
        return self._value

c = Counter()
c.inc(); c.inc()
print("Counter value:", c.value())

h("Inheritance")
class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self.sid = sid
    def introduce(self):
        base = super().introduce()
        return f"{base} (student id: {self.sid})"

s = Student("Aisha", 20, "S123")
print(s.introduce())

h("Polymorphism example")
objs = [p, s]
for o in objs:
    print(o.introduce())

h("Mini Exercises")
# 1) Implement a BankAccount class with deposit, withdraw (prevent negative balance), and __repr__.
# 2) Implement classmethod/staticmethod examples and explain use-cases.

