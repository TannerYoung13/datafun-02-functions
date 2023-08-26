
# Descriptive: Univariant Time Series Data.........................

# describe relationships
# univariant time series data (one variable over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)

import statistics

# Example 1: Song Sales vs Years on the Market
years_on_market = [1, 2, 3, 4, 5]
song_sales = [5000, 8000, 10000, 7500, 6000]

years_std_dev = round(statistics.stdev(years_on_market), 2)
sales_std_dev = round(statistics.stdev(song_sales), 2)

print("Mean:", statistics.mean(years_on_market))
print("Median:", statistics.median(years_on_market))
print("Mode:", statistics.mode(years_on_market))  
print("Variance:", statistics.variance(years_on_market))
print(f"Standard Deviation: {years_std_dev}")
print("Smallest:", min(years_on_market))
print("Largest:", max(years_on_market))
print("Range:", max(years_on_market) - min(years_on_market))

print("Mean:", statistics.mean(song_sales))
print("Median:", statistics.median(song_sales))
print("Mode:", statistics.mode(song_sales))  
print("Variance:", statistics.variance(song_sales))
print(f"Standard Deviation: {sales_std_dev}")
print("Smallest:", min(song_sales))
print("Largest:", max(song_sales))
print("Range:", max(song_sales) - min(song_sales))
