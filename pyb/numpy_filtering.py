
import numpy as np

temperatures = np.array([28, 32, 35, 29, 38, 31, 36])

print("All temperatures:", temperatures)

hot_days = temperatures[temperatures >= 35]
print("Hot days:", hot_days)

comfortable_days = temperatures[(temperatures >= 28) & (temperatures <= 32)]
print("Comfortable days:", comfortable_days)

print("Average temperature:", np.mean(temperatures))
print("Hottest temperature:", np.max(temperatures))
