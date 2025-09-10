"""
01_comprehensions.py
====================
Examples of list, dict, set comprehensions, and generator expressions.
"""

print("\n=== LIST COMPREHENSIONS ===")
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print("Squares:", squares)

# With condition
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)


print("\n=== DICT COMPREHENSIONS ===")
words = ["apple", "banana", "cherry"]
lengths = {w: len(w) for w in words}
print("Word lengths:", lengths)


print("\n=== SET COMPREHENSIONS ===")
text = "hello world"
unique_letters = {ch for ch in text if ch.isalpha()}
print("Unique letters:", unique_letters)


print("\n=== GENERATOR EXPRESSIONS ===")
gen = (n**2 for n in range(5))
print("Generator object:", gen)
print("Values from generator:", list(gen))

