# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = (input("Choose an Operation (+, -, *, /): "))

# Match-case for operation handling
match operator:
    case "+":
        result = num1 + num2
        print(f"Result: {result}")
    case "-":
        result = num1 - num2
        print(f"Result: {result}")
    case "*":
        result = num1 * num2
        print(f"Result: {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {result}")
        else: 
            print("Error: Cannot be divided by zero")
    case _:
        print("Invalid operator selected")