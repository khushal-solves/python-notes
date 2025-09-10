"""
Solutions for 01_exercises.md – Comprehensions
"""

# Q1. Squares of even numbers
squares_even = [n**2 for n in range(1, 21) if n % 2 == 0]
print("Squares of even numbers:", squares_even)


# Q2. Dict comprehension – word lengths
words = ["python", "comprehension", "exercise"]
lengths = {w: len(w) for w in words}
print("Word lengths:", lengths)


# Q3. Set comprehension – unique vowels
text = "comprehensions are powerful"
vowels = {ch for ch in text if ch in "aeiou"}
print("Unique vowels:", vowels)


# Q4. Generator expression – cubes
cubes = (n**3 for n in range(1, 11))
print("Cubes 1–10:", list(cubes))


# Stretch Task 1 – Prime numbers with comprehension
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primes = [n for n in range(1, 101) if is_prime(n)]
print("Primes 1–100:", primes)


# Stretch Task 2 – Nested comprehension (multiplication table)
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table (1–5):")
for row in table:
    print(row)

