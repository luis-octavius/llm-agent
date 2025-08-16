# main.py

import sys
from pkg.calculator import Calculator


def main():
    calculator = Calculator()
    expression = "3 + 7 * 2"
    try:
        result = calculator.evaluate(expression)
        print(result) # Print the result to the console
        with open("output.txt", "w") as f:
            f.write(str(result))
    except Exception as e:
        print(f"Error: {e}") # Print the error to the console
        with open("output.txt", "w") as f:
            f.write(f"Error: {e}")


if __name__ == "__main__":
    main()
