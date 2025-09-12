import math

def area_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length * width

def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    return math.pi * radius ** 2

def area_square():
    side = float(input("Enter the side of the square: "))
    return side ** 2

def area_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return 0.5 * base * height

def area_parallelogram():
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    return base * height

def area_trapezium():
    base1 = float(input("Enter the first base of the trapezium: "))
    base2 = float(input("Enter the second base of the trapezium: "))
    height = float(input("Enter the height of the trapezium: "))
    return 0.5 * (base1 + base2) * height


def main():
    shapes = {
        "1": ("Rectangle", area_rectangle),
        "2": ("Circle", area_circle),
        "3": ("Square", area_square),
        "4": ("Triangle", area_triangle),
        "5": ("Parallelogram", area_parallelogram),
        "6": ("Trapezium", area_trapezium)
    }

    while True:
        print("\nChoose a shape to calculate area:")
        for key, (name, _) in shapes.items():
            print(f"{key}. {name}")
        print("Q. Quit")

        choice = input("Enter your choice: ").strip()

        if choice.upper() == "Q":
            print("Exiting program. Goodbye!")
            break

        if choice in shapes:
            shape_name, func = shapes[choice]
            try:
                area = func()
                print(f"The area of the {shape_name.lower()} is {area:.2f}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

