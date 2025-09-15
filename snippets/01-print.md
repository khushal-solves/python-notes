`print()` isn’t just about “showing text.” It can control formatting, file output, buffering, and more.

### 1. **Basic usage**

```python
print("Hello, World!")
```

Prints text or values to the console.

---

### 2. **Printing multiple items**

```python
print("Name:", "Khushal", "Age:", 28)
```

* By default, items are separated by a space (`sep=" "`).

---

### 3. **Custom separators**

```python
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry
```

You can control what goes between arguments.

---

### 4. **Custom end character**

```python
print("Hello", end=" ")
print("World")
# Output: Hello World
```

* Default `end="\n"` (new line).
* You can change it to space, tab, or nothing.

---

### 5. **Printing variables**

```python
x = 10
print("Value of x:", x)
```

---

### 6. **Formatted printing (f-strings)**

```python
name = "Khushal"
age = 28
print(f"My name is {name} and I am {age} years old.")
```

Recommended for readability and modern style.

---

### 7. **Using `.format()` method**

```python
print("My name is {} and I am {} years old.".format("Khushal", 28))
```

---

### 8. **Old-style formatting**

```python
print("My name is %s and I am %d years old." % ("Khushal", 28))
```

(Less common today, but still used in legacy code.)

| Specifier | Type / Description                                    | Example                        |
| --------- | ----------------------------------------------------- | ------------------------------ |
| `%d`      | Signed integer (decimal)                              | `"%d" % 42` → `42`             |
| `%i`      | Signed integer (decimal)                              | `"%i" % 42` → `42`             |
| `%u`      | Unsigned decimal integer                              | `"%u" % 42` → `42`             |
| `%o`      | Octal integer                                         | `"%o" % 10` → `12`             |
| `%x`      | Hexadecimal (lowercase)                               | `"%x" % 255` → `ff`            |
| `%X`      | Hexadecimal (uppercase)                               | `"%X" % 255` → `FF`            |
| `%f`      | Floating-point decimal format                         | `"%f" % 3.14` → `3.140000`     |
| `%F`      | Floating-point decimal format (same as `%f`)          | `"%F" % 3.14` → `3.140000`     |
| `%e`      | Scientific notation (lowercase `e`)                   | `"%e" % 3.14` → `3.140000e+00` |
| `%E`      | Scientific notation (uppercase `E`)                   | `"%E" % 3.14` → `3.140000E+00` |
| `%g`      | Uses `%f` or `%e` whichever is shorter                | `"%g" % 3.14` → `3.14`         |
| `%G`      | Uses `%F` or `%E` whichever is shorter                | `"%G" % 3.14` → `3.14`         |
| `%c`      | Single character (from integer or string of length 1) | `"%c" % 65` → `A`              |
| `%r`      | `repr()` of the object                                | `"%r" % "hi"` → `'hi'`         |
| `%s`      | `str()` of the object                                 | `"%s" % "hi"` → `hi`           |
| `%%`      | Literal percent sign                                  | `"%%" % ()` → `%`              |

### Note

- format-specifiers can be used with [f-strings](#6-formatted-printing-fstrings) and [.format() method](#7-using-format-method) as well.
- **Width and precision** can be added:

```python
"%5d" % 42        # Minimum width 5 → '   42'
"%.2f" % 3.14159  # 2 decimal places → '3.14'
"%8.2f" % 3.14159 # Width 8, 2 decimals → '    3.14'
```

```python
x = 42
y = 3.14159
print(f"Int: {x:5d}, Float: {y:8.2f}")
# Output: Int:    42, Float:     3.14

pi = 3.14159
print("Pi: {:.2f}".format(pi))
# Output: Pi: 3.14

pi = 3.14159
print("Pi: %.2f" % pi)
# Output: Pi: 3.14
```

---

### 9. **Printing to a file**

```python
with open("output.txt", "w") as f:
    print("This will be written to a file.", file=f)
```

---

### 10. **Flushing output immediately**

```python
import time
for i in range(3):
    print(i, end=" ", flush=True)
    time.sleep(1)
```

Normally output may be buffered. `flush=True` forces immediate display.
[More details on Loops](06-loops.md)

---

### 11. **Multiline printing**

```python
print("""This is
a multiline
string""")
```

---

### 12. **Printing with escape characters**

```python
print("Hello\tWorld")   # tab
print("Hello\nWorld")   # new line
```

