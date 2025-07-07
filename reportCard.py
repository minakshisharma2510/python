# Report Card Generator

# Student details
student = {
    "name": "Minakshi Sharma",
    "class": "10th Grade",
    "roll_no": 23,
    "school": "Green Valley High School"
}

# Marks in different subjects
marks = {
    "English": 87,
    "Math": 92,
    "Science": 89,
    "Social Studies": 85,
    "Computer Science": 94
}

# Calculate total and percentage
total_marks = sum(marks.values())
max_marks = len(marks) * 100
percentage = (total_marks / max_marks) * 100

# Determine Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Needs Improvement"

# Display Report Card
print("\n" + "="*40)
print(" " * 10 + "REPORT CARD")
print("="*40)
print(f"Name     : {student['name']}")
print(f"Class    : {student['class']}")
print(f"Roll No. : {student['roll_no']}")
print(f"School   : {student['school']}")
print("-" * 40)
print("Subjects and Marks:")
for subject, mark in marks.items():
    print(f"{subject:<20}: {mark}/100")
print("-" * 40)
print(f"Total Marks       : {total_marks}/{max_marks}")
print(f"Percentage        : {percentage:.2f}%")
print(f"Grade             : {grade}")
print("="*40)
