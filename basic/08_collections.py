"""
08_collections.py
Purpose: deep dive into list, tuple, set, dict — operations, methods, performance notes.
"""

def h(t): print("\n***", t, "***\n")

h("Lists")
lst = [3,1,4,1,5]
print("list:", lst)
lst.append(9)
lst.insert(1, 2)
print("after append/insert:", lst)
lst.remove(1)   # removes first occurrence
print("after remove(1):", lst)
print("pop:", lst.pop(), "now", lst)
print("slicing lst[1:4]:", lst[1:4])
lst.sort()
print("sorted:", lst)

h("Tuples")
t = (1,2,3)
print("tuple:", t)
# tuples are immutable; to modify convert to list then back

h("Sets")
s1 = {1,2,3}
s2 = {3,4}
print("union:", s1 | s2, "intersection:", s1 & s2, "difference:", s1 - s2)
# sets are unordered and unique

h("Dictionaries")
d = {"name":"K", "age":25}
print("keys:", list(d.keys()), "values:", list(d.values()))
d["city"] = "Delhi"
print("after add:", d)
# iterating dict
for k, v in d.items():
    print(k, "->", v)

h("Comprehensions")
squares = [x*x for x in range(6)]
evens = {x for x in range(10) if x % 2 == 0}
name_map = {i: chr(65+i) for i in range(5)}
print("squares:", squares)
print("evens set:", evens)
print("dict comp:", name_map)

h("Performance notes")
# - list append/pop from end: O(1); insert/pop at 0: O(n)
# - dict/set average lookup O(1)

h("Mini Exercises")
# 1) Given list of numbers, produce a new list of squares but only for even numbers using comprehension.
# 2) Merge two dictionaries preferring non-null values (practice dict methods).

