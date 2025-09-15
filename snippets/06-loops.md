## Introduction / Theory: Loops in Python

Loops allow us to **repeat a block of code multiple times**, which is essential for automating repetitive tasks, processing collections, or performing calculations step by step. Python provides two primary loop constructs:

1. **`for` loops** – iterate over a sequence (list, string, range, etc.).
2. **`while` loops** – repeat until a condition becomes false.

Key points about loops:

* **Loop variable:** Tracks the current iteration or element.
* **Break, Pass and Continue:**

| Keyword    | Effect in Loop                     | When to Use                   |
| ---------- | ---------------------------------- | ----------------------------- |
| `break`    | Exit the loop immediately          | Stop when a condition is met  |
| `continue` | Skip current iteration, go to next | Ignore certain cases          |
| `pass`     | Do nothing (placeholder)           | Keep syntax valid / plan code |

* **Else in loops:** Executes if the loop finishes normally (no `break`).
* **Nested loops:** A loop inside another loop, useful for tables, grids, and pairwise combinations.

**Why practice loop patterns?**
Knowing the syntax is not enough. Most beginner problems are logic-based: counting, summing, searching, filtering, or simulating processes. Recognizing **the pattern** behind a problem makes solving it faster.

---

### Key Points

1. Recognize **patterns**: repetition, accumulation, searching, counting, filtering, max/min, nested, break/else, unknown loops, and simulation.
2. Understand **loop logic** before coding — knowing the pattern makes problem-solving faster.
3. Always think about **edge cases**: empty lists, no matching items, or unusual values.

---

## Common Loop Problem Types

### 1. **Simple Repetition**

* Do something a fixed number of times.

```python
for i in range(5):
    print("Hello")
```

Practice: print stars, repeat greetings, countdowns.

---

### 2. **Accumulation (Summing or Combining)**

* Collect results as you loop.

```python
numbers = [3, 5, 7]
total = 0
for n in numbers:
    total += n
print(total)  # 15
```

Practice: sum of numbers, product of numbers, string concatenation.

---

### 3. **Searching**

* Look for a particular item.

```python
names = ["Ali", "Beena", "Chetan"]
for name in names:
    if name == "Beena":
        print("Found")
        break
```

Practice: check if a value exists, find first occurrence.

---

### 4. **Counting (Frequency)**

* Count how many times something appears.

```python
word = "banana"
count = 0
for ch in word:
    if ch == "a":
        count += 1
print(count)  # 3
```

Practice: count vowels, count even numbers.

---

### 5. **Filtering**

* Select certain items from a collection.

```python
nums = [1, 2, 3, 4, 5]
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)  # [2, 4]
```

* Skip even numbers

```python
for i in range(1, 6):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)
```

Practice: extract positives, filter short words.

---

### 6. **Maximum / Minimum**

* Find the largest or smallest item.

```python
nums = [5, 8, 3]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print(largest)  # 8
```

Practice: highest score, longest word.

---

### 7. **Nested Loops (Combinations / Tables)**

* Loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Practice: multiplication tables, coordinate grids, pair comparisons.

---

### 8. **Loop with Early Exit (break / else)**

* Stop when a condition is met, otherwise do something at the end.

```python
nums = [3, 5, 7]
for n in nums:
    if n % 2 == 0:
        print("Found even number")
        break
else:
    print("No even number found")
```

Practice: prime number check, searching when the item might not exist.

---

### 9. **While Loop for Unknown Repetition**

* Use when you don’t know in advance how many times you’ll loop.

```python
n = 10
while n > 0:
    print(n)
    n -= 1
```

Practice: guessing games, read input until user says stop.

---

### 10. **Simulation / Stepwise Update**

* Change values gradually, track progress.

```python
position = 0
steps = 5
while steps > 0:
    position += 1
    steps -= 1
print("Final position:", position)
```

Practice: moving objects, draining energy, financial growth.

---

### 11. **Pass Keyword**

```python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        pass  # TODO: Implement later
    else:
        print(n)
```

Practice:
- Loop through a list of numbers. For negative numbers, just pass. For positive numbers, print them.
- Use pass as a placeholder while planning a filtering loop that you’ll implement later.

---

### 12. **Else** block with a loop

In Python, you can attach an `else` block to a `for` or `while` loop.

* The `else` part **runs only if the loop finishes normally**
* If the loop is exited early with `break`, the `else` block is skipped.

##### Example with `for ... else`

```python
for num in range(2, 6):
    if num % 2 == 0:
        print(num, "is even")
        break
else:
    print("No even number found")
```

* If the loop finds an even number, it breaks → the `else` won’t run.
* If no even number is found, the loop finishes naturally → `else` runs.

##### Example with `while ... else`

```python
count = 0
while count < 3:
    print("Count:", count)
    count += 1
else:
    print("Loop finished without break")
```

* Since there is no `break`, the `else` executes.

---

##### Why would you use an `else` block?

* Often used when **searching** for something:

  * `for` loop → tries to find an item.
  * If found → `break`.
  * If not found → `else` runs, saying “not found.”

Equivalent to having a “no-break clause.”

---

##### Example without `else`

You’d usually need an extra flag variable: (like `found`)

```python
found = False
for num in range(2, 6):
    if num % 2 == 0:
        print("Found even:", num)
        found = True
        break

if not found:
    print("No even number found")
```

The `else` in loops makes this cleaner and more Pythonic.

