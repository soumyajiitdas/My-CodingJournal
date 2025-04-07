##Simple PYTHON Calculator:
def calculator():
    # Get the user's first number
    num1 = float(input("Enter a number: "))
    # Get the user's second number
    num2 = float(input("Enter another number: "))
    # Get the user's operator
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform the appropriate calculation and print the result
    if operator == "+":
        result = num1 + num2
        print(num1, "+", num2, "=", result)
    elif operator == "-":
        result = num1 - num2
        print(num1, "-", num2, "=", result)
    elif operator == "-" & num1 < num2:
        print(num1, "-", num2, "=", result)
    elif operator == "*":
        result = num1 * num2
        print(num1, "*", num2, "=", result)
    elif operator == "/":
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Invalid operator")

# Run the calculator function
calculator()