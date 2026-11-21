# Define a function that accepts a sentence as input
def word_stats(sentence):

    # Split the sentence into individual words
    words = sentence.split()

    # Count the total number of words
    word_count = len(words)

    # Find the longest word in the sentence
    longest_word = max(words, key=len) if words else ""

    # Return both the word count and the longest word
    return word_count, longest_word


# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Call the word_stats function and store both returned values
count, longest = word_stats(sentence)

# Display the total word count
print(f"Total number of words: {count}")

# Display the longest word
print(f"Longest word: {longest}")