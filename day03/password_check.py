# Define a function to check whether a password meets the requirements
def password_check(pw):

    # Check whether the password contains at least 8 characters
    length_check = len(pw) >= 8

    # Check whether the password contains at least one digit
    digit_check = any(c.isdigit() for c in pw)

    # Check whether the password contains at least one uppercase letter
    uppercase_check = any(c.isupper() for c in pw)

    # Return True only if all three conditions are satisfied
    return length_check and digit_check and uppercase_check


# Ask the user to enter a password
password = input("Enter your password: ")

# Call the function and check whether the password is valid
if password_check(password):
    print("Password is valid: True")
else:
    print("Password is valid: False")