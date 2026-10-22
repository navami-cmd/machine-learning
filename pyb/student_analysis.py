
import numpy as np

students = np.array(["Akhil", "Priya", "Rahul", "Sneha", "Arjun"])

# Columns: Python, Maths, Computer Networks
marks = np.array([
    [85, 78, 92],
    [90, 88, 95],
    [65, 72, 70],
    [95, 91, 89],
    [78, 85, 80]
])

# 1. Display all marks
print("Student Marks:")
print(marks)

# 2. Calculate total marks for each student
total_marks = np.sum(marks, axis=1)

print("\nTotal Marks:")
print(total_marks)

# 3. Calculate average marks for each student
average_marks = np.mean(marks, axis=1)

print("\nAverage Marks:")
print(average_marks)

# 4. Find the topper
topper_index = np.argmax(total_marks)

print("\nClass Topper:")
print(students[topper_index])
print("Total Marks:", total_marks[topper_index])

# 5. Find students who scored at least 80 in every subject
good_students = students[np.all(marks >= 80, axis=1)]

print("\nStudents scoring at least 80 in every subject:")
print(good_students)

# 6. Find the highest mark in each subject
highest_subject_marks = np.max(marks, axis=0)

print("\nHighest mark in each subject:")
print(highest_subject_marks)

# 7. Find students whose total marks are above 250
high_scorers = students[total_marks > 250]

print("\nStudents scoring above 250:")
print(high_scorers)
