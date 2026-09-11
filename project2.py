def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b
# Main program
print("Simple Calculator")
print("Operations: +  -  *  /")
while True:
    # Take input
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    # operation
    if op == "+":
        print("Result:", add(num1, num2))
    elif op == "-":
        print("Result:", subtract(num1, num2))
    elif op == "*":
        print("Result:", multiply(num1, num2))
    elif op == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operator!")
    # Ask 
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        print("Calculator closed.")
        break 
