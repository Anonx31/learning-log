# Dictionary of 5 students and their marks
student_marks = {
    "Alice": 85,
    "Bob": 38,
    "Charlie": 72,
    "David": 45,
    "Eva": 29
}

# --- Topper (student with highest marks) ---
# max() with key= compares by the dictionary values (marks)
topper = max(student_marks, key=student_marks.get)
print(f"Topper: {topper} with {student_marks[topper]} marks")

# --- Class Average ---
# Average = total marks / number of students
class_average = sum(student_marks.values()) / len(student_marks)
print(f"Class Average: {class_average:.2f}")

# --- Students who failed (marks under 40) ---
# List comprehension filters students whose marks < 40
failed_students = [name for name, marks in student_marks.items() if marks < 40]

if failed_students:
    print(f"Failed Students: {', '.join(failed_students)}")
else:
    print("Failed Students: None")