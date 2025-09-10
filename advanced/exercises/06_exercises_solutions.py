"""
Solutions for 06_exercises.md – Virtualenv & pip
Note: Some steps (like creating and activating a virtual environment) must be done in the terminal, 
not inside this script. This file only shows the Python code parts.
"""

# Q2. Install a Package and Test Requests
import requests

def test_requests():
    url = "https://example.com"
    response = requests.get(url)
    print("Status code:", response.status_code)
    print("First 200 characters of HTML:")
    print(response.text[:200])

if __name__ == "__main__":
    test_requests()


# Stretch Task – Weather Fetcher
# (Requires an API key from https://openweathermap.org/api)
# Example endpoint: http://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY&units=metric

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
    else:
        print("Failed to fetch weather data")

# Example usage:
# get_weather("Delhi", "YOUR_API_KEY")

