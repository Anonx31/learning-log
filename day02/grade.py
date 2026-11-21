# Ask the user to enter their obtained marks
marks = int(input("Please enter the obtained marks: "))

# Check whether the entered marks are outside the valid range
if marks < 0 or marks > 100:
    print("Invalid marks. Please enter marks between 0 and 100.")

# Check if the marks are 90 or above
elif marks >= 90:
    print("Grade A")

# Check if the marks are 75 or above
elif marks >= 75:
    print("Grade B")

# Check if the marks are 60 or above
elif marks >= 60:
    print("Grade C")

# If none of the above conditions are satisfied, the student fails
else:
    print("Fail")