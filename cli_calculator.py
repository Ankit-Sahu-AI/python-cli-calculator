"""
Title: Interactive CLI Python Calculator
Description: A simple command-line interface calculator that evaluates mathematical expressions dynamically with error handling.
"""

print("=" * 35)
print("\t🧮CALCULATOR🔢")
print("=" * 35)
print("Tip: type 'exit' for close the calculator\n")
while True:
    expression = input("Enter you expression: ")
    if expression.lower() == "exit":
        print("Bye!👋 Happy coding😇")
        break
    try:
        result = eval(expression)
        print(f"Your expression answer is: {result}")
        print("~" * 32)
    except ZeroDivisionError:
        print("Zero is not divisiable🚫\n")
    except Exception:
        print("Invalid Input! Try again.\n")
    