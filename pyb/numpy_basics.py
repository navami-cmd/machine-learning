
import numpy as np

# Create an array of marks
marks = np.array([78, 92, 65, 88, 45, 95, 73])

print("Original marks:", marks)

# 1. Access individual elements
print("First mark:", marks[0])
print("Last mark:", marks[-1])

# 2. Get a portion of the array
print("First three marks:", marks[:3])

# 3. Find marks above 80
print("Marks above 80:", marks[marks > 80])

# 4. Add 5 bonus marks to everyone
updated_marks = marks + 5
print("Updated marks:", updated_marks)

# 5. Calculate basic statistics
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
