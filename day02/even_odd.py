# Ask the user to enter a number and convert it into an integer
num = int(input("Enter the number: "))

# Check whether the number is divisible by 2 with no remainder
if num % 2 == 0:
    # If the remainder is 0, the number is even
    print("The entered number is Even.")

else:
    # If the remainder is not 0, the number is odd
    print("The entered number is Odd.")