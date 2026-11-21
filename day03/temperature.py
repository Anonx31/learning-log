# Define a function to convert Celsius to Fahrenheit
def c_to_f(celsius):

    # Apply the Celsius to Fahrenheit conversion formula
    fahrenheit = (celsius * 9/5) + 32

    # Return the converted temperature
    return fahrenheit


# Define a function to convert Fahrenheit to Celsius
def f_to_c(fahrenheit):

    # Apply the Fahrenheit to Celsius conversion formula
    celsius = (fahrenheit - 32) * 5/9

    # Return the converted temperature
    return celsius


# Ask the user which temperature conversion they want
choice = input("Choose conversion (C to F / F to C): ").lower()

# Check if the user selected Celsius to Fahrenheit
if choice == "c to f":

    # Ask the user to enter the temperature in Celsius
    temp = float(input("Enter temperature in Celsius: "))

    # Call the conversion function
    result = c_to_f(temp)

    # Display the converted temperature
    print(f"{temp}°C = {result:.2f}°F")

# Check if the user selected Fahrenheit to Celsius
elif choice == "f to c":

    # Ask the user to enter the temperature in Fahrenheit
    temp = float(input("Enter temperature in Fahrenheit: "))

    # Call the conversion function
    result = f_to_c(temp)

    # Display the converted temperature
    print(f"{temp}°F = {result:.2f}°C")

# Handle invalid conversion choices
else:
    print("Invalid choice. Please select C to F or F to C.")