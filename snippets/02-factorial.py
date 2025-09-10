import math
from functools import reduce
import operator


def for_loop_factorial(n):
    """Calculate factorial using a for-loop (multiple styles possible)."""

    # Style 1: Standard for-loop multiplying result
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

    # --- Alternatives (uncomment to test) ---
    # Style 2: Reverse range
    # result = 1
    # for i in range(n, 0, -1):
    #     result *= i
    # return result

    # Style 3: Using math.prod
    # return math.prod(range(1, n + 1))


def while_loop_factorial(n):
    """Calculate factorial using a while-loop (multiple styles possible)."""

    # Style 1: Incrementing counter
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

    # --- Alternatives (uncomment to test) ---
    # Style 2: Decrementing counter
    # result = 1
    # i = n
    # while i > 0:
    #     result *= i
    #     i -= 1
    # return result

    # Style 3: Infinite loop with break
    # result = 1
    # i = 1
    # while True:
    #     if i > n:
    #         break
    #     result *= i
    #     i += 1
    # return result


def recursive_factorial(n):
    """Calculate factorial using recursion (multiple styles possible)."""

    # Style 1: Standard recursive definition
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

    # --- Alternatives (uncomment to test) ---
    # Style 2: Tail recursion (not optimized in Python)
    # def helper(num, acc=1):
    #     if num == 0:
    #         return acc
    #     return helper(num - 1, acc * num)
    # return helper(n)

    # Style 3: Recursive with product of sub-results (inefficient)
    # if n <= 1:
    #     return 1
    # return recursive_factorial(n - 1) * n


# === Other distinct approaches (separate functions) ===

def reduce_factorial(n):
    """Factorial using functools.reduce and operator.mul"""
    if n == 0:
        return 1
    return reduce(operator.mul, range(1, n + 1))


def list_comprehension_factorial(n):
    """Factorial using list comprehension and math.prod"""
    return math.prod([i for i in range(1, n + 1)]) if n > 0 else 1


def builtin_factorial(n):
    """Factorial using Python's built-in math.factorial"""
    return math.factorial(n)


def main():
    print("Factorial Calculation Demonstration")
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return

    print(f"\nFactorial of {n}:")
    print(f"Using for-loop: {for_loop_factorial(n)}")
    print(f"Using while-loop: {while_loop_factorial(n)}")
    print(f"Using recursion: {recursive_factorial(n)}")
    print(f"Using reduce: {reduce_factorial(n)}")
    print(f"Using list comprehension: {list_comprehension_factorial(n)}")
    print(f"Using built-in math.factorial: {builtin_factorial(n)}")


if __name__ == "__main__":
    main()

