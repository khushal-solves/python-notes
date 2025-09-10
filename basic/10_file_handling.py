"""
10_file_handling.py
Purpose: read/write files, modes, context managers, binary vs text, CSV basics.
"""

import os

def h(t): print("\n###", t, "###\n")

h("Write and read text file using context manager")
with open("sample_text.txt", "w", encoding="utf-8") as f:
    f.write("Line1\nLine2\nNumber: 123\n")
print("Wrote sample_text.txt")

with open("sample_text.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("Read content:\n", content)

h("Read line by line")
with open("sample_text.txt", "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        print(f"Line {idx} ->", line.strip())

h("Append mode and existence check")
with open("sample_text.txt", "a", encoding="utf-8") as f:
    f.write("Appended line\n")
print("Appended one line")

h("Binary files (example: writing bytes)")
data = b"\x00\x01\x02"
with open("sample_bin.bin", "wb") as bf:
    bf.write(data)
print("Wrote sample_bin.bin size:", os.path.getsize("sample_bin.bin"))

h("CSV simple handling (no csv module, basic)")
lines = ["name,score\n", "A,10\n", "B,20\n"]
with open("scores.csv", "w", encoding="utf-8") as csvf:
    csvf.writelines(lines)
print("Wrote scores.csv with basic rows")

h("Mini Exercises")
# 1) Read scores.csv, parse it, and print total score.
# 2) Write a program that logs user input lines into 'log.txt' until user types 'quit'.

