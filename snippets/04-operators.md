## What are Operators?

- **Operators** are special symbols or words that perform operations on variables and values.
- Python has different types of operators: Arithmetic, Assignment, Comparison, Logical, Membership, Identity, Bitwise.

---

## 1️⃣ Arithmetic Operators

Used for basic math.

| Operator | Example | Meaning |
|----------|---------|---------|
| `+` | `x + y` | Addition |
| `-` | `x - y` | Subtraction |
| `*` | `x * y` | Multiplication |
| `/` | `x / y` | Division (float) |
| `//` | `x // y` | Floor division |
| `%` | `x % y` | Modulus (remainder) |
| `**` | `x ** y` | Exponentiation |

Example:
```python
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

**Expected Output**
```text
7
3
10
2.5
2
1
25
```

---

## 2️⃣ Assignment Operators

Used to assign values.

| Operator | Example | Meaning |
|----------|---------|---------|
| `=` | `x = 5` | Assign value |
| `+=` | `x += 2` | x = x + 2 |
| `-=` | `x -= 1` | x = x - 1 |
| `*=` | `x *= 3` | x = x * 3 |
| `/=` | `x /= 2` | x = x / 2 |
| `%=` | `x %= 2` | x = x % 2 |
| `**=` | `x **= 2` | x = x ** 2 |

Example:
```python
x = 5
x += 3
print(x)  # 8
x *= 2
print(x)  # 16
```

**Expected Output**
```text
8
16
```

---

## 3️⃣ Comparison Operators

Compare values — result is `True` or `False`.

| Operator | Example |
|----------|---------|
| `==` | `x == y` |
| `!=` | `x != y` |
| `>` | `x > y` |
| `<` | `x < y` |
| `>=` | `x >= y` |
| `<=` | `x <= y` |

---

## 4️⃣ Logical Operators

Combine conditions.

| Operator | Example | Meaning |
|----------|---------|---------|
| `and` | `x > 5 and y < 10` | Both must be True |
| `or` | `x > 5 or y < 3` | One must be True |
| `not` | `not(x > 5)` | Reverse the result |

---

## 5️⃣ Membership Operators

Check if a value is in a sequence.

| Operator | Example |
|----------|---------|
| `in` | `'a' in 'apple'` |
| `not in` | `'x' not in 'apple'` |

Example:
```python
text = "Python"
print('y' in text)      # True
print('z' not in text)  # True
```

**Expected Output**
```text
True
True
```

---

## 6️⃣ Identity Operators

Check if two variables are the same object.

| Operator | Example |
|----------|---------|
| `is` | `x is y` |
| `is not` | `x is not y` |

Example:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)    # True (same object)
print(a is c)    # False (same content, different object)
```

**Expected Output**
```text
True
False
```

---

## Key Points

- Operators perform actions on data.
- Combine multiple operators to write powerful logic.
- Know the difference: `==` checks value, `is` checks identity.

---

## Reflective Questions

- What is the difference between `==` and `is`?
- When would you use `in`?
- Why use `+=` instead of `x = x + y`?

---

## Practice Task

1️⃣ Try arithmetic and assignment operators with any numbers.  
2️⃣ Test `in` and `is` with strings and lists.  
3️⃣ Combine logical and comparison operators in an `if` statement.
