def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform calculations based on the selected operation
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    if num2 != 0:
        result = divide(num1, num2)
    else:
        result = "Cannot divide by zero."
else:
    result = "Invalid operation"

# Display the result
print(f"Result of {num1} {operation} {num2} = {result}")