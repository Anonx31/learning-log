# Iterate through numbers from 1 to 100
for num in range(1, 101):

    # Check if the number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    # Check if the number is divisible by 7
    elif num % 7 == 0:
        print("Seven")

    # Check if the number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")

    # Check if the number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")

    # If none of the conditions match, print the number
    else:
        print(num)