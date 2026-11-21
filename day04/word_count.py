# Ask for a sentence and count how often each word appears.

sentence = input("Enter a sentence: ")

# Normalize: lowercase + split on whitespace
words = sentence.lower().split()

# Count occurrences
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# Print the results
for word, count in counts.items():
    print(f"{word}: {count}")