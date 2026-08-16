# Sales Data Analysis

You are provided with sales data represented as a list of dictionaries. Each dictionary contains the following keys:
- `product_id` (str): The unique identifier for a product.
- `units_sold` (int): The number of units sold in a transaction.
- `revenue` (int): The revenue generated from that transaction.

There will be multiple entries for the same `product_id`. Implement a function `analyse_sales_data(sales_data, task)` where task is one of the following strings:

- `total_revenue`: Returns the total revenue over all transanctions.
- `product_wise_total_units_and_revenue`: Returns a dictionary with `product_id` as keys and a tuple with (the number of units sold for that product, total revenue generated from that product) as values.
- `top_selling_product`: Returns the `product_id` of the product with the highest number of units sold. If there is a tie in units sold, the product with the higher total revenue is returned.
- `average_product_price`: Returns a dictionary with `product_id` as keys and the average price computed as the (total revenue / total units_sold) over all the transanctions for the product rounded to 2 decimal places.

NOTE: This is a function type question, you don't have to take input or print the output, you just have to complete the required function definition.

### Example
```python
sales_data = [
   {"product_id": "P101", "units_sold": 50, "revenue": 400},
   {"product_id": "P102", "units_sold": 30, "revenue": 900},
   {"product_id": "P101", "units_sold": 70, "revenue": 600},
   {"product_id": "P103", "units_sold": 120, "revenue": 600}
]
```
- `total_revenue` -> `2500`
- `product_wise_total_units_and_revenue` -> `{'P101': (120, 1000), 'P102': (30, 900), 'P103': (120, 600)}`
- `top_selling_product` -> `'P101'` (P101 and P103 are tied on units, but P101 has higher revenue.)
- `average_product_price` -> `{'P101': 8.33, 'P102': 30, 'P103': 5}` (For P101, (400+600)/(50+70))
