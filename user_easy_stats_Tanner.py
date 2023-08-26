
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


# if the lists are not the same size,
# log an error and quit the program
if len(years_on_market) != len(song_sales):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(years_on_market)}!={len(song_sales)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the new correlation function from the statistics module
xx_corr = statistics.correlation(years_on_market, years_on_market)
xy_corr = statistics.correlation(years_on_market, song_sales)

# log the information
logger.info("Here's some time series data:")
logger.info(f"xtimes:{years_on_market}")
logger.info(f"yvalues:{song_sales}")
logger.info(f"correlation between xtimes and xtimes = {xx_corr:.2f}")
logger.info(f"correlation between xtimes and yvalues = {xy_corr:.2f}")

# Calculate slope and intercept of a line

# Here's some bivariant data (two series of data)

arrayX = [-200, -150, -100, 50, 0, 50, 100, 150]
arrayY = [-240, -165, -99, 35, 19, 75, 130, 125]

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(arrayX, arrayY)

# Choose an x value off in the future (future x)
future_x = 200

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{arrayX}")
logger.info(f"y:{arrayY}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d},")
logger.info(f"   we predict the value of y will be { future_y:d}.")
logger.info("How'd we do? Does this make sense given the data?")
