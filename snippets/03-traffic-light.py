import time
import sys

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"   # back to default

import time
import sys

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"   # back to default


def countdown(seconds, message, color):
    """Show countdown with colored message, plain dots, and live timer."""
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(
            f"\r{color}{message}{RESET} "
            + "." * (seconds - remaining)   # dots grow with time
            + f" {remaining:2d}s remaining"
        )
        sys.stdout.flush()
        time.sleep(1)
    print()  # move to next line at the end
    
    """Show countdown with colored message and plain dots on the same line."""
    # sys.stdout.write(color + message + RESET)
    # sys.stdout.flush()
    #
    # for _ in range(seconds):
    #     time.sleep(1)
    #     sys.stdout.write(".")   # dots in default color
    #     sys.stdout.flush()
    #
    # print()  # move to next line at the end


def traffic_light(start_light):
    """Simulate a traffic light system with colored prompts and live countdown."""
    lights = ["red", "green", "yellow"]

    start_light = start_light.lower()
    if start_light not in lights:
        print("Invalid light. Defaulting to red.")
        start_light = "red"

    index = lights.index(start_light)

    while True:
        current = lights[index]

        if current == "red":
            countdown(60, " RED light ON → STOP", RED)
        elif current == "green":
            countdown(60, "󰭮 GREEN light ON → GO", GREEN)
        elif current == "yellow":
            countdown(5, "󱤍 YELLOW light ON → WAIT", YELLOW)

        index = (index + 1) % len(lights)


def main():
    print("Traffic Light Simulation")
    start_light = input("Enter starting light (red/green/yellow): ")
    traffic_light(start_light)


if __name__ == "__main__":
    main()

