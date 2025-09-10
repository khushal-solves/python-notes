# python-notes

_Also available in [English](README.md)_

**basic** और **advanced** स्तरों में व्यवस्थित Python lessons और exercises का एक संरचित संग्रह।  

यह repository इन लोगों के लिए उपयुक्त है:  
- स्वयं सीखने वाले, जो step-by-step मार्गदर्शिका चाहते हैं  
- classrooms या coding bootcamps में पढ़ने वाले छात्र  
- instructors, जो तैयार lessons और exercises चाहते हैं  

प्रत्येक topic **self-contained** है, जिसमें example code शामिल है। आप इसे चला सकते हैं, बदल सकते हैं और बिना dependency की चिंता किए प्रयोग कर सकते हैं।  
Exercises के साथ solutions दिए गए हैं ताकि आप स्वयं प्रयास करने के बाद अपनी समझ की जाँच कर सकें।  

---

## सीखने के सुझाव  

1. **छोटे से शुरू करें** – एक समय में केवल एक lesson पर ध्यान दें।  
2. **code चलाएँ और बदलें** – values, loops और functions बदलकर देखें क्या होता है।  
3. **पहले exercises करें** – solution देखने से पहले स्वयं problem हल करने का प्रयास करें।  
4. **नोट्स बनाएँ** – व्याख्या लिखने से concepts और मजबूत होते हैं।  
5. **पुराने topics पर लौटें** – समय-समय पर दोहराएँ; repetition समझ को पक्का करता है।  
6. **examples से आगे प्रयोग करें** – छोटे बदलाव करें, mini-projects बनाएं या कई lessons को जोड़ें।  
7. **exercises का रणनीतिक उपयोग करें** – *stretch challenges* आपकी problem-solving क्षमता बढ़ाने के लिए हैं।  

> याद रखें: महारत **सक्रिय अभ्यास** से आती है, केवल पढ़ने से नहीं।  

---

## आवश्यकताएँ  

- Python 3.8+  
- packages install करें (यदि ज़रूरी हो) इस command से:  

```bash
pip install -r requirements.txt
````

---

## Basic - Overview

| File                                                                | विवरण                                                                                        |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [01\_printing\_and\_comments.py](basic/01_printing_and_comments.py) | text, numbers, multiple items, escape characters, `print()` options, comments और docstrings। |
| [02\_variables\_and\_types.py](basic/02_variables_and_types.py)     | variable naming, dynamic typing, common data types, type checking और type casting।           |
| [03\_operators.py](basic/03_operators.py)                           | arithmetic, comparison, logical, assignment, membership और identity operators।               |
| [04\_input\_output.py](basic/04_input_output.py)                    | input लेना, type conversion, f-strings, `.format()`, और `%` formatting।                      |
| [05\_conditionals.py](basic/05_conditionals.py)                     | `if/elif/else` statements, nested ifs, shorthand if, truthy/falsy values।                    |
| [06\_loops.py](basic/06_loops.py)                                   | `for` और `while` loops, break/continue/pass, nested loops।                                   |
| [07\_functions.py](basic/07_functions.py)                           | functions, arguments, return values, scope और lambda functions।                              |
| [08\_collections.py](basic/08_collections.py)                       | lists, tuples, sets, dictionaries और common operations।                                      |
| [09\_strings\_in\_depth.py](basic/09_strings_in_depth.py)           | indexing, slicing, string methods, escape sequences और f-string formatting।                  |
| [10\_file\_handling.py](basic/10_file_handling.py)                  | file reading/writing, file modes और context managers।                                        |
| [11\_exceptions.py](basic/11_exceptions.py)                         | try/except blocks, specific exceptions पकड़ना, raise करना और finally/else usage।             |
| [12\_classes\_objects.py](basic/12_classes_objects.py)              | classes, attributes, methods, constructors, `self`, और simple inheritance।                   |
| [solutions\_basic.py](basic/solutions_basic.py)                     | सभी basic topics से consolidated solutions और examples।                                      |

---

## Advanced - Overview

| File                                                            | विवरण                                                                               |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [01\_comprehensions.py](advanced/01_comprehensions.py)          | list, dict, set comprehensions और generator expressions।                            |
| [02\_modules\_packages.py](advanced/02_modules_packages.py)     | built-in modules import करना और custom modules/packages बनाना।                      |
| [03\_standard\_libraries.py](advanced/03_standard_libraries.py) | `math`, `random`, `datetime`, `os`, और `sys` का परिचय।                              |
| [04\_oop\_advanced.py](advanced/04_oop_advanced.py)             | advanced OOP: encapsulation, polymorphism, overriding, class vs instance variables। |
| [05\_custom\_exceptions.py](advanced/05_custom_exceptions.py)   | custom exception classes raise और handle करना।                                      |
| [06\_virtualenv\_pip.py](advanced/06_virtualenv_pip.py)         | virtual environments बनाना और pip से packages install करना।                         |
| [solutions\_advanced.py](advanced/solutions_advanced.py)        | सभी advanced topics से consolidated solutions और examples।                          |

---

## Exercises

प्रत्येक exercise में **theory questions, coding tasks, और stretch challenges** शामिल हैं।
Solutions संबंधित `_solutions.py` files में दिए गए हैं।

| Exercises                                              | Solutions                                                                   |
| ------------------------------------------------------ | --------------------------------------------------------------------------- |
| [01\_exercises.md](advanced/exercises/01_exercises.md) | [01\_exercises\_solutions.py](advanced/exercises/01_exercises_solutions.py) |
| [02\_exercises.md](advanced/exercises/02_exercises.md) | [02\_exercises\_solutions.py](advanced/exercises/02_exercises_solutions.py) |
| [03\_exercises.md](advanced/exercises/03_exercises.md) | [03\_exercises\_solutions.py](advanced/exercises/03_exercises_solutions.py) |
| [04\_exercises.md](advanced/exercises/04_exercises.md) | [04\_exercises\_solutions.py](advanced/exercises/04_exercises_solutions.py) |
| [05\_exercises.md](advanced/exercises/05_exercises.md) | [05\_exercises\_solutions.py](advanced/exercises/05_exercises_solutions.py) |
| [06\_exercises.md](advanced/exercises/06_exercises.md) | [06\_exercises\_solutions.py](advanced/exercises/06_exercises_solutions.py) |

---

## योगदान कैसे करें

हम learners, instructors और developers से contributions का स्वागत करते हैं!

1. **नए lessons या topics सुझाएँ**

   * उस topic या concept का विवरण लिखें जिसे जोड़ा जाना चाहिए।
   * एक संक्षिप्त explanation और relevant resources शामिल करें।

2. **मौजूदा lessons सुधारें**

   * typos सुधारें, explanations बेहतर करें या अच्छे examples जोड़ें।
   * अपने सुधारों के साथ एक pull request (PR) बनाएं।

3. **exercises या projects जोड़ें**

   * किसी भी lesson से संबंधित practical exercises तैयार करें।
   * solution file जोड़ें और सुनिश्चित करें कि यह सही से चले।
   * naming conventions का पालन करें: `NN_exercises.md` और `NN_exercises_solutions.py`।

4. **bugs या errors रिपोर्ट करें**

   * यदि कोई code snippet नहीं चलता या अप्रत्याशित व्यवहार करता है, तो एक issue खोलें।
   * error message और आपने जो Python version उपयोग किया वह बताएं।

5. **Code style और standards**

   * साफ, readable code लिखें और proper comments जोड़ें।
   * जहाँ लागू हो, PEP 8 का पालन करें।

6. **Fork और Pull Request workflow**

   * repository fork करें
   * अपने बदलाव नई branch में करें
   * descriptive title और summary के साथ PR सबमिट करें
   * और विवरण के लिए देखें: [first-contributions](https://github.com/firstcontributions/first-contributions)

> आपके contributions से यह repository हर सीखने वाले के लिए बेहतर बनती है!

यदि आपको यह repository पसंद आती है, तो **[इस repository को star देकर हमें प्रेरित करें](https://github.com/khushal-solves/python-notes/stargazers)**।

