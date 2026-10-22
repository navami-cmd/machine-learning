
import numpy as np

# Daily temperatures recorded over 10 days
temperatures = np.array([29, 32, 31, 35, 28, 37, 33, 30, 36, 31])

print("Original temperatures:", temperatures)

# 1. Calculate basic statistics
print("\nAverage temperature:", np.mean(temperatures))
print("Median temperature:", np.median(temperatures))
print("Highest temperature:", np.max(temperatures))
print("Lowest temperature:", np.min(temperatures))
print("Temperature range:", np.ptp(temperatures))

# 2. Find temperatures above the average
average = np.mean(temperatures)
above_average = temperatures[temperatures > average]

print("\nTemperatures above average:", above_average)

# 3. Count hot days (temperature >= 35)
hot_days = np.sum(temperatures >= 35)
print("Number of hot days:", hot_days)

# 4. Sort temperatures
sorted_temperatures = np.sort(temperatures)
print("Sorted temperatures:", sorted_temperatures)

# 5. Replace unusually high readings
corrected = temperatures.copy()
corrected[corrected >= 35] = 34

print("Corrected temperatures:", corrected)

# 6. Calculate day-to-day temperature changes
changes = np.diff(temperatures)
print("Daily temperature changes:", changes)

# 7. Find the index of the hottest day
hottest_day = np.argmax(temperatures)
print("Hottest day: Day", hottest_day + 1)
