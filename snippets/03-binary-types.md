---

## Binary Types

Binary data types are used when you need to store or manipulate **raw data** (like images, audio files, network packets, or encoded text). They are not for human-readable strings, but for **bytes** (0–255 values).

Python has three built-in binary types:

---

### 1. **`bytes`** (Immutable)

* A fixed sequence of byte values (0–255).
* Similar to a string, but each element is a number (not a character).
* Cannot be changed after creation (read-only binary data).

```python
data = b"hello"     # a bytes object
print(data[0])      # 104  (ASCII code for 'h')
```

Use when you want read-only binary data, like loading a file.

---

### 2. **`bytearray`** (Mutable)

* Editable binary data.
* Like `bytes`, but you can change its contents.

```python
arr = bytearray([65, 66, 67])   # A, B, C
arr[0] = 68                     # Change first byte to 'D'
print(arr)                      # bytearray(b'DBC')
```

Use when you need to edit or build binary data.

---

### 3. **`memoryview`** (Shared view)

* Efficient way to access/modify binary data without copying.
* A window into another binary object (`bytes`, `bytearray`, etc.).
* Lets you access parts of data **without copying** it.

```python
data = bytearray(b"Python")
view = memoryview(data)
print(view[0])   # 80 (ASCII code for 'P')

view[0] = 74     # Change 'P' (80) to 'J' (74)
print(data)      # bytearray(b'Jython')
```

Useful for large data (like images) where copying would waste memory.

---

## Everyday Uses of Binary Types

* **File I/O** → reading/writing images, audio, or executables.
* **Networking** → sending/receiving packets.
* **Encoding/Decoding** → handling UTF-8 or other encodings.
* **Memory-efficient processing** → editing large datasets without duplicates.

---

## Strings (`str`) vs. Binary Types (`bytes`, `bytearray`)

| Feature              | **String (`str`)**                 | **Bytes (`bytes`)**                                         | **Bytearray (`bytearray`)**               |
| -------------------- | ---------------------------------- | ----------------------------------------------------------- | ----------------------------------------- |
| **Purpose**          | Human-readable text (characters)   | Raw data (numbers 0–255), often encoded text or files       | Raw data, but editable                    |
| **How it looks**     | `"hello"`                          | `b"hello"`                                                  | `bytearray(b"hello")`                     |
| **Elements are**     | Characters (`'h'`, `'e'`, etc.)    | Integers (ASCII/UTF-8 codes: 104, 101, etc.)                | Integers, but can be modified             |
| **Mutable?**         | ❌ No (immutable)                   | ❌ No (immutable)                                            | ✅ Yes (mutable)                           |
| **Use case**         | User-facing text, messages, labels | File I/O, networking, binary protocols                      | Modifiable binary data (buffers, editing) |
| **Encoding needed?** | Not needed (already text)          | Often converted to/from `str` via `.encode()` / `.decode()` | Same as `bytes`                           |

---

### Examples

**1. String (`str`)**

```python
s = "hello"
print(s[0])        # 'h' (a character)
```

**2. Bytes (`bytes`)**

```python
b = b"hello"
print(b[0])        # 104 (ASCII code of 'h')
```

**3. Bytearray (`bytearray`)**

```python
ba = bytearray(b"hello")
ba[0] = 72         # Change first byte to 'H'
print(ba)          # bytearray(b'Hello')
```

---

### Conversion

Always **encode/decode** when moving between text and binary.

* **String → Bytes** (encoding text to binary form)

```python
s = "hello"
b = s.encode("utf-8")
print(b)   # b'hello'
```

* **Bytes → String** (decoding binary form to readable text)

```python
b = b"hello"
s = b.decode("utf-8")
print(s)   # hello
```

---
