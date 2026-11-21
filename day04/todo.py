tasks = []  # empty list to store tasks

while True:
    # Ask the user for input
    command = input("Enter a task (or type 'show' / 'quit'): ").strip()

    # Normalize for comparison (case-insensitive)
    lower = command.lower()

    # Case A: quit
    if lower == "quit":
        print("Goodbye!")
        break

    # Case B: show all tasks
    elif lower == "show":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            print()  # blank line for readability

    # Case C: blank input
    elif command == "":
        print("Please enter a task.")

    # Case D: add a new task
    else:
        tasks.append(command)
        print(f"Added: {command}")