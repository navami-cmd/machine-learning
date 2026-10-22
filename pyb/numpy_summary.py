
import numpy as np

marks = np.array([78, 85, 92, 67, 88, 95, 73])

print("Student Marks:", marks)
print("Total Students:", len(marks))
print("Average Marks:", np.mean(marks))
print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))

passed = marks[marks >= 40]
print("Students Who Passed:", len(passed))

above_average = marks[marks > np.mean(marks)]
print("Marks Above Average:", above_average)
