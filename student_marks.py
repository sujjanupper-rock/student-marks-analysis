# Student Marks Analysis - Sample Project

student_marks = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 76,
    "Sneha": 88,
    "Kiran": 69
}

total = sum(student_marks.values())
average = total / len(student_marks)

print("STUDENT MARKS ANALYSIS")
print("----------------------")

for name, marks in student_marks.items():
    print(name, ":", marks)

print("----------------------")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", max(student_marks.values()))
print("Lowest Marks:", min(student_marks.values()))
