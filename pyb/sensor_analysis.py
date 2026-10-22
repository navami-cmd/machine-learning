
import numpy as np

# Simulated sensor readings from an industrial machine
sensor_data = np.array([
    42.1, 43.5, 41.8, 44.2, 42.9,
    43.1, 45.0, 44.5, 42.7, 43.8,
    44.1, 43.6, 42.4, 78.5, 43.2
])

# 1. Statistical analysis
mean_value = np.mean(sensor_data)
median_value = np.median(sensor_data)
std_deviation = np.std(sensor_data)
minimum = np.min(sensor_data)
maximum = np.max(sensor_data)

print("SENSOR DATA ANALYSIS")
print("-" * 30)
print(f"Number of readings: {len(sensor_data)}")
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
print(f"Standard deviation: {std_deviation:.2f}")
print(f"Minimum: {minimum:.2f}")
print(f"Maximum: {maximum:.2f}")

# 2. Detect unusual readings using the Z-score
z_scores = (sensor_data - mean_value) / std_deviation
threshold = 2

anomaly_mask = np.abs(z_scores) > threshold
anomalies = sensor_data[anomaly_mask]

print("\nANOMALY DETECTION")
print("-" * 30)
print("Anomalous readings:", anomalies)

# 3. Replace anomalous readings with the median
cleaned_data = sensor_data.copy()
cleaned_data[anomaly_mask] = median_value

print("\nDATA CLEANING")
print("-" * 30)
print("Original readings:", sensor_data)
print("Cleaned readings:", cleaned_data)
print(f"Original mean: {np.mean(sensor_data):.2f}")
print(f"Cleaned mean: {np.mean(cleaned_data):.2f}")
