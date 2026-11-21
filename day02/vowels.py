# Ask the user to enter a word
word = input("Enter a word: ")

# Initialize the vowel counter with 0
count = 0

# Convert the word to lowercase and iterate through each character
for char in word.lower():

    # Check whether the current character is a vowel
    if char in "aeiou":

        # Increase the vowel counter by 1
        count += 1

# Display the total number of vowels
print(f"Total vowels: {count}")