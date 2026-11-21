# Ask the user to enter three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Check if the first number is greater than both other numbers
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")

# Check if the second number is greater than both other numbers
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")

# If neither of the above conditions is true, the third number is largest
else:
    print(f"{num3} is the largest number.")