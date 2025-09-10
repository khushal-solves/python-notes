# Exercises – Virtualenv & pip

## 1. Concept Questions
1. What is the purpose of a **virtual environment** in Python?  
2. What problem does `pip` solve in Python development?  
3. How do you create and activate a virtual environment?  
   - On Linux/Mac  
   - On Windows  
4. What file is commonly used to list dependencies for a project?  
5. What is the difference between `pip install` and `pip freeze`?  

---

## 2. Practical Tasks (Do on your system)

### Q1. Create a Virtual Environment
- Create a virtual environment named `venv`.  
- Activate it and confirm Python is running inside it.  

---

### Q2. Install a Package
- Inside your virtual environment, install the package `requests`.  
- Write a Python script `test_requests.py` that fetches and prints HTML from `"https://example.com"`.  

---

### Q3. Export Dependencies
- Use `pip freeze > requirements.txt` to save all installed dependencies.  
- Open the file and check that `requests` is listed.  

---

### Q4. Reproduce Environment
- Delete your environment folder.  
- Create a fresh virtual environment.  
- Install dependencies again using `pip install -r requirements.txt`.  

---

## 3. Stretch Task – Mini Project

### Task 1 – Weather Fetcher
- Create a virtual environment `weather_env`.  
- Install the `requests` package.  
- Write a script `weather.py` that fetches current weather data (from a free API like OpenWeatherMap) for your city and prints temperature and description.  
- Save dependencies to `requirements.txt`.  

