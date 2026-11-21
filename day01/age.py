# Import the date class from the datetime module
from datetime import date

# Ask the user to enter their birth year
birth_year = input("Enter your birth year: ")

# Get the current year from today's date
current_year = date.today().year

# Convert the birth year to an integer and calculate the age
age = int(current_year) - int(birth_year)

# Display the calculated age using an f-string
print(f"Your current age is {age}")