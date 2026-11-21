# Ask the user to enter a number
num = int(input("Enter the number: "))

# Initialize the counter variable with 1
i = 1

# Initialize total to store the sum
total = 0

# Continue the loop as long as i is less than or equal to num
while i <= num:

    # Add the current value of i to total
    total += i

    # Increment i by 1 after each iteration
    i += 1

# Display the final sum
print(f"The sum of first {num} natural numbers is {total}.")