# python-notes

A structured collection of Python lessons and exercises organized into **basic** and **advanced** levels.

This repository is ideal for:
- Self-learners who want a step-by-step guide  
- Students in classrooms or coding bootcamps  
- Instructors who want ready-to-use lessons and exercises  

Each topic is **self-contained** with example code, so you can run, modify, and experiment without worrying about dependencies.  
Exercises come with solutions, allowing you to check your understanding after trying them yourself.

---

## Learning Tips

1. **Start Small** – Focus on one lesson at a time.  
2. **Run & Modify Code** – Change values, loops, and functions to see what happens.  
3. **Attempt Exercises First** – Try solving problems before checking solutions.  
4. **Take Notes** – Writing down explanations helps reinforce concepts.  
5. **Revisit Topics** – Periodically go back to previous lessons; repetition strengthens understanding.  
6. **Experiment Beyond the Examples** – Try small variations, mini-projects, or integrate multiple lessons.  
7. **Use the Exercises Strategically** – Stretch challenges are meant to push your problem-solving skills.  

> Remember: Mastery comes from **active practice**, not just reading.

---

## Requirements

- Python 3.8+  
- Install packages (if needed) with:  
```bash
  pip install -r requirements.txt
```

---

## Basic - Overview

**01_printing_and_comments.py**
- Printing text, numbers, multiple items
- Escape characters (`\n`, `\t`)
- End and separator options in `print()`
- Single-line vs multi-line comments
- Docstrings

**02_variables_and_types.py**
- Variable naming rules
- Dynamic typing in Python
- Common data types: int, float, str, bool, None
- Type checking (`type()`)
- Type casting (`int()`, `float()`, `str()`)

**03_operators.py**
- Arithmetic, comparison, logical
- Assignment operators (`+=`, `-=`, etc.)
- Membership operators (`in`, `not in`)
- Identity operators (`is`, `is not`)

**04_input_output.py**
- `input()` basics
- Converting input types
- f-strings, `.format()`, `%` formatting

**05_conditionals.py**
- if, elif, else
- Nested if statements
- Short-hand if
- Common pitfalls (indentation, truthy/falsy values)

**06_loops.py**
- `for` loop with `range()`
- Looping through strings, lists, dicts
- `while` loop basics
- `break`, `continue`, `pass`
- Nested loops

**07_functions.py**
- Defining and calling functions
- Parameters vs arguments
- Default arguments
- Return values
- Scope (local vs global)
- Lambda functions

**08_collections.py**
- Lists: indexing, slicing, methods
- Tuples: immutability
- Sets: uniqueness, operations (union, intersection)
- Dictionaries: keys, values, methods

**09_strings_in_depth.py**
- Indexing, slicing, stepping
- String methods (`find`, `replace`, `split`, `join`)
- Escape sequences and raw strings
- f-strings advanced formatting

**10_file_handling.py**
- Reading (`read`, `readline`, `readlines`)
- Writing (`write`, `writelines`)
- File modes (`r`, `w`, `a`, `x`)
- Context manager (`with open(...)`)

**11_exceptions.py**
- Try/except basics
- Catching specific exceptions
- `finally` and `else` blocks
- Raising exceptions manually

**12_classes_objects.py**
- Defining classes
- Attributes and methods
- `__init__` constructor
- `self` keyword explained
- Simple inheritance

1. [Printing & Comments](basic/01_printing_and_comments.py)  
2. [Variables & Types](basic/02_variables_and_types.py)  
3. [Operators](basic/03_operators.py)  
4. [Input & Output](basic/04_input_output.py)  
5. [Conditionals](basic/05_conditionals.py)  
6. [Loops](basic/06_loops.py)  
7. [Functions](basic/07_functions.py)  
8. [Collections (lists, tuples, sets, dicts)](basic/08_collections.py)  
9. [Strings in Depth](basic/09_strings_in_depth.py)  
10. [File Handling](basic/10_file_handling.py)  
11. [Exceptions](basic/11_exceptions.py)  
12. [Classes & Objects](basic/12_classes_objects.py)  

Or see everything in one file: [solutions_basic.py](basic/solutions_basic.py)

---

## Advanced - Overview

**01\_comprehensions.py** → list, dict, set comprehensions, generator expressions
**02\_modules\_packages.py** → importing built-ins, creating custom modules
**03\_standard\_libraries.py** → intro to `math`, `random`, `datetime`, `os`, `sys`
**04\_oop\_advanced.py** → class vs instance variables, encapsulation, polymorphism, overriding
**05\_custom\_exceptions.py** → raising and handling custom exception classes
**06\_virtualenv\_pip.py** → creating virtual environments, installing with pip


1. [Comprehensions](advanced/01_comprehensions.py)  
2. [Modules & Packages](advanced/02_modules_packages.py)  
3. [Standard Libraries](advanced/03_standard_libraries.py)  
4. [OOP Advanced](advanced/04_oop_advanced.py)  
5. [Custom Exceptions](advanced/05_custom_exceptions.py)  
6. [Virtualenv & pip](advanced/06_virtualenv_pip.py)  

Or see everything in one file: [solutions_advanced.py](advanced/solutions_advanced.py)

---

## Exercises

Each exercise has **theory questions, coding tasks, and stretch challenges**.  
Solutions are provided in matching `_solutions.py` files.

- [01_exercises.md](advanced/exercises/01_exercises.md) → [solutions](advanced/exercises/01_exercises_solutions.py)  
- [02_exercises.md](advanced/exercises/02_exercises.md) → [solutions](advanced/exercises/02_exercises_solutions.py)  
- [03_exercises.md](advanced/exercises/03_exercises.md) → [solutions](advanced/exercises/03_exercises_solutions.py)  
- [04_exercises.md](advanced/exercises/04_exercises.md) → [solutions](advanced/exercises/04_exercises_solutions.py)  
- [05_exercises.md](advanced/exercises/05_exercises.md) → [solutions](advanced/exercises/05_exercises_solutions.py)  
- [06_exercises.md](advanced/exercises/06_exercises.md) → [solutions](advanced/exercises/06_exercises_solutions.py)  

---

## How to Contribute

We welcome contributions from learners, instructors, and developers!  

Here’s how you can help:

1. **Suggest New Lessons or Topics**  
   - Open an issue describing the topic or concept you think should be added.  
   - Include a brief explanation and any relevant resources.

2. **Improve Existing Lessons**  
   - Fix typos, improve explanations, or add better examples.  
   - Make a pull request (PR) with your improvements.

3. **Add Exercises or Projects**  
   - Create practical exercises related to any lesson.  
   - Include a solution file and make sure it runs correctly.  
   - Follow the existing naming conventions: `NN_exercises.md` and `NN_exercises_solutions.py`.

4. **Report Bugs or Errors**  
   - If a code snippet doesn’t run or behaves unexpectedly, open an issue.  
   - Provide the error message and the Python version you used.

5. **Code Style and Standards**  
   - Use clear, readable code with proper comments.  
   - Follow PEP 8 where applicable.  

6. **Fork & Pull Request Workflow**  
   - Fork the repository  
   - Make your changes in a new branch  
   - Submit a PR with a descriptive title and summary  
   - For more details: Check [first-contributions](https://github.com/firstcontributions/first-contributions)

> Your contributions help make this repo better for everyone learning Python!
> If you like this repository **motivate us by putting a star to this repository** ...

---
