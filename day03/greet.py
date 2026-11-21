# Define the main function
def main():

    # Ask the user to enter their name
    name = input("Name: ")

    # Call the greet function and pass the user's name as an argument
    greet(name)


# Define a function that accepts a name as a parameter
def greet(name):

    # Print a personalized greeting using an f-string
    print(f"Hello, {name}")


# Call the main function to start program execution
main()