"""
09_strings_in_depth.py
Purpose: indexing, slicing, methods, formatting, raw strings, encoding basics.
"""

def h(t): print("\n---", t, "---\n")

h("Indexing & slicing")
s = "Hello, Python!"
print("s[0]:", s[0], "s[-1]:", s[-1])
print("s[0:5]:", s[0:5])   # H e l l o
print("s[7:]:", s[7:])
print("s[:5] + s[7:]:", s[:5] + s[7:])

h("Common string methods")
print("lower:", s.lower())
print("upper:", s.upper())
print("strip:", "  spaced  ".strip())
print("split:", "a,b,c".split(","))
print("join:", "-".join(["a","b","c"]))
print("find:", s.find("Python"), "replace:", s.replace("Python", "World"))

h("Advanced formatting (f-strings)")
name = "Khushal"
value = 1234.5678
print(f"{name} has {value:,.2f} rupees")  # comma thousand separator, 2 decimals

h("Raw strings & escaping")
path = r"C:\Users\Name\folder"
print("raw path:", path)

h("Encoding basics")
b = s.encode("utf-8")   # bytes
print("bytes:", b)
print("decoded:", b.decode("utf-8"))

h("Mini Exercises")
# 1) Given a sentence, print the words in reverse order.
# 2) Check if a string is a palindrome (ignore case and non-alphanumeric chars).

