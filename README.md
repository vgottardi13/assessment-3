# Assessment 3

The data provided are the sales records of a retail business in July 2021. These data were extracted from different systems therefore they are in different formats:

- ``pc.json``: A JSON dataset extracted from the ERP system which contains the product categories
- ``orders.csv``: Order information including customer names and shipping addresses in the duration
- ``order_details.csv``: The details of orders

Examine the datasets to understand what data you have. Then, write Python programs to find out the facts required by the management as listed below.

## Questions
1. Based on the freights spent on these orders, please estimate the budget of the freights in the next month for this business. Note that you can decide on how to estimate the budget, but the budget should not be lower than the calculated freight cost.
1. Try to find the countries with the most orders, which implies the strong markets that the business should focus on.
1. The business wants to reward customers who buy frequently by rewarding them with discount coupons. Find 3 customers who have the highest number of orders in the dataset.
1. Which product category has the highest sales revenue? These products are popular and there may be implications for business operations. *(Note: The total sales of a product is the sum of the values of ``unit price * quantity`` in all relevant orders. The sales of a product category are the sum of the total sales of the products in the category.)*

## Requirements
1. (For Q4) You need to match the product category ID to its name using a program. Merely reporting the product category ID is not acceptable.
1. The facts should be outputted to the screen in a format of your discretion, however it should be clear and understandable. 
1. Organise your code logically in functions and/or multiple code files so that other business analysts can understand your code.
1. You **cannot** use modules that are not taught in this unit to complete this assessment.
