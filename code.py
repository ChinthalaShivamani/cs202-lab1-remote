"""
This module contains utility functions for mathematical operations.
"""
def calculator():
    """
    Function to perform mathematical operations using user input.

    Args:
        No arguments are required for this function.

    Returns:
        type: returns the calculated result
    """
    print("Select the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter choice (+, -, *, /): ")

        if choice in ['+', '-', '*','/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '+':
                    print(f"The result is: {num1 + num2}")
                elif choice == '-':
                    print(f"The result is: {num1 - num2}")
                elif choice == '*':
                    print(f"The result is: {num1 * num2}")
                elif choice == '/':
                    if num2 != 0:
                        print(f"The result is: {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")

            except ValueError:
                print("Invalid input. Please enter numerical values.")
        else:
            print("Invalid choice. Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the calculator!")
            break

calculator()
