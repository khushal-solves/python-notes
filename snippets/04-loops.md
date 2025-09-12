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

