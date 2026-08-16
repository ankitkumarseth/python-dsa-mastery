# Calculate Total Price

You are given two CSV files:
- `shopping_file`: Contains details of items purchased by the customer which includes names and quantity of the items purchased. (Format: `SNo,ProductName,Qty`)
- `prices_file`: Contains details like product Id, name and price of all available items. (Format: `Id,ProductName,Price`)

The variable `shopping_file` represents the name of the file containing product purchase details, and `prices_file` represents the name of the file containing product prices.

Define a function `calculate_total_price` that takes `shopping_file` and `prices_file` as argument and returns the total amount of goods purchased by the customer.

### Examples

**Input:**
```text
prices_file: shopdata1.csv
shopping_file: shopping1.csv
```
**Expected Output:**
```text
3156
```
