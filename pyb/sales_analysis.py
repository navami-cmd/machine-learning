
import numpy as np

products = np.array(["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"])

prices = np.array([55000, 800, 1500, 12000, 2500])

units_sold = np.array([12, 80, 45, 18, 35])

# 1. Revenue for each product
revenue = prices * units_sold

print("Revenue for each product:")
print(revenue)

# 2. Total revenue of the store
total_revenue = np.sum(revenue)

print("\nTotal store revenue:")
print(total_revenue)

# 3. Product with the highest units sold
highest_index = np.argmax(units_sold)

print("\nBest-selling product:")
print(products[highest_index])
print("Units sold:", units_sold[highest_index])

# 4. Products with more than 30 units sold
popular_products = products[units_sold > 30]

print("\nProducts with more than 30 units sold:")
print(popular_products)

# 5. Products priced below 3000
affordable_products = products[prices < 3000]

print("\nProducts priced below 3000:")
print(affordable_products)

# 6. Average units sold
average_sales = np.mean(units_sold)

print("\nAverage units sold per product:")
print(average_sales)
