# Exercises – Custom Exceptions

## 1. Concept Questions
1. What is the difference between a **built-in exception** and a **custom exception**?  
2. Why would you create your own exception class instead of just using built-ins like `ValueError`?  
3. How do you define a custom exception in Python?  
4. What does the `raise` keyword do in exception handling?  

---

## 2. Coding Exercises

### Q1. Basic Custom Exception
Create a custom exception `NegativeNumberError`.  
Write a function `square_root(n)` that raises this exception if `n` is negative.

---

### Q2. Divide by Zero Handling
Write a function `safe_divide(a, b)` that:  
- Raises a custom exception `ZeroDivisionCustomError` if `b` is zero.  
- Otherwise, returns the division result.  

---

### Q3. Age Validation
Create a class `AgeTooLowError`.  
Write a function `check_age(age)` that raises this exception if the age is less than 18, otherwise prints `"Access granted"`.

---

## 3. Stretch Tasks

### Task 1 – Password Validator
Create a function `validate_password(password)` that:  
- Raises `ShortPasswordError` if the length < 6  
- Raises `NoNumberError` if it doesn’t contain any digit  
- Prints `"Password is valid"` otherwise.  

---

### Task 2 – Banking Exception
Create a class `InsufficientFundsError`.  
Write a `withdraw(balance, amount)` function that raises this exception if `amount > balance`. Otherwise, return the new balance.

