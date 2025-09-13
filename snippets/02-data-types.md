When we talk about **data types in Python**, we’re really asking: *“What kind of value am I working with, and what can I do with it?”*

---

## Main Categories of Python Data Types

### 1. **Numbers**

Python has several numeric types:

* **`int`** → whole numbers

  ```python
  a = 10
  ```
* **`float`** → decimal / real numbers

  ```python
  b = 3.14
  ```
* **`complex`** → numbers with real + imaginary part

  ```python
  c = 2 + 3j
  ```

---

### 2. **Boolean** (`bool`)

* Represents truth values: `True` or `False`
* Often comes from comparisons

  ```python
  x = 5 > 3   # True
  y = (10 == 2)  # False
  ```

---

### 3. **Text** (`str`)

* A sequence of characters

  ```python
  name = "Khushal"
  message = 'Hello'
  ```
* Strings support operations like concatenation, slicing, searching.

---

### 4. **Sequences**

These store ordered collections:

* **List (`list`)** → Mutable (can change)

  ```python
  numbers = [1, 2, 3]
  numbers.append(4)  # [1, 2, 3, 4]
  ```

* **Tuple (`tuple`)** → Immutable (cannot change)

  ```python
  point = (10, 20)
  ```

* **Range (`range`)** → Represents a sequence of numbers

  ```python
  r = range(1, 5)  # 1, 2, 3, 4
  ```

---

### 5. **Sets**

Unordered collections with unique elements.

* **Set (`set`)**

  ```python
  fruits = {"apple", "banana", "apple"}  # {"apple", "banana"}
  ```

* **Frozen Set (`frozenset`)** → Immutable version of set

  ```python
  frozen = frozenset([1, 2, 3])
  ```

---

### 6. **Mapping**

* **Dictionary (`dict`)** → Stores data as key–value pairs

  ```python
  person = {"name": "Khushal", "age": 28}
  print(person["name"])  # Khushal
  ```

---

### 7. **Binary Types** (for working with raw data)

* **`bytes`** → Immutable sequence of bytes
* **`bytearray`** → Mutable sequence of bytes
* **`memoryview`** → View of memory from other binary objects

Example:

```python
data = b"hello"   # bytes
arr = bytearray([65, 66, 67])
```

[More Details](03-binary-types.md)

---

## Special Type: `NoneType`

* **`None`** represents the absence of a value.

```python
result = None
```

---

## Why Data Types Matter

* They decide what **operations** you can perform.
* Example: you can add integers, but not an integer and a string.
* Python is *dynamically typed* → you don’t declare types, but Python assigns them automatically.

```python
x = 10        # int
x = "hello"   # str (type changed automatically)
```
