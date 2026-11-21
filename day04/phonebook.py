# A simple phonebook lookup using a dictionary.

# Dictionary of names → phone numbers (stored as strings to keep formatting)
phonebook = {
    "Alice": "555-1234",
    "Bob":   "555-5678",
    "Carol": "555-9012",
}

# Ask for a name
name = input("Enter a name to look up: ").strip()

# Look up the name
if name in phonebook:
    print(f"{name}'s number is {phonebook[name]}")
else:
    print("Not found")