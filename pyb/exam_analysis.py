
import numpy as np

# Marks of 12 students
marks = np.array([78, 45, 92, 33, 67, 88, 54, 96, 41, 73, 29, 84])

print("EXAM RESULT ANALYSIS")
print("-" * 30)

# 1. Basic statistics
print("Total students:", len(marks))
print("Average marks:", round(np.mean(marks), 2))
print("Median marks:", np.median(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))

# 2. Pass and fail analysis (pass mark = 40)
passed = marks[marks >= 40]
failed = marks[marks < 40]

print("\nPassed students:", len(passed))
print("Failed students:", len(failed))
print("Passing marks:", passed)
print("Failing marks:", failed)

# 3. Find students who scored above the class average
average = np.mean(marks)
above_average = marks[marks > average]

print("\nAbove-average scores:", above_average)
print("Number above average:", len(above_average))

# 4. Assign grades using conditions
grades = np.select(
    [marks >= 90, marks >= 75, marks >= 60, marks >= 40],
    ["A", "B", "C", "D"],
    default="F"
)

print("\nGrades:", grades)

# 5. Count students in each grade
grade_names, grade_counts = np.unique(
    grades, return_counts=True
)

print("\nGRADE DISTRIBUTION")
for grade, count in zip(grade_names, grade_counts):
    print(f"Grade {grade}: {count} student(s)")

# 6. Sort marks from highest to lowest
print("\nRanked marks:", np.sort(marks)[::-1])

# 7. Calculate the percentage of students who passed
pass_percentage = (len(passed) / len(marks)) * 100
print(f"\nPass percentage: {pass_percentage:.2f}%")
