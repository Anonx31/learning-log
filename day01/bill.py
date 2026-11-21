# Ask the user to enter the total bill amount
bill_amt = int(input("Enter the bill amount: "))

# Ask the user to enter the tip percentage
tip = float(input("Enter the tip percent you are willing to tip: "))

# Calculate the tip amount based on the bill amount
tip_amt = (tip / 100) * bill_amt

# Add the tip amount to the original bill to get the final total
total = bill_amt + tip_amt

# Display the final bill amount using an f-string
print(f"The generated bill amount is {total:.2f}.")