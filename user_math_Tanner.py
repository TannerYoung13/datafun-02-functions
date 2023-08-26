'''
Tanner Young
August 26, 2023

Math Module Task 4
'''

import math
import statistics

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

"""
    Calculate the cost of an advertisement based on its dimensions and cost per square unit.
"""

def calculate_advertisement_cost(length, width, cost_per_sq_unit):
    area = length * width
    total_cost = area * cost_per_sq_unit
    return total_cost
advertisement_length = 5.0  
advertisement_width = 3.0   
cost_per_square_unit = 10.0  

total_advertisement_cost = calculate_advertisement_cost(advertisement_length, advertisement_width, cost_per_square_unit)
print("Total advertisement cost:", total_advertisement_cost)

logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
logger.info(f"math.pi = {math.pi}")
logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
logger.info(f"math.radians(180)         = {math.radians(180)}")
logger.info("")

advertisement_1_length = 4.0
advertisement_1_width = 2.5
cost_per_square_unit_1 = 15.0

advertisement_2_length = 3.0
advertisement_2_width = 6.0
cost_per_square_unit_2 = 8.0

advertisement_3_length = 7.0
advertisement_3_width = 4.0
cost_per_square_unit_3 = 12.0

cost_1 = calculate_advertisement_cost(advertisement_1_length, advertisement_1_width, cost_per_square_unit_1)
cost_2 = calculate_advertisement_cost(advertisement_2_length, advertisement_2_width, cost_per_square_unit_2)
cost_3 = calculate_advertisement_cost(advertisement_3_length, advertisement_3_width, cost_per_square_unit_3)

print("Cost of Advertisement 1:", cost_1)
print("Cost of Advertisement 2:", cost_2)
print("Cost of Advertisement 3:", cost_3)

def calculate_total_revenue(sales):
    """
    Calculate the total revenue generated from a list of sales.

    """
    total_revenue = sum(sales)
    return total_revenue


def calculate_average_profit_margin(total_profit, total_revenue):
    """
    Calculate the average profit margin based on the total profit and total revenue.

    """
    if total_revenue == 0:
        return 0.0
    average_margin = (total_profit / total_revenue) * 100
    return average_margin

def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the discounted price of a product.

    """
    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    return discounted_price
