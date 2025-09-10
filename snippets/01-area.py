import math

print("Choose a shape to calculate area:")
print("1. Rectangle")
print("2. Circle")

choice = input("Enter 1 or 2: ")

if choice == "1":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area:.2f}")

elif choice == "2":
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is {area:.2f}")

else:
    print("Invalid choice. Please enter 1 or 2.")
