## What is an If-Else Statement?

- Used to **make decisions** in your program.
- Runs different blocks of code depending on whether a condition is `True` or `False`.

---

## Basic If Statement

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

**Expected Output**
```text
x is greater than 5
```

**How It Works:**  
- `if` checks the condition `x > 5`.
- If `True`, runs the indented block.

---

## Adding Else

```python
num = 3

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

**Expected Output**
```text
Odd number
```

**How It Works:**  
- If the `if` condition is `False`, the `else` block runs.

---

## Using Elif (Else If)

Checks multiple conditions in order.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade D")
```

**Expected Output**
```text
Grade B
```

---

## Nested If

You can put one `if` inside another.

```python
age = 20

if age >= 18:
    print("Adult")
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Not Senior Citizen")
else:
    print("Minor")
```

**Expected Output**
```text
Adult
Not Senior Citizen
```

---

## Using Logical Operators

Combine conditions.

```python
x = 15

if x > 10 and x < 20:
    print("x is between 10 and 20")
```

**Expected Output**
```text
x is between 10 and 20
```

---

## Key Points

- Indentation is **mandatory** for if-else.
- `elif` checks another condition if previous ones are `False`.
- `else` catches everything else.

---

## Reflective Questions

- What happens if you forget to indent an if block?
- When do you need `elif` instead of multiple `if`?
- How can logical operators make conditions clearer?

---

## Practice Task

1️⃣ Write an `if-else` that checks if a number is positive, negative, or zero.  
2️⃣ Use `elif` to check ranges for marks (like grades).  
3️⃣ Try a nested `if` to check if a person is an adult and whether they are a senior citizen.

