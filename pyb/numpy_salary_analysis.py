
import numpy as np

employees = np.array(["Akhil", "Priya", "Rahul", "Sneha", "Arjun"])

salaries = np.array([25000, 40000, 32000, 55000, 28000])

# 1. Display employee details
print("Employee Names:")
print(employees)

print("\nCurrent Salaries:")
print(salaries)

# 2. Calculate a 10% salary increase for everyone
new_salaries = salaries + (salaries * 0.10)

print("\nSalaries After 10% Increase:")
print(new_salaries)

# 3. Find employees earning more than 30000
high_earners = employees[salaries > 30000]

print("\nEmployees Earning Above 30000:")
print(high_earners)

# 4. Calculate the average salary
average_salary = np.mean(salaries)

print("\nAverage Salary:")
print(average_salary)

# 5. Find the employee with the highest salary
highest_index = np.argmax(salaries)

print("\nHighest Paid Employee:")
print(employees[highest_index])
print("Salary:", salaries[highest_index])

# 6. Find employees earning between 25000 and 40000
selected_employees = employees[
    (salaries >= 25000) & (salaries <= 40000)
]

print("\nEmployees Earning Between 25000 and 40000:")
print(selected_employees)

# 7. Calculate the total monthly salary expense
total_expense = np.sum(salaries)

print("\nTotal Monthly Salary Expense:")
print(total_expense)
