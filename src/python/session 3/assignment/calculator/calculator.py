from operations import *

def get_number(message):
    """
    Get a valid number from the user.
    param message: The message displayed to the user.
    type message: str
    raise ValueError: If the input is not a valid number.
    return: A valid floating-point number.
    rtype: float
    """
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    """
    Run the calculator program.
    Displays a menu, performs the selected operation,
    and allows the user to repeat calculations until
    they choose to exit.
    return: None
    rtype: None
    """
    while True:
        print("\n===== Basic Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("Type 'exit' to quit.")
        choice = input("Choose an operation (1-4) or type 'exit': ").lower()
        if choice == "exit":
            print("Thank you for using the calculator!")
            break
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please try again.")
            continue
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == "1":
                result = add(num1, num2)
                print(f"The result of adding {num1} and {num2} is {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"The result of subtracting {num2} from {num1} is {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"The result of multiplying {num1} and {num2} is {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"The result of dividing {num1} by {num2} is {result}")
        except ZeroDivisionError as error:
            print(error)
        again = input("\nDo you want another calculation? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using the calculator!")
            break