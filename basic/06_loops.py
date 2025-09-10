"""
06_loops.py
Purpose: for/while loops, range(), enumerate, iterating different containers, break/continue/pass, nested loops.
"""

def header(t): print("\n~~~", t, "~~~\n")

header("for loop and range()")
for i in range(5):   # 0..4
    print(i, end=" ")
print()

header("range with start, stop, step")
for i in range(2, 10, 2):
    print(i, end=" ")
print()

header("Looping through containers")
s = "abc"
lst = ["x","y","z"]
for idx, val in enumerate(lst):
    print("index", idx, "value", val)

for ch in s:
    print(ch)

header("while loop and common pitfall (infinite loop)")
count = 0
while count < 3:
    print("count", count)
    count += 1

header("break and continue")
for i in range(6):
    if i == 3:
        continue  # skip 3
    if i == 5:
        break     # stop loop
    print("i:", i)

header("Nested loops")
for r in range(2):
    for c in range(3):
        print(f"r{r}c{c}", end=" ")
    print()

header("Mini Exercises")
# 1) Print multiplication table (1-5) using nested loops.
# 2) Given a list of numbers, print only primes (simple check).

