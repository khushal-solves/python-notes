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

* Recommended for readability and modern style.

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

