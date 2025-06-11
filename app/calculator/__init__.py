## Calculator Interface
## Evan Garvey
## IS 601, Module 3

from app.operations import add, subtract, multiply, divide


## This calculator is heavily based on the previous calculator that we made in module 2.
## However, this time, I have started completely from scratch and will only be referencing module 2 for the operations.
def calculator():

    print("Welcome to the Calculator Interface! Type 'quit' at any time to exit.")

    while True:

        user_input = input("Enter a desired operation (add, subtract, multiply, divide), and then two numbers separated by a space.")

        ## Check if an exit is desired

        if lower(user_input) == "quit":
            print("Goodbye!")
            break

        ## Check if operation is in valid form

        try:

            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)

        except ValueError:

            print("Invalid input. Please try again.")
            continue

        ## Once operation has been validated, parse and compute

        if operation == "add":
            result = addition(num1, num2)

        elif operation == "subtract":
            result = subtraction(num1, num2)

        elif operation == "multiply":
            result = multiplication(num1, num2)

        elif operation == "divide":
            try:
                result = division(num1, num2)
            except ZeroDivisionError:
                print("Cannot divide by zero. Please try again.")
                continue

        else:
            print("Invalid operation. Please try again.")
            continue

        print(f"Result: {result}")