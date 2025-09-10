"""
06_virtualenv_pip.py
====================
Intro to virtual environments and pip usage.
"""

print("\n=== VIRTUAL ENVIRONMENTS ===")
print("To create a venv:")
print("    python -m venv myenv")
print("To activate:")
print("    myenv\\Scripts\\activate   (Windows)")
print("    source myenv/bin/activate (Linux/Mac)")

print("\n=== USING PIP ===")
print("To install a package:")
print("    pip install requests")
print("To list installed packages:")
print("    pip list")

# Example (needs 'requests' installed):
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

