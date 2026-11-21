# Ask the user to enter a number
num = int(input("Enter the number: "))

# Iterate from 1 to 10
for i in range(1, 11):

    # Calculate the multiplication result
    result = num * i

    # Print the multiplication table
    print(f"{num} x {i} = {result}")