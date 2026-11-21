# Ask the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask the user to select an arithmetic operation
op = input("Enter operation from (add, sub, mul, div): ")

# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def sub(num1, num2):
    return num1 - num2

# Function to perform multiplication
def mul(num1, num2):
    return num1 * num2

# Function to perform division
def div(num1, num2):
    return num1 / num2

# Check the selected operation and call the respective function
if op == "add":
    print(f"Result: {add(num1, num2)}")

elif op == "sub":
    print(f"Result: {sub(num1, num2)}")

elif op == "mul":
    print(f"Result: {mul(num1, num2)}")

elif op == "div":
    # Check whether the second number is zero
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result: {div(num1, num2)}")

# Handle invalid operations
else:
    print("Enter valid input.")