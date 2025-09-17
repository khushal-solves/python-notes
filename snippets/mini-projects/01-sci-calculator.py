import math

def single_input_operation(op, num):
    """Handles operations that require one number."""
    if op == "square":
        return num ** 2
    elif op == "cube":
        return num ** 3
    elif op == "sqrt":
        return math.sqrt(num)
    elif op == "log":  # natural log
        if num > 0:
            return math.log(num)
        else:
            return "Error: Log undefined for non-positive numbers"
    elif op == "exp":
        return math.exp(num)
    elif op == "abs":
        return abs(num)
    elif op == "factorial":
        if num >= 0 and num.is_integer():
            return math.factorial(int(num))
        else:
            return "Error: Factorial only defined for non-negative integers"
    elif op == "sin":
        return math.sin(math.radians(num))
    elif op == "cos":
        return math.cos(math.radians(num))
    elif op == "tan":
        return math.tan(math.radians(num))
    elif op == "deg":
        return math.degrees(num)  # radians → degrees
    elif op == "rad":
        return math.radians(num)  # degrees → radians
    else:
        return "Invalid single-input operator"


def double_input_operation(op, num1, num2):
    """Handles operations that require two numbers."""
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif op == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: Modulus by zero"
    elif op == "pow":
        return math.pow(num1, num2)
    elif op == "log_base":  # log with custom base
        if num1 > 0 and num1 != 1 and num2 > 0:
            return math.log(num2, num1)
        else:
            return "Error: Invalid base or argument for log"
    elif op == "gcd":
        return math.gcd(int(num1), int(num2))
    elif op == "lcm":
        return math.lcm(int(num1), int(num2))
    elif op == "hypot":
        return math.hypot(num1, num2)
    elif op == "max":
        return max(num1, num2)
    elif op == "min":
        return min(num1, num2)
    else:
        return "Invalid double-input operator"


def calculator():
    print("\n=== Scientific Calculator ===")
    print("Single-input operations: square, cube, sqrt, log, exp, abs, factorial, sin, cos, tan, deg, rad, exit")
    print("Two-input operations: +, -, *, /, %, pow, log_base, gcd, lcm, hypot, max, min")

    op = input("Enter operation: ").strip()
    
    if op == "exit":
        return None     # Type 'exit' to quit

    if op in ("square", "cube", "sqrt", "log", "exp", "abs", "factorial", "sin", "cos", "tan", "deg", "rad"):
        num = float(input("Enter the number: "))
        result = single_input_operation(op, num)
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = double_input_operation(op, num1, num2)

    return f"Result: {result}"

while True:
    output = calculator()
    if output is None:
        print("Exiting calculator. Goodbye!")
        break
    print(output)

